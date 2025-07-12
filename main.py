import os
from pydub import AudioSegment
from pydub.effects import normalize


# === CONFIG ===
input_folder = r"C:\Users\ahmed\Desktop\Piano_pp_aiif\aiff_files"        # Replace with your .aiff folder
output_folder = r"C:\Users\ahmed\Desktop\Piano_pp_aiif\wav_files"       # Replace with your desired .wav output folder
clip_duration_ms = 1000                        # Try 50ms for a musical note, adjust as needed

# === SETUP ===
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".aiff", ".aif")):
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + ".wav"
        output_path = os.path.join(output_folder, output_filename)

        try:
            # Load AIFF
            audio = AudioSegment.from_file(input_path, format="aiff")

            # Slice to desired duration
            trimmed_audio = audio[:clip_duration_ms]

            # Normalize volume (auto-boosts to max without clipping)
            enhanced_audio = normalize(trimmed_audio)

            # Export to WAV
            enhanced_audio.export(output_path, format="wav")

            print(f"✅ Converted & normalized: {filename} → {output_filename} ({clip_duration_ms}ms)")

        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

print("\n🎯 All AIFF files processed and beautified.")
