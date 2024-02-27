import sys
sys.path.insert(0, './model')

from fastapi import FastAPI, UploadFile, File
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import torch
import os
# Create a list of allowed origins
origins = ["http://localhost:5173"]

app = FastAPI()
print(torch.__version__)

model_path = './model/best.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
print(model)
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



@app.post("/upload-video")
async def upload_video(video: UploadFile = File(...)):
    try:
        content = await video.read()

        # # Save the video file (replace with your desired logic)
        # with open(f"uploads/{video.filename}", "wb") as f:
        #     f.write(content)
        print(video.filename)
        return {"message": "Video uploaded successfully!"}

    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}


# Run the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)