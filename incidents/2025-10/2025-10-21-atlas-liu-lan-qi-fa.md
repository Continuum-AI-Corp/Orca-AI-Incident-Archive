---
id: 2025-10-21-atlas-liu-lan-qi-fa
title: "OpenAI launches the Atlas browser"
title_zh: "OpenAI Atlas 浏览器发布"
title_ja: "OpenAIがAtlasブラウザを公開"
title_ko: "OpenAI, Atlas 브라우저 출시"
title_de: "OpenAI startet den Atlas-Browser"
title_fr: "OpenAI lance le navigateur Atlas"
title_es: "OpenAI lanza el navegador Atlas"
date: 2025-10-21
date_precision: day
date_raw: "2025-10-21"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  The release notes state plainly: "Do not use Atlas with regulated or production data." On launch day Brave disclosed the same class of issue in Comet, and three days later NeuralTrust broke through the omnibox


summary_zh: |
  发布说明明写「不要用 Atlas 处理受监管或生产数据」。发布当天即遭 Brave 披露 Comet 同类问题，三天后被 NeuralTrust 打穿 omnibox

summary_ja: |
  リリースノートは明言している：「規制対象データや本番データでAtlasを使用しないこと」。公開当日にBraveがCometの同種の問題を公表し、3日後にNeuralTrustがオムニボックスを突破した

summary_ko: |
  릴리스 노트에 명시되어 있다: "규제 대상 또는 프로덕션 데이터와 함께 Atlas를 사용하지 마십시오." 출시 당일 Brave가 Comet에서 같은 종류의 문제를 공개했고, 사흘 뒤 NeuralTrust가 옴니박스를 뚫었다

summary_de: |
  Die Versionshinweise sagen es unverblümt: „Do not use Atlas with regulated or production data.“ Am Starttag legte Brave dieselbe Problemklasse in Comet offen, und drei Tage später durchbrach NeuralTrust die Omnibox

summary_fr: |
  Les notes de version l'indiquent clairement : « Do not use Atlas with regulated or production data. » Le jour du lancement, Brave a divulgué la même classe de problème dans Comet, et trois jours plus tard NeuralTrust perçait l'omnibox

summary_es: |
  Las notas de la versión lo dicen sin rodeos: "No uses Atlas con datos regulados o de producción". El día del lanzamiento Brave divulgó el mismo tipo de problema en Comet, y tres días después NeuralTrust burló la omnibox

sources:
  - url: https://www.wiz.io/blog/agentic-browser-security-2025-year-end-review
    label: Wiz year-end review

disputed: false
landmark: false
scan_month: 2025-10
scan_ref: "SCAN.md §5 2025-10"
---

# OpenAI launches the Atlas browser

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

The release notes state plainly: "Do not use Atlas with regulated or production data." On launch day Brave disclosed the same class of issue in Comet, and three days later NeuralTrust broke through the omnibox

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
| 1 | Wiz year-end review | <https://www.wiz.io/blog/agentic-browser-security-2025-year-end-review> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-10-21` (raw: 2025-10-21, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-10-21-atlas-liu-lan-qi-fa` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2025-10-07` [OpenAI October threat report](2025-10-07-shi-wei-xie-bao-gao.md)<br>  <sub>OpenAI October threat report</sub>
- `2025-11-19` [EU "Digital Omnibus" proposes delaying the AI Act](../2025-11/2025-11-19-digital-omnibus-act.md)<br>  <sub>EU "Digital Omnibus" proposes delaying the AI Act</sub>
- `2025-08-25` [Anthropic starts the Claude for Chrome pilot](../2025-08/2025-08-25-anthropic-claude-chrome.md)<br>  <sub>Anthropic starts the Claude for Chrome pilot</sub>
- `2025-12-09` [OWASP Top 10 for Agentic Applications 2026](../2025-12/2025-12-09-owasp-top-agentic-applications.md)<br>  <sub>OWASP Top 10 for Agentic Applications 2026</sub>

---

[← 2025-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-10/2025-10-21-atlas-liu-lan-qi-fa.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
