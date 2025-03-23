
# AI/ML Model for Predicting Kubernetes Issues

## Phase 1 – Hackathon Submission | Team Envision

### Problem Statement
Kubernetes clusters can face failures such as:
- Pod crashes
- Resource bottlenecks (CPU, memory)
- Network issues (latency, congestion)

**Goal:** Build an AI/ML-based system to predict these issues before they happen using historical and real-time cluster metrics.

---

## Solution Overview
We created a machine learning pipeline and real-time microservice that:
- Trains an **XGBoost** model on labeled network metrics.
- Serves predictions via a **FastAPI** API.
- Is Dockerized and ready for real-time deployment.

---

## 1. Data Handling & EDA
- Labeled dataset with per-second network flow metrics.
- Performed EDA to visualize trends and class distribution.
- Outputs: heatmap, boxplots, statistics.

**Script:** `eda.py`

---

## 2. Model Training
- **Model:** XGBoost Classifier
- **Preprocessing:**
  - Dropped identifiers (IP, Flow ID, Timestamp)
  - Feature scaling with StandardScaler
- Trained on 80/20 split and saved using joblib.

**Script:** `train.py`

---

## 3. Inference API (FastAPI)
- POST `/predict`
- Accepts JSON payload:
```json
{
  "features": [list of 59 float values]
}
```
- Returns:
```json
{
  "prediction": 0 or 1
}
```

**File:** `main.py`  
**Model Files:** `xgb_model.pkl`, `scaler.pkl`

---

## 4. Dockerized Deployment
**Dockerfile includes:**
- Python base image
- All dependencies
- Model and API code

**Build & Run**
```bash
docker build -t pod-failure-api .
docker run -d -p 8000:8000 pod-failure-api
```

**Test API**
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [107, 137, 107, 21.4, ..., 0]}'
```

---

## 5. Real-Time Ready (Phase 2 Preview)
- Kafka-compatible architecture
- Prometheus/Grafana monitoring
- Ready for Kubernetes HPA and Operator automation

---

## Project Structure
```
pod_failure_detection/
├── train.py
├── eda.py
├── src/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
```

---

## Future Enhancements
- LSTM for time-sequence learning
- Kafka + Prometheus integration
- Auto-remediation with Kubernetes

