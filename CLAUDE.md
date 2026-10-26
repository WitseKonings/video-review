# CLAUDE.md

## Plans: an AI plan plus a visual flowchart

Every plan has two parts, for two readers.

1. **The AI plan (for Claude/Codex).** Write it in whatever form gives the best result: structured
   text, numbered steps, file paths, commands, checks, risks. Do NOT force it into a flowchart or
   cut detail to make it look simpler. This is the plan you execute from.
2. **The visual plan (for Witse).** Alongside the AI plan, give a flowchart that shows the same
   steps in plain words, so Witse can follow what will happen. It is drawn from the AI plan, never
   the other way round. Update it whenever the plan changes, and again after building.

Flowchart rules (visual plan only):

- **Colour carries the meaning**; shapes are secondary. Put a colour legend at the top.

| Colour | Meaning | Examples |
|---|---|---|
| Green | Start | "Start: 07:00 daily", "New email arrives" |
| Red | Stop, or something rejected / dropped | "Stop", "Rejected", "Skipped" |
| Purple | AI step: AI judges, decides or writes | Jev scoring, Claude/GPT writing |
| Gold | Owner's decision: a step where Witse has to act | "Do I approve?" |
| Blue | Automatic step by code or a service, no AI | Script checks, Drive, Sheets, posting |
| Grey | Data going in or coming out | A folder, a Sheet row, a file |

- Read top to bottom, Start to Stop. Every yes/no question is a diamond with **Yes**/**No** on its
  arrows; branches merge back. Loops are arrows going back up.
- Plain words in the boxes, not code names. Number the steps; keep the text large and readable
  (prefer a hand-built page over a tiny auto-laid-out diagram when there are many steps).
- Deliver it as a visual page, and for a workflow or automation keep a Mermaid copy in its README
  ("How it works").
- Mermaid colours: `classDef start fill:#2e9e5b,color:#fff` · `stop fill:#d7263d,color:#fff` ·
  `ai fill:#7b4fd6,color:#fff` · `me fill:#f2b632,color:#1a1300` · `auto fill:#2f7fd8,color:#fff` ·
  `data fill:#d5d9de,color:#1a1d21`
