import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv("datasets/cleaned_claim_dataset.csv")

# Select features for anomaly detection
features = [
    "Claim_Amount",
    "Billing_Amount",
    "Approved_amount",
    "Length_of_Stay",
    "Documentation_Delay_Days",
    "Expected_Revenue"
]

X = df[features]

# Train Isolation Forest
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

df["Anomaly_Flag"] = model.fit_predict(X)

df["Anomaly_Flag"] = df["Anomaly_Flag"].map({1:0, -1:1})

anomaly_percentage = (df["Anomaly_Flag"].sum() / len(df)) * 100

print("Anomaly Detection Completed")
print("Total Anomalies Detected:", df["Anomaly_Flag"].sum())
print("Anomaly Percentage:", anomaly_percentage)

output = df[["Claim_ID","Anomaly_Flag"]]

output.to_csv("datasets/anomaly_flags.csv", index=False)