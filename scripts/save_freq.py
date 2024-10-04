import numpy as np
from scipy.io import wavfile

def save_frequencies(audiofile, cleaned_audiofile, filename):
    
    fs, audio = wavfile.read(audiofile)
    
    if(len(audio.shape) > 1):
        audio = np.mean(audio, axis=1)
    
    audio_fft = np.fft.fft(audio)
    frequencies =  np.fft.fftfreq(len(audio), 1/fs)
    
    magnitudes = np.abs(audio_fft)
    
    with open(f"./data/txt/{filename}.txt", 'w') as f:
        f.write("Frecuencia (Hz), Amplitud\n")
        for freq, mag in zip(frequencies, magnitudes):
            f.write(f"{freq},{mag}\n")
    
    
    clean_fs, clean_audio = wavfile.read(cleaned_audiofile)
    
    clean_audio_fft = np.fft.fft(clean_audio)
    clean_frequencies =  np.fft.fftfreq(len(clean_audio), 1/clean_fs)
    
    clean_magnitudes = np.abs(clean_audio_fft)
    
    with open(f"./data/txt/{filename}_cleaned.txt", 'w') as f:
        f.write("Frecuencia (Hz), Amplitud\n")
        for freq, mag in zip(clean_frequencies, clean_magnitudes):
            f.write(f"{freq},{mag}\n")

    print(f"Frequencies saved ")
