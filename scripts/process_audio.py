from scipy.io.wavfile import read
from scipy.fft import fft, fftfreq
import numpy as np
from scipy.signal import butter, filtfilt


def low_pass_filter(data, fc, fs):
    b, a = butter(4, fc / (0.5 * fs), btype='lowpass')
    return filtfilt(b, a, data)

def high_pass_filter(data, fc, fs):
    b, a = butter(4, fc / (0.5 * fs), btype='highpass')
    return filtfilt(b, a, data)
    

def process_audiofile(path_file):
    fs, data = read(path_file)

    data = data.flatten()

    fft_data = fft(data)
    
    frequencies = fftfreq(len(data), 1/fs)

    idx_positive_frequencies = (frequencies > 0) & (frequencies <= 500)
    positive_frequencies = frequencies[idx_positive_frequencies]
    positive_amplitudes = np.abs(fft_data[idx_positive_frequencies])
    
        
    fc_low = 1000
    low_data = low_pass_filter(data, fc_low, fs)
    fft_low = fft(low_data)
    low_amplitudes = np.abs(fft_low[idx_positive_frequencies])
    
    
    fc_high = 500
    high_data = high_pass_filter(data, fc_high, fs)
    fft_high = fft(high_data)
    high_amplitudes = np.abs(fft_high[idx_positive_frequencies])



    return positive_frequencies, positive_amplitudes, low_amplitudes, high_amplitudes