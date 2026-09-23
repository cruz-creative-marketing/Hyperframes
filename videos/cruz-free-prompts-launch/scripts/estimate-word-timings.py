#!/usr/bin/env python3
"""Estimate word timings for the Kokoro narration (no Whisper available offline).

Each line is split into phrases; ffmpeg silencedetect finds the pauses, and each
phrase is mapped onto one speech segment. Words are spread through their segment
by character length. Display text is normalised for captions (numbers, URL).
Run from the project root: python3 scripts/estimate-word-timings.py
"""
import json, re, subprocess

LINES = {
    1: [["Your", "AI", "content…"], ["looks", "like", "AI", "content."]],
    2: [["Same", "AI."], ["Better", "prompt."], ["Now", "it", "looks", "like", "your", "brand."]],
    3: [["Cruz", "Creative", "just", "made", "its", "15", "client-tested", "prompts…"], ["free."]],
    4: [["On-brand", "graphics."], ["A", "voice", "that", "sounds", "like", "you."],
        ["Product", "shots", "that", "save", "you", "thousands."]],
    5: [["Built", "from", "real", "client", "work."], ["Already", "used", "by", "50+", "businesses."]],
    # spoken: "at free prompts dot cruz creative dot net" -> one URL token with the spoken weight
    6: [["Grab", "all", "15,"], ["free,"], ["at", ("freeprompts.cruzcreative.net", 36)]],
}
LEAD = 0.05

def speech_segments(path, total):
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af",
                          "silencedetect=noise=-35dB:d=0.12", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", out)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", out)]
    ends += [total] * (len(starts) - len(ends))
    segs, cur = [], LEAD
    for s, e in zip(starts, ends):
        if s - cur > 0.02:
            segs.append([cur, s])
        cur = e
    if total - cur > 0.15:
        segs.append([cur, total])
    return segs

meta = json.load(open("audio_meta.json"))
for v in meta["voices"]:
    phrases = LINES[v["frame"]]
    segs = speech_segments(v["path"], v["duration_s"])
    if len(segs) != len(phrases):  # fall back: one span over all speech
        segs = [[segs[0][0], segs[-1][1]]] * 1
        phrases = [[w for p in phrases for w in p]]
    words = []
    for (s, e), phrase in zip(segs, phrases):
        items = [w if isinstance(w, tuple) else (w, len(w)) for w in phrase]
        weights = [n + 1 for _, n in items]
        t, span = s, e - s
        for (text, _), wt in zip(items, weights):
            d = span * wt / sum(weights)
            words.append({"text": text, "start": round(t, 3), "end": round(t + d - 0.02, 3)})
            t += d
    v["words"] = words
    print(v["frame"], len(segs), "segments ->", " ".join(f'{w["text"]}@{w["start"]}' for w in words))
json.dump(meta, open("audio_meta.json", "w"), indent=2)
