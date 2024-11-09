import librosa
import numpy as np
import pandas as pd
import os

def extract_features(audio_path, user, output_csv='./data/csv/audio_features.csv'):
    # Cargar el archivo de audio
    y, sr = librosa.load(audio_path, sr=None)

    # Extraer MFCC
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_mean = np.mean(mfcc, axis=1)

    # Extraer Delta y Delta-Delta de MFCC
    delta_mfcc = librosa.feature.delta(mfcc)
    delta_mfcc_mean = np.mean(delta_mfcc, axis=1)

    delta2_mfcc = librosa.feature.delta(mfcc, order=2)
    delta2_mfcc_mean = np.mean(delta2_mfcc, axis=1)

    # Extraer Pitch (Frecuencia Fundamental)
    pitch = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))
    pitch_mean = np.nanmean(pitch) if pitch is not None else np.nan

    # Extraer Energía
    energy = librosa.feature.rms(y=y)
    energy_mean = np.mean(energy)

    # Extraer Zero-Crossing Rate
    zcr = librosa.feature.zero_crossing_rate(y)
    zcr_mean = np.mean(zcr)

    # Extraer Spectral Rolloff
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    rolloff_mean = np.mean(rolloff)

    # Crear un diccionario con los nombres de las columnas y las características extraídas
    data = {
        'user_id': user[0]["id"],
        'mfcc_1': [mfcc_mean[0]], 'mfcc_2': [mfcc_mean[1]], 'mfcc_3': [mfcc_mean[2]],
        'mfcc_4': [mfcc_mean[3]], 'mfcc_5': [mfcc_mean[4]], 'mfcc_6': [mfcc_mean[5]],
        'mfcc_7': [mfcc_mean[6]], 'mfcc_8': [mfcc_mean[7]], 'mfcc_9': [mfcc_mean[8]],
        'mfcc_10': [mfcc_mean[9]], 'mfcc_11': [mfcc_mean[10]], 'mfcc_12': [mfcc_mean[11]],
        'mfcc_13': [mfcc_mean[12]],

        'delta_mfcc_1': [delta_mfcc_mean[0]], 'delta_mfcc_2': [delta_mfcc_mean[1]],
        'delta_mfcc_3': [delta_mfcc_mean[2]], 'delta_mfcc_4': [delta_mfcc_mean[3]],
        'delta_mfcc_5': [delta_mfcc_mean[4]], 'delta_mfcc_6': [delta_mfcc_mean[5]],
        'delta_mfcc_7': [delta_mfcc_mean[6]], 'delta_mfcc_8': [delta_mfcc_mean[7]],
        'delta_mfcc_9': [delta_mfcc_mean[8]], 'delta_mfcc_10': [delta_mfcc_mean[9]],
        'delta_mfcc_11': [delta_mfcc_mean[10]], 'delta_mfcc_12': [delta_mfcc_mean[11]],
        'delta_mfcc_13': [delta_mfcc_mean[12]],

        'delta2_mfcc_1': [delta2_mfcc_mean[0]], 'delta2_mfcc_2': [delta2_mfcc_mean[1]],
        'delta2_mfcc_3': [delta2_mfcc_mean[2]], 'delta2_mfcc_4': [delta2_mfcc_mean[3]],
        'delta2_mfcc_5': [delta2_mfcc_mean[4]], 'delta2_mfcc_6': [delta2_mfcc_mean[5]],
        'delta2_mfcc_7': [delta2_mfcc_mean[6]], 'delta2_mfcc_8': [delta2_mfcc_mean[7]],
        'delta2_mfcc_9': [delta2_mfcc_mean[8]], 'delta2_mfcc_10': [delta2_mfcc_mean[9]],
        'delta2_mfcc_11': [delta2_mfcc_mean[10]], 'delta2_mfcc_12': [delta2_mfcc_mean[11]],
        'delta2_mfcc_13': [delta2_mfcc_mean[12]],

        'pitch_mean': [pitch_mean],
        'energy_mean': [energy_mean],
        'zcr_mean': [zcr_mean],
        'rolloff_mean': [rolloff_mean],
    }
    
    

    # Convertir a DataFrame
    df = pd.DataFrame(data)

    # Verificar si el archivo ya existe para añadir nuevas filas en lugar de sobrescribir
    if os.path.exists(output_csv):
        df.to_csv(output_csv, mode='a', header=False, index=False)
    else:
        df.to_csv(output_csv, index=False)
        
    print(f"Características de audio guardadas en '{output_csv}'")

