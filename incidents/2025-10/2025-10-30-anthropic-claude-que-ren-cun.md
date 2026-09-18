---
id: 2025-10-30-anthropic-claude-que-ren-cun
title: "Anthropic confirms a prompt-injection flaw in Claude"
title_zh: "Anthropic 确认 Claude 存在提示注入缺陷"
title_ja: "AnthropicがClaudeのプロンプトインジェクション欠陥を確認"
title_ko: "Anthropic, Claude의 프롬프트 인젝션 결함 확인"
title_de: "Anthropic bestätigt eine Prompt-Injection-Schwachstelle in Claude"
title_fr: "Anthropic confirme une faille d'injection de prompt dans Claude"
title_es: "Anthropic confirma un fallo de inyección de prompt en Claude"
date: 2025-10-30
date_precision: day
date_raw: "2025-10-30"

kind: vulnerability
type: [IPI]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  ⚠️ **This record is a time anchor for the 2026-01 Cowork incident**: the flaw had been reported and confirmed by Anthropic **three months before Cowork shipped (2026-01-12)**, was **still unfixed at launch**, and was later rated **CVSS 10/10**. Anthropic's written position is that it "falls outside the current threat model" — wording that matches its response in the 2026-07 GhostApproval incident


summary_zh: |
  ⚠️ **本条是为 2026-01 Cowork 事件建立时间锚点**：该缺陷在 **Cowork 发布（2026-01-12）前三个月**就已被报告并获 Anthropic 确认，**发布时仍未修复**，随后被评为 **CVSS 10/10**。Anthropic 的书面立场是它「落在当前威胁模型之外」—— 与 2026-07 GhostApproval 事件中的回应用词一致

summary_ja: |
  ⚠️ **この記録は2026-01のCoworkインシデントの時間軸上の基準点**：欠陥は**Coworkの出荷（2026-01-12）の3か月前**にAnthropicへ報告され確認済みだったが、**出荷時点でも未修正**で、後に**CVSS 10/10**と評価された。Anthropicの書面での立場は「現在の脅威モデルの範囲外」——2026-07のGhostApprovalインシデントでの回答と同じ表現である

summary_ko: |
  ⚠️ **이 기록은 2026-01 Cowork 사건의 시간 기준점이다**: 이 결함은 **Cowork 출시(2026-01-12) 3개월 전에** Anthropic에 신고되어 확인되었고, **출시 시점에도 수정되지 않았으며**, 이후 **CVSS 10/10**으로 평가되었다. Anthropic의 공식 입장은 "현재 위협 모델의 범위를 벗어난다"였으며, 이는 2026-07 GhostApproval 사건에서의 대응과 같은 표현이다

summary_de: |
  ⚠️ **Dieser Eintrag ist ein Zeitanker für den Cowork-Vorfall von 2026-01**: Die Schwachstelle war **drei Monate vor dem Start von Cowork (2026-01-12)** an Anthropic gemeldet und bestätigt worden, war **zum Start noch nicht behoben** und wurde später mit **CVSS 10/10** bewertet. Anthropics schriftliche Position ist, sie „falle außerhalb des aktuellen Bedrohungsmodells“ — eine Formulierung, die zu ihrer Antwort im GhostApproval-Vorfall von 2026-07 passt

summary_fr: |
  ⚠️ **Cet enregistrement est un repère temporel pour l'incident Cowork de 2026-01** : la faille avait été signalée et confirmée par Anthropic **trois mois avant la sortie de Cowork (2026-01-12)**, **n'était toujours pas corrigée au lancement**, et a ensuite été notée **CVSS 10/10**. La position écrite d'Anthropic est qu'elle « sort du modèle de menace actuel » — une formulation identique à sa réponse dans l'incident GhostApproval de 2026-07

summary_es: |
  ⚠️ **Este registro es un ancla temporal para el incidente Cowork de 2026-01**: el fallo había sido reportado y confirmado por Anthropic **tres meses antes de que se lanzara Cowork (2026-01-12)**, **seguía sin corregir en el lanzamiento** y luego fue calificado **CVSS 10/10**. La postura escrita de Anthropic es que "queda fuera del modelo de amenaza actual" — una redacción que coincide con su respuesta en el incidente GhostApproval de 2026-07

sources:
  - url: https://www.govinfosecurity.com/anthropics-cowork-shipped-known-vulnerability-a-30553
    label: GovInfoSecurity

disputed: false
landmark: false
scan_month: 2025-10
scan_ref: "SCAN.md §5 2025-10"
---

# Anthropic confirms a prompt-injection flaw in Claude

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square)

## Summary

⚠️ **This record is a time anchor for the 2026-01 Cowork incident**: the flaw had been reported and confirmed by Anthropic **three months before Cowork shipped (2026-01-12)**, was **still unfixed at launch**, and was later rated **CVSS 10/10**. Anthropic's written position is that it "falls outside the current threat model" — wording that matches its response in the 2026-07 GhostApproval incident

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    I["Acts beyond its authority as the attacker intends<br/><i>(flaw disclosed, no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | GovInfoSecurity | <https://www.govinfosecurity.com/anthropics-cowork-shipped-known-vulnerability-a-30553> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-10-30` (raw: 2025-10-30, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-10-30-anthropic-claude-que-ren-cun` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2025-10-02` [CometJacking](2025-10-02-cometjacking.md)<br>  <sub>CometJacking</sub>
- `2025-10-08` [CamoLeak (GitHub Copilot Chat)](2025-10-08-camoleak-github-copilot-chat.md)<br>  <sub>CamoLeak (GitHub Copilot Chat)</sub>
- `2025-10-31` [Agent Session Smuggling: agents deceiving agents over A2A](2025-10-31-agent-session-smuggling-a2a.md)<br>  <sub>Agent Session Smuggling: agents deceiving agents over A2A</sub>
- `2025-10-21` [Brave discloses screenshot-based injection in Comet](2025-10-21-brave-comet-pi-lu-jie.md)<br>  <sub>Brave discloses screenshot-based injection in Comet</sub>

---

[← 2025-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-10/2025-10-30-anthropic-claude-que-ren-cun.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
