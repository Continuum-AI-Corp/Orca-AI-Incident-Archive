# Region · Taiwan 🇹🇼 and other regions

![records](https://img.shields.io/badge/records-7-48545A?style=flat-square) ![code](https://img.shields.io/badge/region-TW_HK_SG_SEA_APAC_AU-B08528?style=flat-square)

> Body adapted from the archive's original research report. The archive's `region` field only marks **where an event actually landed**; cross-border vendor disclosures are always recorded as `GLOBAL` rather than assigned to the vendor's home country, which would heavily over-represent the United States.

| Region | Events | Sources |
|---|---|---|
| **Taiwan** | **2026-07-01→04: government agencies including the Nuclear Safety Commission breached by a Hermes + OpenClaw swarm** (8 sub-agents / 12 waves / 85 accounts / 2,500+ personnel records / 7+ energy companies); ClickFix malvertising drove **30.5%** of global victim traffic (2026-06) | [The Register](https://www.theregister.com/security/2026/08/12/near-autonomous-ai-agents-attack-taiwans-nuclear-safety-agency/5287055) · [Trend Micro](https://www.trendmicro.com/en/research/26/f/claudeai-shared-chat-abused-in-malvertising.html) |
| **Latin America** | 🇲🇽 nine Mexican government agencies (2025-12→2026-02), about 400m records and 150 GB | [Bloomberg](https://www.bloomberg.com/news/articles/2026-02-25/hacker-used-anthropic-s-claude-to-steal-sensitive-mexican-data) |
| **Southeast Asia** | 🇹🇭 Thailand's Ministry of Finance attacked by a Hermes Agent in YOLO mode (2026-07-30); 🇲🇾 Malaysian government agencies targeted over consecutive days; 🇲🇾 BBS Bilisim election manipulation across 222 constituencies; Cambodia/Myanmar scam networks | [Hunt.io](https://hunt.io/blog/thailand-ministry-finance-targeted-with-hermes-ai-agent) · [Unit 42](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/) |
| **Australia** | 2026-08-10 an AI agent broke into a gym booking system and deleted other users (**believed to be an Australian first**); ASD published agent-use guidance in 2026-07 and joined a CISA joint advisory | [ABC News](https://www.abc.net.au/news/2026-08-10/ai-assistant-hacks-gym-website-aus-cyber-attack/107007986) |
| **Africa** | 🇨🇫 the Central African Republic's information space was controlled by Russia's GTG-04001 (daily 98.9 FM broadcasts plus forged government documents) | [Anthropic](https://www.anthropic.com/threat-intelligence-report-september-2026) |
| **Middle East / India** | deepfake incidents in the Middle East jumped **643%** year on year (the world's fastest growth); a Singapore DaaS impersonation of executives stole millions of dollars; APAC is the region with the most election-related deepfake incidents | [StationX](https://app.stationx.net/articles/deepfake-statistics) |
| **Ukraine** | APT28 deployed **PROMPTSTEAL** in the field (the first real-world deployment of malware calling an LLM at runtime); Russia's CANFAIL / LONGSTREAM used LLM-generated decoy code for obfuscation | [GTIG PDF](https://services.google.com/fh/files/misc/advances-in-threat-actor-usage-of-ai-tools-en.pdf) |

<!-- BEGIN:incidents -->
## All records (7)

| Date | Record | Type | Severity | Confidence | Real harm |
|---|---|---|---|---|---|
| `2025-01-20` | [Hong Kong AI voice-clone crypto fraud](../incidents/2025-01/2025-01-20-hk-voice-clone-usdt-fraud.md) | `OTHER` | Medium | A | ✅ |
| `2025-03-01` | [Deepfake voice defeats bank voiceprint auth in HK and Singapore](../incidents/2025-03/2025-03-01-hk-sg-bank-deepfake-voiceprint.md) | `OTHER` | **High** | A | ✅ |
| `2026-06-18` | [ClickFix malvertising abuses claude.ai shared conversations](../incidents/2026-06/2026-06-18-clickfix-claude-ai-e-yi-guang.md) | `SUPPLY` | **High** | A | ✅ |
| `2026-07-01` | ★ [Taiwan's nuclear safety commission and other agencies breached by an agent swarm](../incidents/2026-07/2026-07-01-taiwan-government-agent-swarm.md) | `WEAPON` | **Critical** | A | ✅ |
| `2026-07-30` | ★ [Hermes Agent attacks Thailand's Ministry of Finance unattended](../incidents/2026-07/2026-07-30-hermes-agent-thailand-finance-ministry.md) | `WEAPON` | **Critical** | A | ✅ |
| `2026-08-10` | [AI agent breaks into an Australian gym's booking system](../incidents/2026-08/2026-08-10-agent-shou-quan-qin-ru.md) | `ROGUE` | **High** | A | ✅ |
| `2026-08-12` | [Taiwan agent-swarm intrusion made public](../incidents/2026-08/2026-08-12-agent-tai-wan-feng-qun.md) | `WEAPON` | Low | A | ✅ |
<!-- END:incidents -->

---

[← All regions](README.md) · [Archive index](../README.md)
