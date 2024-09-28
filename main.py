from scripts.record_audio import record_audiofile
from scripts.process_audio import transform_audio

audiofile, filename = record_audiofile()

transform_audio(audiofile, filename)


