from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import device_alerts

app = FastAPI(
    title="SafeNest Security API",
    description="Smart Threat Detection using Google Home + Gemini AI",
    version="1.0.0"
)

# Allow CORS (for mobile/web integration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific domain(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all route modules
app.include_router(device_alerts.router, prefix="/api/v1/alerts", tags=["Alerts"])

@app.get("/")
def read_root():
    return {"message": "Welcome to SafeNest Security API!"}
