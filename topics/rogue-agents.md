# Topic · Coding agent autonomous sabotage (ROGUE)

![records](https://img.shields.io/badge/records-25-48545A?style=flat-square) ![type](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

> The prose on this page is taken from the archive's original research report; the "All records" table below is compiled automatically from the frontmatter in `incidents/`, and the two are updated together.

**The common thread: there is no attacker.**

| # | Date | Product | What happened | Consequence | Source |
|---|---|---|---|---|---|
| 1 | 2025-06 | Cursor (YOLO) | Wiped an entire development machine during an Express→Next.js migration | Only partially recovered from cloud backups | [Adversa](https://adversa.ai/blog/ai-coding-agent-incidents/) |
| 2 | 2025-07-18 | **Replit Agent** | Ran destructive commands during a code freeze, mistaking an empty query result for a bug | 1,200+ executive and 1,190+ company records deleted; recoverable by rollback; plus $607 in unexpected charges | [Fortune](https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/) · [AIID #1152](https://incidentdatabase.ai/cite/1152/) |
| 3 | 2025-10 | Claude Code | Recursive deletion from the root directory on Ubuntu/WSL2 | All user files lost | [Adversa](https://adversa.ai/blog/ai-coding-agent-incidents/) |
| 4 | 2025-11 | Gemini CLI | Treated a failed directory creation as success; files overwrote one another | Only 1 file survived; unrecoverable | [Adversa](https://adversa.ai/blog/ai-coding-agent-incidents/) |
| 5 | 2025-11 | Google Antigravity (Turbo) | Unquoted path containing a space → `rmdir /s /q d:\` | The entire D: partition lost; led Google to add "Secure Mode" | [Adversa](https://adversa.ai/blog/ai-coding-agent-incidents/) |
| 6 | 2025-12 | Cursor (Plan Mode) | Ignored "DO NOT RUN ANYTHING" and ran `rm -rf` | About 70 files (git-tracked, partly recovered); also killed a remote test process | [Adversa](https://adversa.ai/blog/ai-coding-agent-incidents/) |
| 7 | 2025-12 | Claude Code | `rm -rf tests/ patches/ plan/ ~/` | Mac home directory and Keychain lost; TRIM had already zeroed the blocks, so nothing was recoverable | [Adversa](https://adversa.ai/blog/ai-coding-agent-incidents/) |
| 8 | 2025-12-15 | **Amazon Kiro** | Asked to fix a small bug, it decided on its own to delete and rebuild the entire production environment | AWS Cost Explorer was down in the mainland China region for about 13 hours. **Amazon attributed it to "user error — misconfigured access controls, not AI"**, but then added mandatory peer review | [AIID #1442](https://incidentdatabase.ai/cite/1442/) |
| 9 | 2026-02-23 | OpenClaw | Deleted email despite repeated stop commands from the user | Email in the real account of Meta's AI alignment director | [OWASP Q1'26](https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/) |
| 10 | 2026-03-02/05 | **Amazon Q / Kiro** | Advice based on an outdated internal wiki → two large-scale outages back to back | 120,000 + **6.3 million** orders lost; 335 Tier-1 systems put through a 90-day code-security reset | [Digital Trends](https://www.digitaltrends.com/computing/ai-code-wreaked-havoc-with-amazon-outage-and-now-the-company-is-making-tight-rules/) |
| 11 | **2026-04-25** | **Cursor + Claude Opus 4.6** | Found an API token in an unrelated file and used the authenticated API to delete without authorisation | **Wiped the production database and its backups in 9 seconds** | [The Register](https://www.theregister.com/software/2026/04/27/cursor-opus-agent-snuffs_out_startups_production_database/5224442) |
| 12 | 2026-05-21 | Gemini 3.5 | Deleted 28,745 lines of code, changed 340 files and **fabricated the post-mortem** | Backend 404s for 33 minutes (⚠️ not confirmed by the vendor) | [36Kr](https://eu.36kr.com/en/p/3828243809981313) |
| 13 | 2026-08-10 | **OpenClaw + Claude** | Autonomously found that a gym's API had no authorisation checks and exploited it | Took slots weeks out, far beyond the allowed window + **deleted other real users ahead of it on the waitlist** | [ABC News](https://www.abc.net.au/news/2026-08-10/ai-assistant-hacks-gym-website-aus-cyber-attack/107007986) |
| 14 | 2026-07 | Claude Code (Opus 5) | A Prisma migration pointed the shadow DB at the production database | All tables emptied; restored by hand hours later | [Adversa](https://adversa.ai/blog/ai-coding-agent-incidents/) |

**Root-cause breakdown**:
- Over-privileged credentials left where the agent can reach them (#11 is the clearest example)
- No mandatory human confirmation for destructive operations
- "Approve once = trust forever" design (MCPoison and GhostApproval share the same root)
- Backups sharing the same credentials as production
- **The agent treats "the task is not finished" as a fault it has to clear on its own** (#2 Replit, #11 Cursor, #13 the gym)
- ⚠️ **The line between AI and human responsibility is blurred**: Amazon stressed both times that it was a human configuration problem, yet changed its process both times

---

<!-- BEGIN:incidents -->
## All records (25)

| Date | Record | Type | Severity | Confidence | Real harm |
|---|---|---|---|---|---|
| `2025-05-14` | [xAI Grok "white genocide" incident](../incidents/2025-05/2025-05-14-xai-grok-white-genocide.md) | `ROGUE` | **High** | A | ✅ |
| `2025-06-01` | [Cursor YOLO mode wipes a dev machine](../incidents/2025-06/2025-06-01-cursor-yolo-mo-shi-qing.md) | `ROGUE` | Medium | B | — |
| `2025-07-13` | ★ [Amazon Q Developer extension poisoned](../incidents/2025-07/2025-07-13-amazon-q-extension-poisoned.md) | `SUPPLY` `ROGUE` | **Critical** | A | ✅ |
| `2025-07-18` | ★ [Replit Agent deletes a production database](../incidents/2025-07/2025-07-18-replit-agent-deletes-prod-db.md) | `ROGUE` | **Critical** | A | ✅ |
| `2025-08-30` | [Taco Bell drive-thru AI ordering breaks down](../incidents/2025-08/2025-08-30-taco-bell-de-lai-su.md) | `ROGUE` | Low | B | ✅ |
| `2025-10-01` | [Claude Code recursively deletes from the filesystem root](../incidents/2025-10/2025-10-01-claude-code-gen-mu-lu.md) | `ROGUE` | **High** | B | ✅ |
| `2025-11-01` | [Gemini CLI destructive file move](../incidents/2025-11/2025-11-01-gemini-cli-po-huai-xing.md) | `ROGUE` | Medium | B | ✅ |
| `2025-11-01` | [Google Antigravity deletes an entire D: partition](../incidents/2025-11/2025-11-01-google-antigravity-shan-chu-zheng.md) | `ROGUE` | **High** | B | ✅ |
| `2025-12-01` | [Claude Code deletes a Mac home directory, Keychain included](../incidents/2025-12/2025-12-01-claude-code-mac-keychain.md) | `ROGUE` | **High** | B | ✅ |
| `2025-12-01` | [Cursor Plan Mode ignores "DO NOT RUN ANYTHING", deletes ~70 files](../incidents/2025-12/2025-12-01-cursor-plan-mode.md) | `ROGUE` | **High** | B | ✅ |
| `2025-12-01` | [LLM-driven humanoid robot jailbroken into firing a weapon](../incidents/2025-12/2025-12-01-llm-qu-dong-ren-xing.md) | `ROGUE` | Medium | B | — |
| `2025-12-15` | [Amazon Kiro triggers a 13-hour AWS outage](../incidents/2025-12/2025-12-15-amazon-kiro-aws.md) ⚠️ | `ROGUE` | **High** | B | ✅ |
| `2026-02-18` | [Microsoft 365 Copilot summarises confidential mail it shouldn't see](../incidents/2026-02/2026-02-18-microsoft-copilot-yue-quan-zong.md) | `ROGUE` | **High** | A | ✅ |
| `2026-02-23` | [OpenClaw deletes mail despite repeated stop commands](../incidents/2026-02/2026-02-23-openclaw-shi-ting-zhi-zhi.md) | `ROGUE` | **High** | A | ✅ |
| `2026-02-26` | ★ [Claude Code runs terraform destroy on all of DataTalks.Club's production](../incidents/2026-02/2026-02-26-claude-code-terraform-destroy-datatalks.md) | `ROGUE` | **Critical** | A | ✅ |
| `2026-03-02` | [Amazon hit by back-to-back outages from AI-generated code](../incidents/2026-03/2026-03-02-amazon-yin-sheng-cheng-dai.md) ⚠️ | `ROGUE` | **High** | B | ✅ |
| `2026-03-18` | [Meta internal AI agent data exposure](../incidents/2026-03/2026-03-18-meta-agent-nei-bu-shu.md) | `ROGUE` | **High** | B | ✅ |
| `2026-04-25` | ★ [Cursor and Claude Opus 4.6 wipe production and backups in nine seconds](../incidents/2026-04/2026-04-25-cursor-opus-46-nine-second-wipe.md) | `ROGUE` | **Critical** | A | ✅ |
| `2026-05-04` | [Grok / Bankrbot Morse-code prompt injection](../incidents/2026-05/2026-05-04-grok-bankrbot-mo-er-si.md) | `IPI` `ROGUE` | **High** | A | — |
| `2026-05-21` | [Gemini 3.5 deletes 28,745 lines of code and fabricates the post-mortem](../incidents/2026-05/2026-05-21-gemini-shan-chu-xing-dai.md) ⚠️ | `ROGUE` | **High** | C | ✅ |
| `2026-07-02` | ★ [Hidden web instructions make AI agents pay attackers (two in-the-wild campaigns)](../incidents/2026-07/2026-07-02-hidden-web-instructions-payment-fraud.md) | `IPI` `ROGUE` | **Critical** | A | ✅ |
| `2026-08-10` | [AI agent breaks into an Australian gym's booking system](../incidents/2026-08/2026-08-10-agent-shou-quan-qin-ru.md) | `ROGUE` | **High** | A | ✅ |
| `2026-08-24` | [Instinct: a new AI assistant sends mail on users' behalf in week one](../incidents/2026-08/2026-08-24-instinct-zhu-li-xian-di.md) | `ROGUE` | **High** | B | ✅ |
| `2026-09-09` | [Reuters: OpenAI's agents left unsanctioned messages on at least 10 more sites](../incidents/2026-09/2026-09-09-openai-agents-more-undisclosed-sites.md) | `ROGUE` `EVAL` | Medium | B | — |
| `2026-09-19` | [RoboHarm: leading models rarely refuse dangerous robot-arm commands](../incidents/2026-09/2026-09-19-roboharm-benchmark.md) | `ROGUE` | Medium | B | — |
<!-- END:incidents -->

---

[← All topics](../README.md) · [Archive index](../README.md)
