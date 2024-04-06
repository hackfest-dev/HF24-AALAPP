from audiocraft.models import musicgen
import torch
import soundfile as sf
import subprocess

model = musicgen.MusicGen.get_pretrained('small', device='cuda')

model.set_generation_params(duration=8)

model.lm.load_state_dict(torch.load('.\models\lm_final.pt'))

res = model.generate([
    'generate a carnatic music raaga with just violins in hindola'
],
    progress=True)
# Move the generated audio from GPU to CPU
res = res.cpu().numpy()

# Remove unnecessary dimensions
res = res.squeeze()  # Remove dimensions of size 1

# Save the audio to a file
output_file = 'generated_audio.wav'
sf.write(output_file, res, 32000)

# Play the audio using the default system player
subprocess.call(['start', output_file], shell=True)