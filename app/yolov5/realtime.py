import cv2
import numpy as np
import torch
import os
import math
from sort import *

class ViewTransformer:
    def __init__(self, source: np.ndarray, target: np.ndarray) -> None:
        source = source.astype(np.float32)
        target = target.astype(np.float32)
        self.m = cv2.getPerspectiveTransform(source, target)

    def transform_points(self, points: np.ndarray) -> np.ndarray:
        if points.size == 0:
            return points

        reshaped_points = points.reshape(-1, 1, 2).astype(np.float32)
        transformed_points = cv2.perspectiveTransform(reshaped_points, self.m)
        transformed_points = self.handle_small_floats(transformed_points)
        return transformed_points.reshape(-1, 2)
    
    def handle_small_floats(self, points: np.ndarray) -> np.ndarray:
        return np.where(np.abs(points) < 1e-15, 0, points)

class ObjectDetection:
    """
    Class implements Yolo5 model to make inferences on a youtube video using OpenCV.
    """

    def __init__(self):
        """
        Initializes the class with youtube url and output file.
        """
        self.model = self.load_model()
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.roi = None
        print("\n\nDevice Used:", self.device)

        self.source_points = []
        self.clicked_points = []
        
        self.classes = {
            0: '2 Wheeler',
            1: 'Car',
            2: 'Bus',
            3: 'Minibus',
            4: 'Tempo',
            5: 'Truck'
        }

        self.colors = {
            0: (255, 255, 0),
            1: (0, 255, 255),
            2: (255, 0, 255),
            3: (255, 0, 0),
            4: (0, 255, 0),
            5: (0, 0, 255)
        }

        self.prev_speed = {}
        self.moving_avg_window = 5

    def load_model(self):
        """
        Loads Yolo5 model from pytorch hub.
        """
        model_path = os.path.join(os.getcwd(), './yolov5')
        model = torch.hub.load(model_path, 'custom', source='local', path='yolov5/models/best.pt', force_reload=True)
        return model

    def score_frame(self, frame):
        """
        Takes a single frame as input, and scores the frame using yolo5 model.
        """
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
     
        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        return labels, cord

    def class_to_label(self, x):
        """
        For a given label value, return corresponding string label.
        """
        return self.classes[int(x)]

    def plot_boxes(self, results, frame):
        """
        Takes a frame and its results as input, and plots the bounding boxes and label on to the frame.
        """
        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.5:
                x1, y1, x2, y2 = int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
                if self.roi is not None:
                    if self.point_in_roi((x1 + x2) / 2, (y1 + y2) / 2):
                        bgr = self.colors[int(labels[i])]
                        cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                        #cv2.putText(frame, self.class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)
                else:
                    bgr = self.colors[int(labels[i])]
                    cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                    #cv2.putText(frame, self.class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)

        if self.roi is not None:
            cv2.polylines(frame, [self.roi], isClosed=True, color=(238,169,144), thickness=2)
        
        return frame
    
    def point_in_roi(self, x, y):
        """
        Checks if a point is inside the ROI.
        """
        if self.roi is None:
            return False
        
        p = np.array([x, y])
        return cv2.pointPolygonTest(np.array(self.roi), tuple(p), False) >= 0

    def set_roi(self, VIDEO_PATH):
        """
        Function to set ROI dynamically using mouse events.
        """      

        def mouse_callback(event, x, y, flags, param):
            nonlocal select_roi
            # if event == cv2.EVENT_MOUSEMOVE:
            #     print("Coordinates (x, y):", x, y)
            if event == cv2.EVENT_LBUTTONDOWN and select_roi == True:
                if len(self.clicked_points) < 4:
                    self.clicked_points.append([x, y])

                    if len(self.clicked_points) == 4:  # If four points are clicked, update self.source_points
                        self.source_points = np.array(self.clicked_points)
                        print(self.source_points[3][1])

                        self.roi = self.source_points

                        self.clicked_points = []
                        select_roi = False

        cv2.namedWindow("img")
        cv2.setMouseCallback("img", mouse_callback)

        # get the video file inside the video path
        video_files = os.listdir(VIDEO_PATH)
        for video_file in video_files:
            video_path = os.path.join(VIDEO_PATH, video_file)

        select_roi = True
        cap = cv2.VideoCapture(video_path)
        
        while(1):
            ret, frame = cap.read()
            if not ret:
                break

            for pt in self.clicked_points:
                cv2.circle(frame, tuple(pt), 2, (238,169,144), -1)
            if len(self.clicked_points) > 1:
                for i in range(len(self.clicked_points) - 1):
                    cv2.line(frame, tuple(self.clicked_points[i]), tuple(self.clicked_points[(i+1)%4]), (238,169,144), 2)
            

            cv2.imshow('img', frame)
            key=cv2.waitKey(1)
            if key == 27 or len(self.source_points) == 4:
                break

        cap.release()

    def track(self, results, frame, mot_tracker):
        labels, coordinates = results
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        id = 0
        detection = torch.zeros((40, 6), device = 'cuda' if torch.cuda.is_available() else 'cpu')
        n = len(labels)
        for i in range(n):
            coordinate = coordinates[i]
            score = coordinate[4]
            if score > 0.5:
                x1, y1, x2, y2 = int(coordinate[0]*x_shape), int(coordinate[1]*y_shape), int(coordinate[2]*x_shape), int(coordinate[3]*y_shape)
                detection[id] = torch.tensor([x1, y1, x2, y2, score.item(), labels[i].item()], device = 'cuda' if torch.cuda.is_available() else 'cpu')
                id += 1
        
        tracker = mot_tracker.update(detection[:id].cpu())

        return tracker

    
    def finder(self, track_id, tracker):
        for trk, track in enumerate(tracker):
            if track[-2] == track_id:
                return trk
        return -1

    def find_direction(self, direction, tracker, prev_track):
        for track in tracker:
            track_id = track[-2]
            if track_id not in direction:
                direction[track_id] = None
            elif direction.get(track_id) is None:
                i = self.finder(track_id, prev_track)
                if i != - 1 and prev_track[i][1] - track[1] > 1:
                    direction[track_id] = "North"
                elif i != -1 and track[1] - prev_track[i][1] > 1:
                    direction[track_id] = "South" 
        #print(direction)
        return direction
    
    def count(self, direction, tracker, north, south, north_count, south_count, north_pos, south_pos):
        for track in tracker:
            track_id, class_id = track[-2], int(track[-1])
            x_centre_of_bounding_box = (track[0] + track[2]) / 2
            y_centre_of_bounding_box = (track[1] + track[3]) / 2

            if self.point_in_roi(x_centre_of_bounding_box, y_centre_of_bounding_box):
                vehicle_pos = y_centre_of_bounding_box
                if vehicle_pos < north_pos and track_id not in north and direction[track_id] == "North":
                    north_count[class_id] += 1
                    north.append(track_id)
                elif vehicle_pos > south_pos and track_id not in south and direction[track_id] == "South":
                    south_count[class_id] += 1
                    south.append(track_id)
        return north, south, north_count, south_count

    
    def speed_measurement(self, tracker, track_id_array, prev_frame_numbers, view_transformer, video, prev_position, fps, frame):
        for track in tracker:
            track_id, class_id = track[-2], int(track[-1])

            x_centre_of_bounding_box = (track[0] + track[2]) / 2
            y_centre_of_bounding_box = (track[1] + track[3]) / 2

            if self.point_in_roi(x_centre_of_bounding_box, y_centre_of_bounding_box):
                present_track_id = track_id
                if present_track_id in track_id_array:
                    current_frame_number = video.get(cv2.CAP_PROP_POS_FRAMES)
                    prev_frame_number = prev_frame_numbers[present_track_id]
                    frame_difference = current_frame_number - prev_frame_number
                    time = frame_difference / fps

                    transformed_point1 = view_transformer.transform_points(points=np.array(prev_position[present_track_id]))[0].astype(float)
                    transformed_point2 = view_transformer.transform_points(points=np.array([x_centre_of_bounding_box, y_centre_of_bounding_box]))[0].astype(float)
                    x1, y1 = transformed_point1
                    x2, y2 = transformed_point2

                    distance = math.sqrt((abs(x2 - x1) ** 2) + (abs(y2 - y1) ** 2))
                    speed = 3.6 * distance / time

                    if present_track_id in self.prev_speed:
                        self.prev_speed[present_track_id].append(speed)
                        if len(self.prev_speed[present_track_id]) > self.moving_avg_window:
                            self.prev_speed[present_track_id].pop(0)
                        
                        avg_speed = sum(self.prev_speed[present_track_id]) / len(self.prev_speed[present_track_id])
                    else:
                        avg_speed = speed
                        self.prev_speed[present_track_id] = [speed]

                    frame = cv2.putText(frame, f'Speed: {avg_speed:.2f} km/hr', (int(track[0]), int(track[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, self.colors[class_id], 2)
                    frame = cv2.putText(frame, self.classes[class_id], (int(track[0]), int(track[1] - 20)), cv2.FONT_HERSHEY_SIMPLEX, 1, self.colors[class_id], 2)

                prev_frame_numbers[present_track_id] = video.get(cv2.CAP_PROP_POS_FRAMES)

                prev_position[present_track_id] = [x_centre_of_bounding_box, y_centre_of_bounding_box]

                if track_id not in track_id_array:
                    track_id_array.append(track_id)

    def put_text_on_frame(self, frame, class_counts, width):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.rectangle(frame, (40, 0), (width-130, 40), (0, 0, 0), -1)

        x_offset = 50 
        for i in range(6):
            count = class_counts.get(i, 0)
            text = f"{self.classes[i]}: {count}"
            text_width = cv2.getTextSize(text, font, 1, 2)[0][0]
            cv2.putText(frame, text, (x_offset, 30), font, 1, (50, 205, 50))
            x_offset += text_width + 10


    def count_vehicles_in_roi(self, tracker):
        """
        Count the number of vehicles within the ROI.
        """
        roi_count = {}
        for track in tracker:
            class_id = int(track[-1])
            x_centre_of_bounding_box = (track[0] + track[2]) / 2
            y_centre_of_bounding_box = (track[1] + track[3]) / 2
                
            if self.point_in_roi(x_centre_of_bounding_box, y_centre_of_bounding_box):
                if class_id not in roi_count:
                    roi_count[class_id] = 1
                else:
                    roi_count[class_id] += 1
        return roi_count

    def run(self, VIDEO_PATH):
        """
        This function is called when class is executed, it runs the loop to read the video frame by frame,
        and write the output into a new file.
        """
        # get the video file inside the video path
        video_files = os.listdir(VIDEO_PATH)
        for video_file in video_files:
            video_path = os.path.join(VIDEO_PATH, video_file)
        TARGET_WIDTH = 15
        TARGET_HEIGHT = 30

        TARGET = np.array(
            [
                [0, 0],
                [TARGET_WIDTH - 1, 0],
                [TARGET_WIDTH - 1, TARGET_HEIGHT - 1],
                [0, TARGET_HEIGHT - 1],
            ]
        )
        self.set_roi(VIDEO_PATH)
        view_transformer = ViewTransformer(source=self.roi, target=TARGET)
        north_pos = max([self.source_points[i][1] for i in range(0, 4)])
        south_pos = min([self.source_points[i][1] for i in range(0, 4)])
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        prev_track, north, south = [], [], []
        direction, north_count, south_count = {}, {}, {}
        track_id_array = []
        prev_frame_numbers = {}
        prev_position = {}
        mot_tracker = Sort()
        for i in range(6):
            north_count[i] = 0
            south_count[i] = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            results = self.score_frame(frame)
            frame = self.plot_boxes(results, frame)

            tracker = self.track(results=results, frame=frame, mot_tracker=mot_tracker)

            direction = self.find_direction(direction, tracker, prev_track)
            north, south, north_count, south_count = self.count(direction, tracker, north, south, north_count, south_count, north_pos, south_pos)

            self.speed_measurement(tracker, track_id_array, prev_frame_numbers, view_transformer, cap, prev_position, fps, frame)

            for i in range(6):
                frame = cv2.putText(frame, self.classes[i] + ':' + str(north_count[i]), (100, 50*(i+2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                frame = cv2.putText(frame, self.classes[i] + ':' + str(south_count[i]), (800, 50*(i+2)), cv2.FONT_HERSHEY_SIMPLEX, 1,  (0, 255, 0), 2)

            roi_count = self.count_vehicles_in_roi(tracker)
        
            self.put_text_on_frame(frame, roi_count, frame.shape[1])

            cv2.imshow("img", frame)

            prev_track = tracker

            key=cv2.waitKey(1)
            if key == 27 or key == ord('q'):
                break
        print(north_count)
        print(south_count)
        cap.release()
        cv2.destroyAllWindows()

# Create a new object and execute.
detection = ObjectDetection()
def real_time_detection(VIDEO_PATH):
    detection.run(VIDEO_PATH)


    
