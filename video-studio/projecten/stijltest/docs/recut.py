#!/usr/bin/env python3
"""Shorten pauses + speed up so the footage fits the YC 60 s limit. No words are cut.
Usage: python3 docs/recut.py <input> <output> [--plan]
Writes docs/recut_plan.json (segments kept + speed) so the final render from the
original uses exactly the same cut as the draft."""
import json, os, re, subprocess, sys

SRC, OUT = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = 57.25         # footage length; end card (2.5 s) comes after -> under 60 s
TAIL = float(os.environ.get("TAIL", 0.16))       # kept after speech: word endings fade out softly
LEAD = float(os.environ.get("LEAD", 0.05))       # kept before speech: onsets are sharp
SENT_TAIL = float(os.environ.get("SENT_TAIL", 0.22))  # a little more breathing room after a full stop

dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                     "-of", "csv=p=0", SRC]).decode())
log = subprocess.run(["ffmpeg", "-nostats", "-i", SRC, "-af", f"silencedetect=noise={os.environ.get('NOISE', '-30')}dB:d=0.2",
                      "-f", "null", "-"], capture_output=True, text=True).stderr
starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
sil = list(zip(starts, ends))

# sentence ends from the transcript, to give those pauses a bit more room
words = json.load(open(os.path.join(HERE, "..", "transcript.json")))
stops = [w["end"] for w in words if w["text"].strip().endswith((".", "?", "!"))]

keep, cur = [], 0.0
for s, e in sil:
    if s <= 0.05:                      # leading silence
        cur = max(0.0, e - LEAD); continue
    if e >= dur - 0.05:                # trailing silence
        keep.append((cur, min(dur, s + TAIL))); cur = None; break
    sent = any(abs(t - s) < 0.6 for t in stops)
    tail = SENT_TAIL if sent else TAIL
    if e - s <= tail + LEAD: continue  # already short
    keep.append((cur, s + tail)); cur = e - LEAD
if cur is not None: keep.append((cur, dur))

cut_len = sum(b - a for a, b in keep)
speed = max(1.0, cut_len / TARGET)
plan = {"source": os.path.basename(SRC), "segments": [[round(a, 3), round(b, 3)] for a, b in keep],
        "cut_length": round(cut_len, 3), "speed": round(speed, 4), "final_length": round(cut_len / speed, 3)}
json.dump(plan, open(os.path.join(HERE, "recut_plan.json"), "w"), indent=1)
print(f"{len(keep)} segments, {dur:.2f}s -> {cut_len:.2f}s after pauses, speed x{speed:.3f} -> {cut_len/speed:.2f}s")
if "--plan" in sys.argv: sys.exit(0)

# trim + concat (8 ms audio fades at every seam against clicks), then speed with pitch kept
f, n = [], len(keep)
for i, (a, b) in enumerate(keep):
    f.append(f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS[v{i}]")
    f.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.008,afade=t=out:st={b-a-0.008:.3f}:d=0.008[a{i}]")
f.append("".join(f"[v{i}][a{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=1[cv][ca]")
f.append(f"[cv]setpts=PTS/{speed:.4f},fps=30[vo]")
f.append(f"[ca]atempo={speed:.4f}[ao]")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", SRC, "-filter_complex", ";".join(f),
                "-map", "[vo]", "-map", "[ao]", "-c:v", "libx264", "-crf", "16", "-g", "30", "-keyint_min", "30",
                "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-c:a", "aac", "-b:a", "192k", OUT], check=True)
print("written", OUT)
