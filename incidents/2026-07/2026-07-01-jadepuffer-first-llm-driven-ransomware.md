---
id: 2026-07-01-jadepuffer-first-llm-driven-ransomware
title: "JADEPUFFER: first ransomware driven end-to-end by an LLM"
title_zh: "JADEPUFFER：首起 LLM 全程驱动的勒索攻击"
title_ja: "JADEPUFFER：LLMがエンドツーエンドで主導した初のランサムウェア"
title_ko: "JADEPUFFER: LLM이 종단 간 구동한 최초의 랜섬웨어"
title_de: "JADEPUFFER: erste durchgängig LLM-gesteuerte Ransomware"
title_fr: "JADEPUFFER : premier ransomware piloté de bout en bout par un LLM"
title_es: "JADEPUFFER: el primer ransomware dirigido de extremo a extremo por un LLM"
date: 2026-07-01
date_precision: day
date_raw: "2026-07-01"

kind: incident
type: [WEAPON]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Sysdig discloses JADEPUFFER: the first attack driven end-to-end by an LLM, from reconnaissance and lateral movement to encryption and extortion, with humans authorising only at key points.


summary_zh: |
  Sysdig 披露 JADEPUFFER：首起从侦察、横移到加密勒索全程由 LLM 驱动的攻击，人类只在关键节点授权。

summary_ja: |
  SysdigがJADEPUFFERを公表：偵察と横展開から暗号化と恐喝までLLMがエンドツーエンドで主導し、人間は要所での承認のみを行った初の攻撃である。

summary_ko: |
  Sysdig가 JADEPUFFER를 공개했다. 정찰과 측면 이동부터 암호화와 갈취까지 LLM이 종단 간 구동하고 사람은 핵심 지점에서만 승인하는 최초의 공격이다.

summary_de: |
  Sysdig legt JADEPUFFER offen: der erste Angriff, der durchgängig von einem LLM gesteuert wurde — von Aufklärung und lateraler Bewegung bis Verschlüsselung und Erpressung, wobei Menschen nur an Schlüsselstellen genehmigten.

summary_fr: |
  Sysdig divulgue JADEPUFFER : la première attaque pilotée de bout en bout par un LLM, de la reconnaissance et du mouvement latéral au chiffrement et à l'extorsion, les humains n'autorisant qu'à des points clés.

summary_es: |
  Sysdig divulga JADEPUFFER: el primer ataque dirigido de extremo a extremo por un LLM, desde el reconocimiento y el movimiento lateral hasta el cifrado y la extorsión, con humanos autorizando solo en puntos clave.

sources:
  - url: https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion
    label: Sysdig

disputed: false
landmark: true
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# JADEPUFFER: first ransomware driven end-to-end by an LLM

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

Sysdig discloses JADEPUFFER: the first attack driven end-to-end by an LLM, from reconnaissance and lateral movement to encryption and extortion, with humans authorising only at key points.

## Attack chain

```mermaid
flowchart LR
    E["Attacker + jailbreak script"]:::entry
    S0["LLM orchestrator drives a cluster of sub-agents"]:::step
    I["Target systems compromised"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

| Stage | Detail |
|---|---|
| Initial intrusion | Internet-exposed **Langflow** with missing authentication on the code-validation endpoint (**CVE-2025-3248**) → unauthenticated arbitrary Python execution |
| Reconnaissance | Enumerated hosts and hunted for LLM-provider API keys and cloud/database credentials; dumped Langflow's own Postgres; enumerated MinIO with default credentials to grab `credentials.json`; planted a cron calling out every 30 minutes |
| Actual target | A separate internet-facing server running **MySQL + Alibaba Nacos** |
| Success | root on MySQL; took over Nacos with the 2021 auth bypass **CVE-2021-29441** plus the default signing key, and injected a backdoor admin |
| Damage | Encrypted **1,342 Nacos configuration entries** with `AES_ENCRYPT()`, dropped the original and history tables, and left a ransom note |
| **Fatal detail** | **The key was randomly generated, shown once on standard output, and never saved or sent — paying the ransom would not restore anything** |
| Evidence it was AI-driven | ① Natural-language comments in the code explaining the reasoning for each step ② a precise correction within **31 seconds** of a failed login ③ 600+ consistent actions |

> This is the endgame form of the `WEAPON` category: **the attackers did not even check whether their own ransomware could decrypt**. AI industrialised the attack, and industrialised the sloppiness too.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Sysdig | <https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-01` (raw: 2026-07-01, precision `day`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-07-01-jadepuffer-first-llm-driven-ransomware` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-07-01` [Taiwan's nuclear safety commission and other agencies breached by an agent swarm](2026-07-01-taiwan-government-agent-swarm.md)<br>  <sub>Taiwan's nuclear safety commission and other agencies breached by an agent swarm</sub>
- `2026-07-09` [OpenAI's agents breach Hugging Face](2026-07-09-openai-agents-breach-huggingface.md)<br>  <sub>OpenAI's agents breach Hugging Face</sub>
- `2026-07-30` [Hermes Agent attacks Thailand's Ministry of Finance unattended](2026-07-30-hermes-agent-thailand-finance-ministry.md)<br>  <sub>Hermes Agent attacks Thailand's Ministry of Finance unattended</sub>
- `2026-07-30` [Unit 42: autonomous campaigns run by Chinese-speaking operators](2026-07-30-unit42-chinese-speaking-autonomous-campaigns.md)<br>  <sub>Unit 42: autonomous campaigns run by Chinese-speaking operators</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-01-jadepuffer-first-llm-driven-ransomware.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
