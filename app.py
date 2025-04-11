from flask import Flask, render_template, request, redirect, url_for, send_file
import os
from datetime import datetime
from fpdf import FPDF

app = Flask(__name__)

# Create logs folder if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Extended Disease database

# NOTE: This includes 50+ diseases with key symptoms (you can add more as needed)
disease_db = {
    "Common Cold": ["cough", "sore throat", "runny nose", "sneezing"],
    "Flu": ["fever", "headache", "muscle pain", "fatigue", "cough"],
    "COVID-19": ["fever", "dry cough", "fatigue", "loss of taste", "shortness of breath"],
    "Malaria": ["fever", "chills", "sweating", "nausea", "headache"],
    "Dengue": ["fever", "joint pain", "rash", "muscle pain", "headache"],
    "Typhoid": ["fever", "weakness", "abdominal pain", "constipation", "rash"],
    "Migraine": ["headache", "nausea", "sensitivity to light", "vomiting"],
    "Pneumonia": ["cough", "fever", "chest pain", "shortness of breath"],
    "Asthma": ["shortness of breath", "chest tightness", "wheezing", "cough"],
    "Gastroenteritis": ["diarrhea", "vomiting", "nausea", "fever"],
    "Hypertension": ["headache", "dizziness", "chest pain"],
    "Diabetes": ["frequent urination", "fatigue", "blurred vision"],
    "Tuberculosis": ["persistent cough", "weight loss", "fever", "night sweats"],
    "Allergic Rhinitis": ["sneezing", "runny nose", "itchy eyes"],
    "Bronchitis": ["cough", "mucus", "fatigue", "shortness of breath"],
    "Anemia": ["fatigue", "pale skin", "dizziness", "shortness of breath"],
    "Appendicitis": ["abdominal pain", "nausea", "vomiting", "fever"],
    "Chickenpox": ["rash", "fever", "fatigue", "itchy skin"],
    "Measles": ["rash", "fever", "cough", "runny nose"],
    "Mumps": ["swollen glands", "fever", "headache", "muscle aches"],
    "Hepatitis A": ["fatigue", "nausea", "abdominal pain", "loss of appetite"],
    "Hepatitis B": ["fatigue", "abdominal pain", "jaundice", "joint pain"],
    "Jaundice": ["yellowing of skin", "fatigue", "dark urine", "abdominal pain"],
    "UTI": ["burning urination", "frequent urination", "pelvic pain"],
    "Sinusitis": ["facial pain", "runny nose", "headache", "nasal congestion"],
    "Conjunctivitis": ["red eyes", "itchy eyes", "eye discharge"],
    "Scabies": ["intense itching", "rash", "sores"],
    "Ringworm": ["scaly skin", "itchy patches", "circular rash"],
    "Psoriasis": ["scaly patches", "itching", "dry skin"],
    "Arthritis": ["joint pain", "stiffness", "swelling"],
    "Depression": ["fatigue", "loss of interest", "sadness", "sleep problems"],
    "Anxiety": ["restlessness", "rapid heartbeat", "nervousness", "fatigue"],
    "Food Poisoning": ["vomiting", "diarrhea", "abdominal cramps", "fever"],
    "Heat Stroke": ["high fever", "dry skin", "confusion", "rapid pulse"],
    "Lung Cancer": ["persistent cough", "weight loss", "chest pain"],
    "Skin Cancer": ["new mole", "changing mole", "bleeding mole"],
    "Stomach Ulcer": ["abdominal pain", "nausea", "bloating"],
    "Tonsillitis": ["sore throat", "swollen tonsils", "fever"],
    "Vertigo": ["dizziness", "loss of balance", "nausea"],
    "Gallstones": ["abdominal pain", "nausea", "vomiting"],
    "Kidney Stones": ["back pain", "blood in urine", "frequent urination"],
    "Pancreatitis": ["upper abdominal pain", "fever", "nausea"],
    "Liver Cirrhosis": ["fatigue", "easy bruising", "swelling abdomen"],
    "Thyroid Disorder": ["fatigue", "weight gain/loss", "mood swings"],
    "Epilepsy": ["seizures", "confusion", "loss of consciousness"],
    "Obesity": ["fatigue", "joint pain", "shortness of breath"],
    "Stroke": ["numbness", "confusion", "trouble speaking"],
    "Parkinson's Disease": ["tremors", "slow movement", "balance issues"],
    "Alzheimer's": ["memory loss", "confusion", "difficulty thinking"],
    "Celiac Disease": ["bloating", "diarrhea", "fatigue"],
    "IBS": ["abdominal pain", "bloating", "constipation", "diarrhea"]
}

distinct_symptoms = sorted(set(sym for sym_list in disease_db.values() for sym in sym_list))

def save_log(selected_symptoms, diagnosis):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_content = f"Time: {timestamp}\nSymptoms: {', '.join(selected_symptoms)}\nDiagnosis: {diagnosis}\n\n"
    with open(f"logs/{timestamp}.txt", "w") as log_file:
        log_file.write(log_content)

def create_pdf(diagnosis):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, diagnosis)
    file_path = "diagnosis.pdf"
    pdf.output(file_path)
    return file_path

@app.route("/", methods=["GET", "POST"])
def index():
    diagnosis = ""
    selected_symptoms = []
    if request.method == "POST":
        selected_symptoms = request.form.getlist("symptoms")
        if not selected_symptoms:
            diagnosis = "No symptoms selected. Please try again."
        else:
            disease_scores = {
                disease: len(set(selected_symptoms) & set(symptoms)) / len(symptoms)
                for disease, symptoms in disease_db.items()
            }
            sorted_diseases = sorted(disease_scores.items(), key=lambda x: x[1], reverse=True)
            if sorted_diseases[0][1] == 0:
                diagnosis = "No close match found. Please consult a medical professional."
            else:
                diagnosis = f"Most likely: {sorted_diseases[0][0]} ({round(sorted_diseases[0][1]*100)}% match)\nOther possibilities:\n"
                for disease, score in sorted_diseases[1:4]:
                    if score > 0:
                        diagnosis += f"- {disease} ({round(score*100)}% match)\n"

            save_log(selected_symptoms, diagnosis)

    return render_template("index.html", symptoms=distinct_symptoms, diagnosis=diagnosis, selected_symptoms=selected_symptoms)

@app.route("/download")
def download_pdf():
    diagnosis = request.args.get("text", "No diagnosis available")
    file_path = create_pdf(diagnosis)
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
