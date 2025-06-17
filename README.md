# 🛡️ SafeNest Security API

SafeNest is an AI-powered smart home security system that integrates with Google Home devices.

It listens for sensor alerts like motion, door breach, or glass break,

and uses Gemini AI to determine threat levels (Low, Medium, High) — ensuring smarter, faster responses.

---

## 🧰 Tech Stack
```
-> Language:    Python 3.10
-> Framework:   FastAPI
-> AI: Gemini   Pro API (via Google MakerSuite)
-> Development: Render / Google Cloud Run
-> Testing:     Pytest
-> Docs:        Swagger UI (OpenAPI)
```
---

## 🚀 Features

- ✅ Real-time smart device alerts via REST API
- 🧠 Risk classification using Gemini Pro
- 🔒 Fully secured input validation & error handling
- 📦 Professional folder structure and tested API
- 🌍 Designed for mobile, speaker, and TV integration (breadth ✅)
- 🧪 `pytest` included with logs

---

## 📦 Folder Structure
```
SafeNest-Security-API/
│
├── app/
│   ├── __init__.py
│   ├── main.py                # FastAPI main app entry
│   ├── routes/
│   │   ├── __init__.py
│   │   └── device_alerts.py   # Endpoints for handling alerts
│   ├── services/
│   │   ├── __init__.py
│   │   └── gemini_risk.py     # Handles Gemini API integration & classification
│   ├── utils/
│   │   ├── __init__.py
│   │   └── logger.py          # Logger setup
│   └── models/
│       ├── __init__.py
│       └── alert_model.py     # Pydantic models for request/response
│
├── tests/
│   ├── __init__.py
│   └── test_main.py           # API unit tests
│
├── docs/
│   ├── SafeNest_Demo.mp4      # Demo video
│   └── README.pdf             # PDF version of documentation
│
├── .env.example               # Env config template
├── deployment.md              # Guide to deploy locally & on cloud
├── test_logs.txt              # Pytest output for proof
├── requirements.txt           # Python dependencies
├── README.md                  # Full project documentation
└── README.pdf                 # Same as above, for submission
```

---

## 🔧 Installation

```bash
git clone https://github.com/dragonwolf1o1/SafeNest-Security-API.git
cd SafeNest-Security-API
pip install -r requirements.txt
cp .env.example .env  # Add your Gemini API key
uvicorn app.main:app --reload
```

---

## 🚀 How to Use the API (Step-by-Step)

### Step 1: Send an Alert
#### &ensp;&ensp; POST /api/v1/alerts/send-alert
```
{
  "device_id": "sensor_frontdoor_01",
  "location": "Main Door",
  "event": "motion detected",
  "timestamp": "2025-06-08T19:30:00Z"
}
```

#### &ensp;&ensp; 🔁 Response:

```
{
  "device_id": "sensor_frontdoor_01",
  "location": "Main Door",
  "event": "motion detected",
  "threat_level": "Medium",
  "status": "Alert processed"
}
```

### Step 2: Test the API
```
pytest tests/
```

### Step 3: View Logs (Optional)
```
cat test_logs.txt
```
---

## 🏆 Challenge

**This project was developed as a submission for the:**
## Google Home API Developer Challenge 2025
```"Built for the Safety & Security theme, designed to protect homes using AI and cloud technology."```