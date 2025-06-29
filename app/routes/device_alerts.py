from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.gemini_risk import classify_threat
from app.utils.logger import logger

router = APIRouter()

class AlertRequest(BaseModel):
    device_id: str
    location: str
    event: str  # e.g., "motion detected", "glass break", "door opened"
    timestamp: str

@router.post("/send-alert")
async def send_alert(alert: AlertRequest):
    try:
        logger.info(f"Received alert from device: {alert.device_id} - Event: {alert.event}")

        threat_level = classify_threat(alert.event) 

        response = {
            "device_id": alert.device_id,
            "location": alert.location,
            "event": alert.event,
            "threat_level": threat_level,
            "status": "Alert processed"
        }

        logger.info(f"Threat Level: {threat_level} | Location: {alert.location}")
        return response

    except Exception as e:
        logger.error(f"Error processing alert: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
