import random
import pandas as pd

def generate_data(n=1000):
    data = {
        'heart_rate': [random.randint(50, 120) for _ in range(n)],
        'blood_pressure': [random.randint(90, 180) for _ in range(n)],
        'oxygen_saturation': [random.uniform(85.0, 100.0) for _ in range(n)]
    }
    df = pd.DataFrame(data)
    return df
