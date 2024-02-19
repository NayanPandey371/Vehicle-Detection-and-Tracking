from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Run the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)