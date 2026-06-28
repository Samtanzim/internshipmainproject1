import os
import joblib
import pandas as pd

# Get the current folder (ml_model)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the trained model
rf = joblib.load(os.path.join(BASE_DIR, "random_forest.pkl"))

def predict_fraud(amount, velocity, location_risk, device_change):

    data = pd.DataFrame(
        [[amount, velocity, location_risk, device_change]],
        columns=[
            "amount",
            "velocity",
            "location_risk",
            "device_change"
        ]
    )

    prediction = rf.predict(data)

    return prediction[0]