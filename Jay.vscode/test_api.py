import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "heart_rate": 85,
    "blood_pressure": 130,
    "oxygen_saturation": 95.2
}

response = requests.post(url, json=data)
print("API Response:", response.json())
