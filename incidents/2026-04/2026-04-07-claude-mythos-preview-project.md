---
id: 2026-04-07-claude-mythos-preview-project
title: "Claude Mythos Preview cyber capability disclosure, Project Glasswing formed"
title_zh: "Claude Mythos Preview 网络能力披露 + Project Glasswing 成立"
title_ja: "Claude Mythos Previewのサイバー能力公表、Project Glasswing発足"
title_ko: "Claude Mythos Preview 사이버 능력 공개, Project Glasswing 결성"
title_de: "Claude Mythos Preview: Offenlegung der Cyber-Fähigkeiten, Project Glasswing gegründet"
title_fr: "Divulgation de la capacité cyber de Claude Mythos Preview, création de Project Glasswing"
title_es: "Divulgación de capacidad ciber de Claude Mythos Preview y formación del Project Glasswing"
date: 2026-04-07
date_precision: day
date_raw: "2026-04-07"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Mythos autonomously found zero-days in mainstream OSes and browsers and could build **multi-stage ROP chains** (previously thought beyond AI). Because of the dual-use risk, the defensive alliance **Project Glasswing**, with AWS / Google / Microsoft participating, was formed to restrict access. Bloomberg: **the US Treasury Secretary and the Fed Chair called an emergency meeting of major US bank CEOs over this** (04-10)


summary_zh: |
  Mythos 自主发现主流 OS 与浏览器的零日，并能构造**多级 ROP 链**（此前被认为 AI 做不到）。因双用途风险，成立由 AWS / Google / Microsoft 参与的防御性联盟 **Project Glasswing** 限制访问。Bloomberg：**美财长与美联储主席为此紧急召集美国各大银行 CEO 开会**（04-10）

summary_ja: |
  Mythosは主要OSやブラウザのゼロデイを自律的に発見し、（従来はAIには不可能と考えられていた）**多段階ROPチェーン**を構築できた。デュアルユースのリスクから、AWS／Google／Microsoftが参加する防御同盟**Project Glasswing**がアクセス制限のために発足した。Bloomberg：**米財務長官とFRB議長がこれを巡り米主要銀行CEOの緊急会議を招集した**（04-10）

summary_ko: |
  Mythos는 주류 OS와 브라우저에서 제로데이를 자율적으로 찾아냈고 **다단계 ROP 체인**까지 구성할 수 있었다(이전에는 AI의 능력 밖으로 여겨졌다). 이중 용도 위험 때문에 AWS / Google / Microsoft가 참여하는 방어 연합 **Project Glasswing**이 결성되어 접근을 제한했다. Bloomberg: **미국 재무장관과 연준 의장이 이 문제로 미국 주요 은행 CEO들을 긴급 소집했다**(04-10)

summary_de: |
  Mythos fand autonom Zero-Days in gängigen Betriebssystemen und Browsern und konnte **mehrstufige ROP-Ketten** aufbauen (was zuvor für KI als unmöglich galt). Wegen des Dual-Use-Risikos wurde die Verteidigungsallianz **Project Glasswing** mit Beteiligung von AWS / Google / Microsoft gegründet, um den Zugang zu beschränken. Bloomberg: **Der US-Finanzminister und der Fed-Vorsitzende beriefen deswegen am 04-10 eine Notfallsitzung mit den CEOs großer US-Banken ein**

summary_fr: |
  Mythos a trouvé de façon autonome des zero-days dans des OS et navigateurs grand public et pouvait construire des **chaînes ROP multi-étapes** (jusqu'alors considérées hors de portée de l'IA). En raison du risque dual, l'alliance défensive **Project Glasswing**, avec la participation d'AWS / Google / Microsoft, a été formée pour restreindre l'accès. Bloomberg : **le secrétaire au Trésor américain et la présidente de la Fed ont convoqué une réunion d'urgence des PDG des grandes banques américaines à ce sujet** (04-10)

summary_es: |
  Mythos encontró de forma autónoma zero-days en SO y navegadores convencionales y podía construir **cadenas ROP de múltiples etapas** (algo que antes se consideraba fuera del alcance de la IA). Por el riesgo de doble uso, se formó la alianza defensiva **Project Glasswing**, con la participación de AWS / Google / Microsoft, para restringir el acceso. Bloomberg: **el secretario del Tesoro de Estados Unidos y el presidente de la Reserva Federal convocaron una reunión de emergencia con los principales CEO bancarios estadounidenses por esto** (04-10)

sources:
  - url: https://www.anthropic.com/glasswing
    label: Anthropic Glasswing
  - url: https://red.anthropic.com/2026/mythos-preview/
    label: red.anthropic.com
  - url: https://www.bloomberg.com/jp/news/articles/2026-04-10/TD95ABT9NJMP00
    label: Bloomberg

disputed: false
landmark: true
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# Claude Mythos Preview cyber capability disclosure, Project Glasswing formed

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Mythos autonomously found zero-days in mainstream OSes and browsers and could build **multi-stage ROP chains** (previously thought beyond AI). Because of the dual-use risk, the defensive alliance **Project Glasswing**, with AWS / Google / Microsoft participating, was formed to restrict access. Bloomberg: **the US Treasury Secretary and the Fed Chair called an emergency meeting of major US bank CEOs over this** (04-10)

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
| 1 | Anthropic Glasswing | <https://www.anthropic.com/glasswing> |
| 2 | red.anthropic.com | <https://red.anthropic.com/2026/mythos-preview/> |
| 3 | Bloomberg | <https://www.bloomberg.com/jp/news/articles/2026-04-10/TD95ABT9NJMP00> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-04-07` (raw: 2026-04-07, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-04-07-claude-mythos-preview-project` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-04-13` [UK AISI independently evaluates Claude Mythos Preview](2026-04-13-uk-aisi-claude-mythos.md)<br>  <sub>UK AISI independently evaluates Claude Mythos Preview</sub>
- `2026-04-14` [Vidoc reproduces Mythos's findings with public models](2026-04-14-vidoc-mythos-yong-gong-kai.md)<br>  <sub>Vidoc reproduces Mythos's findings with public models</sub>
- `2026-04-30` [OpenAI launches Advanced Account Security](2026-04-30-tui-chu-gao-ji-zhang.md)<br>  <sub>OpenAI launches Advanced Account Security</sub>
- `2026-05-12` [Brazilian labour court sanctions lawyers over prompt injection](../2026-05/2026-05-12-brazil-labor-court-prompt-injection-sanction.md)<br>  <sub>Brazilian labour court sanctions lawyers over prompt injection</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-07-claude-mythos-preview-project.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
