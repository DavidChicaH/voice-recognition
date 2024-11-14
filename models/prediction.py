import joblib
import pandas as pd
import numpy as np
from scripts.extract_and_test_features import extract_features_for_prediction

def predict():
    # Extraer características
    features = extract_features_for_prediction('./data/cleaned/prediction_audio_test.wav')
    
    # Convertir a DataFrame
    features_df = pd.DataFrame(features)

    # Cargar el scaler
    scaler = joblib.load('./models/scaler.pkl')
    features_normalized = scaler.transform(features_df)

    # Cargar el modelo
    model = joblib.load('./models/svm_model.pkl')

    # Obtener la predicción
    prediction = model.predict(features_normalized)
    probabilities = model.predict_proba(features_normalized)

    # Umbral de confianza
    max_prob = np.max(probabilities)
    if max_prob >= 0.6:
        user_id = prediction[0]
        print(f"ID de usuario predicho: {user_id} (Confianza: {max_prob*100:.2f}%)")
    else:
        print("La voz no coincide con ninguno de los usuarios registrados.")
