import librosa

def transform_audio(audiofile, filename):
    y, sr = librosa.load(audiofile)

    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    with open(f"./data/txt/{filename}.txt", "w") as f:
        f.write(y)
