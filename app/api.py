from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import torch
import os
from yolov5.detect import run_model
from yolov5.new import video_processing
import shutil

# Create a list of allowed origins
origins = ["http://localhost:5173"]

app = FastAPI()

# Add the CORSMiddleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Allow cookies and other credentials
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all request headers
)

@app.get('/')
def sayhello():
    return{"Hello"}

RELATIVE_UPLOAD_DIR = './yolov5/uploads'
RELATIVE_DETECT_DIR = './yolov5/runs/detect'
CURRENT_DIRECTORY = os.getcwd()

@app.post("/upload-video")
async def upload_video(video: UploadFile = File(...)):
    try:
        UPLOAD_DIR = os.path.join(CURRENT_DIRECTORY, RELATIVE_UPLOAD_DIR)
        DETECT_DIR = os.path.join(CURRENT_DIRECTORY, RELATIVE_DETECT_DIR)
        # Get all files in the directory
        files = os.listdir(UPLOAD_DIR)
        # Iterate through each file and remove it
        for filename in files:
            # Construct the full path to the file
            file_path = os.path.join(UPLOAD_DIR, filename)
            # Check if it's a file (not a directory) before removing
            if os.path.isfile(file_path):
                os.remove(file_path)

        os.makedirs(UPLOAD_DIR, exist_ok=True)

        # remove the detect folder if it exists
        if os.path.exists(DETECT_DIR):
            shutil.rmtree(DETECT_DIR)

        # save the video content
        with open(f"{UPLOAD_DIR}/{video.filename}", "wb") as f:
            f.write(video.file.read())
        run_model()
        return {"message": "Video uploaded successfully!"}

    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}


@app.get("/get-result")
async def generate_result():
    # video path
    VIDEO_RELATIVE_PATH = './yolov5/uploads'
    OUTPUT_RELATIVE_PATH = '../frontend/public/videos'
    VIDEO_PATH = os.path.join(CURRENT_DIRECTORY, VIDEO_RELATIVE_PATH)
    OUTPUT_PATH = os.path.join(CURRENT_DIRECTORY, OUTPUT_RELATIVE_PATH)
    try:
        video_processing(VIDEO_PATH, OUTPUT_RELATIVE_PATH)

        for file in os.listdir(OUTPUT_PATH):
            if(file == 'out.mp4'):
                VIDEO_FILE_PATH = os.path.join(OUTPUT_PATH, file)

        return VIDEO_FILE_PATH
    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}

# def compress_video(input_path):
#     absolute_path = os.path.abspath('./yolov5/output/out.mp4')
#     original_video = VideoFileClip(absolute_path)
#     compressed_video = './yolov5/output/compressed.mp4'
#     original_video.write_videofile(compressed_video, codec="libx264", bitrate="5000k")

# Run the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, timeout_keep_alive=1200)
    # generate_result()