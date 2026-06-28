import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import joblib

df = pd.read_csv("../dataset/upi_transactions.csv")

X = df.drop("fraud",axis=1)
y = df["fraud"]

X_train,X_test,y_train,y_test = train_test_split(
X,y,test_size=0.2,random_state=42
)

rf = RandomForestClassifier()
rf.fit(X_train,y_train)

xgb = XGBClassifier()
xgb.fit(X_train,y_train)

joblib.dump(rf,"random_forest.pkl")
joblib.dump(xgb,"xgboost_model.pkl")

print("Models Trained")