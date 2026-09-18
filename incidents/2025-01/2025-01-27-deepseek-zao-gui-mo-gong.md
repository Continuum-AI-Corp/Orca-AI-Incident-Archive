---
id: 2025-01-27-deepseek-zao-gui-mo-gong
title: "DeepSeek hit by large-scale attacks, halts signups"
title_zh: "DeepSeek 遭大规模攻击，限制注册"
title_ja: "DeepSeek、大規模攻撃を受け新規登録を停止"
title_ko: "DeepSeek, 대규모 공격으로 신규 가입 중단"
title_de: "DeepSeek von groß angelegten Angriffen getroffen, Registrierungen gestoppt"
title_fr: "DeepSeek visé par des attaques à grande échelle et suspend les inscriptions"
title_es: "DeepSeek sufre ataques a gran escala y suspende los registros"
date: 2025-01-27
date_precision: day
date_raw: "2025-01-27"

kind: incident
type: [OTHER]
severity: medium
confidence: B
real_harm: true
ai_involvement: confirmed

region: [CN]

summary: |
  QiAnXin XLab recorded several waves of reflection attacks, HTTP proxy attacks, DDoS and botnet traffic


summary_zh: |
  奇安信 XLab 记录反射攻击、HTTP 代理攻击、DDoS、僵尸网络多轮

summary_ja: |
  QiAnXin XLabは反射攻撃、HTTPプロキシ攻撃、DDoS、ボットネットトラフィックの複数波を記録した

summary_ko: |
  QiAnXin XLab은 반사 공격, HTTP 프록시 공격, DDoS, 봇넷 트래픽 등 여러 차례의 공격 파도를 기록했다

summary_de: |
  QiAnXin XLab verzeichnete mehrere Wellen von Reflection-Angriffen, HTTP-Proxy-Angriffen, DDoS und Botnet-Traffic

summary_fr: |
  QiAnXin XLab a enregistré plusieurs vagues d'attaques par réflexion, d'attaques via proxy HTTP, de DDoS et de trafic de botnets

summary_es: |
  QiAnXin XLab registró varias oleadas de ataques de reflexión, ataques de proxy HTTP, DDoS y tráfico de botnets

sources:
  - url: https://www.secrss.com/articles/86614
    label: Security Reference

disputed: false
landmark: false
scan_month: 2025-01
scan_ref: "SCAN.md §5 2025-01"
---

# DeepSeek hit by large-scale attacks, halts signups

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

QiAnXin XLab recorded several waves of reflection attacks, HTTP proxy attacks, DDoS and botnet traffic

## Attack chain

```mermaid
flowchart LR
    E["Entry point"]:::entry
    S0["Process"]:::step
    I["Result"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Security Reference | <https://www.secrss.com/articles/86614> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-01-27` (raw: 2025-01-27, precision `day`) |
| Kind | Incident `incident` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **Medium** `medium` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [China](../../regions/cn.md) |
| Archive ID | `2025-01-27-deepseek-zao-gui-mo-gong` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2025-01 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-01/2025-01-27-deepseek-zao-gui-mo-gong.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
