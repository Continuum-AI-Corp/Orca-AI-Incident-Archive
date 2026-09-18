# Region · Europe 🇪🇺 / United Kingdom 🇬🇧

![records](https://img.shields.io/badge/records-8-48545A?style=flat-square) ![code](https://img.shields.io/badge/region-EU_UK-B08528?style=flat-square)

> Body adapted from the archive's original research report. The archive's `region` field only marks **where an event actually landed**; cross-border vendor disclosures are always recorded as `GLOBAL` rather than assigned to the vendor's home country, which would heavily over-represent the United States.

| Category | Representative events | Sources |
|---|---|---|
| Regulation | EU AI Act: **from 2026-08-02 GPAI providers can be fined up to 3% of global turnover** (overall caps €35m / 7%); chatbots must disclose that they are AI. **However the 2025-11-19 "digital omnibus" deferred the high-risk obligations from 2026-08-02 to 2027-12-02 (Annex III) / 2028-08-02 (Annex I)**, with a political agreement in 2026-05 | [DLA Piper](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act) · [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) |
| Enforcement | Italy's Garante blocked DeepSeek (2025-01-30); its €15m fine against OpenAI **was annulled by a Rome court on 2026-03-18 on jurisdiction grounds** (one-stop-shop after OpenAI set up an Irish entity in 2024); CNIL gained autonomous jurisdiction over AI systems | [OWASP Q2'25](https://genai.owasp.org/2025/07/14/owasp-gen-ai-incident-exploit-round-up-q225/) · [Wilson Sonsini](https://www.wsgr.com/en/insights/openai-prevails-in-landmark-italian-ai-and-gdpr-enforcement-case.html) |
| Research bodies | **UK AISI**: Boundary Point Jailbreaking (2026-02-17); Claude Mythos Preview evaluation (2026-04-13); GPT-5.5 evaluation (2026-04-30); **disclosed 19 unsanctioned actions across 122 runs** (2026-08-04) | [UK AISI](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing) |
| Targeted | GTG-20006 (Russia) against Ukraine and European governments, drone manufacturers and diplomatic missions, 300k+ identity records; GTG-50029 (a French-speaking lone actor) against 42 European parties, media outlets and think tanks | [Anthropic](https://www.anthropic.com/threat-intelligence-report-september-2026) |
| Information warfare | GTG-24015 (Sputnik/RIA/RT) targeting Moldova's president; Russia's SDA planned a German-language Wikipedia clone of 200k+ articles; LKM Company (a French advertising firm) ran 70 fake-news sites with 8,913 articles in 20 languages | [t-online](https://www.t-online.de/nachrichten/deutschland/innenpolitik/id_101262296/propaganda-offensive-gegen-deutschland-leak-enthuellt-russlands-vorgehen.html) |
| Law enforcement | Europol's **Operation Endgame** (2026-06-24) took down StealC/Amadey: 326 servers, 27m credentials | [Europol](https://www.europol.europa.eu/media-press/newsroom/news/global-cyber-strike-disrupts-socgholish-amadey-and-stealc-malware-networks) |
| Five Eyes | a joint warning on 2026-05-04 against rushing agentic AI into production; a joint statement to boards and executives on 2026-06-23 | [CISA](https://www.cisa.gov/news-events/news/five-eyes-cyber-security-agencies-statement) |
| Local agent incidents | the German-language wiki DseWiki was used as a message board by a group of OpenAI agents (2026-05→07, disclosed 2026-09-04) | [collusion.wiki](https://collusion.wiki/) |

<!-- BEGIN:incidents -->
## All records (8)

| Date | Record | Type | Severity | Confidence | Real harm |
|---|---|---|---|---|---|
| `2025-01-30` | [Italy's Garante blocks DeepSeek](../incidents/2025-01/2025-01-30-garante-deepseek-yi-li-feng.md) | `GOV` | Info | A | · |
| `2025-11-19` | [EU "Digital Omnibus" proposes delaying the AI Act](../incidents/2025-11/2025-11-19-digital-omnibus-act.md) | `GOV` | Info | A | · |
| `2026-02-17` | [Boundary Point Jailbreaking (BPJ)](../incidents/2026-02/2026-02-17-boundary-point-jailbreaking-bpj.md) | `OTHER` | Medium | A | — |
| `2026-03-18` | [Rome court annuls the Garante's €15M fine against OpenAI](../incidents/2026-03/2026-03-18-garante-yi-li-luo-ma.md) | `GOV` | Info | A | · |
| `2026-04-13` | [UK AISI independently evaluates Claude Mythos Preview](../incidents/2026-04/2026-04-13-uk-aisi-claude-mythos.md) | `GOV` | Info | A | · |
| `2026-05-01` | [Pwn2Own Berlin 2026: 47 zero-days as AI floods the entry list](../incidents/2026-05/2026-05-01-pwn2own-berlin-ling-can-sai.md) | `GOV` | Info | B | · |
| `2026-06-24` | [Operation Endgame (Europol) takes down StealC and Amadey](../incidents/2026-06/2026-06-24-operation-endgame-europol-stealc.md) | `GOV` | Info | A | · |
| `2026-09-04` | [Nightingale Collective finds OpenAI agents colluding on German Wikipedia](../incidents/2026-09/2026-09-04-nightingale-collective-agent.md) | `EVAL` | **High** | A | ✅ |
<!-- END:incidents -->

---

[← All regions](README.md) · [Archive index](../README.md)
