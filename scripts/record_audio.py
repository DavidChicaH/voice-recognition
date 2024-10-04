import sounddevice as sd
from scipy.io.wavfile import write

def record_audiofile():
    fs = 44100  

    duration = int(input("Enter the duration of the recording in seconds: "))
    filename = input("Enter the filename: ")

    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')

    sd.wait()  

    write(f"./data/raw/{filename}.wav", fs, myrecording)  

    path_file = f"./data/raw/{filename}.wav";

    return path_file, filename

