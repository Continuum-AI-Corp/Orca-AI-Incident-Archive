---
id: 2026-01-25-clawhub-skill-e-yi-ji
title: "Malicious ClawHub skills surge"
title_zh: "ClawHub 恶意 skill 激增"
title_ja: "悪性ClawHubスキルが急増"
title_ko: "악성 ClawHub 스킬 급증"
title_de: "Bösartige ClawHub-Skills nehmen sprunghaft zu"
title_fr: "Explosion des skills malveillants sur ClawHub"
title_es: "Aumentan las skills maliciosas de ClawHub"
date: 2026-01-25
date_precision: part
date_raw: "late 2026-01"

kind: incident
type: [SUPPLY]
severity: high
confidence: B
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Grew from 28 to 386 in four days, disguised as cryptocurrency tools


summary_zh: |
  4 天内从 28 个涨到 386 个，伪装成加密货币工具

summary_ja: |
  4日間で28件から386件に増加。暗号資産ツールを装っていた

summary_ko: |
  나흘 만에 28개에서 386개로 늘었고, 가상자산 도구로 위장했다

summary_de: |
  Wuchsen in vier Tagen von 28 auf 386, getarnt als Krypto-Tools

summary_fr: |
  Passés de 28 à 386 en quatre jours, déguisés en outils de cryptomonnaie

summary_es: |
  Pasaron de 28 a 386 en cuatro días, disfrazadas de herramientas de criptomonedas

sources:
  - url: https://theori.io/ko/blog/2026-h1-hot-security-issue-case
    label: Theori 2026 H1 roundup

disputed: false
landmark: false
scan_month: 2026-01
scan_ref: "SCAN.md §6 2026-01"
---

# Malicious ClawHub skills surge

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## Summary

Grew from 28 to 386 in four days, disguised as cryptocurrency tools

## Attack chain

```mermaid
flowchart LR
    E["Poisoned packages / repositories / agent config"]:::entry
    S0["Developer or agent installs it automatically"]:::step
    I["Credential theft and self-propagation"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Theori 2026 H1 roundup | <https://theori.io/ko/blog/2026-h1-hot-security-issue-case> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-01-25` (raw: late 2026-01, precision `part`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning |
| Severity | **High** `high` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-01-25-clawhub-skill-e-yi-ji` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-02-09` [Clinejection](../2026-02/2026-02-09-clinejection.md)<br>  <sub>Clinejection</sub>
- `2026-02-01` [ClawHavoc campaign](../2026-02/2026-02-01-clawhavoc-zhan-yi.md)<br>  <sub>ClawHavoc campaign</sub>
- `2025-11-21` [Shai-Hulud 2.0](../2025-11/2025-11-21-shai-hulud.md)<br>  <sub>Shai-Hulud 2.0</sub>
- `2026-03-01` [Hades: a sustained campaign turning AI coding assistants into the attack surface](../2026-03/2026-03-01-hades-campaign-ai-coding-assistants.md)<br>  <sub>Hades: a sustained campaign turning AI coding assistants into the attack surface</sub>

---

[← 2026-01 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-01/2026-01-25-clawhub-skill-e-yi-ji.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
