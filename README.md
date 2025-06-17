# 🛡️ SafeNest Security API

SafeNest is an AI-powered smart home security system that integrates with Google Home devices. It listens for sensor alerts like motion, door breach, or glass break, and uses Gemini AI to determine threat levels (Low, Medium, High) — ensuring smarter, faster responses.

---

## 🔗 Live Demo

- 📺 [Demo Video](docs/SafeNest_Demo.mp4)
- 🌐 API Endpoint: `http://localhost:8000/api/v1/alerts/send-alert`

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


---

## 🔧 Installation

```bash
git clone https://github.com/dragonwolf1o1/SafeNest-Security-API.git
cd SafeNest-Security-API
pip install -r requirements.txt
cp .env.example .env  # Add your Gemini API key
uvicorn app.main:app --reload
