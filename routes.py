from fastapi import APIRouter
from ml_model.fraud_detection import predict_fraud

router = APIRouter()

@router.post("/predict")
def fraud(
amount:int,
velocity:int,
location_risk:int,
device_change:int
):

    result = predict_fraud(
        amount,
        velocity,
        location_risk,
        device_change
    )

    return {
        "Fraud":int(result)
    }