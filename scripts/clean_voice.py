import noisereduce as nr
import librosa.display
import soundfile as sf
import numpy as np

def clean_voice(audio_path, filename):
    audio, sr = librosa.load(audio_path)
    
    reduced_noise = nr.reduce_noise(y=audio, sr=sr)
    
    sf.write(f"./data/cleaned/{filename}.wav", reduced_noise, sr, 'PCM_24')
    
    return f"./data/cleaned/{filename}.wav"
