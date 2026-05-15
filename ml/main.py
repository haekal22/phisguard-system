from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from predict_model import predict_for_backend
import logging

app = FastAPI(title="Phisguard ML API")

class PredictRequest(BaseModel):
    message: str

@app.post("/predict")
def predict(req: PredictRequest):
    if not req.message or not req.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    try:
        result = predict_for_backend(req.message)
        return result
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail="Internal ML Error")

@app.get("/")
def read_root():
    return {"status": "ML API is running"}
