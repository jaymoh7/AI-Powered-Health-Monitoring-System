# 🧠 AI-Powered Health Monitoring System

![Project Banner](screenshots/banner.png)

> ⚕️ Real-time Health Assessment using AI – Fast, Smart, and Accessible Diagnostics

---

## 📌 Overview

The **AI-Powered Health Monitoring System** is a lightweight, web-based application that uses machine learning to evaluate basic human health vitals — **Heart Rate**, **Body Temperature**, and **Oxygen Saturation** — to determine whether a user is in a **Normal** or **Abnormal** health condition.

This solution is ideal for:
- Personal health checks
- Remote clinics
- Health education demos
- Hackathons & rapid prototypes

---

## 🚀 Features

✅ AI-based Prediction Model  
✅ Real-time Feedback  
✅ Lightweight Flask API  
✅ Simple Frontend UI  
✅ Easy to Deploy & Extend  
✅ Screenshot Gallery Included  

---

## 🖥️ Project Demo

📸 **Screenshots**:  
Check the `/screenshots` folder for:
- Input Form Interface  
- Output Predictions  
- Backend API Flow  
- Sample Error Handling

> 🔗 *(Optional)* Live demo or video walkthrough link can be added here

---

## 🧬 How It Works

1. **User Input**:  
   - Heart Rate (bpm)  
   - Body Temperature (°C)  
   - Oxygen Saturation (%)  

2. **ML Model Prediction**:  
   - Trained logic-based classifier makes an assessment  

3. **Output**:  
   - `Normal` or `Alert: Abnormal signs detected`

---

## 🧰 Tech Stack

| Layer      | Technologies                  |
|------------|-------------------------------|
| Frontend   | HTML, CSS, JavaScript         |
| Backend    | Python, Flask                 |
| AI Model   | scikit-learn, pandas          |
| Environment| Virtualenv (`health_env`)     |

---

## 🗂️ Project Structure

AI-Health-Monitoring-System/
│
├── api/
│ ├── app.py # Main Flask application
│ ├── model_trainer.py # (Optional) Train or tune your model
│ ├── health_model.pkl # Pre-trained model file
│ └── templates/
│ └── index.html # User interface
│
├── screenshots/ # UI and functionality captures
│
├── requirements.txt # Project dependencies
├── README.md # Project documentation
└── .gitignore # Ignored files


---

## ⚙️ Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/AI-Health-Monitoring-System.git
cd AI-Health-Monitoring-System
```
2. Create & Activate Virtual Environment
```
bash
python -m venv health_env
# Windows
health_env\Scripts\activate
# Linux/Mac
source health_env/bin/activate
```
3. Install Dependencies
```
bash
pip install -r requirements.txt
```
4. Run the Application
```
bash
cd api
python app.py
```
Visit http://localhost:5000 in your browser.

📊 Model Details
The AI model is a simple yet effective rule-based classifier that:

Labels a user as Normal if all 3 vital signs are within medically accepted healthy ranges.

Otherwise, labels as Alert.

You can later upgrade to a trained decision tree, SVM, or neural network using real health datasets.

🌐 Future Enhancements
🔄 Real-time sensor integration (e.g., wearable/IoT)

📱 Mobile version with React Native

🧠 Advanced deep learning model integration

🌍 Multilingual UI for global reach

🔔 Smart alerts + health logs

👨‍💻 Author
James Njoroge
AI-Powered Full Stack Developer | Data & Automation Specialist
🚀 NeuronCode Tech Agency

📝 License
This project is licensed under the MIT License – feel free to use, modify, and distribute.
```
⚠️ Disclaimer: This app is for educational/demo purposes and not a certified medical diagnostic tool.
