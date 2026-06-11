from fastapi import FastAPI
from pydantic import BaseModel
from src.db import conn, cursor
import joblib

app = FastAPI()

model = joblib.load("models/fraud_model.pkl")

class Transaction(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(data: Transaction):

    prediction = int(
        model.predict([data.features])[0]
    )

    print("Prediction:", prediction)

    cursor.execute(
        """
        INSERT INTO transactions(prediction)
        VALUES (%s)
        """,
        (prediction,)
    )

    conn.commit()

    print("Inserted into database")

    return {
        "fraud_prediction": prediction
    }