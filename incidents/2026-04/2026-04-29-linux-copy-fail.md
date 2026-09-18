---
id: 2026-04-29-linux-copy-fail
title: "Linux \"Copy Fail\" CVE-2026-31431"
title_zh: "Linux \"Copy Fail\" CVE-2026-31431"
title_ja: "Linux「Copy Fail」CVE-2026-31431"
title_ko: "Linux \"Copy Fail\" CVE-2026-31431"
title_de: "Linux „Copy Fail“ CVE-2026-31431"
title_fr: "« Copy Fail » de Linux (CVE-2026-31431)"
title_es: "Linux \"Copy Fail\" CVE-2026-31431"
date: 2026-04-29
date_precision: day
date_raw: "2026-04-29"

kind: research
type: [OTHER]
severity: low
confidence: A
real_harm: false
ai_involvement: not-applicable

region: [GLOBAL]

summary: |
  No direct AI connection, but it sits within the 2026 backdrop of "AI-accelerated vulnerability discovery"


summary_zh: |
  与 AI 无直接关系，但属 2026 年「AI 加速漏洞发现」大背景

summary_ja: |
  AIとの直接の関係はないが、2026年の「AIによる脆弱性発見の加速」という背景の中に位置する

summary_ko: |
  AI와 직접적 관련은 없지만 "AI가 가속하는 취약점 발견"이라는 2026년의 배경 속에 있다

summary_de: |
  Kein direkter KI-Bezug, doch er gehört in den Hintergrund von 2026 mit „KI-beschleunigter Schwachstellensuche“

summary_fr: |
  Aucun lien direct avec l'IA, mais cela s'inscrit dans le contexte 2026 de la « découverte de vulnérabilités accélérée par l'IA »

summary_es: |
  Sin conexión directa con la IA, pero se sitúa dentro del contexto de 2026 del "descubrimiento de vulnerabilidades acelerado por IA"

sources:
  - url: https://copy.fail/
    label: copy.fail

disputed: false
landmark: false
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# Linux "Copy Fail" CVE-2026-31431

![severity: low](https://img.shields.io/badge/severity-low-8C6A6A?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: not-applicable](https://img.shields.io/badge/AI_involvement-not--applicable-9AA8AD?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

No direct AI connection, but it sits within the 2026 backdrop of "AI-accelerated vulnerability discovery"

## Attack chain

```mermaid
flowchart LR
    E["Entry point"]:::entry
    S0["Process"]:::step
    I["Result<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | copy.fail | <https://copy.fail/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-04-29` (raw: 2026-04-29, precision `day`) |
| Kind | Research demo `research` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **Low** `low` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Not applicable `not-applicable` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-04-29-linux-copy-fail` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `low`: context entry, kept for timeline continuity. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-29-linux-copy-fail.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
