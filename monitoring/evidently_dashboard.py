import os
import pandas as pd
import joblib
# import webbrowser
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
from evidently.metrics import ClassificationQualityMetric  # ✅ Corrected import
from evidently import ColumnMapping  # ✅ Required for target & prediction mapping

# Get absolute paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Move up one level
DATA_PATH = os.path.join(BASE_DIR, "data", "fraud_data.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "fraud_model.pkl")
REPORT_PATH = os.path.join(BASE_DIR, "monitoring", "data_model_drift_report.html")

# Load dataset
df = pd.read_csv(DATA_PATH)

# Simulate reference and current datasets
reference_data = df.sample(1100, random_state=42)
current_data = df.sample(1100, random_state=123)

# Load trained model
with open(MODEL_PATH, "rb") as f:
    model = joblib.load(f)

# Prepare input and labels
X_reference = reference_data.drop(columns=["Class"])
y_reference = reference_data["Class"]
y_pred_reference = model.predict(X_reference)

X_current = current_data.drop(columns=["Class"])
y_current = current_data["Class"]
y_pred_current = model.predict(X_current)

# Add predictions to dataframes
reference_data["prediction"] = y_pred_reference
current_data["prediction"] = y_pred_current

# Define column mapping for Evidently
column_mapping = ColumnMapping(
    target="Class",  # The actual target column in the dataset
    prediction="prediction",  # The column where model predictions are stored
)

# Create Evidently AI report with Data Drift + Model Performance
report = Report(metrics=[
    DataDriftPreset(), 
    ClassificationQualityMetric()  # ✅ No arguments needed
])

report.run(reference_data=reference_data, current_data=current_data, column_mapping=column_mapping)

# Save and open report
report.save_html(REPORT_PATH)
# webbrowser.open("file://" + REPORT_PATH)

print(f"🚀 Data & Model Drift Report saved at: {REPORT_PATH}")
