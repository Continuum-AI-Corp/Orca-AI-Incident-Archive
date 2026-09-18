---
id: 2026-03-06-microsoft-as-tradecraft
title: "Microsoft, \"AI as tradecraft\""
title_zh: "Microsoft《AI as tradecraft》"
title_ja: "Microsoft「AI as tradecraft」"
title_ko: "마이크로소프트, \"AI as tradecraft\""
title_de: "Microsoft: „AI as tradecraft“"
title_fr: "Microsoft : « AI as tradecraft »"
title_es: "Microsoft, \"AI as tradecraft\""
date: 2026-03-06
date_precision: day
date_raw: "2026-03-06"

kind: report
type: [WEAPON]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  North Korea-linked **Jasper Sleet and Coral Sleet** use LLMs across the whole chain — phishing, code generation, persona fabrication and infrastructure management


summary_zh: |
  朝鲜系 **Jasper Sleet、Coral Sleet** 在钓鱼、代码生成、人物捏造、基础设施管理全链路使用 LLM

summary_ja: |
  北朝鮮関連の**Jasper SleetとCoral Sleet**が、フィッシング、コード生成、ペルソナの偽造、インフラ管理という全チェーンでLLMを使用

summary_ko: |
  북한 연계 **Jasper Sleet과 Coral Sleet**은 피싱, 코드 생성, 페르소나 조작, 인프라 관리까지 전 과정에서 LLM을 사용한다

summary_de: |
  Die mit Nordkorea verbundenen Gruppen **Jasper Sleet und Coral Sleet** nutzen LLMs über die gesamte Kette — Phishing, Codegenerierung, Erstellung von Personas und Infrastrukturverwaltung

summary_fr: |
  Les groupes liés à la Corée du Nord **Jasper Sleet et Coral Sleet** utilisent des LLM sur toute la chaîne — phishing, génération de code, fabrication de personas et gestion d'infrastructure

summary_es: |
  **Jasper Sleet y Coral Sleet**, vinculados a Corea del Norte, usan LLM en toda la cadena — phishing, generación de código, fabricación de personajes y gestión de infraestructura

sources:
  - url: https://www.microsoft.com/en-us/security/blog/2026/03/06/ai-as-tradecraft-how-threat-actors-operationalize-ai/
    label: Microsoft

disputed: false
landmark: false
scan_month: 2026-03
scan_ref: "SCAN.md §6 2026-03"
---

# Microsoft, "AI as tradecraft"

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

North Korea-linked **Jasper Sleet and Coral Sleet** use LLMs across the whole chain — phishing, code generation, persona fabrication and infrastructure management

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

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Microsoft | <https://www.microsoft.com/en-us/security/blog/2026/03/06/ai-as-tradecraft-how-threat-actors-operationalize-ai/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-03-06` (raw: 2026-03-06, precision `day`) |
| Kind | Threat report `report` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-03-06-microsoft-as-tradecraft` |

<sub>**Why this classification:** Threat intelligence report covering several incidents; it is not counted as a single incident itself, so `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-02-20` [AI-augmented actor compromises 600+ FortiGate devices](../2026-02/2026-02-20-fortigate-600-devices-compromised.md)<br>  <sub>AI-augmented actor compromises 600+ FortiGate devices</sub>
- `2026-02-25` [Nine Mexican government agencies breached](../2026-02/2026-02-25-mexico-nine-agencies-breached.md)<br>  <sub>Nine Mexican government agencies breached</sub>
- `2026-02-28` [CodeWall breaches McKinsey's internal "Lilli" AI platform](../2026-02/2026-02-28-codewall-breaches-mckinsey-lilli.md)<br>  <sub>CodeWall breaches McKinsey's internal "Lilli" AI platform</sub>
- `2026-04-08` [Aurora ransomware operators use Cursor Agent in live intrusions](../2026-04/2026-04-08-aurora-cursor-agent.md)<br>  <sub>Aurora ransomware operators use Cursor Agent in live intrusions</sub>

---

[← 2026-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-03/2026-03-06-microsoft-as-tradecraft.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
