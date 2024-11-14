import sounddevice as sd
from scipy.io.wavfile import write

def record_audiofile(duration, filename):
    fs = 44100  

    print("Recording")
    
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')

    sd.wait()  

    write(f"./data/raw/{filename}.wav", fs, myrecording)  

    path_file = f"./data/raw/{filename}.wav";

    print("Audio recording complete , saved as " + path_file)
    return path_file, filename

