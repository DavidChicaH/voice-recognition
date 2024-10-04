from scipy.io import wavfile
from scipy.io.wavfile import read
from scipy.fft import fft, fftfreq
import numpy as np
from scipy.signal import butter, filtfilt, lfilter


def low_pass_filter(data, fc, fs, order = 5 ):
    nyquist = 0.5 * fs
    normal_fc = fc / nyquist
    b, a = butter(order,  normal_fc, btype='lowpass')
    y = lfilter(b, a, data)
    return y
def high_pass_filter(data, fc, fs, order = 5):
    nyquist = 0.5 * fs
    normal_fc = fc / nyquist
    b, a = butter(order,  normal_fc, btype='highpass')
    y = lfilter(b, a, data)
    return y
    

def process_audiofile(audiofile, filename):
    fs, audio = wavfile.read(audiofile)
    
    audio_fft = np.fft.fft(audio)
    frequencies =  np.fft.fftfreq(len(audio), 1/fs)
    
    magnitudes = np.abs(audio_fft)
    
    with open(f"./data/txt/{filename}.txt", 'w') as f:
        f.write("Frecuencia (Hz), Amplitud\n")
        for freq, mag in zip(frequencies, magnitudes):
            f.write(f"{freq},{mag}\n")

    print(f"Frequencies saved in {filename}.txt")