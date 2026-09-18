---
id: 2025-03-01-chatgpt-ssrf-ye-li-yong
title: "ChatGPT SSRF CVE-2024-27564 exploited in the wild"
title_zh: "ChatGPT SSRF CVE-2024-27564 在野利用"
title_ja: "ChatGPTのSSRF脆弱性CVE-2024-27564が実悪用される"
title_ko: "ChatGPT SSRF CVE-2024-27564, 실제 공격에 악용"
title_de: "ChatGPT-SSRF CVE-2024-27564 in freier Wildbahn ausgenutzt"
title_fr: "CVE-2024-27564 : SSRF dans ChatGPT exploité en conditions réelles"
title_es: "CVE-2024-27564: SSRF de ChatGPT explotado en entornos reales"
date: 2025-03-01
date_precision: month
date_raw: "2025-03"

kind: incident
type: [INFRA]
severity: high
confidence: B
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Veriti observed 10,479 attack attempts in a single week, mostly against financial institutions


summary_zh: |
  Veriti 一周内观测到 10,479 次攻击尝试，主要打金融机构

summary_ja: |
  Veritiは1週間で10,479件の攻撃試行を観測。大半は金融機関を標的としていた

summary_ko: |
  Veriti는 한 주에 10,479건의 공격 시도를 관찰했으며 대부분 금융기관을 겨냥했다

summary_de: |
  Veriti beobachtete 10,479 Angriffsversuche in einer einzigen Woche, überwiegend gegen Finanzinstitute

summary_fr: |
  Veriti a observé 10 479 tentatives d'attaque en une seule semaine, principalement contre des institutions financières

summary_es: |
  Veriti observó 10,479 intentos de ataque en una sola semana, en su mayoría contra instituciones financieras

sources:
  - url: https://genai.owasp.org/2025/07/14/owasp-gen-ai-incident-exploit-round-up-q225/
    label: "OWASP Q2'25"

disputed: false
landmark: false
scan_month: 2025-03
scan_ref: "SCAN.md §5 2025-03"
---

# ChatGPT SSRF CVE-2024-27564 exploited in the wild

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

Veriti observed 10,479 attack attempts in a single week, mostly against financial institutions

## Attack chain

```mermaid
flowchart LR
    E["Agent infrastructure exposed to the internet"]:::entry
    S0["Unauthenticated access"]:::step
    I["RCE / data leak"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | OWASP Q2'25 | <https://genai.owasp.org/2025/07/14/owasp-gen-ai-incident-exploit-round-up-q225/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-03-01` (raw: 2025-03, precision `month`) |
| Kind | Incident `incident` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **High** `high` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-03-01-chatgpt-ssrf-ye-li-yong` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2025-03-03` [DeepSeek exposure window closes](2025-03-03-deepseek-bao-lu-chuang-kou.md)<br>  <sub>DeepSeek exposure window closes</sub>
- `2025-02-01` [Thousands of Ollama servers exposed without auth](../2025-02/2025-02-01-ollama-fu-wu-qi-gui.md)<br>  <sub>Thousands of Ollama servers exposed without auth</sub>
- `2025-04-29` [NVIDIA TensorRT-LLM deserialization RCE](../2025-04/2025-04-29-nvidia-tensorrt-llm-rce.md)<br>  <sub>NVIDIA TensorRT-LLM deserialization RCE</sub>
- `2025-01-29` [DeepSeek ClickHouse database left wide open](../2025-01/2025-01-29-deepseek-clickhouse-exposed.md)<br>  <sub>DeepSeek ClickHouse database left wide open</sub>

---

[← 2025-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-03/2025-03-01-chatgpt-ssrf-ye-li-yong.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
