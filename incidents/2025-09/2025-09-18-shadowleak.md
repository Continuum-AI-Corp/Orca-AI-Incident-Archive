---
id: 2025-09-18-shadowleak
title: "ShadowLeak"
title_zh: "ShadowLeak"
title_ja: "ShadowLeak"
title_ko: "ShadowLeak"
title_de: "ShadowLeak"
title_fr: "ShadowLeak"
title_es: "ShadowLeak"
date: 2025-09-18
date_precision: day
date_raw: "2025-09-18"

kind: research
type: [IPI, EXFIL]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Radware (Zvika Babo / Gabi Nakibly / Maor Uziel): zero-click, **server-side exfiltration**. HTML instructions hidden in an email mean that when the user simply says "summarize today's emails", the Deep Research agent sends data to the attacker's URL **on OpenAI's own cloud** — completely invisible to local and enterprise-side defenses. Reported via BugCrowd on 06-18, fixed in early August, **marked resolved on 09-03**


summary_zh: |
  Radware（Zvika Babo / Gabi Nakibly / Maor Uziel）：零点击、**服务端外带**。邮件里藏 HTML 指令，用户只要说「总结今天的邮件」，Deep Research agent 就在 **OpenAI 自己的云上**把数据发到攻击者 URL —— 本地与企业侧防御完全看不见。06-18 经 BugCrowd 报告，8 月初修复，**09-03 标记为已解决**

summary_ja: |
  Radware（Zvika Babo氏／Gabi Nakibly氏／Maor Uziel氏）：ゼロクリックの**サーバー側外部送信**。メールに隠されたHTML指示により、ユーザーが「今日のメールを要約して」と言うだけで、Deep Researchエージェントが**OpenAI自身のクラウド上**で攻撃者のURLへデータを送信する——ローカルおよび企業側の防御からは完全に見えない。06-18にBugCrowd経由で報告、8月初旬に修正、**09-03に解決済みとマーク**

summary_ko: |
  Radware(Zvika Babo / Gabi Nakibly / Maor Uziel): 제로클릭, **서버 측 유출**. 이메일에 숨겨진 HTML 지시로 사용자가 "오늘 온 메일 요약해줘"라고 말하기만 하면 Deep Research 에이전트가 **OpenAI 자체 클라우드에서** 공격자의 URL로 데이터를 보낸다 — 로컬 및 기업 측 방어로는 전혀 보이지 않는다. 06-18 BugCrowd를 통해 신고되었고 8월 초 수정, **09-03 해결 처리**되었다

summary_de: |
  Radware (Zvika Babo / Gabi Nakibly / Maor Uziel): Zero-Click, **serverseitige Exfiltration**. In einer E-Mail versteckte HTML-Anweisungen führen dazu, dass der Deep-Research-Agent, wenn der Nutzer nur „fasse die heutigen E-Mails zusammen“ sagt, Daten an die URL des Angreifers sendet — **auf OpenAIs eigener Cloud** und völlig unsichtbar für lokale und unternehmensseitige Abwehrmaßnahmen. Gemeldet über BugCrowd am 06-18, Anfang August behoben, **am 09-03 als gelöst markiert**

summary_fr: |
  Radware (Zvika Babo / Gabi Nakibly / Maor Uziel) : zero-click, **exfiltration côté serveur**. Des instructions HTML cachées dans un e-mail font que, lorsque l'utilisateur dit simplement « résume les e-mails du jour », l'agent Deep Research envoie les données vers l'URL de l'attaquant **sur le cloud d'OpenAI lui-même** — totalement invisible pour les défenses locales et d'entreprise. Signalé via BugCrowd le 06-18, corrigé début août, **marqué résolu le 09-03**

summary_es: |
  Radware (Zvika Babo / Gabi Nakibly / Maor Uziel): zero-click, **exfiltración del lado del servidor**. Instrucciones HTML ocultas en un correo hacen que, cuando el usuario simplemente dice "resume los correos de hoy", el agente Deep Research envíe datos a la URL del atacante **en la propia nube de OpenAI** — completamente invisible para las defensas locales y del lado empresarial. Reportado vía BugCrowd el 06-18, corregido a principios de agosto, **marcado como resuelto el 09-03**

sources:
  - url: https://www.radware.com/getattachment/7bf74537-e90e-414e-a82b-d7b4935bae08/Threat-Advisory-ShadowLeak-Sept-2025.pdf.aspx
    label: Radware PDF
  - url: https://thehackernews.com/2025/09/shadowleak-zero-click-flaw-leaks-gmail.html
    label: THN

disputed: false
landmark: true
scan_month: 2025-09
scan_ref: "SCAN.md §5 2025-09"
---

# ShadowLeak

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

Radware (Zvika Babo / Gabi Nakibly / Maor Uziel): zero-click, **server-side exfiltration**. HTML instructions hidden in an email mean that when the user simply says "summarize today's emails", the Deep Research agent sends data to the attacker's URL **on OpenAI's own cloud** — completely invisible to local and enterprise-side defenses. Reported via BugCrowd on 06-18, fixed in early August, **marked resolved on 09-03**

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["Exfiltration via the vendor's trusted domain<br/>image rendering · API · proxy"]:::step
    I["Data ends up with the attacker<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Radware PDF | <https://www.radware.com/getattachment/7bf74537-e90e-414e-a82b-d7b4935bae08/Threat-Advisory-ShadowLeak-Sept-2025.pdf.aspx> |
| 2 | THN | <https://thehackernews.com/2025/09/shadowleak-zero-click-flaw-leaks-gmail.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-09-18` (raw: 2025-09-18, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-09-18-shadowleak` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2025-09-19` [Notion 3.0 agent hits the lethal trifecta](2025-09-19-notion-agent-zhi-ming-san.md)<br>  <sub>Notion 3.0 agent hits the lethal trifecta</sub>
- `2025-09-25` [ForcedLeak (Salesforce Agentforce)](2025-09-25-forcedleak-salesforce-agentforce.md)<br>  <sub>ForcedLeak (Salesforce Agentforce)</sub>
- `2025-09-30` [Gemini "Trifecta"](2025-09-30-gemini-trifecta.md)<br>  <sub>Gemini "Trifecta"</sub>
- `2025-08-06` [AgentFlayer zero-click attack set (Black Hat USA)](../2025-08/2025-08-06-agentflayer-black-hat-usa.md)<br>  <sub>AgentFlayer zero-click attack set (Black Hat USA)</sub>

---

[← 2025-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-09/2025-09-18-shadowleak.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
