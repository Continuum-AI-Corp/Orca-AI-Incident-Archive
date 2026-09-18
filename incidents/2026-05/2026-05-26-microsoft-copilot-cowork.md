---
id: 2026-05-26-microsoft-copilot-cowork
title: "Microsoft Copilot Cowork file exfiltration"
title_zh: "Microsoft Copilot Cowork 文件外泄"
title_ja: "Microsoft Copilot Coworkのファイル外部送信"
title_ko: "Microsoft Copilot Cowork 파일 유출"
title_de: "Microsoft Copilot Cowork: Dateiexfiltration"
title_fr: "Exfiltration de fichiers par Microsoft Copilot Cowork"
title_es: "Exfiltración de archivos en Microsoft Copilot Cowork"
date: 2026-05-26
date_precision: day
date_raw: "2026-05-26"

kind: research
type: [IPI, EXFIL]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  PromptArmor: poisoning a **"skill" that loads automatically** from a user-controllable path makes the agent generate a message containing a pre-authenticated download link. **That message is auto-approved and sent to the user themselves, bypassing security controls**; the moment the user opens it, the agent sends a request to the attacker's server. **Model-agnostic** (Claude Opus 4.7 behaves the same), with the scheduled-task feature amplifying the threat


summary_zh: |
  PromptArmor：污染用户可控路径下**自动加载的 "skill"**，诱导 agent 生成含预认证下载链接的消息。**该消息是自动批准发给用户本人的，因此绕过安全控制**；用户一打开，agent 就向攻击者服务器发请求。**与模型无关**（Claude Opus 4.7 亦然），配合定时任务功能威胁放大

summary_ja: |
  PromptArmor：ユーザーが制御可能なパスから**自動的に読み込まれる「スキル」**を汚染すると、エージェントが事前認証済みのダウンロードリンクを含むメッセージを生成する。**そのメッセージは自動承認されてユーザー本人に送信され、セキュリティ制御をバイパスする**。ユーザーが開いた瞬間、エージェントは攻撃者のサーバーへリクエストを送る。**モデル非依存**（Claude Opus 4.7でも同様に動作）で、スケジュールタスク機能が脅威を増幅する

summary_ko: |
  PromptArmor: 사용자가 제어 가능한 경로에서 **자동으로 로드되는 "스킬"**을 오염시키면 에이전트가 사전 인증된 다운로드 링크가 담긴 메시지를 생성한다. **그 메시지는 자동 승인되어 사용자 본인에게 발송되며 보안 통제를 우회한다** — 사용자가 그것을 여는 순간 에이전트가 공격자 서버로 요청을 보낸다. **모델에 무관**하며(Claude Opus 4.7도 동일하게 동작) 예약 작업 기능이 위협을 증폭시킨다

summary_de: |
  PromptArmor: Die Vergiftung eines **„Skills“, der automatisch aus einem vom Nutzer kontrollierbaren Pfad geladen wird**, bringt den Agenten dazu, eine Nachricht mit einem vorauthentifizierten Download-Link zu erzeugen. **Diese Nachricht wird automatisch genehmigt und an den Nutzer selbst gesendet, unter Umgehung der Sicherheitskontrollen**; in dem Moment, in dem der Nutzer sie öffnet, sendet der Agent eine Anfrage an den Server des Angreifers. **Modellunabhängig** (Claude Opus 4.7 verhält sich gleich), wobei die Funktion für geplante Aufgaben die Bedrohung verstärkt

summary_fr: |
  PromptArmor : empoisonner un **« skill » qui se charge automatiquement** depuis un chemin contrôlable par l'utilisateur amène l'agent à générer un message contenant un lien de téléchargement pré-authentifié. **Ce message est auto-approuvé et envoyé à l'utilisateur lui-même, contournant les contrôles de sécurité** ; à l'instant où l'utilisateur l'ouvre, l'agent envoie une requête au serveur de l'attaquant. **Indépendant du modèle** (Claude Opus 4.7 se comporte pareil), la fonctionnalité de tâches planifiées amplifiant la menace

summary_es: |
  PromptArmor: envenenar una **"skill" que se carga automáticamente** desde una ruta controlable por el usuario hace que el agente genere un mensaje con un enlace de descarga preautenticado. **Ese mensaje se aprueba automáticamente y se envía al propio usuario, eludiendo los controles de seguridad**; en el momento en que el usuario lo abre, el agente envía una solicitud al servidor del atacante. **Agnóstico al modelo** (Claude Opus 4.7 se comporta igual), y la función de tareas programadas amplifica la amenaza

sources:
  - url: https://www.promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files
    label: PromptArmor

disputed: false
landmark: true
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# Microsoft Copilot Cowork file exfiltration

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

PromptArmor: poisoning a **"skill" that loads automatically** from a user-controllable path makes the agent generate a message containing a pre-authenticated download link. **That message is auto-approved and sent to the user themselves, bypassing security controls**; the moment the user opens it, the agent sends a request to the attacker's server. **Model-agnostic** (Claude Opus 4.7 behaves the same), with the scheduled-task feature amplifying the threat

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
| 1 | PromptArmor | <https://www.promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-26` (raw: 2026-05-26, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-26-microsoft-copilot-cowork` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-05-04` [Grok / Bankrbot Morse-code prompt injection](2026-05-04-grok-bankrbot-mo-er-si.md)<br>  <sub>Grok / Bankrbot Morse-code prompt injection</sub>
- `2026-05-12` [Brazilian labour court sanctions lawyers over prompt injection](2026-05-12-brazil-labor-court-prompt-injection-sanction.md)<br>  <sub>Brazilian labour court sanctions lawyers over prompt injection</sub>
- `2026-05-12` [ClaudeBleed: a zero-permission extension hijacks Claude for Chrome](2026-05-12-claudebleed-claude-chrome.md)<br>  <sub>ClaudeBleed: a zero-permission extension hijacks Claude for Chrome</sub>
- `2026-05-22` [Google AI Search "disregard" bug](2026-05-22-google-disregard-bug.md)<br>  <sub>Google AI Search "disregard" bug</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-26-microsoft-copilot-cowork.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
