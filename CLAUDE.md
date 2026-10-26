# Notes for Claude

## Workflow flowcharts

Whenever we design or change a workflow or automation, draw it as a flowchart before (and after) building it. **Colour carries the meaning**; shapes are secondary. Put a colour legend at the top.

| Colour | Meaning | Examples |
|---|---|---|
| Green | Start | "Start: 07:00 daily", "New email arrives" |
| Red | Stop, or something rejected / dropped | "Stop", "Rejected", "Skipped" |
| Purple | AI step: AI judges, decides or writes | Jev scoring, Claude/GPT writing |
| Gold | Owner's decision: a step where I have to act | "Do I approve?" |
| Blue | Automatic step by code or a service, no AI | Script checks, Drive, Sheets, posting |
| Grey | Data going in or coming out | A folder, a Sheet row, a file |

- Read top to bottom, Start to Stop. Every yes/no question is a diamond with **Yes**/**No** on its arrows; branches merge back. Loops are arrows going back up.
- Plain words in the boxes, not code names.
- Deliver it as a visual page, and keep a Mermaid copy in the README ("How it works"). Update both whenever the workflow changes.
- Mermaid colours: `classDef start fill:#2e9e5b,color:#fff` · `stop fill:#d7263d,color:#fff` · `ai fill:#7b4fd6,color:#fff` · `me fill:#f2b632,color:#1a1300` · `auto fill:#2f7fd8,color:#fff` · `data fill:#d5d9de,color:#1a1d21`
