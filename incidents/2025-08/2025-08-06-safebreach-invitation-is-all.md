---
id: 2025-08-06-safebreach-invitation-is-all
title: "SafeBreach \"Invitation Is All You Need\""
title_zh: "SafeBreach \"Invitation Is All You Need\""
title_ja: "SafeBreach「Invitation Is All You Need」"
title_ko: "SafeBreach \"Invitation Is All You Need\""
title_de: "SafeBreach: „Invitation Is All You Need“"
title_fr: "SafeBreach : « Invitation Is All You Need »"
title_es: "SafeBreach \"Invitation Is All You Need\""
date: 2025-08-06
date_precision: day
date_raw: "2025-08-06"

kind: research
type: [IPI]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Or Yair / Ben Nassi / Stav Cohen presented **Targeted Promptware** at Black Hat USA: hijacking Gemini for Workspace through Google Calendar invitations, with **15 exploits** spanning web / mobile / Google Assistant that could generate harmful content, spam and phishing, delete calendar events, **control smart-home devices**, and reach video streams and location. Disclosed responsibly to Google in 2025-02; their TARA assessment rated **73% of the risks High-Critical**


summary_zh: |
  Or Yair / Ben Nassi / Stav Cohen 在 Black Hat USA 展示 **Targeted Promptware**：通过 Google 日历邀请劫持 Gemini for Workspace，**15 种利用**覆盖 web / 移动端 / Google Assistant，可生成有害内容、垃圾与钓鱼、删除日历事件、**控制智能家居设备**、视频流与定位。2025-02 已向 Google 负责任披露；其 TARA 评估认为 **73% 的风险为 High-Critical**

summary_ja: |
  Or Yair氏、Ben Nassi氏、Stav Cohen氏がBlack Hat USAで**Targeted Promptware**を発表：Googleカレンダーの招待を通じてWorkspace向けGeminiをハイジャックする手法で、Web／モバイル／Google Assistantにまたがる**15のエクスプロイト**により、有害コンテンツ・スパム・フィッシングの生成、カレンダー予定の削除、**スマートホーム機器の制御**、映像ストリームや位置情報への到達が可能だった。2025-02にGoogleへ責任ある開示を実施。同社のTARA評価では**リスクの73%がHigh〜Critical**とされた

summary_ko: |
  Or Yair / Ben Nassi / Stav Cohen는 Black Hat USA에서 **Targeted Promptware**를 발표했다. Google Calendar 초대장을 통해 Gemini for Workspace를 하이재킹하는 것으로, 웹 / 모바일 / Google Assistant에 걸친 **15개의 익스플로잇**이 유해 콘텐츠 생성, 스팸·피싱, 캘린더 일정 삭제, **스마트홈 기기 제어**, 영상 스트림과 위치 정보 접근까지 가능했다. 2025-02 구글에 책임 있게 신고했으며, 이들의 TARA 평가는 **위험의 73%를 높음~심각**으로 평가했다

summary_de: |
  Or Yair / Ben Nassi / Stav Cohen präsentierten auf der Black Hat USA **Targeted Promptware**: Hijacking von Gemini for Workspace über Google-Kalender-Einladungen, mit **15 Exploits** über Web / Mobile / Google Assistant, die schädliche Inhalte, Spam und Phishing erzeugen, Kalendereinträge löschen, **Smart-Home-Geräte steuern** sowie Videostreams und Standort erreichen konnten. Verantwortungsvoll im 2025-02 an Google gemeldet; ihre TARA-Bewertung stufte **73% der Risiken als High bis Critical** ein

summary_fr: |
  Or Yair / Ben Nassi / Stav Cohen ont présenté **Targeted Promptware** au Black Hat USA : détournement de Gemini for Workspace via des invitations Google Calendar, avec **15 exploits** couvrant web / mobile / Google Assistant capables de générer du contenu nuisible, du spam et du phishing, de supprimer des événements d'agenda, de **contrôler des appareils domotiques** et d'atteindre des flux vidéo et la localisation. Divulgué de façon responsable à Google en 2025-02 ; leur évaluation TARA classait **73 % des risques en High-Critical**

summary_es: |
  Or Yair / Ben Nassi / Stav Cohen presentaron **Targeted Promptware** en Black Hat USA: secuestro de Gemini for Workspace mediante invitaciones de Google Calendar, con **15 exploits** que abarcan web / móvil / Google Assistant y podían generar contenido dañino, spam y phishing, borrar eventos de calendario, **controlar dispositivos de casa inteligente** y alcanzar transmisiones de video y ubicación. Divulgado de forma responsable a Google en 2025-02; su evaluación TARA calificó **el 73% de los riesgos como Alto-Crítico**

sources:
  - url: https://www.safebreach.com/blog/invitation-is-all-you-need-hacking-gemini/
    label: SafeBreach

disputed: false
landmark: false
scan_month: 2025-08
scan_ref: "SCAN.md §5 2025-08"
---

# SafeBreach "Invitation Is All You Need"

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square)

## Summary

Or Yair / Ben Nassi / Stav Cohen presented **Targeted Promptware** at Black Hat USA: hijacking Gemini for Workspace through Google Calendar invitations, with **15 exploits** spanning web / mobile / Google Assistant that could generate harmful content, spam and phishing, delete calendar events, **control smart-home devices**, and reach video streams and location. Disclosed responsibly to Google in 2025-02; their TARA assessment rated **73% of the risks High-Critical**

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    I["Takes unauthorized actions as the attacker intends<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | SafeBreach | <https://www.safebreach.com/blog/invitation-is-all-you-need-hacking-gemini/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-08-06` (raw: 2025-08-06, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-08-06-safebreach-invitation-is-all` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2025-08-06` [AgentFlayer zero-click attack set (Black Hat USA)](2025-08-06-agentflayer-black-hat-usa.md)<br>  <sub>AgentFlayer zero-click attack set (Black Hat USA)</sub>
- `2025-08-01` ["Man in the Prompt" browser-extension attack](2025-08-01-man-prompt-liu-lan-qi.md)<br>  <sub>"Man in the Prompt" browser-extension attack</sub>
- `2025-09-18` [ShadowLeak](../2025-09/2025-09-18-shadowleak.md)<br>  <sub>ShadowLeak</sub>
- `2025-09-19` [Notion 3.0 agent hits the lethal trifecta](../2025-09/2025-09-19-notion-agent-zhi-ming-san.md)<br>  <sub>Notion 3.0 agent hits the lethal trifecta</sub>

---

[← 2025-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-08/2025-08-06-safebreach-invitation-is-all.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
