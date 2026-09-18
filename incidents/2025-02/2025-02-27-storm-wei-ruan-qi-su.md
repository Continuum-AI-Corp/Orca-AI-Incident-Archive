---
id: 2025-02-27-storm-wei-ruan-qi-su
title: "Microsoft sues Storm-2139 and names the defendants"
title_zh: "微软起诉 Storm-2139，公开被告身份"
title_ja: "Microsoft、Storm-2139を提訴し被告を公表"
title_ko: "마이크로소프트, Storm-2139 제소하고 피고 실명 공개"
title_de: "Microsoft verklagt Storm-2139 und nennt die Beklagten"
title_fr: "Microsoft poursuit Storm-2139 et nomme les défendeurs"
title_es: "Microsoft demanda a Storm-2139 y revela los nombres de los acusados"
date: 2025-02-27
date_precision: day
date_raw: "2025-02-27"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [US]

summary: |
  Microsoft's complaint publicly names 4 core members of Storm-2139, a group that abused stolen Azure OpenAI credentials and resold generated content that bypassed content safety.


summary_zh: |
  微软在起诉书中公开点名 Storm-2139 的 4 名核心成员，该团伙盗用 Azure OpenAI 凭据并转售绕过内容安全的生成服务。

summary_ja: |
  Microsoftの訴状は、盗まれたAzure OpenAIの認証情報を悪用し、コンテンツ安全機構を回避して生成したコンテンツを転売していたグループStorm-2139の中核メンバー4名の実名を公開した。

summary_ko: |
  마이크로소프트의 소장은 Storm-2139의 핵심 구성원 4명을 공개했다. 이 그룹은 도난당한 Azure OpenAI 자격 증명을 악용하고 콘텐츠 안전을 우회한 생성물을 재판매했다.

summary_de: |
  Microsofts Klageschrift nennt öffentlich 4 Kernmitglieder von Storm-2139, einer Gruppe, die gestohlene Azure-OpenAI-Zugangsdaten missbrauchte und generierte Inhalte weiterverkaufte, die die Inhaltssicherheit umgangen hatten.

summary_fr: |
  La plainte de Microsoft nomme publiquement 4 membres clés de Storm-2139, un groupe qui a abusé d'identifiants Azure OpenAI volés et revendu du contenu généré ayant contourné les filtres de sécurité.

summary_es: |
  La demanda de Microsoft identifica públicamente a 4 miembros centrales de Storm-2139, un grupo que abusó de credenciales robadas de Azure OpenAI y revendió contenido generado que eludía la seguridad de contenido.

sources:
  - url: https://blogs.microsoft.com/on-the-issues/2025/02/27/disrupting-cybercrime-abusing-gen-ai/
    label: Microsoft

disputed: false
landmark: false
scan_month: 2025-02
scan_ref: "SCAN.md §5 2025-02"
---

# Microsoft sues Storm-2139 and names the defendants

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Microsoft's complaint publicly names 4 core members of Storm-2139, a group that abused stolen Azure OpenAI credentials and resold generated content that bypassed content safety.

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
| 1 | Microsoft | <https://blogs.microsoft.com/on-the-issues/2025/02/27/disrupting-cybercrime-abusing-gen-ai/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-02-27` (raw: 2025-02-27, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [United States](../../regions/us.md) |
| Archive ID | `2025-02-27-storm-wei-ruan-qi-su` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2025-02-21` [OpenAI bans accounts behind the "Peer Review" surveillance tool](2025-02-21-peer-review-feng-jin-jian.md)<br>  <sub>OpenAI bans accounts behind the "Peer Review" surveillance tool</sub>
- `2025-01-30` [Italy's Garante blocks DeepSeek](../2025-01/2025-01-30-garante-deepseek-yi-li-feng.md)<br>  <sub>Italy's Garante blocks DeepSeek</sub>
- `2025-01-23` [OpenAI Operator launches (context entry)](../2025-01/2025-01-23-operator-fa-bu-bei-jing.md)<br>  <sub>OpenAI Operator launches (context entry)</sub>
- `2025-03-01` [Sony pulls 75,000+ AI deepfake tracks](../2025-03/2025-03-01-sony-jia-wan-shen-wei.md)<br>  <sub>Sony pulls 75,000+ AI deepfake tracks</sub>

---

[← 2025-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-02/2025-02-27-storm-wei-ruan-qi-su.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
