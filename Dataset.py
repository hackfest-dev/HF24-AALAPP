import os
import random
from pydub import AudioSegment

import soundfile as sf
import numpy as np

def process_audio(file_path, output_dir, segment_length=30):
    # Load audio file
    audio = AudioSegment.from_file(file_path)

    # Get file name without extension for caption
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # Convert segment length to milliseconds
    segment_length_ms = segment_length * 1000

    # Set the sample rate to 32000 Hz
    audio = audio.set_frame_rate(32000)

    # Calculate the number of segments
    num_segments = (len(audio) + segment_length_ms - 1) // segment_length_ms

    # Loop through segments
    for i in range(num_segments):
        # Get start time for the segment
        start_time = i * segment_length_ms

        # If this is the last segment, adjust start_time
        if i == num_segments - 1:
            start_time = len(audio) - segment_length_ms

        # Get end time for the segment
        end_time = start_time + segment_length_ms

        # Extract the segment
        segment = audio[start_time:end_time]

        # Save the segment
        segment.export(os.path.join(output_dir, f'segment_{i:03d}.wav'), format='wav')

        # Save the caption
        with open(os.path.join(output_dir, f'segment_{i:03d}.txt'), 'w') as f:
            f.write(file_name)


# Folder names
input_folder_name = "raw"
output_folder_name = "output"

if not os.path.exists(input_folder_name):
    os.makedirs(input_folder_name)
    print(f"'{input_folder_name}' folder created.")

if not os.path.exists(output_folder_name):
    os.makedirs(output_folder_name)
    print(f"'{output_folder_name}' folder created.")


# Directory setup
output_directory = 'output'
samples_directory = 'raw'

# Check if the output directory exists, if not, create it
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Iterate through the files in the "samples" directory
for file_name in os.listdir(samples_directory):
    if file_name.endswith('.wav') or file_name.endswith('.mp3'):
        file_path = os.path.join(samples_directory, file_name)
        process_audio(file_path, output_directory, segment_length=30)