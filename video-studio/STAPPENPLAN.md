---
name: video-maken
description: Turn one of Witse's recordings into a finished Torch Education video with motion graphics, subtitles, music and the flame signature. Use when Witse says "maak een video van <path>", "make a video of <path>", or asks to edit, package or render a Torch video in this studio.
---

# Make a Torch video

Read `stijl/STIJL.md`, `stijl/BEWEGING.md`, `stijl/AUDIO.md` and `stijl/GELEERD.md` before any creative decision. Read the HyperFrames skills (`hyperframes-core`, `talking-head-recut`) before building. Keep `docs/review_log.md` and `versies/` up to date as you work, so Witse can stop and resume at any time.

## 1. Intake (Witse: nothing, one question round at most)
1. Check the file exists and is local (not cloud-only). Quote paths with spaces.
2. `ffprobe` it: duration, resolution, fps, audio. Check the last frames aren't black: the duration is what actually decodes.
3. Check free disk space (a 4K render needs ~0.75 GB per minute, plus the same again while rendering).
4. Ask (only if unclear): format (reel 9:16 or YouTube/website 16:9 or both), audience (students or parents), CTA, and whether it is a story video (flame pass) or not.
5. Create the project: `bash motor/nieuw-project.sh "<path>" <name>`. This copies the original into `projecten/<name>/bron/` (read-only), makes a 1080p proxy with dense keyframes, extracts audio and transcribes to `projecten/<name>/transcript.json` (word array `[{text,start,end}]`).
6. Read the whole transcript. Fix misheard names (Torch, Oxbridge, UCAS, Witse).

## 2. Shotlist (Witse: **approve**)
Write `projecten/<name>/docs/shotlist.md`:
- B-roll / screen-recording times at the top (nothing goes over them).
- Per scene: time, what is said, the visual that explains it, layout, landing words with their times.
- Where the flame lights up (the single most important moment), and whether the torch pass is used.
- Emotion arc for the music.
- For 9:16: the hook text (max 2 lines) and the lock-in zone.
Show Witse a short summary: number of scenes, the 3-5 strongest visuals, the music arc. **Wait for his go.** Change only what he names.

## 3. Build
- One scene file per scene in `projecten/<name>/public/scenes/`, CSS scoped under `#sceneId`, using `motor/torch.css` and `motor/torch.js`.
- Subtitles: `node motor/ondertitels.mjs projecten/<name>/transcript.json > projecten/<name>/public/ondertitels.html` (groups of 2-3 words, key-word pill).
- Parent-facing video or longer than 3 min: split the timeline into 3-5 pieces (cut where the face is full in frame) and start one subagent per piece in parallel. Each edits only its own scene file in its own work folder. Give them a short team brief (style, limits, pitfalls), not this conversation.
- Then: `npx hyperframes check` (0 findings), snapshots on the key words, and step through the whole timeline every 0.5 s without errors.

## 4. Sound
Cues from the animations → the single flame effect → music → mix → measure (−16 LUFS, true peak ≤ −1.5 dBTP).

## 5. Critic loop
Render a draft (1080p, 30 fps, with sound) → make review sheets (`bash motor/reviewbladen.sh draft.mp4`: 1 frame per 2 s, a 360 px phone sheet, 12-frame strips around transitions) → start a **new** critic subagent each round with `stijl/KRITIEK.md` → fix → repeat.
- Reels: until all scores ≥ 8, max 3 rounds.
- Parent-facing videos: until all scores ≥ 8 (maximum level).
Log everything in `docs/review_log.md`.

## 6. Draft (Witse: **watch, feedback or "go"**)
Back up to `versies/v<N>/` before every feedback round. Send Witse the path, 3-5 moments (with times) to look at, and "watch it on your phone too". His feedback: summarise it word for word in the log, taste rules go to `stijl/GELEERD.md`, change only what he names, short critic round, new draft.

## 7. Final
After his "go": render at full resolution from the **original** (long videos in chunks of ~100 s; compare a few frames per chunk with the draft and check the seams) → check frame count, duration, loudness, no black ending → save to `eindversies/<name>_v<N>.mp4` (never overwrite) → clean up only your own intermediate files and say what you removed → report path, resolution, duration, size, and how to test it.

Finally add one row to "Videos so far" in `CLAUDE.md` (name, date, what worked).
