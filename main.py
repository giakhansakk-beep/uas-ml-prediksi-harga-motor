from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pickle
import numpy as np

app = FastAPI()

with open("model_harga.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/predict")
def predict(year: int):
    prediction = model.predict(np.array([[year]]))[0]

    if prediction < 30000:
        category = "Murah"
    elif prediction <= 70000:
        category = "Sedang"
    else:
        category = "Mahal"

    return {
        "year": year,
        "predicted_price": float(prediction),
        "category": category
    }
