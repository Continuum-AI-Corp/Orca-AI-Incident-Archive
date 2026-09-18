---
id: 2026-06-09-anthropic-claude-fable-ga
title: "Anthropic Claude Fable 5 GA, Mythos 5 limited release"
title_zh: "Anthropic Claude Fable 5 GA + Mythos 5 限定"
title_ja: "Anthropic Claude Fable 5がGA、Mythos 5は限定リリース"
title_ko: "Anthropic Claude Fable 5 GA, Mythos 5 제한 공개"
title_de: "Anthropic: Claude Fable 5 allgemein verfügbar, Mythos 5 in begrenzter Freigabe"
title_fr: "Claude Fable 5 en GA chez Anthropic, sortie limitée de Mythos 5"
title_es: "Anthropic: Claude Fable 5 disponible de forma general y Mythos 5 con lanzamiento limitado"
date: 2026-06-09
date_precision: day
date_raw: "2026-06-09"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Mythos 5 is available only to a small number of cyber defenders and critical-infrastructure providers in Project Glasswing. Fable 5 ships with three domain classifiers (cyber / bio / distillation); when one triggers, Opus 4.8 answers instead (triggered in under 5% of sessions on average)


summary_zh: |
  Mythos 5 仅向 Project Glasswing 的少数网络防御者与关基提供商开放。Fable 5 带网络/生化/蒸馏三领域分类器，触发时由 Opus 4.8 代答（平均 < 5% 会话触发）

summary_ja: |
  Mythos 5はProject Glasswingの少数のサイバー防御担当者と重要インフラ事業者にのみ提供される。Fable 5には3つのドメイン分類器（サイバー／バイオ／蒸留）が搭載され、1つが発動すると代わりにOpus 4.8が回答する（平均でセッションの5%未満で発動）

summary_ko: |
  Mythos 5는 Project Glasswing의 소수 사이버 방어자와 핵심 인프라 제공자에게만 제공된다. Fable 5는 세 가지 영역 분류기(사이버 / 바이오 / 증류)와 함께 출시되며, 하나라도 작동하면 대신 Opus 4.8이 답한다(평균 세션의 5% 미만에서 작동)

summary_de: |
  Mythos 5 steht nur einer kleinen Zahl von Cyber-Verteidigern und Betreibern kritischer Infrastruktur in Project Glasswing zur Verfügung. Fable 5 wird mit drei Domänenklassifikatoren ausgeliefert (Cyber / Bio / Destillation); wenn einer auslöst, antwortet stattdessen Opus 4.8 (im Durchschnitt in unter 5% der Sitzungen ausgelöst)

summary_fr: |
  Mythos 5 n'est accessible qu'à un petit nombre de cyberdéfenseurs et de fournisseurs d'infrastructures critiques au sein de Project Glasswing. Fable 5 est livré avec trois classifieurs de domaine (cyber / bio / distillation) ; quand l'un se déclenche, c'est Opus 4.8 qui répond (déclenché dans moins de 5 % des sessions en moyenne)

summary_es: |
  Mythos 5 solo está disponible para un pequeño número de defensores ciber y proveedores de infraestructura crítica del Project Glasswing. Fable 5 se lanza con tres clasificadores de dominio (ciber / bio / destilación); cuando uno se activa, responde Opus 4.8 en su lugar (se activó en menos del 5% de las sesiones de media)

sources:
  - url: https://www.anthropic.com/news/claude-fable-5-mythos-5
    label: Anthropic
  - url: https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf
    label: System Card

disputed: false
landmark: false
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# Anthropic Claude Fable 5 GA, Mythos 5 limited release

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Mythos 5 is available only to a small number of cyber defenders and critical-infrastructure providers in Project Glasswing. Fable 5 ships with three domain classifiers (cyber / bio / distillation); when one triggers, Opus 4.8 answers instead (triggered in under 5% of sessions on average)

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
| 1 | Anthropic | <https://www.anthropic.com/news/claude-fable-5-mythos-5> |
| 2 | System Card | <https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-09` (raw: 2026-06-09, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-09-anthropic-claude-fable-ga` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-06-11` [CISA BOD 26-04](2026-06-11-cisa-bod.md)<br>  <sub>CISA BOD 26-04</sub>
- `2026-06-12` [US government issues export controls to Anthropic](2026-06-12-anthropic-mei-guo-zheng-fu.md)<br>  <sub>US government issues export controls to Anthropic</sub>
- `2026-06-12` [Google sues the China-linked "Outsider Enterprise" smishing network](2026-06-12-google-outsider-enterprise.md)<br>  <sub>Google sues the China-linked "Outsider Enterprise" smishing network</sub>
- `2026-06-23` [Five Eyes joint statement to boards and executives](2026-06-23-five-eyes-zhi-qi-ye.md)<br>  <sub>Five Eyes joint statement to boards and executives</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-09-anthropic-claude-fable-ga.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
