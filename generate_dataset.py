import pandas as pd
import random

data = []

for i in range(10000):
    amount = random.randint(100,50000)
    velocity = random.randint(1,20)
    location_risk = random.randint(0,1)
    device_change = random.randint(0,1)

    fraud = 1 if (
        amount > 20000 and
        velocity > 10
    ) else 0

    data.append([
        amount,
        velocity,
        location_risk,
        device_change,
        fraud
    ])

df = pd.DataFrame(data,
columns=[
'amount',
'velocity',
'location_risk',
'device_change',
'fraud'
])

df.to_csv("upi_transactions.csv",index=False)

print("Dataset Created")