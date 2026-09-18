# Topic · Offensive AI capability evolution (WEAPON)

![records](https://img.shields.io/badge/records-43-48545A?style=flat-square) ![type](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

> The prose on this page is taken from the archive's original research report; the "All records" table below is compiled automatically from the frontmatter in `incidents/`, and the two are updated together.

```
2025 Q1-Q2  │ AI as adviser
            │ OpenAI/Anthropic's assessment: wiring AI onto the old playbook sped things up but produced no new capability
            │
2025 Q3     │ AI as tool (vibe hacking)
            │ GTG-2002: Claude Code extorted 17 organisations (it even worked out the ransoms), humans still in the loop
            │ HexStrike-AI: 150 agents compressed the Citrix 0-day exploitation window to 10 minutes
            │
2025 Q4     │ AI as runtime (malware calls the LLM)
            │ PROMPTSTEAL (APT28, used live against Ukraine) called Qwen through the HF API to generate commands dynamically
            │ PROMPTFLUX called Gemini to obfuscate itself (still being tested)
            │ SesameOp used the OpenAI Assistants API as C2
            │
2025-11     │ ★ AI as orchestrator (GTG-1002)
            │ 80-90% of tactical actions executed autonomously, about 30 targets, peaks of several requests per second
            │ But: Claude frequently exaggerated results and even fabricated data → human review still required
            │
2026 Q1     │ ★ Capability diffusion: one person = a nation-state (Mexico)
            │ 1,088 prompts → 5,000+ commands, 9 government agencies, 400 million records
            │ AWS FortiGate campaign: no zero-day needed, AI provided the scale, 600+ devices in 5 weeks
            │
2026 Q2     │ AI turns on the defenders' AI
            │ macOS.Gaslight: 38 forged system messages prompt-injecting an AI analyst
            │ GTG-50020: prompt injection against AI evaluation sandboxes, 30 AI companies hit in 4 days
            │ N-hour: Firefox patch diff → 8 working exploits within 12 hours (the first in under 1 hour)
            │
2026 Q3     │ ★ Full autonomy + swarms
            │ Taiwan: 8 sub-agents / 12 waves / 4 days / 85 government accounts (Hermes + OpenClaw)
            │ JADEPUFFER: ransomware driven end to end by an LLM (it did not even save the keys)
            │ PaperCut swarm: hundreds of agents, 11 organisations breached in 26 seconds, 395 in 48 countries
            │ Unit 42: the autonomous parts still fail when preconditions are not met, but operationally it already works
```

**Actor profiles from the GTIG 2026-05 report** ([source](https://cloud.google.com/blog/ja/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)):

| Actor | Attribution | Use of AI |
|---|---|---|
| **UNC2814** | China | Persona-based jailbreaks ("embedded-device security expert") for RCE vulnerability research on TP-Link firmware / OFTP |
| **APT45** | China | Thousands of repeated prompts to recursively analyse CVEs and validate PoCs; trialled agent tools such as OpenClaw / OneClaw plus deliberately vulnerable test environments |
| **APT27** | China | Used Gemini to speed up development of relay-box management applications for the ORB network (`maxHops=3`, 4G/5G SIM residential IPs) |
| **UNC6201** | China | Python scripts on GitHub automatically register and deregister premium LLM accounts, bypassing CAPTCHAs and SMS verification to evade bans |
| **UNC5673** (TEMP.Hex) | China | Claude-Relay-Service and CLI-Proxy-API to pool accounts + anti-detect browsers; targets are South Asian / Southeast Asian governments |
| **Hexstrike actor** | China | Hexstrike + the Graphiti temporal knowledge graph for autonomous reconnaissance; targets include **a Japanese technology company** and an East Asian cybersecurity platform |
| Russian-linked intrusion group | Russia | **CANFAIL / LONGSTREAM**: used an LLM to generate long stretches of harmless decoy code as obfuscation (the comments even say the filler is what the LLM asked for) |
| **TeamPCP (UNC6780)** | Criminal | Trivy / Checkmarx / LiteLLM / BerriAI supply chains, planting the SANDCLOCK credential stealer |
| **PROMPTSPY** | — | Android backdoor: calls `gemini-2.5-flash-lite`, serialises the UI hierarchy to XML for Gemini, parses the JSON reply into CLICK/SWIPE instructions to **operate the phone autonomously**; captures biometrics for authentication-gesture replay; covers the uninstall button with an invisible overlay |

**Three counter-intuitive facts** (all from primary sources, and worth writing into the README):

1. **AI attackers hallucinate.** In GTG-1002, the credentials Claude claimed to have obtained were invalid and its reported "major findings" were public information. [Anthropic says explicitly that this remains the main obstacle to fully autonomous attacks](https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf).
2. **The autonomous part does not have a high success rate.** In the Chinese-speaking actor campaign [Unit 42](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/) observed, the autonomous execution failed because the targets did not meet its preconditions; **what actually succeeded was the manual part**.
3. **Most AI-generated patches do not fix the problem.** [1Password](https://1password.com/blog/why-ai-generated-patches-still-require-human-review): of 6,080 AI patches, only 26.0% eliminated the vulnerability completely, and 53.9% left it in place or introduced a new one. **AI capability is not growing symmetrically on the two sides.**

---

<!-- BEGIN:incidents -->
## All records (44)

| Date | Record | Type | Severity | Confidence | Real harm |
|---|---|---|---|---|---|
| `2025-01-26` | [Harbin Asian Winter Games systems attacked](../incidents/2025-01/2025-01-26-harbin-asian-winter-games-attack.md) ⚠️ | `WEAPON` | **High** | D | ✅ |
| `2025-04-24` | [Anthropic's first misuse report](../incidents/2025-04/2025-04-24-anthropic-shou-fen-lan-yong.md) | `WEAPON` | Info | A | · |
| `2025-05-01` | [Anthropic logs the start of GTG-2002 activity](../incidents/2025-05/2025-05-01-anthropic-gtg-ji-lu-huo.md) | `WEAPON` | Medium | A | — |
| `2025-05-01` | [AI-driven credential stuffing and scanning goes to scale](../incidents/2025-05/2025-05-01-qu-dong-zhuang-ku-zi.md) | `WEAPON` | Medium | A | — |
| `2025-06-01` | [Anthropic logs the precursor to GTG-1002](../incidents/2025-06/2025-06-01-anthropic-gtg-ji-lu-shen.md) | `WEAPON` | Medium | A | — |
| `2025-06-01` | [Check Point's "Skynet" sample](../incidents/2025-06/2025-06-01-check-point-skynet.md) | `WEAPON` | Medium | A | — |
| `2025-06-05` | [OpenAI June threat report](../incidents/2025-06/2025-06-05-liu-wei-xie-bao-gao.md) | `WEAPON` | Info | A | · |
| `2025-08-26` | [ESET finds PromptLock](../incidents/2025-08/2025-08-26-eset-promptlock-fa-xian.md) | `WEAPON` | **High** | A | ✅ |
| `2025-08-27` | [Anthropic August threat report](../incidents/2025-08/2025-08-27-anthropic-ba-wei-xie-bao.md) | `WEAPON` | Info | A | · |
| `2025-09-01` | [Villager (Cyberspike) AI pentest tool](../incidents/2025-09/2025-09-01-villager-cyberspike-shen-tou-gong.md) | `WEAPON` | **High** | A | ✅ |
| `2025-09-02` | [HexStrike-AI turned on a Citrix zero-day](../incidents/2025-09/2025-09-02-hexstrike-citrix-day.md) | `WEAPON` | **High** | A | ✅ |
| `2025-09-15` | [Anthropic detects GTG-1002](../incidents/2025-09/2025-09-15-anthropic-gtg-jian-ce-dao.md) | `WEAPON` | Medium | A | — |
| `2025-10-07` | [OpenAI October threat report](../incidents/2025-10/2025-10-07-shi-wei-xie-bao-gao.md) | `WEAPON` `GOV` | Info | A | · |
| `2025-11-03` | [SesameOp](../incidents/2025-11/2025-11-03-sesameop.md) | `WEAPON` | **High** | A | ✅ |
| `2025-11-05` | [GTIG: PROMPTFLUX / PROMPTSTEAL](../incidents/2025-11/2025-11-05-gtig-promptflux-promptsteal.md) | `WEAPON` | **High** | A | ✅ |
| `2025-11-13` | ★ [GTG-1002: first AI-orchestrated cyber-espionage campaign](../incidents/2025-11/2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md) | `WEAPON` | **Critical** | A | ✅ |
| `2025-12-28` | [Mexico government intrusion campaign begins](../incidents/2025-12/2025-12-28-mexico-government-intrusion-begins.md) | `WEAPON` | Medium | A | ✅ |
| `2026-01-01` | [Claude Code sprays credentials at a Mexican water utility's OT network](../incidents/2026-01/2026-01-01-ot-claude-code.md) | `WEAPON` | Low | B | ✅ |
| `2026-02-20` | ★ [AI-augmented actor compromises 600+ FortiGate devices](../incidents/2026-02/2026-02-20-fortigate-600-devices-compromised.md) | `WEAPON` | **Critical** | A | ✅ |
| `2026-02-25` | ★ [Nine Mexican government agencies breached](../incidents/2026-02/2026-02-25-mexico-nine-agencies-breached.md) | `WEAPON` | **Critical** | A | ✅ |
| `2026-02-28` | ★ [CodeWall breaches McKinsey's internal "Lilli" AI platform](../incidents/2026-02/2026-02-28-codewall-breaches-mckinsey-lilli.md) | `WEAPON` `INFRA` | **Critical** | A | ✅ |
| `2026-03-06` | [Microsoft, "AI as tradecraft"](../incidents/2026-03/2026-03-06-microsoft-as-tradecraft.md) | `WEAPON` | Info | A | · |
| `2026-04-08` | [Aurora ransomware operators use Cursor Agent in live intrusions](../incidents/2026-04/2026-04-08-aurora-cursor-agent.md) | `WEAPON` | **High** | A | ✅ |
| `2026-05-10` | ★ [First in-the-wild LLM agent running the full post-exploitation chain](../incidents/2026-05/2026-05-10-first-in-wild-autonomous-llm-post-exploitation.md) | `WEAPON` | **Critical** | A | ✅ |
| `2026-05-12` | [GTIG AI threat tracker, 2026 edition](../incidents/2026-05/2026-05-12-gtig-wei-xie-zhui-zong.md) | `WEAPON` | Info | A | · |
| `2026-06-02` | [CleverHans Lab adaptive AI worm PoC](../incidents/2026-06/2026-06-02-cleverhans-lab-poc.md) | `WEAPON` | Medium | A | — |
| `2026-06-03` | [Anthropic, "LLM ATT&CK Navigator"](../incidents/2026-06/2026-06-03-anthropic-llm-att-ck.md) | `WEAPON` | Info | A | · |
| `2026-06-09` | [Anthropic: N-day is really "N-hour"](../incidents/2026-06/2026-06-09-anthropic-day-hour.md) | `WEAPON` | Info | A | · |
| `2026-06-15` | [UNC6508 breaches North American research institutions via REDCap](../incidents/2026-06/2026-06-15-unc6508-redcap-jing-ru-qin.md) | `WEAPON` | **High** | A | ✅ |
| `2026-06-24` | [macOS.Gaslight: malware prompt-injects the AI analyst](../incidents/2026-06/2026-06-24-macos-gaslight-e-yi-ruan-jian.md) | `WEAPON` | Medium | A | — |
| `2026-07-01` | ★ [JADEPUFFER: first ransomware driven end-to-end by an LLM](../incidents/2026-07/2026-07-01-jadepuffer-first-llm-driven-ransomware.md) | `WEAPON` | **Critical** | A | ✅ |
| `2026-07-01` | ★ [Taiwan's nuclear safety commission and other agencies breached by an agent swarm](../incidents/2026-07/2026-07-01-taiwan-government-agent-swarm.md) | `WEAPON` | **Critical** | A | ✅ |
| `2026-07-08` | [Sygnia: AI-assisted attackers own an AWS environment in 72 hours](../incidents/2026-07/2026-07-08-sygnia-aws-fu-zhu-shi.md) | `WEAPON` | **High** | A | ✅ |
| `2026-07-09` | ★ [OpenAI's agents breach Hugging Face](../incidents/2026-07/2026-07-09-openai-agents-breach-huggingface.md) | `EVAL` `WEAPON` | **Critical** | A | ✅ |
| `2026-07-17` | [wp2shell: pre-auth RCE in WordPress core](../incidents/2026-07/2026-07-17-wp2shell-wordpress-rce.md) | `WEAPON` | **High** | A | — |
| `2026-07-30` | ★ [Hermes Agent attacks Thailand's Ministry of Finance unattended](../incidents/2026-07/2026-07-30-hermes-agent-thailand-finance-ministry.md) | `WEAPON` | **Critical** | A | ✅ |
| `2026-07-30` | ★ [Unit 42: autonomous campaigns run by Chinese-speaking operators](../incidents/2026-07/2026-07-30-unit42-chinese-speaking-autonomous-campaigns.md) | `WEAPON` | **Critical** | A | ✅ |
| `2026-08-12` | [Taiwan agent-swarm intrusion made public](../incidents/2026-08/2026-08-12-agent-tai-wan-feng-qun.md) | `WEAPON` | Low | A | ✅ |
| `2026-08-28` | ★ [PaperCut AI agent swarm campaign begins](../incidents/2026-08/2026-08-28-papercut-agent-swarm-campaign-begins.md) | `WEAPON` | **Critical** | A | ✅ |
| `2026-09-02` | [Unit 42: AI agents compress two weeks of intrusion work into 10 hours](../incidents/2026-09/2026-09-02-unit-agent-liang-ru-qin.md) | `WEAPON` | Info | A | · |
| `2026-09-10` | ★ [Anthropic September threat intelligence report](../incidents/2026-09/2026-09-10-anthropic-september-threat-report.md) | `WEAPON` | **Critical** | A | ✅ |
| `2026-09-11` | ★ [Claude used to scan 1.8 million Android apps for secrets](../incidents/2026-09/2026-09-11-claude-scans-18m-android-apks.md) | `WEAPON` | **Critical** | A | ✅ |
| `2026-09-14` | ★ [Spain's AEPD receives the first AI-agent-driven breach notification](../incidents/2026-09/2026-09-14-spain-aepd-agent-breach.md) | `WEAPON` | **Critical** | A | ✅ |
| `2026-09-15` | ★ [PaperCut AI agent swarm attack made public](../incidents/2026-09/2026-09-15-papercut-agent-swarm-disclosed.md) | `WEAPON` | **Critical** | A | ✅ |
<!-- END:incidents -->

---

[← All topics](../README.md) · [Archive index](../README.md)
