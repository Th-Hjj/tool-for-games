"""Small offline audio authoring fixture. No TTS service or game runtime."""

import argparse
from array import array
import json
import math
from pathlib import Path
import wave

ROOT = Path(__file__).parent
RATE = 8000
CONTROLS = ("grit", "echo", "low")


def read_config():
    return json.loads((ROOT / "voices.json").read_text())


def synthesize(text, character):
    frequency = 160 + sum(map(ord, character)) % 80
    count = max(1600, min(len(text) * 180, RATE * 2))
    return [int(11000 * math.sin(2 * math.pi * frequency * i / RATE)
                + 2500 * math.sin(2 * math.pi * 900 * i / RATE))
            for i in range(count)]


def write_wav(path, samples):
    with wave.open(str(path), "wb") as stream:
        stream.setparams((1, 2, RATE, 0, "NONE", "not compressed"))
        stream.writeframes(array("h", samples).tobytes())


def read_wav(path):
    with wave.open(str(path), "rb") as stream:
        if stream.getnchannels() != 1 or stream.getsampwidth() != 2 or stream.getframerate() != RATE:
            raise ValueError("Expected mono 16-bit 8 kHz source")
        samples = array("h")
        samples.frombytes(stream.readframes(stream.getnframes()))
        return list(samples)


def process(samples, settings):
    result = []
    smooth = 0.0
    delay = RATE // 10
    for i, sample in enumerate(samples):
        grit = settings["grit"]
        driven = math.tanh(sample / 16000 * (1 + 5 * grit)) * 16000
        value = sample * (1 - grit) + driven * grit
        smooth = smooth * .88 + value * .12
        value = value * (1 - settings["low"]) + smooth * settings["low"]
        if i >= delay:
            value += samples[i - delay] * settings["echo"] * .5
        result.append(max(-32768, min(32767, int(value))))
    return result


def resolve(config, character, line_id, draft):
    voice = config["characters"][character]
    line = voice["lines"].get(line_id, {})
    return voice["defaults"] | draft | line.get("overrides", {})


def preview(character, line_id, text, draft, output):
    config = read_config()
    line = config["characters"][character]["lines"].get(line_id, {})
    settings = resolve(config, character, line_id, draft)
    if line.get("recording"):
        samples = read_wav(ROOT / line["recording"])
    else:
        samples = process(synthesize(text, character), settings)
    write_wav(output, samples)
    return {"output": str(output), "settings": settings}


def save_defaults(character, draft):
    config = read_config()
    config["characters"][character]["defaults"].update(draft)
    (ROOT / "voices.json").write_text(json.dumps(config, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--character", default="guide")
    parser.add_argument("--line", default="greeting")
    parser.add_argument("--text", default="A new line to compare.")
    parser.add_argument("--output", default="preview.wav")
    parser.add_argument("--save-defaults", action="store_true")
    for control in CONTROLS:
        parser.add_argument("--" + control, type=float)
    args = parser.parse_args()
    draft = {key: getattr(args, key) for key in CONTROLS if getattr(args, key) is not None}
    if any(not 0 <= value <= 1 for value in draft.values()):
        parser.error("Controls must be between 0 and 1")
    result = preview(args.character, args.line, args.text, draft, args.output)
    if args.save_defaults:
        save_defaults(args.character, draft)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
