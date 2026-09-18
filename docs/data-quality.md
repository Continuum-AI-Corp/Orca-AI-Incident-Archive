# Data quality

![records](https://img.shields.io/badge/records-313-48545A?style=flat-square) ![source links](https://img.shields.io/badge/source_links-513-48545A?style=flat-square) ![unique URLs](https://img.shields.io/badge/unique_URLs-447-48545A?style=flat-square) ![unsourced records](https://img.shields.io/badge/unsourced_records-0-157A41?style=flat-square)

## Methodology risk

In 2026 a fair share of "AI incident round-up" pages are **themselves AI-generated SEO content at scale**, inventing CVE numbers, inventing victim organisations, and writing demo PoCs up as real damage.

This review confirmed 3 specific contamination cases:

| Claim | What actually happened |
|---|---|
| "EchoLeak caused about US$200 million in financial impact" | **Fabricated.** Microsoft confirmed no known in-the-wild exploitation, and no primary report carries this figure. Removed in v2 |
| "Step Finance's AI trading agent had approval-free authority to move large transfers" | **No primary source supports it.** CoinDesk states plainly that "how the attacker gained access was not explained", and AI appears nowhere in the article. The AI framework appears only in AI marketing blogs. Downgraded in v2 |
| "Attackers used Claude Code as a C2 server for 18 days" | **No such event exists.** Suspected garbling of a Check Point CVE disclosure dated 2026-02-27. Removed in v2 |

**Therefore: every grade C entry must be re-verified before it enters the archive.**

---

## Still without a primary source

> ✅ **v3 tightened this a lot**: of the 19 entries v2 listed as "seen only on the Permission Protocol tracker, untraceable", the v3 pass verified them one by one
> and **traced 13 to a primary source, upgrading them to grade A** (several turned out to have been badly understated), while **2 were merged into other entries after verification**. Only the following remain.

| Entry | Status |
|---|---|
| A Chinese manufacturing firm's OpenClaw line halted for 72 hours, 20M+ lost | Industry self-media, no verifiable detail. **Recommend dropping** |
| "The OpenAI plugin-ecosystem supply chain caused credentials from 47 enterprise deployments to be harvested" | Seen only in a vendor marketing blog, no primary source. **Recommend dropping** |
| Smithery.ai path traversal (2025-06) | Seen only in Chinese year-end round-ups |
| OpenAI Guardrails broken by HiddenLayer (2025-10) | Seen only in Chinese year-end round-ups |
| "204 of the 395 PaperCut victim organisations are educational institutions" | Primary reporting says only "concentrated mainly in the US education sector"; **the 204 breakdown has no primary support** and is flagged in the record body |
| "88% / 65% of organisations experienced an AI agent incident" | The two surveys contradict each other; neither sample nor method is clear |

**The 13 entries upgraded from "unverifiable" to primary-source-confirmed in v3** (all substantially expanded in the record bodies):
Copilot Studio Connected Agents (Zenity) · Cursor CVE-2026-22708 (Pillar) · Claude Code Terraform destroys DataTalks.Club (AIID #1424) · OpenClaw Claw Chain four CVEs (Cyera) · Gemini CLI CVSS 10 (GHSA-wpqr-6v78-jr5g) · TrustFall (Adversa) · Semantic Kernel double CVE (self-disclosed by Microsoft) · Claudy Day (Oasis, month corrected) · Mastra/Sapphire Sleet (Microsoft) · Zscaler's two in-the-wild payment campaigns · SharedRoot (Accomplish AI) · Copilot Autofix/Snowflake (Wiz) · CoSnitch (Varonis) · Context7 CVE-2026-75130 · AWS Transform MCP CVE-2026-18953 · GitLab Duo CVE-2026-18252 · ChatGPT cross-account Gmail exfiltration (Check Point)

## Disputed attribution or facts

| Entry | Point of dispute |
|---|---|
| **Harbin Asian Winter Games** (2025-01/02) | China attributed it unilaterally to NSA agents and US universities; "the first large-scale AI agent attack" is a phrase from media commentary; the number of attacks is given both as 270,167 (competition systems) and as 50M+ (critical infrastructure across the province). **No independent verification.** Recommend `attribution: disputed` and noting that the sources are Chinese official/media |
| **Step Finance** (2026-01-31) | CoinDesk states plainly that "how the attacker gained access was not explained", and **AI appears nowhere in the article**. "The AI agent could transfer without approval" appears only in AI marketing blogs. **Recommend dropping, or downgrading to `ai_involvement: unverified`** |
| **Amazon Kiro / AWS outage** (2025-12-15) | Amazon officially attributed it to "user error — a misconfigured access control, not AI"; but the company then added mandatory peer review for all production changes. **Both narratives coexist** |
| **Gemini 3.5 deletes code and fabricates a report** (2026-05-21) | The origin is a Reddit post, **not confirmed by the vendor**; OrcaRouter wrote a piece specifically questioning "3 reports, 0 confirmations" |
| **PromptLock** (2025-08) | ESET first described it as the first in-the-wild "AI ransomware"; **the academic authors later made contact and confirmed it was an NYU research prototype (Ransomware 3.0)**. The entry must carry this correction |
| **Hunt.io Thailand case vs Unit 42 Chinese-speaking-actor case** | Technically very similar, but **the two reports are independent and give no evidence of the same actor** (IPA explicitly warns of this) |
| **Amazon 6.3 million orders** (2026-03) | Business Insider says it obtained internal documents, but **the documents themselves are not public**; all other reports are second-hand |
| **Copilot Autofix / Snowflake Jira token** (2026-08) | **Authorship is disputed**: Wiz says the flaw was introduced by a 2026-06-18 change "co-signed by Copilot Autofix"; **GitHub counters that the faulty logic traces back to a human engineer's commit in 2025-08**, the Autofix tag being attached only at squash-merge time. Both accounts stand side by side |
| **Gemini 3.5 deletes code and fabricates a report** (2026-05) | Beyond the missing vendor confirmation, v3 also traced the root cause to **a "high-autonomy" instruction injected by a third-party npm rules package that overrode the safety warning** — if accurate, this should be reclassified as `SUPPLY` rather than pure `ROGUE` |

## Conflicting numbers

| Entry | Conflicting values |
|---|---|
| ClawHub malicious skills | 341 (Koi audit of 2,857) / 824 / 1,184 / 1,200+ |
| OpenClaw exposed instances | 900 (2026-01) / 15,200 (SecurityScorecard) / 40,214 / 42,665 (Oasis) / 135,000 / 245,000 |
| LiteLLM backdoored-release downloads | 119,000 in 2.5 hours / 47,000 in 3 hours |
| Mexico case record count | 400 million (195M SAT + 220M civil registry) / 195 million (SAT only) |
| Salesloft Drift victim organisations | 700+ / 760+ |
| Step Finance loss | $27M (CoinDesk) / $28.9M (the then-value of 261,854 SOL) / $29M / $30M / $40M / $45M |
| Grok Morse-code loss | $150,000 / $200,000 |
| SearchLeak severity | MSRC base score 6.5 / Varonis says Microsoft rated it critical |
| Harbin Asian Winter Games attack count | 270,167 (competition information systems) / 50M+ (critical infrastructure in Heilongjiang province) |
| "Share of organisations that experienced an AI agent incident" | 88% / 65% |
| McHire leak scale | 64 million records theoretically reachable / Paradox says only 5 were actually accessed |
| Total OpenClaw CVEs | 138 (2026-04-06, 63-day window) / 512 vulnerabilities on the first audit (2026-01-25) — different measures (CVEs vs audit findings) |
| Mexico case command count | Gambit primary-confirmed **1,088 attacker prompts**; "5,000+ AI-executed commands across 34 sessions" comes from **a separate Check Point tally** and is not in the Gambit report |
| PaperCut domain-admin time | One US high-school case: **7 minutes** (primary) / a secondary round-up once said "6–7 hours" (v2 accepted that by mistake, corrected in v3) |
| Mastra poisoned packages | 144 (Microsoft) / 143 (safedep) / 145 (another round-up) |

---

## Entries flagged as disputed (13)

| Date | Event | Confidence | AI involvement |
|---|---|---|---|
| `2025-01-26` | [Harbin Asian Winter Games systems attacked](../incidents/2025-01/2025-01-26-harbin-asian-winter-games-attack.md) | D | `disputed` |
| `2025-02-01` | [Thousands of Ollama servers exposed without auth](../incidents/2025-02/2025-02-01-ollama-fu-wu-qi-gui.md) | A | `confirmed` |
| `2025-06-04` | [Asana MCP server cross-tenant data exposure](../incidents/2025-06/2025-06-04-asana-mcp-server.md) | B | `confirmed` |
| `2025-08-01` | [Cursor CurXecute (CVE-2025-54135)](../incidents/2025-08/2025-08-01-cursor-curxecute.md) | A | `confirmed` |
| `2025-08-28` | [TransUnion leaks 4.4-4.5M people via a third-party app](../incidents/2025-08/2025-08-28-transunion-jing-di-san-fang.md) | B | `not-applicable` |
| `2025-11-01` | [ShadowRay 2.0 (Ray framework)](../incidents/2025-11/2025-11-01-shadowray-2-ray-framework.md) | B | `confirmed` |
| `2025-12-01` | [Three CVEs in Anthropic's Git MCP Server](../incidents/2025-12/2025-12-01-anthropic-git-mcp-server.md) | A | `confirmed` |
| `2025-12-15` | [Amazon Kiro triggers a 13-hour AWS outage](../incidents/2025-12/2025-12-15-amazon-kiro-aws.md) | B | `disputed` |
| `2026-01-31` | [Step Finance treasury drained](../incidents/2026-01/2026-01-31-step-finance-jin-ku-dao.md) | D | `unverified` |
| `2026-02-27` | [Check Point publishes two Claude Code CVEs](../incidents/2026-02/2026-02-27-check-point-claude-code.md) | A | `confirmed` |
| `2026-03-02` | [⚠️ Amazon hit by back-to-back outages from AI-generated code](../incidents/2026-03/2026-03-02-amazon-yin-sheng-cheng-dai.md) | B | `disputed` |
| `2026-04-15` | [ShareLeak (CVE-2026-21520) and PipeLeak](../incidents/2026-04/2026-04-15-shareleak-pipeleak.md) | A | `confirmed` |
| `2026-05-21` | [Gemini 3.5 deletes 28,745 lines of code and fabricates the post-mortem](../incidents/2026-05/2026-05-21-gemini-shan-chu-xing-dai.md) | C | `disputed` |

## What the four review rounds did

| Round | Goal | Result |
|---|---|---|
| v1 | Build the timeline | No source links; included 2 fabricated entries that were later deleted |
| v2 | Add a primary source to every entry | 317 primary-source URLs added; every line must have a source |
| v3 | Fact-check every entry | Fabricated entries deleted; PaperCut's "6 hours" corrected to **7 minutes**; Step Finance downgraded to grade D |
| v4 | **Find the gaps** | After comparison with peer projects, about 11% of missing entries were added |

**The methodological conclusion from v4 deserves a note of its own**: entry-by-entry review and coverage auditing catch **completely different** problems.
The first three rounds checked every single entry, and still missed a full 11% — because "are the entries we have correct" and
"have we collected all the entries we should have" are two independent questions, and each has to be asked separately.

---

[← Back to home](../README.md) · [Scope](scope.md) · [Sources](sources.md)
