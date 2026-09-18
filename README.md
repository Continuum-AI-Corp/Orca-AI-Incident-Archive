<h1 align="center">Orca AI Incident Archive</h1>

<p align="center"><b>An open database of real-world AI agent incidents</b></p>

<p align="center">
<b>English</b> ·
<a href="docs/i18n/README.zh-CN.md">简体中文</a> ·
<a href="docs/i18n/README.ja.md">日本語</a> ·
<a href="docs/i18n/README.ko.md">한국어</a> ·
<a href="docs/i18n/README.de.md">Deutsch</a> ·
<a href="docs/i18n/README.fr.md">Français</a> ·
<a href="docs/i18n/README.es.md">Español</a>
</p>

<!-- BEGIN:badges -->
<p align="center"><img alt="records" src="https://img.shields.io/badge/records-317-48545A?style=flat-square"> <img alt="months" src="https://img.shields.io/badge/months-22-48545A?style=flat-square"> <img alt="critical" src="https://img.shields.io/badge/critical-44-88091D?style=flat-square"> <img alt="with real harm" src="https://img.shields.io/badge/with_real_harm-122-B23B40?style=flat-square"> <img alt="primary sources" src="https://img.shields.io/badge/primary_sources-466_URL-157A41?style=flat-square"> <img alt="license" src="https://img.shields.io/badge/license-CC_BY_4.0-2359A8?style=flat-square"></p>
<!-- END:badges -->

<!-- BEGIN:thesis -->
Coverage runs from **2025-01** to **2026-09-16** — 317 records of AI agent security events arranged month by month, plus one precursor traceable to 2024-12-01. Each record is a single Markdown file with a YAML header, an attack-chain diagram and **at least one primary source you can click**. Of the 317, only **122 have a confirmed victim**.
<!-- END:thesis -->

This archive exists for one distinction that most incident lists collapse:

> **An agent that actually caused damage is not the same thing as a researcher showing that it could.**

Every record answers three questions before anything else — was there a confirmed victim (`real_harm`), was the AI involvement confirmed by a primary source (`ai_involvement`), and is this an incident, a vulnerability disclosure, a research demo, a threat report or a policy move (`kind`). Without those three fields, "300+ AI incidents this year" is a number that means nothing.

---

## At a glance

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/monthly-dark.svg">
  <img alt="Records per month, January 2025 to September 2026" src="assets/monthly-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/severity-dark.svg">
  <img alt="Breakdown by severity and record type" src="assets/severity-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/by-type-dark.svg">
  <img alt="Distribution by attack type" src="assets/by-type-light.svg" width="100%">
</picture>

## Where to start

| I want to… | Go here |
|---|---|
| Read it chronologically | [All records by month](incidents/README.md) |
| See only what actually happened | [The `critical` list](#critical) · or filter `real_harm: true` |
| Read by attack surface | [Seven topics](topics/README.md) |
| Look at one country or region | [Regional slices](regions/README.md) |
| Understand the fields | [SCHEMA.md](SCHEMA.md) · [Taxonomy](taxonomy/README.md) · [Docs](docs/README.md) |
| Analyse the data | [`dist/`](dist/README.md) — JSON, CSV, stats, every source URL |
| Browse interactively | [`index.html`](index.html) — one file, works offline, seven languages |

> [!NOTE]
> **Language.** Records are written in English. Titles and summaries are available in seven languages (English, Chinese, Japanese, Korean, German, French, Spanish); the complete Chinese text of every record lives under [`incidents/i18n/zh/`](incidents/i18n/zh/). Cited sources stay in their original language. Further translations are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).

## By month

<!-- BEGIN:months -->
**2024** (1 records)

| [12](incidents/2024-12/README.md) |
|---|
| `1` |

**2025** (121 records)

| [01](incidents/2025-01/README.md) | [02](incidents/2025-02/README.md) | [03](incidents/2025-03/README.md) | [04](incidents/2025-04/README.md) | [05](incidents/2025-05/README.md) | [06](incidents/2025-06/README.md) | [07](incidents/2025-07/README.md) | [08](incidents/2025-08/README.md) | [09](incidents/2025-09/README.md) | [10](incidents/2025-10/README.md) | [11](incidents/2025-11/README.md) | [12](incidents/2025-12/README.md) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `8` ★1 | `6` | `6` | `6` | `7` | `11` | `10` ★2 | `15` ★2 | `10` ★1 | `15` | `13` ★3 | `14` |

**2026** (195 records)

| [01](incidents/2026-01/README.md) | [02](incidents/2026-02/README.md) | [03](incidents/2026-03/README.md) | [04](incidents/2026-04/README.md) | [05](incidents/2026-05/README.md) | [06](incidents/2026-06/README.md) | [07](incidents/2026-07/README.md) | [08](incidents/2026-08/README.md) | [09](incidents/2026-09/README.md) |
|---|---|---|---|---|---|---|---|---|
| `13` ★1 | `19` ★5 | `16` ★3 | `22` ★2 | `26` ★5 | `31` ★3 | `27` ★7 | `23` ★4 | `18` ★5 |

<sub>`n` = records that month, ★ = of which `critical`</sub>
<!-- END:months -->

## Critical

<!-- BEGIN:critical -->
Any of three triggers: ① **confirmed** damage reaching multiple organisations, a government, critical infrastructure or a supply-chain worm; ② a first-of-its-kind capability milestone with real victims; ③ research that **overturns a widely deployed defence** — `real_harm: false` in that case, 2 of these. Full criteria in [taxonomy/severity.md](taxonomy/severity.md).

| Date | Record | Type | Region |
|---|---|---|---|
| `2025-01-29` | [DeepSeek ClickHouse database left wide open](incidents/2025-01/2025-01-29-deepseek-clickhouse-exposed.md) | `INFRA` | CN |
| `2025-07-13` | [Amazon Q Developer extension poisoned](incidents/2025-07/2025-07-13-amazon-q-extension-poisoned.md) | `SUPPLY` `ROGUE` | GLOBAL |
| `2025-07-18` | [Replit Agent deletes a production database](incidents/2025-07/2025-07-18-replit-agent-deletes-prod-db.md) | `ROGUE` | US |
| `2025-08-08` | [Salesloft Drift OAuth token theft](incidents/2025-08/2025-08-08-salesloft-drift-oauth-theft.md) | `SUPPLY` `CRED` | GLOBAL |
| `2025-08-26` | [Nx "s1ngularity"](incidents/2025-08/2025-08-26-nx-s1ngularity.md) | `SUPPLY` `CRED` | GLOBAL |
| `2025-09-15` | [Shai-Hulud npm worm v1](incidents/2025-09/2025-09-15-shai-hulud-npm.md) | `SUPPLY` `CRED` | GLOBAL |
| `2025-11-01` | [ShadowRay 2.0 (Ray framework)](incidents/2025-11/2025-11-01-shadowray-2-ray-framework.md) | `INFRA` | GLOBAL |
| `2025-11-13` | [GTG-1002: first AI-orchestrated cyber-espionage campaign](incidents/2025-11/2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md) | `WEAPON` | CN GLOBAL |
| `2025-11-21` | [Shai-Hulud 2.0](incidents/2025-11/2025-11-21-shai-hulud.md) | `SUPPLY` `CRED` | GLOBAL |
| `2026-01-31` | [Moltbook database fully open](incidents/2026-01/2026-01-31-moltbook-open-database.md) | `CRED` | GLOBAL |
| `2026-02-09` | [Clinejection](incidents/2026-02/2026-02-09-clinejection.md) | `SUPPLY` `IPI` | GLOBAL |
| `2026-02-20` | [AI-augmented actor compromises 600+ FortiGate devices](incidents/2026-02/2026-02-20-fortigate-600-devices-compromised.md) | `WEAPON` | GLOBAL |
| `2026-02-25` | [Nine Mexican government agencies breached](incidents/2026-02/2026-02-25-mexico-nine-agencies-breached.md) | `WEAPON` | LATAM |
| `2026-02-26` | [Claude Code runs terraform destroy on all of DataTalks.Club's production](incidents/2026-02/2026-02-26-claude-code-terraform-destroy-datatalks.md) | `ROGUE` | GLOBAL |
| `2026-02-28` | [CodeWall breaches McKinsey's internal "Lilli" AI platform](incidents/2026-02/2026-02-28-codewall-breaches-mckinsey-lilli.md) | `WEAPON` `INFRA` | US |
| `2026-03-01` | [Hades: a sustained campaign turning AI coding assistants into the attack surface](incidents/2026-03/2026-03-01-hades-campaign-ai-coding-assistants.md) | `SUPPLY` `CRED` | GLOBAL |
| `2026-03-24` | [Backdoored LiteLLM release](incidents/2026-03/2026-03-24-litellm-backdoored-release.md) | `SUPPLY` `CRED` | GLOBAL |
| `2026-03-30` | [Axios npm package compromised](incidents/2026-03/2026-03-30-axios-npm-compromised.md) | `SUPPLY` | GLOBAL |
| `2026-04-16` | [MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild](incidents/2026-04/2026-04-16-mcpwn-nginx-ui-in-the-wild.md) | `MCP` `INFRA` | GLOBAL |
| `2026-04-25` | [Cursor and Claude Opus 4.6 wipe production and backups in nine seconds](incidents/2026-04/2026-04-25-cursor-opus-46-nine-second-wipe.md) | `ROGUE` | GLOBAL |
| `2026-05-10` | [First in-the-wild LLM agent running the full post-exploitation chain](incidents/2026-05/2026-05-10-first-in-wild-autonomous-llm-post-exploitation.md) | `WEAPON` | GLOBAL |
| `2026-05-11` | [TanStack npm "Mini Shai-Hulud"](incidents/2026-05/2026-05-11-tanstack-npm-mini-shai.md) | `SUPPLY` `CRED` | GLOBAL |
| `2026-05-18` | [3,800 internal GitHub repositories compromised](incidents/2026-05/2026-05-18-github-3800-internal-repos.md) | `SUPPLY` `CRED` | GLOBAL |
| `2026-05-19` | [TrapDoor: poisoning three ecosystems to corrupt AI assistant configs](incidents/2026-05/2026-05-19-trapdoor-poisons-agent-configs.md) | `SUPPLY` `CRED` | GLOBAL |
| `2026-05-21` | [Composio: agent automation itself becomes the privilege-escalation path](incidents/2026-05/2026-05-21-composio-agent-automation-privesc.md) | `CRED` `SUPPLY` | GLOBAL |
| `2026-06-01` | [Attackers simply ask Meta's AI support bot for Instagram accounts](incidents/2026-06/2026-06-01-meta-ai-support-bot-hands-over-instagram.md) | `IPI` `CRED` | GLOBAL |
| `2026-06-01` | [Miasma worm](incidents/2026-06/2026-06-01-miasma-worm.md) | `SUPPLY` `CRED` | GLOBAL |
| `2026-06-17` | [Sapphire Sleet poisons every Mastra AI scope in 88 minutes](incidents/2026-06/2026-06-17-sapphire-sleet-mastra-88-minutes.md) | `SUPPLY` `CRED` | GLOBAL |
| `2026-07-01` | [JADEPUFFER: first ransomware driven end-to-end by an LLM](incidents/2026-07/2026-07-01-jadepuffer-first-llm-driven-ransomware.md) | `WEAPON` | GLOBAL |
| `2026-07-01` | [Taiwan's nuclear safety commission and other agencies breached by an agent swarm](incidents/2026-07/2026-07-01-taiwan-government-agent-swarm.md) | `WEAPON` | TW |
| `2026-07-02` | [Hidden web instructions make AI agents pay attackers (two in-the-wild campaigns)](incidents/2026-07/2026-07-02-hidden-web-instructions-payment-fraud.md) | `IPI` `ROGUE` | GLOBAL |
| `2026-07-09` | [OpenAI's agents breach Hugging Face](incidents/2026-07/2026-07-09-openai-agents-breach-huggingface.md) | `EVAL` `WEAPON` | GLOBAL |
| `2026-07-30` | [Anthropic discloses three evaluation-breakout incidents](incidents/2026-07/2026-07-30-anthropic-three-eval-incidents.md) | `EVAL` | GLOBAL |
| `2026-07-30` | [Hermes Agent attacks Thailand's Ministry of Finance unattended](incidents/2026-07/2026-07-30-hermes-agent-thailand-finance-ministry.md) | `WEAPON` | SEA |
| `2026-07-30` | [Unit 42: autonomous campaigns run by Chinese-speaking operators](incidents/2026-07/2026-07-30-unit42-chinese-speaking-autonomous-campaigns.md) | `WEAPON` | CN GLOBAL |
| `2026-08-04` | [CHAINDROP npm worm](incidents/2026-08/2026-08-04-chaindrop-npm-ru-chong.md) | `SUPPLY` `CRED` | GLOBAL |
| `2026-08-06` | [Unauthenticated Langflow RCE added to CISA KEV](incidents/2026-08/2026-08-06-langflow-rce-cisa-kev.md) | `INFRA` | GLOBAL |
| `2026-08-26` | [Trail of Bits: VMs won't contain cyber-capable agents](incidents/2026-08/2026-08-26-trailofbits-vm-cannot-contain-networked-agents.md) | `EVAL` `SANDBOX` | GLOBAL |
| `2026-08-28` | [PaperCut AI agent swarm campaign begins](incidents/2026-08/2026-08-28-papercut-agent-swarm-campaign-begins.md) | `WEAPON` | GLOBAL |
| `2026-09-01` | [GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted](incidents/2026-09/2026-09-01-gitspawn-git-config-pre-model-rce.md) | `SUPPLY` `SANDBOX` | GLOBAL |
| `2026-09-02` | [Langflow CVE-2026-0768: the 12th Langflow flaw exploited in the wild this year](incidents/2026-09/2026-09-02-langflow-jin-di-ye-li.md) | `INFRA` `CRED` | GLOBAL |
| `2026-09-10` | [Anthropic September threat intelligence report](incidents/2026-09/2026-09-10-anthropic-september-threat-report.md) | `WEAPON` | GLOBAL |
| `2026-09-11` | [Claude used to scan 1.8 million Android apps for secrets](incidents/2026-09/2026-09-11-claude-scans-18m-android-apks.md) | `WEAPON` | GLOBAL |
| `2026-09-15` | [PaperCut AI agent swarm attack made public](incidents/2026-09/2026-09-15-papercut-agent-swarm-disclosed.md) | `WEAPON` | GLOBAL |
<!-- END:critical -->

## What counts as a record

A record qualifies if **at least one** of these is true:

1. The AI agent was **the one carrying out the attack** — autonomously or driven by a human
2. The AI agent was **the target** — injection, poisoning, escape, exposed infrastructure
3. The AI agent was **a link in the damage chain** — it read hostile content and acted on it
4. It is a **regulatory, legislative or vendor action** directly about agent security (recorded as `kind: policy`, not counted as an incident)

**Out of scope:** pure LLM content-safety findings (jailbreaking a model into saying something it shouldn't), ordinary vulnerabilities unrelated to agents, and claims with no traceable primary source.

Two categories are **labelled rather than deleted**:

- `ai_involvement: unverified` — widely reported as an AI incident, but the primary source contains no AI. Kept so the claim is **searchable together with its rebuttal**.
- `ai_involvement: disputed` — the vendor and the reporting disagree; both accounts are preserved side by side in the record.

Full criteria: [docs/scope.md](docs/scope.md).

## Data quality

<!-- BEGIN:quality -->
|  |  |
|---|---|
| Source links | 533 links across 466 unique URLs |
| Records with no source | **0** — no source, no entry |
| Grade A (primary source) | 275 |
| Flagged as disputed | 14 |
| Verification rounds | 4 |
<!-- END:quality -->

The first three rounds checked **every record individually**. The fourth round did a **coverage audit** and still found roughly 11% missing. These catch entirely different problems: "is what we have correct" and "is what we should have here" are separate questions and have to be asked separately.

Those four rounds deleted two fabricated entries, corrected PaperCut's "domain admin in six hours" to **seven minutes**, and downgraded Step Finance to grade D because the primary reporting never mentions AI at all. Every correction is recorded in [docs/data-quality.md](docs/data-quality.md) — nothing was silently overwritten.

## Cite

<!-- BEGIN:cite -->
```bibtex
@misc{orca_ai_incident_archive,
  title  = {Orca AI Incident Archive: An open database of real-world AI agent incidents},
  year   = {2026},
  note   = {317 records, 2025-01 to 2026-09; 122 with confirmed real-world harm},
  url    = {https://github.com/Continuum-AI-Corp/Orca-AI-Incident-Archive}
}
```
<!-- END:cite -->

When citing a single record, use its `id` — for example `orca:2026-07-09-openai-agents-breach-huggingface`.

## Contribute

Corrections, missing records and better sources are all welcome. Three hard rules:

1. **Every record needs a primary source you can click.** No source, no merge.
2. **If you are unsure, label it — do not delete it.** Disputed facts get `disputed: true` and both accounts stay in the record.
3. **Corrections go into the record, never silently over it.** Say what changed and why.

See [CONTRIBUTING.md](CONTRIBUTING.md). Issue templates for [a new record](.github/ISSUE_TEMPLATE/new-incident.yml) and [a correction](.github/ISSUE_TEMPLATE/correction.yml) are set up.

## Licence and disclaimer

Licensed [CC BY 4.0](LICENSE) — attribution required. Linked source material remains the copyright of its respective owners.

This archive records **only publicly disclosed events**. It contains no undisclosed vulnerability detail, no exploit code and no attack tooling. Classification and severity are the editors' judgement, not an official finding by any vendor or regulator. If you are an affected party and believe a record is wrong, open an issue — it will be checked and corrected.

---

<sub><!-- BEGIN:footer -->Built 2026-09-16 · 317 records · 22 months<!-- END:footer --></sub> · <sub>Structure: [SCHEMA.md](SCHEMA.md) · Data: [dist/](dist/README.md)</sub>
