"""Generate deterministic source signals for this fixture, not voice recordings."""

from studio import ROOT, synthesize, write_wav

for character in ("guide", "rival"):
    write_wav(ROOT / (character + ".wav"), synthesize("Fixed source for comparison.", character))

print("Created guide.wav and rival.wav from deterministic synthetic signals.")
