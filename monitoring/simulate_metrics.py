from prometheus_client import start_http_server, Gauge
import time
import random

# Define metrics
data_drift_score = Gauge('data_drift_score', 'Data Drift Score')
model_accuracy = Gauge('model_accuracy', 'Model Accuracy')

# Start Prometheus HTTP server
start_http_server(8001)

# Simulate metric updates
while True:
    data_drift_score.set(random.uniform(0, 1))  # Random drift score
    model_accuracy.set(random.uniform(0.8, 1))  # Random accuracy
    time.sleep(4)  # Update every 10 seconds