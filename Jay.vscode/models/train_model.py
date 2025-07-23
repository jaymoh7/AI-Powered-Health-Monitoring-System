import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

# Realistic health data
# Format: [Heart Rate, Temperature (°C), Oxygen Level (%)]
X = np.array([
    [70, 36.6, 98],   # Healthy
    [72, 36.8, 97],   # Healthy
    [75, 36.9, 99],   # Healthy
    [90, 37.4, 96],   # Healthy
    [65, 36.5, 98],   # Healthy
    [85, 37.0, 97],   # Healthy

    [110, 38.5, 90],  # Unhealthy
    [120, 39.2, 85],  # Unhealthy
    [130, 40.0, 80],  # Unhealthy
    [50, 35.5, 91],   # Unhealthy
    [45, 34.8, 89],   # Unhealthy
    [95, 39.5, 88],   # Unhealthy
    [140, 41.0, 70],  # Unhealthy
    [60, 36.0, 92],   # Unhealthy
])

y = [
    "Healthy", "Healthy", "Healthy", "Healthy", "Healthy", "Healthy",
    "Unhealthy", "Unhealthy", "Unhealthy", "Unhealthy", "Unhealthy", "Unhealthy", "Unhealthy", "Unhealthy"
]

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the trained model
with open('health_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

print("✅ Model trained and saved successfully!")
