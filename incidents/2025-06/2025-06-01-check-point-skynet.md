---
id: 2025-06-01-check-point-skynet
title: "Check Point's \"Skynet\" sample"
title_zh: "Check Point「Skynet」样本"
title_ja: "Check Pointの「Skynet」サンプル"
title_ko: "Check Point의 \"Skynet\" 샘플"
title_de: "Check Points „Skynet“-Sample"
title_fr: "L'échantillon « Skynet » de Check Point"
title_es: "La muestra \"Skynet\" de Check Point"
date: 2025-06-01
date_precision: month
date_raw: "2025-06"

kind: research
type: [WEAPON]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Malware embeds a prompt-injection string that makes an AI analysis engine output "NO MALWARE DETECTED" — **the first evasion sample aimed at AI analyzers**


summary_zh: |
  恶意软件内嵌提示注入串，诱导 AI 分析引擎输出「NO MALWARE DETECTED」—— **首个针对 AI 分析器的规避样本**

summary_ja: |
  マルウェアがプロンプトインジェクション文字列を埋め込み、AI解析エンジンに「NO MALWARE DETECTED」と出力させる——**AIアナライザーを狙った初の回避サンプル**

summary_ko: |
  악성코드가 프롬프트 인젝션 문자열을 내장해 AI 분석 엔진이 "NO MALWARE DETECTED"를 출력하게 만들었다 — **AI 분석기를 겨냥한 최초의 회피 샘플**

summary_de: |
  Malware bettet einen Prompt-Injection-String ein, der eine KI-Analyse-Engine dazu bringt, „NO MALWARE DETECTED“ auszugeben — **das erste Evasion-Sample, das auf KI-Analysatoren abzielt**

summary_fr: |
  Un malware intègre une chaîne d'injection de prompt qui pousse un moteur d'analyse IA à afficher « NO MALWARE DETECTED » — **le premier échantillon d'évasion visant les analyseurs IA**

summary_es: |
  El malware incrusta una cadena de inyección de prompt que hace que un motor de análisis de IA responda "NO MALWARE DETECTED" — **la primera muestra de evasión dirigida a analizadores de IA**

sources:
  - url: https://research.checkpoint.com/2025/ai-evasion-prompt-injection/
    label: Check Point Research

disputed: false
landmark: false
scan_month: 2025-06
scan_ref: "SCAN.md §5 2025-06"
---

# Check Point's "Skynet" sample

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

Malware embeds a prompt-injection string that makes an AI analysis engine output "NO MALWARE DETECTED" — **the first evasion sample aimed at AI analyzers**

## Attack chain

```mermaid
flowchart LR
    E["Attacker + jailbreak prompts"]:::entry
    S0["An LLM orchestrator drives a cluster of sub-agents"]:::step
    I["The target system is compromised<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Check Point Research | <https://research.checkpoint.com/2025/ai-evasion-prompt-injection/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-06-01` (raw: 2025-06, precision `month`) |
| Kind | Research demo `research` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-06-01-check-point-skynet` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2025-06-01` [Anthropic logs the precursor to GTG-1002](2025-06-01-anthropic-gtg-ji-lu-shen.md)<br>  <sub>Anthropic logs the precursor to GTG-1002</sub>
- `2025-06-05` [OpenAI June threat report](2025-06-05-liu-wei-xie-bao-gao.md)<br>  <sub>OpenAI June threat report</sub>
- `2025-05-01` [Anthropic logs the start of GTG-2002 activity](../2025-05/2025-05-01-anthropic-gtg-ji-lu-huo.md)<br>  <sub>Anthropic logs the start of GTG-2002 activity</sub>
- `2025-05-01` [AI-driven credential stuffing and scanning goes to scale](../2025-05/2025-05-01-qu-dong-zhuang-ku-zi.md)<br>  <sub>AI-driven credential stuffing and scanning goes to scale</sub>

---

[← 2025-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-06/2025-06-01-check-point-skynet.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
