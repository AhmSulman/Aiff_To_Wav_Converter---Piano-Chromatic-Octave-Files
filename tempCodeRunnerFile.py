for filename in os.listdir(input_folder):
    if filename.lower().endswith((".aiff", ".aif")):
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + ".wav"
        output_path = os.path.join(output_folder, output_filename)