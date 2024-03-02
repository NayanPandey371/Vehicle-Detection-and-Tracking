from sort import *
import cv2
import numpy as np
import os
import math

#for transformation of pixel into distance
TARGET_WIDTH = 2
TARGET_HEIGHT = 2

TARGET = np.array(
    [
        [0, 0],
        [TARGET_WIDTH - 1, 0],
        [TARGET_WIDTH - 1, TARGET_HEIGHT - 1],
        [0, TARGET_HEIGHT - 1],
    ]
)

classes = {
    0: '2 Wheeler',
    1: 'Car',
    2: 'Bus',
    3: 'Minibus',
    4: 'Tempo',
    5: 'Truck'
}

def finder(track_id, tracker):
    for trk, track in enumerate(tracker):
        if track[-1] == track_id:
            return trk
    return -1

colors = {
    0: (255, 255, 0),
    1: (0, 255, 255),
    2: (255, 0, 255),
    3: (255, 0, 0),
    4: (0, 255, 0),
    5: (0, 0, 255)
}

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
        return transformed_points.reshape(-1, 2)

def vehicle_class(class_id):
    class_mapping = {
        '0': '2 wheeler',
        '1': 'car',
        '2': 'bus',
        '3': 'minibus',
        '4': 'tempo',
        '5': 'truck'
    }
    return class_mapping.get(class_id, 'Unknown')

clicked_points = []
source_points = []

# Define a mouse callback function to capture four points for the polygon
def mouse_callback(event, x, y, flags, param):
    global clicked_points, source_points
    if event == cv2.EVENT_MOUSEMOVE:
        print("Coordinates (x, y):", x, y)
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(clicked_points) < 4:
            clicked_points.append([x, y])
            cv2.circle(resized_frame, (x, y), 5, (0, 255, 0), -1)  # Draw a dot at the clicked point

            if len(clicked_points) > 1:  # Draw a line between points for every other click
                cv2.line(resized_frame, tuple(clicked_points[-2]), tuple(clicked_points[-1]), (0, 0, 255), 2)

            if len(clicked_points) == 4:  # If four points are clicked, update source_points
                cv2.line(resized_frame, tuple(clicked_points[0]), tuple(clicked_points[3]), (0, 0, 255), 2)
                source_points = np.array(clicked_points)
                print(source_points[3][1])

                source_points[:, 0] = source_points[:, 0] * width / desired_width
                source_points[:, 1] = source_points[:, 1] * height / desired_height

                clicked_points = []

north_count = []
south_count = []

video = None
def get_video(video_path):
    global video 
    video = cv2.VideoCapture(video_path)
    
# video path
# video_path = 'Vehicle-Detection-and-Counting-6/balkumari.mp4'
# video = cv2.VideoCapture(video_path)

if not video.isOpened():
    print("Error: Unable to open video file.")
    exit()

success, frame = video.read()

if not success:
    print("Error: Failed to read the frame.")
    exit()

width = frame.shape[0]
height = frame.shape[1]

# Define the desired width and height for the resized frame
desired_width = 1280
desired_height = 720

# Resize the frame
resized_frame = cv2.resize(frame, (desired_width, desired_height))

#for mouse callback
cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', mouse_callback)
while(1):
   cv2.imshow('Frame', resized_frame)
   key=cv2.waitKey(1)
   if key == 27 or len(source_points) == 4:
      cv2.destroyWindow('Frame')
      break

# Defining the points for polygon
SOURCE = np.array(source_points)

fps = video.get(cv2.CAP_PROP_FPS)

mot_tracker = Sort()

font = cv2.FONT_HERSHEY_SIMPLEX

#line_pos = int(height/2) - 200
line_pos = SOURCE[3][1]
print(line_pos)

video_out = cv2.VideoWriter('output/out.mp4', cv2.VideoWriter_fourcc(*'mp4v'), video.get(cv2.CAP_PROP_FPS), (width, height))

# Check if the video writer is initialized successfully
if not video_out.isOpened():
    print("Error: Unable to initialize video writer.")
    exit()

view_transformer = ViewTransformer(source=SOURCE, target=TARGET)

count= 1
detections = np.zeros(shape=(40, 6))
direction = {}

class_counts = {}

print('Processing. Please Wait')

while success:
    id = 0
    label_path = 'runs/detect/exp15/labels/balkumari_'+str(count)+'.txt'
    if os.path.exists(label_path):
      label = open(label_path, 'r')
      for line in label:
        l = line.split()
        class_id = int(l[0])
        x_center = float(l[1]) * width
        y_center = float(l[2]) * height
        obj_width = float(l[3]) * width
        obj_height = float(l[4]) * height
        score = float(l[5])

        x_top = int(x_center - obj_width/2)
        y_top = int(y_center - obj_height/2)
        x_low = int(x_center + obj_width/2)
        y_low = int(y_center + obj_height/2)

        if cv2.pointPolygonTest(SOURCE, (x_center, y_center), False) >= 0:
          detections[id] = np.array([x_top, y_top, x_low, y_low, score, class_id])
          id += 1
          cv2.rectangle(frame, (int(x_top), int(y_top)), (int(x_low), int(y_low)), colors[class_id], 2)
        #   class_counts[class_id] = class_counts.get(class_id, 0) + 1

        cv2.polylines(frame, [SOURCE], isClosed=True, color=(0, 255, 0), thickness=2)

    tracker = mot_tracker.update(detections[:id])

    # for class_id, count in class_counts.items():
    #     class_name = vehicle_class(class_id)
    #     text = f"{class_name}: {count}"
    #     cv2.putText(frame, text, (20, 20 + 30 * class_id), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    if count != 0:
        for track in tracker:
            if track[-1] not in direction:
                direction[track[-1]] = None
            elif direction.get(track[-1]) is None:
                i = finder(track[-1], prev_track)
                if i != - 1 and prev_track[i][1] - track[1] > 2:
                    direction[track[-1]] = "North"
                else:
                    direction[track[-1]] = "South" 

    #cv2.line(frame, (0, line_pos), (width, line_pos), (0, 0, 255), 2)
    for track in tracker:
        track_id = track[-1]
        if track[1] < line_pos and track_id not in north_count and direction[track_id] == "North":
            north_count.append(track[-1])
        elif track[1] > line_pos and (track[-1] not in south_count) and direction[track[-1]] == "South":
            south_count.append(track[-1])
        
        #for speed measurement
        transformed_point1 = view_transformer.transform_points(points=np.array([track[0], track[1]]))[0].astype(int)
        transformed_point2 = view_transformer.transform_points(points=np.array([track[2], track[3]]))[0].astype(int)
        x1, y1 = transformed_point1
        x2, y2 = transformed_point2

        distance = math.sqrt((abs(y2 - x2) ** 2) + (abs(y1 - x1) ** 2))
        time = 1 / fps
        speed = distance / time
        frame = cv2.putText(frame, f'Speed: {speed:.2f} km/hr', (int(track[0]), int(track[1])), font, 1, (0,0,255), 2)
        #frame = cv2.putText(frame, vehicle_class(track[-2]) + str(int(track_id)), (int(track[0]), int(track[1] - 20)), font, 1, (0,0,255), 2)

    frame = cv2.putText(frame, "North: " + str(len(north_count)), (100, 100), font, 1,(0, 0, 255), 2)
    frame = cv2.putText(frame, "South: " + str(len(south_count)), (800, 100), font, 1,  (0, 0, 255), 2)

    video_out.write(frame)
    success, frame = video.read()
    count += 1
    detections = np.zeros(shape=(40, 6))
    prev_track = tracker
    label.close()

video.release()
video_out.release()
cv2.destroyAllWindows()