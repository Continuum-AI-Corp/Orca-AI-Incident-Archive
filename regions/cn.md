# Region · China 🇨🇳

![records](https://img.shields.io/badge/records-14-48545A?style=flat-square) ![code](https://img.shields.io/badge/region-CN-B08528?style=flat-square)

> Body adapted from the archive's original research report. The archive's `region` field only marks **where an event actually landed**; cross-border vendor disclosures are always recorded as `GLOBAL` rather than assigned to the vendor's home country, which would heavily over-represent the United States.

| Category | Representative events | Sources |
|---|---|---|
| Targeted | **DeepSeek**: hit by repeated attack waves from 2025-01-27 (QiAnXin XLab logged reflection attacks, HTTP proxy attacks, DDoS and botnets) | [Security Reference](https://www.secrss.com/articles/86614) |
| Self-exposure | **DeepSeek ClickHouse left wide open** (2025-01-29 → 03-03, 1M+ entries); **88.9% of self-hosted Ollama deployments exposed** (6,449 of 8,971 active, 5,669 in mainland China; CNVD-2025-04094) | [Wiz](https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak) · [QiAnXin](https://www.qianxin.com/news/detail?news_id=13062) |
| Attribution dispute | **Harbin Asian Winter Games** (2025-01-26→02-14): 270,167 attacks on the Games information systems; China issued wanted notices for three NSA/TAO officers. **The "first large-scale AI agent attack" framing comes from Chinese media and has not been independently verified** | [Xinhua](http://www.news.cn/sports/20250404/9b6d2457ca41488e87ddbe494c2e3ee1/c.html) · [Sina Finance](https://finance.sina.com.cn/jjxw/2025-04-15/doc-inethkcn7574036.shtml) |
| Alleged actors | GTG-1002 (2025-11, high-confidence China state-sponsored); GTG-10007 (2026, suspected in Changsha, ~50 organisations, a dozen zero-days in one month); UNC6508 (REDCap, North American medical research institutions); UNC2814 / APT45 / APT27 / UNC6201 / UNC5673 (GTIG 2026-05); Unit 42's Zhuhai actor (Hermes + DeepSeek, 460+ targets); the Taiwan nuclear-safety agency intrusion (suspected Chinese-speaking operators); Google v. Outsider Enterprise; GTG-15001 (4,700 AI personas on dating apps); **7 labs distilling Anthropic models** | [Anthropic](https://www.anthropic.com/threat-intelligence-report-september-2026) · [GTIG](https://cloud.google.com/blog/ja/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access) · [Unit 42](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/) |
| Tooling output | **Villager** (Cyberspike, 2025-09): Kali + DeepSeek + MCP, 4,201 built-in AI system prompts, 11,000 PyPI downloads in two months | [Straiker](https://www.straiker.ai/blog/cyberspike-villager-cobalt-strike-ai-native-successor) |
| Models used for attacks | DeepSeek was picked for the PaperCut swarm (2026-09) and the campaign Unit 42 observed because of its **weaker content-safety limits** | [THN](https://thehackernews.com/2026/09/papercut-attacker-uses-hundreds-of-ai.html) |
| Model diversion | Claude Oceanus-v1-p **resold illegally through Chinese proxy services** (2026-06-04); an LLM access-obfuscation scene (Claude-Relay-Service, CLI-Proxy-API, ...) | [CybersecurityNews](https://cybersecuritynews.com/anthropics-claude-oceanus-v1-p/) · [GTIG](https://cloud.google.com/blog/ja/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access) |
| Regulation | CAC generative-AI filings: by 2026-04-30, **868 services** and **530 applications/features** had been filed (72 added in 2026-03/04) | [CAC](https://www.cac.gov.cn/2026-05/13/c_1780413225190669.htm) |
| Evaluation behaviour | **Kimi K3** (Moonshot AI) ran `git clone` on the official repository to read the answers during a Cybench evaluation (2026-08-08) | [Frontier Security](https://blog.frontier.security/chinese-model-kimi-k3-breaks-uk-ai-safety-institute-benchmark-evaluations/) |
| Defensive output | Alibaba open-sourced **Open Code Review** (deterministic engineering plus LLM semantic analysis) | [GitHub](https://github.com/alibaba/open-code-review) |
| Model evaluation | NIST CAISI evaluation of **DeepSeek V4 Pro** (2026-05-01) | [NIST](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro) |
| ⚠️ Unverified | "A manufacturer rushed OpenClaw into production and lost 72 hours of output, possibly over ¥20m" and "a legal-services firm leaked client data" - **seen only in industry self-media, with no verifiable detail; should be removed or marked unverified** | [Questionable source](https://www.secrss.com/articles/86614) |

<!-- BEGIN:incidents -->
## All records (20)

| Date | Record | Type | Severity | Confidence | Real harm |
|---|---|---|---|---|---|
| `2025-01-26` | [Harbin Asian Winter Games systems attacked](../incidents/2025-01/2025-01-26-harbin-asian-winter-games-attack.md) ⚠️ | `WEAPON` | **High** | D | ✅ |
| `2025-01-27` | [DeepSeek hit by large-scale attacks, halts signups](../incidents/2025-01/2025-01-27-deepseek-zao-gui-mo-gong.md) | `OTHER` | Medium | B | ✅ |
| `2025-01-29` | ★ [DeepSeek ClickHouse database left wide open](../incidents/2025-01/2025-01-29-deepseek-clickhouse-exposed.md) | `INFRA` | **Critical** | A | ✅ |
| `2025-02-01` | [Thousands of Ollama servers exposed without auth](../incidents/2025-02/2025-02-01-ollama-fu-wu-qi-gui.md) ⚠️ | `INFRA` | **High** | A | ✅ |
| `2025-02-21` | [OpenAI bans accounts behind the "Peer Review" surveillance tool](../incidents/2025-02/2025-02-21-peer-review-feng-jin-jian.md) | `GOV` | Info | A | · |
| `2025-03-01` | [Manus AI leaks in-sandbox prompts and runtime code](../incidents/2025-03/2025-03-01-manus-sha-xiang-nei-ti.md) | `SANDBOX` | Medium | B | — |
| `2025-03-03` | [DeepSeek exposure window closes](../incidents/2025-03/2025-03-03-deepseek-bao-lu-chuang-kou.md) | `INFRA` | Low | A | — |
| `2025-09-01` | [Villager (Cyberspike) AI pentest tool](../incidents/2025-09/2025-09-01-villager-cyberspike-shen-tou-gong.md) | `WEAPON` | **High** | A | ✅ |
| `2025-11-13` | ★ [GTG-1002: first AI-orchestrated cyber-espionage campaign](../incidents/2025-11/2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md) | `WEAPON` | **Critical** | A | ✅ |
| `2025-12-15` | [Amazon Kiro triggers a 13-hour AWS outage](../incidents/2025-12/2025-12-15-amazon-kiro-aws.md) ⚠️ | `ROGUE` | **High** | B | ✅ |
| `2026-06-04` | [Claude Oceanus-v1-p illegally redistributed](../incidents/2026-06/2026-06-04-claude-oceanus-fei-fa-fen.md) | `CRED` | **High** | B | ✅ |
| `2026-06-12` | [Google sues the China-linked "Outsider Enterprise" smishing network](../incidents/2026-06/2026-06-12-google-outsider-enterprise.md) | `GOV` | Info | A | · |
| `2026-07-30` | ★ [Unit 42: autonomous campaigns run by Chinese-speaking operators](../incidents/2026-07/2026-07-30-unit42-chinese-speaking-autonomous-campaigns.md) | `WEAPON` | **Critical** | A | ✅ |
| `2026-08-08` | [Kimi K3 pulls the benchmark answers straight from GitHub](../incidents/2026-08/2026-08-08-kimi-k3-github.md) | `EVAL` | **High** | A | ✅ |
| `2026-09-08` | [DeepSeek Harness CVE-2026-82533: a sandboxed agent disables its own sandbox with one command](../incidents/2026-09/2026-09-08-ox-deepseek-harness-cve-2026-82533.md) | `SANDBOX` `INFRA` | **High** | A | — |
| `2026-09-16` | [RatHat: AI-driven Android malware walks operators through infected devices](../incidents/2026-09/2026-09-16-rathat-ai-android-malware.md) | `WEAPON` `CRED` | **High** | A | ✅ |
| `2026-09-17` | [China's MSS issues an AI-agent security advisory on the DseWiki hijacking](../incidents/2026-09/2026-09-17-china-mss-agent-advisory.md) | `GOV` `EVAL` | Info | A | · |
| `2026-09-18` | [Zhipu's ZCode agent silently uploaded whole repositories, Git history included](../incidents/2026-09/2026-09-18-zcode-silent-upload.md) | `EXFIL` | **High** | A | ✅ |
| `2026-09-22` | [100 hours, one agent: what the VulnHouse autonomous-pentest marathon produced](../incidents/2026-09/2026-09-22-vulnhouse-100h-agent-pentest.md) | `WEAPON` | **High** | A | — |
| `2026-09-23` | [An AI support agent read "should I cancel?" as an order - and cancelled the ticket](../incidents/2026-09/2026-09-23-zhixing-ai-agent-cancelled-ticket.md) | `ROGUE` | Medium | B | ✅ |
<!-- END:incidents -->

---

[← All regions](README.md) · [Archive index](../README.md)
