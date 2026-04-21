from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io
from app.predict import predict

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Image Classifier API is running"}

@app.post("/predict")
async def predict_api(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    label, confidence = predict(image)

    return {
        "prediction": label,
        "confidence": confidence
    }