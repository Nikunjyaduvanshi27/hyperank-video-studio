"""Synthesize the film's own SFX (own work, no third-party rights): python sfx.py -> assets/audio/sfx/{swell,air,sparkle}.wav"""
from pathlib import Path
import numpy as np
import soundfile as sf

SR = 48000
OUT = Path(__file__).resolve().parent / "assets/audio/sfx"
rng = np.random.default_rng(20261019)


def lowpass(x, fc):
    """one-pole low-pass; fc may vary per sample"""
    a = np.exp(-2 * np.pi * np.broadcast_to(fc, x.shape) / SR)
    y, acc = np.empty_like(x), 0.0
    for i in range(len(x)):
        acc = (1 - a[i]) * x[i] + a[i] * acc
        y[i] = acc
    return y


def env(n, a, r):
    e = np.ones(n); ka, kr = int(a * SR), int(r * SR)
    e[:ka] = np.linspace(0, 1, ka) ** 2; e[-kr:] *= np.linspace(1, 0, kr) ** 2
    return e


# low air: soft brown noise, the room before the question
n = int(5.0 * SR)
air = lowpass(np.cumsum(rng.standard_normal(n)) * 0.02, 380.0)
air -= lowpass(air, 30.0)
air = air / np.abs(air).max() * 0.22 * env(n, 1.2, 1.8)
sf.write(OUT / "air.wav", np.stack([air, np.roll(air, 240)], 1), SR)

# the reveal swell: filtered noise opening up plus a rising two-voice pad, cresting into a soft bloom
n = int(3.4 * SR); t = np.arange(n) / SR
rise = np.clip(t / 2.6, 0, 1)
noise = lowpass(rng.standard_normal(n), 200 + 5200 * rise ** 2.2) * (0.15 + 0.85 * rise ** 1.6)
f0 = 110 * 2 ** (rise * 7 / 12)
pad = sum(np.sin(2 * np.pi * np.cumsum(f0 * m) / SR + p) * g for m, p, g in ((1, 0, 0.5), (1.5, 1.1, 0.3), (2.003, 2.0, 0.22), (3.01, 0.5, 0.08)))
pad *= rise ** 1.4
bloom = np.where(t > 2.6, np.exp(-(t - 2.6) * 2.4), 0) * np.sin(2 * np.pi * 58 * t) * 0.5
x = 0.55 * noise / np.abs(noise).max() + 0.45 * pad / np.abs(pad).max() + bloom
x *= env(n, 0.05, 0.75)
x = x / np.abs(x).max() * 0.8
sf.write(OUT / "swell.wav", np.stack([x, np.roll(x, 360)], 1), SR)

# a soft shimmer for the mark resolving
n = int(1.6 * SR); t = np.arange(n) / SR
sh = sum(np.sin(2 * np.pi * f * t) * np.exp(-t * d) * g for f, d, g in ((1568, 3.2, 0.5), (2093, 3.8, 0.35), (2637, 4.4, 0.25), (3136, 5.0, 0.18), (1046, 2.6, 0.3)))
sh *= env(n, 0.012, 0.4)
sh = sh / np.abs(sh).max() * 0.5
sf.write(OUT / "sparkle.wav", np.stack([sh, np.roll(sh, 180)], 1), SR)
print("ok")
