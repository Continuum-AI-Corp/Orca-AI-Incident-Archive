---
id: 2025-10-21-brave-comet-pi-lu-jie
title: "Brave discloses screenshot-based injection in Comet"
title_zh: "Brave 披露 Comet 截图型注入"
title_ja: "BraveがCometのスクリーンショット経由インジェクションを公表"
title_ko: "Brave, Comet의 스크린샷 기반 인젝션 공개"
title_de: "Brave legt screenshot-basierte Injection in Comet offen"
title_fr: "Brave divulgue une injection via capture d'écran dans Comet"
title_es: "Brave divulga inyección basada en capturas de pantalla en Comet"
date: 2025-10-21
date_precision: day
date_raw: "2025-10-21"

kind: research
type: [IPI]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Hidden text inside an image is processed and taken as instructions. Found 10-01, reported 10-02, disclosed 10-21 (the same day as the Atlas launch)


summary_zh: |
  图片中的隐藏文字被处理后当成指令。10-01 发现、10-02 通知、10-21 公开（与 Atlas 发布同日）

summary_ja: |
  画像内に隠されたテキストが処理され、指示として扱われる。10-01に発見、10-02に報告、10-21に公表（Atlas公開と同じ日）

summary_ko: |
  이미지 안에 숨겨진 텍스트가 처리되어 지시로 받아들여진다. 10-01 발견, 10-02 신고, 10-21 공개(Atlas 출시와 같은 날)

summary_de: |
  Versteckter Text in einem Bild wird verarbeitet und als Anweisung genommen. Gefunden am 10-01, gemeldet am 10-02, offengelegt am 10-21 (am selben Tag wie der Atlas-Start)

summary_fr: |
  Un texte caché dans une image est traité et pris pour des instructions. Découvert le 10-01, signalé le 10-02, divulgué le 10-21 (le jour même du lancement d'Atlas)

summary_es: |
  El texto oculto dentro de una imagen se procesa y se toma como instrucciones. Encontrado el 10-01, reportado el 10-02, divulgado el 10-21 (el mismo día del lanzamiento de Atlas)

sources:
  - url: https://brave.com/blog/comet-prompt-injection/
    label: Brave

disputed: false
landmark: false
scan_month: 2025-10
scan_ref: "SCAN.md §5 2025-10"
---

# Brave discloses screenshot-based injection in Comet

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square)

## Summary

Hidden text inside an image is processed and taken as instructions. Found 10-01, reported 10-02, disclosed 10-21 (the same day as the Atlas launch)

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    I["Acts beyond its authority as the attacker intends<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Brave | <https://brave.com/blog/comet-prompt-injection/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-10-21` (raw: 2025-10-21, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-10-21-brave-comet-pi-lu-jie` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2025-10-02` [CometJacking](2025-10-02-cometjacking.md)<br>  <sub>CometJacking</sub>
- `2025-10-08` [CamoLeak (GitHub Copilot Chat)](2025-10-08-camoleak-github-copilot-chat.md)<br>  <sub>CamoLeak (GitHub Copilot Chat)</sub>
- `2025-10-31` [Agent Session Smuggling: agents deceiving agents over A2A](2025-10-31-agent-session-smuggling-a2a.md)<br>  <sub>Agent Session Smuggling: agents deceiving agents over A2A</sub>
- `2025-10-24` [Atlas omnibox jailbreak](2025-10-24-atlas-omnibox-yue-yu.md)<br>  <sub>Atlas omnibox jailbreak</sub>

---

[← 2025-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-10/2025-10-21-brave-comet-pi-lu-jie.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
