from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS (important for Vercel frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Input(BaseModel):
    symptoms: str


@app.get("/")
def home():
    return {"message": "Jeevan Rakshak AI running 🚑"}


# ✅ MAIN LOGIC
def analyze_symptoms(text):
    text = text.lower()

    # 🔴 CRITICAL
    critical_keywords = [
        "chest pain","heart attack","breathing difficulty","shortness of breath",
        "unconscious","fainting","severe bleeding","stroke","paralysis",
        "seizure","convulsion","cardiac arrest","blue lips","no pulse",
        "vomiting blood","coughing blood","head injury","fracture",
        "electric shock","burn severe","poison","overdose","suicide",

        # Hindi
        "सीने में दर्द","दिल का दौरा","सांस लेने में दिक्कत","बेहोश",
        "खून बहना","लकवा","दौरा","नीले होंठ","नाड़ी नहीं",

        # Gujarati
        "છાતીમાં દુખાવો","હાર્ટ એટેક","શ્વાસ લેવામાં તકલીફ","બેહોશ",
        "ખૂન વહેવું","લકવો","આંચકો","નીલા હોઠ","નાડી નથી"
    ]

    # 🟠 MODERATE
    moderate_keywords = [
        "fever","high fever","headache","migraine","vomiting","nausea",
        "diarrhea","stomach pain","back pain","joint pain","fatigue",
        "weakness","dizziness","cold","cough","sore throat","infection",

        # Hindi
        "बुखार","सिरदर्द","उल्टी","मतली","दस्त","पेट दर्द","खांसी",

        # Gujarati
        "તાવ","માથાનો દુખાવો","ઉલ્ટી","દસ્ત","પેટ દુખાવો","ખાંસી"
    ]

    # 🟢 MILD
    mild_keywords = [
        "tired","stress","anxiety","light pain","minor cold","runny nose",

        # Hindi
        "थकान","तनाव","हल्का दर्द",

        # Gujarati
        "થાક","તાણ","હલકો દુખાવો"
    ]

    # 🔴 CRITICAL RESPONSE
    for word in critical_keywords:
        if word in text:
            return {
                "level": "🚨 Critical",
                "advice": "Life-threatening emergency.\n\n"
                          "Advice: Go to hospital immediately.\n"
                          "Medicines: Do NOT self-medicate.\n"
                          "Precautions: Call ambulance immediately.\n\n"
                          "⚠️ Do not take any medicine without consulting a doctor."
            }

    # 🟠 MODERATE RESPONSE
    for word in moderate_keywords:
        if word in text:
            return {
                "level": "⚠️ Moderate",
                "advice": "Possible infection or illness.\n\n"
                          "Advice: Take rest and stay hydrated.\n"
                          "Medicines: Paracetamol, ORS.\n"
                          "Precautions: Monitor symptoms.\n\n"
                          "⚠️ Do not take any medicine without consulting a doctor."
            }

    # 🟢 MILD RESPONSE
    for word in mild_keywords:
        if word in text:
            return {
                "level": "✅ Mild",
                "advice": "Minor health issue.\n\n"
                          "Advice: Rest properly.\n"
                          "Medicines: Home remedies.\n"
                          "Precautions: Maintain healthy routine.\n\n"
                          "⚠️ Do not take any medicine without consulting a doctor."
            }

    # ❓ DEFAULT
    return {
        "level": "ℹ️ Unknown",
        "advice": "Condition unclear.\n\n⚠️ Please consult a doctor before taking any medication."
    }


# ✅ API ROUTE (VERY IMPORTANT)
@app.post("/analyze")
def analyze(data: Input):
    return analyze_symptoms(data.symptoms)
