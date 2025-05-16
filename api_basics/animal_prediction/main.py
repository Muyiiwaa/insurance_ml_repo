from fastapi import FastAPI,UploadFile, File, HTTPException
from pathlib import Path
import shutil
import os
from schema import UserResponse
from utils import predict_image
import uvicorn
import PIL


# init the app
app = FastAPI(
    title= "Animal Prediction API"
)

# set up the root endpoint
@app.get("/")
async def root():
    return {"message": "Hello!"}

# setup the image prediction endpoint
@app.post("/predict_image/", response_model=UserResponse)
def predict(file: UploadFile = File(..., description="Upload the animal image here")):
    try:
        temp_file = Path(f"temp_{file.filename}")
        with temp_file.open(mode = "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        pred_class, probs = predict_image(temp_file)

        temp_file.unlink()
    except PIL.UnidentifiedImageError as err:
        raise HTTPException(status_code=500, detail=f"Encountered error {err} are you sure you uploaded an image file")

    return UserResponse(
        predicted_class= pred_class,
        probability= probs
    )


if __name__ == "__main__":
    uvicorn.run("main:app", port = 8080, host = "localhost", reload = True)
