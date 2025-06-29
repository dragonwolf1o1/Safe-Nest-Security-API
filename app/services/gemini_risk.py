import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

# ✅ STEP 1: Load environment variables from .env
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

# ✅ STEP 2: Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
print("✅ Loaded API key:", api_key)

if not api_key or "ENTER YOUR GEMINI" in api_key:
    raise ValueError("❌ GEMINI_API_KEY not found or invalid. Please fix your .env file.")

# ✅ STEP 3: Configure Gemini client
genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-2.0-flash")  # or whichever works from list_models


# ✅ STEP 4: Define threat classifier function
def classify_threat(event_text: str) -> str:
    try:
        prompt = f"""
        You are an AI security threat classifier. Based on the following smart home event, classify the threat level.

        Event: \"{event_text}\"

        Respond with only one word: Low, Medium, or High.
        Do not add any punctuation, quotes, or explanation.
        """

        print("⏩ Prompt sent to Gemini:\n", prompt)

        response = model.generate_content(prompt)
        print("⏪ Raw Gemini response:\n", response.text)

        result = response.text.strip().capitalize()
        print("🎯 Parsed response:", result)

        if result in ["Low", "Medium", "High"]:
            return result
        else:
            print("⚠️ Unexpected response format:", result)
            return "Medium"  # fallback

    except Exception as e:
        print("❌ Gemini error:", str(e))
        return "Medium"
