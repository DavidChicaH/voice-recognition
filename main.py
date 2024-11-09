from scripts.record_audio import record_audiofile
from scripts.save_freq import save_frequencies
from scripts.freq_graph import freq_graph
from scripts.clean_voice import clean_voice
from scripts.extract_features import extract_mfccs
from scripts.extra import extract_features
from scripts.createUser import createUser

users = createUser()

duration = int(input("Enter the duration of the recording in seconds: "))
filename = input("Enter the filename: ")

audiofile, filename = record_audiofile(duration, filename)

cleaned_audio_file = clean_voice(audiofile, filename)

txt_file_path = f"./data/txt/{filename}.txt"

txt_cleaned_file_path = f"./data/txt/{filename}_cleaned.txt"

audio_data = save_frequencies(audiofile,cleaned_audio_file, filename)


#freq_graph(audiofile, cleaned_audio_file, txt_file_path, txt_cleaned_file_path)

# extract_mfccs(cleaned_audio_file)

extract_features(cleaned_audio_file, users)


while True:
    record = input("Do you want to record a new audio? (yes/no): ")
    if record == "yes":
        
        audiofile, filename = record_audiofile(duration, filename)

        cleaned_audio_file = clean_voice(audiofile, filename)

        txt_file_path = f"./data/txt/{filename}.txt"

        txt_cleaned_file_path = f"./data/txt/{filename}_cleaned.txt"

        audio_data = save_frequencies(audiofile,cleaned_audio_file, filename)


        #freq_graph(audiofile, cleaned_audio_file, txt_file_path, txt_cleaned_file_path)

        # extract_mfccs(cleaned_audio_file)

        extract_features(cleaned_audio_file, users)

    elif record == "no":
        exit()
    else:
        print("Invalid option, please try again")



