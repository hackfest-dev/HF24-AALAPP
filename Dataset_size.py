
import librosa
import os

# Directory where the WAV files are saved
output_directory = 'output'

# Iterate through the files in the directory
for file_name in os.listdir(output_directory):
    # Check if the file is a WAV file
    if file_name.endswith('.wav'):
        # Load the audio file
        file_path = os.path.join(output_directory, file_name)
        audio, sample_rate = librosa.load(file_path, sr=None)

        # Check the shape of the audio
        if audio.shape[0] == 32000 * 30:
            print(f"{file_name} has the correct shape: {audio.shape[0]}")
        else:
            print(f"{file_name} does not have the correct shape. Actual shape: {audio.shape[0]}")
