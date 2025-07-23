# 🧠 AI-Powered Health Monitoring System

An AI-driven web application that analyzes vital signs (heart rate, temperature, and oxygen level) to detect potential health anomalies in real-time. Built with Python (Flask), machine learning, and a responsive frontend.

---

## 📸 Screenshots

| Input Form | Result Display |
|------------|----------------|
| ![Input](screenshots/input.png) | ![Result](screenshots/result.png) |

---

## ⚙️ Features

- 🧠 Machine Learning for anomaly detection
- 🖥️ Simple & intuitive web interface
- 🔁 Real-time health status prediction
- 📊 Inputs: Heart Rate, Body Temperature (°C), Oxygen Level (%)
- 📡 REST API using Flask backend

---

## 🗂️ Project Structure
AI Software Project/
│
├── Jay.vscode/
│ └── api/
│ ├── app.py # Flask API backend
│ ├── train_model.py # ML model training script
│ ├── health_model.pkl # Trained machine learning model
│
├── index.html # Frontend UI
├── style.css # Styling for UI
├── script.js # Frontend JS logic
├── screenshots/ # Screenshots for documentation
│ ├── input.png
│ └── result.png
│
└── README.md # Project documentation


---

## 🚀 Getting Started

### 1. Clone the Project

```bash
git clone https://github.com/yourusername/health-monitoring-ai.git
cd "AI Software Project"

2. Set Up Virtual Environment (Optional but Recommended)

python -m venv health_env
.\health_env\Scripts\activate

Install Dependencies
pip install -r requirements.txt

pip install -r requirements.txt

pip install flask pandas scikit-learn
4. Train the Model (optional if you already have health_model.pkl)

cd Jay.vscode/api
python train_model.py

5. Run the Flask Server
python app.py
The server will run at: http://127.0.0.1:5000

🌐 Frontend Usage
Open index.html in your browser.

Enter Heart Rate, Temperature, and Oxygen Level.

Click Check Health.

The result will display your Health Status.

📡 API Endpoint
POST /api/analyze

Payload:
{
  "heart_rate": 70,
  "temperature": 36.6,
  "oxygen_level": 98
}

Response:

{
  "result": "Alert: Abnormal signs detected"
}

🧠 ML Model
Trained using synthetic logic or classification algorithm.

Features: heart_rate, temperature, oxygen_level

Output: Normal or Alert

You can improve the model by retraining with real datasets.

🛠️ Technologies Used
Frontend: HTML, CSS, JavaScript

Backend: Flask (Python)

Machine Learning: scikit-learn, pandas

Environment: Windows, VS Code, Python 3.10+

📝 License
This project is licensed under the MIT License.

🙌 Acknowledgments
Inspired by healthcare needs in developing real-time health diagnostics.

Developed as part of a 2-day rapid development challenge.

💡 Future Improvements
Add real-time data streaming from wearable devices

Add user authentication and health logs

Mobile app version (React Native)

Deployment to cloud (e.g., Render, Heroku, or AWS)


Let me know if you'd like me to auto-generate the `requirements.txt`, deployment guide, or add links to your socials/portfolio.


