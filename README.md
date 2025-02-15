# **Model Monitoring Project**

This project demonstrates how to monitor machine learning models in production by detecting data drift, tracking model performance, and setting up alerts using tools like **FastAPI**, **Evidently AI**, **Prometheus**, and **Grafana**.

---

Note - Docker is needed on window machine
---

## **Overview**
The goal of this project is to:
- **Deploy a fraud detection model using FastAPI**.
- **Monitor data drift using Evidently AI**.
- **Set up alerts and visualize metrics using Prometheus and Grafana**.
- **Automate model retraining based on detected drift** (future enhancement).

---

## **Directory Structure**
```
model_monitoring/
│
├── data/                     # Folder for dataset files
│   └── fraud_data.csv        # Example dataset
│
├── models/                   # Folder for saving trained models
│   └── fraud_model.pkl       # Trained model file
│
├── app/                      # FastAPI application
│   ├── main.py               # FastAPI app to serve the model
│   └── requirements.txt      # Python dependencies for FastAPI
│
├── monitoring/               # Monitoring setup
│   ├── evidently_dashboard.py  # Evidently AI dashboard for data drift
│   ├── prometheus_config.yml   # Prometheus configuration
│   ├── grafana_dashboard.json  # Grafana dashboard JSON
│   └── simulate_metrics.py     # Script to simulate metrics for testing
│
├── notebooks/                # Jupyter notebooks for experimentation
│   └── train_model.ipynb     # Notebook to train and save the model
│
├── README.md                 # Project documentation
└── docker-compose.yml        # Docker Compose for running Prometheus and Grafana
```

---

## **Prerequisites**
Before running the project, ensure you have the following installed:
- **Python 3.8+**
- **Docker and Docker Compose**
- **Libraries:** Install dependencies from `app/requirements.txt` and `notebooks/requirements.txt`.

### **Install Python dependencies:**
```bash
pip install -r app/requirements.txt
pip install -r notebooks/requirements.txt
```

---

## **Setup Instructions**
### **1. Train the Model**
- Open the notebook `notebooks/train_model.ipynb`.
- Run all cells to preprocess the dataset, train the model, and save it to `models/fraud_model.pkl`.

### **2. Start the FastAPI Application**
Navigate to the `app/` directory and start the FastAPI server:
```bash
cd app
uvicorn main:app --reload
```
- The API will be available at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**.

### **3. Monitor Data Drift with Evidently AI**
Run the script to generate a data drift report:
```bash
python monitoring/evidently_dashboard.py
```
- The report will be saved as `monitoring/data_drift_report.html`. Open it in your browser to view the results.

### **4. Start Prometheus and Grafana**
Start the services using Docker Compose:
```bash
docker-compose up -d
```
- Access **Prometheus** at [http://localhost:9090](http://localhost:9090).
- Access **Grafana** at [http://localhost:3000](http://localhost:3000) (login with `admin/admin`).

### **5. Import the Grafana Dashboard**
- Go to **Grafana > Create > Import**.
- Upload `monitoring/grafana_dashboard.json` or paste its contents.
- Select the **Prometheus data source** and click **Import**.

### **6. Simulate Metrics for Testing**
Run the script to simulate metrics:
```bash
python monitoring/simulate_metrics.py
```
- This script exposes metrics at `http://localhost:8001/metrics`, which Prometheus will scrape.

---

## **Running the Application**
### **Test the FastAPI Endpoint**
Send a POST request to the `/predict` endpoint:
```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"V1": -1.35, "V2": 1.2, ...}'
```

### **View Metrics in Grafana**
- After importing the dashboard, you should see live updates of simulated metrics (e.g., **data drift score** and **model accuracy**).

---

## **Monitoring and Visualization**
| Tool | Purpose |
|------|---------|
| **Evidently AI** | Generates detailed reports on data drift. |
| **Prometheus** | Collects metrics from the application and simulated sources. |
| **Grafana** | Visualizes metrics in real-time dashboards. |

---

