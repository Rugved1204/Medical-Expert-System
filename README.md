# 🧠 Smart Medical Expert System

This is a **Flask-based web application** that functions as a simple expert system to predict the most likely diseases based on selected symptoms. It supports over **50 diseases**, generates intelligent match scores, and allows PDF download of the result.


## 🚀 Features

- 🔍 Intelligent symptom-based disease prediction  
- ✅ Match scoring logic with multiple possible conditions  
- 🖥️ Clean HTML frontend with Flask backend  
- 📄 Diagnosis PDF download  
- 🗂️ Logging of user results for future use  


## 🛠️ Technologies Used

- Python 3.x  
- Flask  
- HTML & CSS (Jinja2 templating)  
- FPDF (for PDF generation)  


## 📂 Project Structure

medical-expert-system/
├── app.py                 # Main Flask app
├── templates/
│   └── index.html         # Frontend UI
├── logs/                  # User session logs
├── diagnosis.pdf          # Generated PDF (auto-created)
├── .gitignore
└── README.md


## 🧪 How It Works

1. User selects symptoms from a checklist.  
2. The backend compares symptoms to a disease database.  
3. Scores are computed based on symptom matches.  
4. The most probable disease is displayed, with alternatives.  
5. User can download the diagnosis as a PDF.  

## 💻 Run Locally

### Step 1: Clone the Repository


git clone https://github.com/your-username/medical-expert-system.git
cd medical-expert-system

### Step 2: Install Dependencies

pip install flask fpdf


### Step 3: Run the Flask App

python app.py


Then open your browser and go to:

http://127.0.0.1:5000

## 🧾 Sample Output


Most likely: - Flu (80% match)
Other possibilities:
- COVID-19 (60% match)
- Common Cold (40% match)




## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).


## 👨‍⚕️ Disclaimer

This tool is **not a substitute** for professional medical advice, diagnosis, or treatment.  
Always seek the guidance of a qualified healthcare provider.



## 🌐 Created by

Rugved Gaikwad
Connect with me on Linkedin : www.linkedin.com/in/rugvedgaikwad


