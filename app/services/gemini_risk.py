import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("ENTER YOUR GEMINI API KEY HERE")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-pro")

async def classify_threat(event_text: str) -> str:
    """
    Classifies the security event using Gemini AI.
    Returns: Low, Medium, High
    """

    prompt = f"""
    Analyze the following smart home security event:
    Event: "{event_text}"

    Based on risk, classify as one of:
    - Low (minor, safe)
    - Medium (potential concern)
    - High (urgent danger)

    Only respond with one of: Low, Medium, High.
    """

    try:
        response = model.generate_content(prompt)
        risk = response.text.strip()

        if risk in ["Low", "Medium", "High"]:
            return risk
        else:
            return "Medium"  

    except Exception as e:
        print("Error with Gemini API:", str(e))
        return "Medium"
