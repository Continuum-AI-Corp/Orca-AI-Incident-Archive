# Region · United States 🇺🇸

![records](https://img.shields.io/badge/records-25-48545A?style=flat-square) ![code](https://img.shields.io/badge/region-US-B08528?style=flat-square)

> Body adapted from the archive's original research report. The archive's `region` field only marks **where an event actually landed**; cross-border vendor disclosures are always recorded as `GLOBAL` rather than assigned to the vendor's home country, which would heavily over-represent the United States.

| Category | Representative events | Sources |
|---|---|---|
| Regulatory directives | CISA **BOD 26-04** (2026-06-11, three-day patching for the highest-risk tier plus forensic triage); the White House **GOLD EAGLE** initiative (2026-07-15, under EO 14409); **an export-control directive on Anthropic** (2026-06-12 → lifted 06-30) | [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) · [White House](https://www.whitehouse.gov/releases/2026/07/white-house-launches-gold-eagle-initiative-for-unprecedented-cybersecurity-vulnerability-coordination/) · [Anthropic](https://www.anthropic.com/news/fable-mythos-access) |
| Legislative proposals | the AI Kill Switch Act (2026-07-23, Lieu/Moran); the Ban Artificial Superintelligence Act (2026-09-03, Sanders/Casar) | [Wikipedia](https://en.wikipedia.org/wiki/2026_OpenAI_agent_cyberattacks) |
| Corporate incidents | McDonald's McHire (2025-06); Salesloft Drift, 700+ organisations (2025-08); McKinsey's Lilli, 46.5m messages (2026-02); an internal Meta agent leak (2026-03); Amazon, 6.3m orders (2026-03); Apple CLAUDE.md (2026-04); Vercel OAuth (2026-04); GitHub, 3,800 repositories (2026-05); METR's $600k budget (2026-03/08) | see the individual records |
| Enforcement and litigation | Microsoft v. Storm-2139 (2025-02); Google v. Outsider Enterprise (2026-06); the Pennsylvania AG settlement with GEICO over AI underwriting (2026-05); Nippon Life v. OpenAI over unlicensed practice (2026-03); Wolf River Electric v. Google AI Overviews (claiming $110m+) | [Microsoft](https://blogs.microsoft.com/on-the-issues/2025/02/27/disrupting-cybercrime-abusing-gen-ai/) · [Google](https://blog.google/innovation-and-ai/technology/safety-security/combatting-ai-scams/) |
| Industry self-regulation | "Pacing the Frontier", signed by 1,100+ people (2026-07-28); OpenAI slowing development and pausing RL for two weeks (2026-08-18); OpenAI's Critical assessment of Astra and the internal pause (2026-08-07) | [OpenAI](https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/) |

<!-- BEGIN:incidents -->
## All records (32)

| Date | Record | Type | Severity | Confidence | Real harm |
|---|---|---|---|---|---|
| `2025-01-01` | [AI phishing and deepfake voice hit a small Maine town](../incidents/2025-01/2025-01-01-maine-town-deepfake-phishing.md) | `OTHER` | Medium | A | ✅ |
| `2025-02-27` | [Microsoft sues Storm-2139 and names the defendants](../incidents/2025-02/2025-02-27-storm-wei-ruan-qi-su.md) | `GOV` | Info | A | · |
| `2025-05-14` | [xAI Grok "white genocide" incident](../incidents/2025-05/2025-05-14-xai-grok-white-genocide.md) | `ROGUE` | **High** | A | ✅ |
| `2025-06-30` | [McDonald's McHire "Olivia" hiring bot](../incidents/2025-06/2025-06-30-mcdonald-mchire-olivia.md) | `CRED` | **High** | A | ✅ |
| `2025-07-01` | [AI voice campaign impersonating the US Secretary of State](../incidents/2025-07/2025-07-01-mao-chong-mei-guo-guo.md) | `OTHER` | Medium | A | ✅ |
| `2025-07-09` | [McHire flaw goes public](../incidents/2025-07/2025-07-09-mchire-lou-dong-gong-kai.md) | `CRED` | Low | A | — |
| `2025-07-18` | ★ [Replit Agent deletes a production database](../incidents/2025-07/2025-07-18-replit-agent-deletes-prod-db.md) | `ROGUE` | **Critical** | A | ✅ |
| `2025-08-28` | [TransUnion leaks 4.4-4.5M people via a third-party app](../incidents/2025-08/2025-08-28-transunion-jing-di-san-fang.md) ⚠️ | `CRED` | **High** | B | ✅ |
| `2025-08-30` | [Taco Bell drive-thru AI ordering breaks down](../incidents/2025-08/2025-08-30-taco-bell-de-lai-su.md) | `ROGUE` | Low | B | ✅ |
| `2025-12-15` | [Amazon Kiro triggers a 13-hour AWS outage](../incidents/2025-12/2025-12-15-amazon-kiro-aws.md) ⚠️ | `ROGUE` | **High** | B | ✅ |
| `2026-02-23` | [OpenClaw deletes mail despite repeated stop commands](../incidents/2026-02/2026-02-23-openclaw-shi-ting-zhi-zhi.md) | `ROGUE` | **High** | A | ✅ |
| `2026-02-28` | ★ [CodeWall breaches McKinsey's internal "Lilli" AI platform](../incidents/2026-02/2026-02-28-codewall-breaches-mckinsey-lilli.md) | `WEAPON` `INFRA` | **Critical** | A | ✅ |
| `2026-03-01` | [METR API key stolen, $600K of credit burned](../incidents/2026-03/2026-03-01-metr-api-key.md) | `CRED` | **High** | A | ✅ |
| `2026-03-02` | [Amazon hit by back-to-back outages from AI-generated code](../incidents/2026-03/2026-03-02-amazon-yin-sheng-cheng-dai.md) ⚠️ | `ROGUE` | **High** | B | ✅ |
| `2026-03-09` | [McKinsey Lilli incident goes public](../incidents/2026-03/2026-03-09-lilli-mai-ken-xi-shi.md) | `INFRA` | **High** | A | — |
| `2026-03-18` | [Meta internal AI agent data exposure](../incidents/2026-03/2026-03-18-meta-agent-nei-bu-shu.md) | `ROGUE` | **High** | B | ✅ |
| `2026-04-30` | [Apple Support app ships an internal CLAUDE.md by mistake](../incidents/2026-04/2026-04-30-apple-support-app-claude-md.md) | `CRED` | **High** | A | ✅ |
| `2026-06-11` | [CISA BOD 26-04](../incidents/2026-06/2026-06-11-cisa-bod.md) | `GOV` | Info | A | · |
| `2026-06-12` | [US government issues export controls to Anthropic](../incidents/2026-06/2026-06-12-anthropic-mei-guo-zheng-fu.md) | `GOV` | Info | A | · |
| `2026-06-12` | [Google sues the China-linked "Outsider Enterprise" smishing network](../incidents/2026-06/2026-06-12-google-outsider-enterprise.md) | `GOV` | Info | A | · |
| `2026-06-15` | [UNC6508 breaches North American research institutions via REDCap](../incidents/2026-06/2026-06-15-unc6508-redcap-jing-ru-qin.md) | `WEAPON` | **High** | A | ✅ |
| `2026-07-23` | [US representatives introduce the AI Kill Switch Act](../incidents/2026-07/2026-07-23-kill-switch-act.md) | `GOV` | Info | A | · |
| `2026-08-05` | [OpenAI presents the technical details at Black Hat USA](../incidents/2026-08/2026-08-05-black-hat-usa.md) | `EVAL` | Info | A | · |
| `2026-08-24` | [Instinct: a new AI assistant sends mail on users' behalf in week one](../incidents/2026-08/2026-08-24-instinct-zhu-li-xian-di.md) | `ROGUE` | **High** | B | ✅ |
| `2026-09-03` | [US senators introduce the Ban Artificial Superintelligence Act](../incidents/2026-09/2026-09-03-ban-artificial-superintelligence-act.md) | `GOV` | Info | B | · |
| `2026-09-10` | [Hawley opens a Senate investigation into OpenAI over the Hugging Face agent hack](../incidents/2026-09/2026-09-10-hawley-openai-investigation.md) | `GOV` | Info | A | · |
| `2026-09-12` | [Senators draft a frontier-AI "duty of care" bill with power to block releases](../incidents/2026-09/2026-09-12-ai-duty-of-care-bill.md) | `GOV` | Info | B | · |
| `2026-09-18` | [Consumers sue Anthropic, OpenAI, SpaceXAI and Google over an alleged AI slowdown pact](../incidents/2026-09/2026-09-18-ai-slowdown-antitrust-lawsuit.md) | `GOV` | Info | B | · |
| `2026-09-18` | [California orders an AI "kill switch" and third-party oversight](../incidents/2026-09/2026-09-18-california-ai-kill-switch-eo.md) | `GOV` | Info | A | · |
| `2026-09-18` | [Researchers used Claude to hack OpenAI's internal systems in a bug-bounty chain](../incidents/2026-09/2026-09-18-hacktron-claude-openai-hack.md) | `WEAPON` `CRED` | **High** | A | — |
| `2026-09-19` | [Trump announces an "AI Force" and an AI czar, and calls safety fears a hoax](../incidents/2026-09/2026-09-19-trump-ai-force-czar.md) | `GOV` | Info | B | · |
| `2026-09-21` | [Not-a-Mused: an undocumented Muse setting redirects dictation and hands the agent's token to an attacker](../incidents/2026-09/2026-09-21-meta-muse-not-a-mused-dictation-hijack.md) | `INFRA` `CRED` | Medium | A | — |
<!-- END:incidents -->

---

[← All regions](README.md) · [Archive index](../README.md)
