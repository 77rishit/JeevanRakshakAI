from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Input(BaseModel):
    symptoms: str

def analyze_symptoms(text):
    text = text.lower()

    critical_keywords = [
        "chest pain", "breathing", "shortness of breath", "unconscious",
        "bleeding", "heavy bleeding", "heart attack", "stroke",
        "severe injury", "accident", "burn", "electric shock",
        "not breathing", "no pulse"
    ]

    moderate_keywords = [
        "fever", "vomiting", "dizziness", "infection", "pain",
        "headache", "migraine", "cough", "cold", "sore throat",
        "stomach pain", "body ache", "fatigue", "weakness",
        "diarrhea", "nausea"
    ]

    safe_keywords = [
        "mild headache", "tired", "stress", "light pain"
    ]

    for word in critical_keywords:
        if word in text:
            return {
                "level": "🚨 Critical",
                "advice": "Call ambulance immediately (Dial 108). Stay calm and do not delay medical help."
            }

    for word in moderate_keywords:
        if word in text:
            return {
                "level": "⚠ Moderate",
                "advice": "Consult a doctor soon. Monitor symptoms and take rest."
            }

    for word in safe_keywords:
        if word in text:
            return {
                "level": "✅ Safe",
                "advice": "Rest and stay hydrated. Seek help if condition worsens."
            }

    return {
        "level": "ℹ️ Unknown",
        "advice": "Unable to determine severity. Please consult a doctor."
    }

@app.post("/analyze")
def analyze(input: Input):
    return analyze_symptoms(input.symptoms)
