import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "churn_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")

DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "customer_churn.csv")