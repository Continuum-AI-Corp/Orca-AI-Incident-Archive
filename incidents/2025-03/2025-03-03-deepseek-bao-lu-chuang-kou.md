---
id: 2025-03-03-deepseek-bao-lu-chuang-kou
title: "DeepSeek exposure window closes"
title_zh: "DeepSeek 暴露窗口关闭"
title_ja: "DeepSeekの露出期間が終了"
title_ko: "DeepSeek 노출 기간 종료"
title_de: "DeepSeek-Expositionsfenster schließt sich"
title_fr: "La fenêtre d'exposition de DeepSeek se referme"
title_es: "Se cierra la ventana de exposición de DeepSeek"
date: 2025-03-03
date_precision: day
date_raw: "2025-03-03"

kind: incident
type: [INFRA]
severity: low
confidence: A
real_harm: false
ai_involvement: confirmed

region: [CN]

summary: |
  OWASP records the exposure window as 01-29 → 03-03


summary_zh: |
  OWASP 记录暴露期为 01-29 → 03-03

summary_ja: |
  OWASPは露出期間を01-29 → 03-03と記録

summary_ko: |
  OWASP는 노출 기간을 01-29 → 03-03으로 기록했다

summary_de: |
  OWASP verzeichnet das Expositionsfenster als 01-29 → 03-03

summary_fr: |
  OWASP fixe la fenêtre d'exposition du 01-29 au 03-03

summary_es: |
  OWASP registra la ventana de exposición como 01-29 → 03-03

sources:
  - url: https://genai.owasp.org/2025/07/14/owasp-gen-ai-incident-exploit-round-up-q225/
    label: "OWASP Q2'25"

disputed: false
landmark: false
scan_month: 2025-03
scan_ref: "SCAN.md §5 2025-03"
---

# DeepSeek exposure window closes

![severity: low](https://img.shields.io/badge/severity-low-8C6A6A?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

OWASP records the exposure window as 01-29 → 03-03

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
| Date | `2025-03-03` (raw: 2025-03-03, precision `day`) |
| Kind | Incident `incident` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **Low** `low` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [China](../../regions/cn.md) |
| Archive ID | `2025-03-03-deepseek-bao-lu-chuang-kou` |

<sub>**Why this classification:** Real incident without a confirmed specific victim. Rated `low`: context entry, kept for timeline continuity. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2025-03-01` [ChatGPT SSRF CVE-2024-27564 exploited in the wild](2025-03-01-chatgpt-ssrf-ye-li-yong.md)<br>  <sub>ChatGPT SSRF CVE-2024-27564 exploited in the wild</sub>
- `2025-02-01` [Thousands of Ollama servers exposed without auth](../2025-02/2025-02-01-ollama-fu-wu-qi-gui.md)<br>  <sub>Thousands of Ollama servers exposed without auth</sub>
- `2025-04-29` [NVIDIA TensorRT-LLM deserialization RCE](../2025-04/2025-04-29-nvidia-tensorrt-llm-rce.md)<br>  <sub>NVIDIA TensorRT-LLM deserialization RCE</sub>
- `2025-01-29` [DeepSeek ClickHouse database left wide open](../2025-01/2025-01-29-deepseek-clickhouse-exposed.md)<br>  <sub>DeepSeek ClickHouse database left wide open</sub>

---

[← 2025-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-03/2025-03-03-deepseek-bao-lu-chuang-kou.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
