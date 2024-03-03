from fastapi import FastAPI, UploadFile, File
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import torch
import os
from yolov5.detect import run_model
# Create a list of allowed origins
origins = ["http://localhost:5173"]

app = FastAPI()
# print(torch.__version__)

# model_path = './model/best.pt'
# model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
# # print(model)
# print(model)
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
@app.post("/upload-video")
async def upload_video(video: UploadFile = File(...)):
    try:
        # save the video content 
        current_directory = os.getcwd()
        UPLOAD_DIR = os.path.join(current_directory, RELATIVE_UPLOAD_DIR)
       
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
        with open(f"{UPLOAD_DIR}/{video.filename}", "wb") as f:
            f.write(video.file.read())
        # run_model()
        return {"message": "Video uploaded successfully!"}

    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}


# Run the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, timeout_keep_alive=600)