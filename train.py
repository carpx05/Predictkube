import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
import joblib

# Load the dataset
df = pd.read_excel("data_merged.xlsx", engine="openpyxl")

# Drop non-numeric/irrelevant columns
df = df.drop(columns=["Flow ID", "Src IP", "Dst IP", "Timestamp"])

# Separate features and label
X = df.drop(columns=["Label"])
y = df["Label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train XGBoost model
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate model
y_pred = model.predict(X_test_scaled)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save model and scaler
joblib.dump(model, "xgb_model.pkl")
joblib.dump(scaler, "scaler.pkl")
print("Model and scaler saved successfully.")