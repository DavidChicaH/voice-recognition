import librosa
import numpy as np

def extract_features_for_prediction(audio_path):
    # Cargar el archivo de audio
    y, sr = librosa.load(audio_path, sr=None)

    # Extraer MFCC y sus derivadas
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_mean = np.mean(mfcc, axis=1)

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

    # Extraer Zero-Crossing Rate y Spectral Rolloff
    zcr = librosa.feature.zero_crossing_rate(y)
    zcr_mean = np.mean(zcr)

    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    rolloff_mean = np.mean(rolloff)

    # Combinar todas las características y asegurarse de que sea 2D
    features = np.hstack([mfcc_mean, delta_mfcc_mean, delta2_mfcc_mean, pitch_mean, energy_mean, zcr_mean, rolloff_mean])
    return features.reshape(1, -1)