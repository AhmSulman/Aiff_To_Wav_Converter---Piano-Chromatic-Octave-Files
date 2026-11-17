# AIFF → WAV Piano Sample Converter

A small Python batch tool that converts a folder of `.aiff` piano samples into trimmed, volume-normalised `.wav` files ready for web and app playback.

The repo also contains the output: **87 chromatic piano notes** (`Piano.pp.<Note><Octave>.wav`, pianissimo dynamic) in `Piano/`. These are the samples used by the piano tools in [Octave Live Wire](https://github.com/AhmSulman/Octave_Live_Wire).

## What it does

For every `.aiff` / `.aif` file in the input folder, it:
1. Loads the file with `pydub`
2. Trims it to `clip_duration_ms` (default 1000 ms)
3. Normalises loudness to peak without clipping
4. Exports it as `.wav` with the same base name

## Usage

```bash
pip install pydub        # also needs ffmpeg on PATH
```

Set `input_folder`, `output_folder` and `clip_duration_ms` at the top of `main.py`, then run:

```bash
python main.py
```

## License

AGPL-3.0
