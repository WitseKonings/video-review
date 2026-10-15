# Shotlist: stijltest (YC application video)

- Source: `bron/Movie on 13-10-2026 at 15.29.mov`, 83.4 s, 1080×720 landscape webcam, mono
- Output: 16:9, 1920×1080, quality **maximum**
- Length: 83.4 s of footage + 3 s end card = ~86.5 s
- B-roll / screen recordings: none
- Transcript fixes (subtitles only): "UIC" → "YC" (0:00), "Witzer" → "Witse" (0:07), "hook" → "ad hoc" (0:45), "Up YC" → "YC" (1:18)
- Partner names at 0:57 are not shown anywhere, subtitles included. The subtitle reads "global education platforms", then skips to "and I'm also working with schools"

## Scenes

| # | Time | Spoken (key words) | Layout | Visual (what it explains) |
|---|---|---|---|---|
| 1 | 0.0–5.0 | "democratize the **access** to **elite universities**" | split (face right) | Hook card: Playfair title "Democratize access to elite universities", fully visible from frame 0. A closed gate drawn below it swings open on "democratize" (1.68) |
| 2 | 5.0–9.6 | "I'm **Witse**, founder of **Torch Education**" | stack (face top, card below) | Name card grows: "Witse" (7.12) → "Founder, TORCH EDUCATION" wordmark + navy (unlit) flame icon on "Torch" (8.32) |
| 3 | 9.6–21.2 | "**Belgian state school** … into **Oxford**" · "hard worker? … parents are **academics** … **showed me the way**" | split | One card that grows: a school icon labelled "Belgian state school" (10.24) → a path draws (11.6) → plain text "Oxford" node (13.04). Then "Hard work?" appears and is struck through (15.4–16.6). Two simple parent figures appear beside the path (18.64) and the path lights gold from them to Oxford on "showed me the way" (19.68) |
| 4 | 21.3–28.9 | "students … **smarter** than me … **don't get in** … **insider playbook**" | pip (content full width, face card bottom right) | A row of 7 drawn student figures (22.8). A gate closes in front of them (25.28). Behind the gate, a navy book labelled "Insider playbook" (27.92). Holds 3 s |
| 5 | 29.0–39.9 | "past **three years** guiding students … **expensive** … my **availability**" | split | Bottleneck diagram: one node "Witse" with lines to a few student dots, label "3 years of guiding students" (29.76). A price-tag icon lands on the lines (34.72). A week grid with almost every slot filled (38.48) |
| 6 | 39.9–48.6 | "that's what we're changing at **Torch**" · "**elite admissions advice** available **ad hoc** through **AI tools**" | pip | **Signature moment:** two drawn torches. The flame travels from the left torch to the right one and **lights orange on "Torch" (41.52)**, with the video's one sound (a soft ignition). Holds to 44.0, then morphs in place into a mock-up in Torch's UI style (navy sidebar, white card, stage dots): a student question bubble and an answer drawn as grey lines, with a gold "AI" pill (46.8). Holds to 50.3 |
| 7 | 50.3–64.3 | "**creative** … forming **partnerships** … **global education platforms** … **schools** … **first pilots**" | split | Network diagram: a centre node with the flame (50.3). Empty link stubs sprout on "partnerships" (52.48), a node "Global education platforms" (56.0), a node "Schools" (61.2) and a gold pill "First pilots" on it (62.8). No logos, no names |
| 8 | 64.3–71.9 | "my first **leads** for **next year's season** … **interview season** about to kick off" | stack | A simple timeline (no dates): "Now" → "Next year's season". The schools node from scene 7 slides onto the timeline as "First leads" (66.21). A marker "Interview season" lands near "Now" with an arrow "about to kick off" (69.73) |
| 9 | 72.0–77.9 | "recruiting **student ambassadors** … my **first sale** this year" | pip | Three student figures with gold badges, "Student ambassadors" (73.65). Arrows meet in a green tick, "First sale" (76.13) |
| 10 | 77.9–83.4 | "**YC**, very keen to **accelerate** … **work together**" · "Thank you for your time" | split | A line drawn as an accelerating curve (plain shape, no axes or numbers) on "accelerate" (80.21). Then the flame icon and the text "YC" join with a "+" on "work together" (81.57). Holds through "Thank you" |
| 11 | 83.4–86.5 | — | end card | Hard cut (no wipe over the face) to a solid navy card: orange flame, Playfair line in white "Thank you for your time." No CTA. Holds 3 s |

Layout order: split, stack, split, pip, split, pip, split, stack, pip, split. Never 3 in a row, and no scene stays on one card for more than 15 s (scene 3 changes visual at 15.4; scene 7 is 14 s).

## Subtitles
- 2–3 words per group, bold navy Inter, no pill. In split layouts they sit under the card on the left; in stack and pip layouts, at the bottom left, never over the face card.
- Gold pill on at most one key word per group: universities, Torch, Oxford, admissions, and the point of the sentence (playbook, expensive, ad hoc, ambassadors).

## Sound
- **Music:** there's no ElevenLabs key in `.env` and nothing in `assets/muziek/`. Without one of those, the draft has no music.
- **Effect:** one soft ignition at 41.52, which I make myself.
- **Mix:** voice brought up to −16 LUFS.

## Checks
- Numbers: only "three years", which you say. Everything else is shapes.
- No university crests, no partner logos, no student data. "Oxford" and "YC" only as plain text, only where spoken.
