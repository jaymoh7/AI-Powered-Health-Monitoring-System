from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

# Load the model safely
with open('health_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/api/analyze', methods=['POST'])
def analyze_health():
    data = request.get_json()

    try:
        heart_rate = float(data['heart_rate'])
        temperature = float(data['temperature'])
        oxygen_level = float(data['oxygen_level'])

        input_data = np.array([[heart_rate, temperature, oxygen_level]])
        prediction = model.predict(input_data)[0]

        status = "Normal" if prediction == 0 else "Alert: Abnormal signs detected"

        return jsonify({'result': status})

    except Exception as e:
        print("Error during analysis:", e)
        return jsonify({'result': 'Error processing data'}), 400

if __name__ == '__main__':
    app.run(debug=True)
