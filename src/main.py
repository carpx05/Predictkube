from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load model and scaler
model = joblib.load("xgb_model.pkl")
scaler = joblib.load("scaler.pkl")

class Metrics(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(data: Metrics):
    try:
        # Scale input
        input_scaled = scaler.transform([data.features])
        # Predict
        prediction = model.predict(input_scaled)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))