from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Input(BaseModel):
    symptoms: str
    lang: str


@app.get("/")
def home():
    return {"message": "Jeevan Rakshak AI running 🚑"}


@app.post("/analyze")
def analyze(data: Input):

    text = data.symptoms.lower()
    lang = data.lang

    # 🔴 CRITICAL
    if "chest" in text or "heart" in text:
        if lang == "hi":
            return {
                "level": "🚨 गंभीर",
                "advice": "संभावित स्थिति: गंभीर समस्या\n\nसलाह:\nतुरंत अस्पताल जाएं\n\nदवाएं:\nखुद दवा न लें\n\n⚠️ डॉक्टर से सलाह लें"
            }
        elif lang == "gu":
            return {
                "level": "🚨 ગંભીર",
                "advice": "સંભવિત સ્થિતિ: ગંભીર સમસ્યા\n\nસલાહ:\nતાત્કાલિક હોસ્પિટલ જાઓ\n\nદવાઓ:\nખુદ દવા ન લો\n\n⚠️ ડોક્ટરની સલાહ લો"
            }
        else:
            return {
                "level": "🚨 Critical",
                "advice": "Possible Condition: Serious issue\n\nAdvice:\nGo to hospital immediately\n\nMedicines:\nDo NOT self-medicate\n\n⚠️ Consult a doctor"
            }

    # 🟠 MODERATE
    if "fever" in text or "cold" in text or "cough" in text:
        if lang == "hi":
            return {
                "level": "⚠️ मध्यम",
                "advice": "संभावित स्थिति: संक्रमण\n\nसलाह:\nआराम करें और पानी पिएं\n\nदवाएं:\nपैरासिटामोल, ओआरएस\n\n⚠️ डॉक्टर से सलाह लें"
            }
        elif lang == "gu":
            return {
                "level": "⚠️ મધ્યમ",
                "advice": "સંભવિત સ્થિતિ: સંક્રમણ\n\nસલાહ:\nઆરામ કરો અને પાણી પીવો\n\nદવાઓ:\nપેરાસીટામોલ, ઓઆરએસ\n\n⚠️ ડોક્ટરની સલાહ લો"
            }
        else:
            return {
                "level": "⚠️ Moderate",
                "advice": "Possible Condition: Infection\n\nAdvice:\nTake rest and stay hydrated\n\nMedicines:\nParacetamol, ORS\n\n⚠️ Consult a doctor"
            }

    # 🟢 MILD
    if "tired" in text or "stress" in text:
        if lang == "hi":
            return {
                "level": "✅ हल्का",
                "advice": "संभावित स्थिति: सामान्य समस्या\n\nसलाह:\nआराम करें\n\n⚠️ डॉक्टर से सलाह लें"
            }
        elif lang == "gu":
            return {
                "level": "✅ હળવું",
                "advice": "સંભવિત સ્થિતિ: સામાન્ય સમસ્યા\n\nસલાહ:\nઆરામ કરો\n\n⚠️ ડોક્ટરની સલાહ લો"
            }
        else:
            return {
                "level": "✅ Mild",
                "advice": "Possible Condition: Minor issue\n\nAdvice:\nTake rest\n\n⚠️ Consult a doctor"
            }

    return {
        "level": "ℹ️ Unknown",
        "advice": "Consult a doctor"
    }
