---
id: 2026-05-20-google-universal-cart-ucp
title: "Google ships Universal Cart, UCP and AP2"
title_zh: "Google 发布 Universal Cart + UCP + AP2"
title_ja: "GoogleがUniversal Cart、UCP、AP2を提供開始"
title_ko: "구글, Universal Cart, UCP, AP2 출시"
title_de: "Google liefert Universal Cart, UCP und AP2 aus"
title_fr: "Google livre Universal Cart, UCP et AP2"
title_es: "Google lanza Universal Cart, UCP y AP2"
date: 2026-05-20
date_precision: day
date_raw: "2026-05-20"

kind: policy
type: [OTHER]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Agent commerce protocols; AP2 (Agent Payments Protocol) imposes strict limits and a verifiable audit trail on AI payments


summary_zh: |
  agent 电商协议；AP2 (Agent Payments Protocol) 对 AI 支付设严格限制与可验证审计轨迹

summary_ja: |
  エージェントコマースプロトコル。AP2（Agent Payments Protocol）はAI決済に厳格な制限と検証可能な監査証跡を課す

summary_ko: |
  에이전트 커머스 프로토콜. AP2(Agent Payments Protocol)는 AI 결제에 엄격한 한도와 검증 가능한 감사 추적을 부과한다

summary_de: |
  Agent-Commerce-Protokolle; AP2 (Agent Payments Protocol) setzt strenge Grenzen und einen überprüfbaren Prüfpfad für KI-Zahlungen durch

summary_fr: |
  Protocoles de commerce agentique ; AP2 (Agent Payments Protocol) impose des limites strictes et une piste d'audit vérifiable aux paiements par IA

summary_es: |
  Protocolos de comercio para agentes; AP2 (Agent Payments Protocol) impone límites estrictos y un rastro de auditoría verificable a los pagos con IA

sources:
  - url: https://blog.google/intl/ja-jp/products/explore-get-answers/google-shopping-cart/
    label: Google

disputed: false
landmark: false
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# Google ships Universal Cart, UCP and AP2

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

Agent commerce protocols; AP2 (Agent Payments Protocol) imposes strict limits and a verifiable audit trail on AI payments

## Attack chain

```mermaid
flowchart LR
    E["Regulatory or policy action"]:::entry
    S0["Falls on vendors and users"]:::step
    I["Compliance requirements change"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Google | <https://blog.google/intl/ja-jp/products/explore-get-answers/google-shopping-cart/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-20` (raw: 2026-05-20, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-20-google-universal-cart-ucp` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-20-google-universal-cart-ucp.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
