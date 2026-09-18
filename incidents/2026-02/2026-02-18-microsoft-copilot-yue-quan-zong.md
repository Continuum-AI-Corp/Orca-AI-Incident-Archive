---
id: 2026-02-18-microsoft-copilot-yue-quan-zong
title: "Microsoft 365 Copilot summarises confidential mail it shouldn't see"
title_zh: "Microsoft 365 Copilot 越权总结机密邮件"
title_ja: "Microsoft 365 Copilotが本来見るべきでない機密メールを要約"
title_ko: "Microsoft 365 Copilot, 보아서는 안 되는 기밀 메일을 요약"
title_de: "Microsoft 365 Copilot fasst vertrauliche E-Mails zusammen, die es nicht sehen dürfte"
title_fr: "Microsoft 365 Copilot résume des e-mails confidentiels qu'il ne devrait pas voir"
title_es: "Microsoft 365 Copilot resume correo confidencial que no debería ver"
date: 2026-02-18
date_precision: day
date_raw: "2026-02-18"

kind: vulnerability
type: [ROGUE]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Tracking ID **CW1226324**. A code defect made the Copilot "Work" tab read protected content in "Sent Items" and "Drafts" against its configuration, **bypassing configured DLP policies and sensitivity labels**. Detected on 2026-01-21; Microsoft says it only processed information the user was already entitled to see, and has rolled out a fix worldwide


summary_zh: |
  追踪 ID **CW1226324**。代码缺陷导致 Copilot「工作」标签页违反配置读取「已发送」「草稿」中的受保护内容，**绕过已配置的 DLP 策略与敏感度标签**。2026-01-21 检测到，微软称仅处理了用户本就有权查看的信息，已全球推送修复

summary_ja: |
  トラッキングID **CW1226324**。コードの欠陥により、Copilotの「Work」タブが「送信済みアイテム」と「下書き」の保護されたコンテンツを設定に反して読み取り、**構成済みのDLPポリシーと機密ラベルをバイパス**した。2026-01-21に検知。Microsoftはユーザーが元々閲覧する権利のある情報しか処理していないとし、修正を全世界に展開済み

summary_ko: |
  추적 ID **CW1226324**. 코드 결함으로 Copilot "Work" 탭이 설정에 어긋나게 "보낸 편지함"과 "임시 보관함"의 보호된 콘텐츠를 읽었고, **설정된 DLP 정책과 민감도 레이블을 우회**했다. 2026-01-21에 탐지되었으며, 마이크로소프트는 사용자가 이미 볼 권한이 있는 정보만 처리했다고 밝히고 전 세계에 수정을 배포했다

summary_de: |
  Tracking-ID **CW1226324**. Ein Codeproblem führte dazu, dass die Registerkarte „Work“ von Copilot entgegen ihrer Konfiguration geschützte Inhalte in „Gesendete Elemente“ und „Entwürfe“ las und dabei **konfigurierte DLP-Richtlinien und Vertraulichkeitsbezeichnungen umging**. Entdeckt am 2026-01-21; Microsoft erklärt, es habe nur Informationen verarbeitet, zu deren Einsicht der Nutzer ohnehin berechtigt gewesen sei, und hat weltweit eine Korrektur ausgerollt

summary_fr: |
  ID de suivi **CW1226324**. Un défaut de code faisait que l'onglet « Work » de Copilot lisait du contenu protégé dans « Éléments envoyés » et « Brouillons » contre sa configuration, **contournant les politiques DLP configurées et les étiquettes de sensibilité**. Détecté le 2026-01-21 ; Microsoft affirme n'avoir traité que des informations auxquelles l'utilisateur avait déjà droit, et a déployé un correctif dans le monde entier

summary_es: |
  ID de seguimiento **CW1226324**. Un defecto de código hizo que la pestaña "Work" de Copilot leyera contenido protegido en "Elementos enviados" y "Borradores" contra su configuración, **eludiendo las políticas DLP configuradas y las etiquetas de confidencialidad**. Detectado el 2026-01-21; Microsoft dice que solo procesó información que el usuario ya tenía derecho a ver, y ha desplegado una corrección en todo el mundo

sources:
  - url: https://www.bleepingcomputer.com/news/microsoft/microsoft-says-bug-causes-copilot-to-summarize-confidential-emails/
    label: BleepingComputer

disputed: false
landmark: false
scan_month: 2026-02
scan_ref: "SCAN.md §6 2026-02"
---

# Microsoft 365 Copilot summarises confidential mail it shouldn't see

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: ROGUE](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

## Summary

Tracking ID **CW1226324**. A code defect made the Copilot "Work" tab read protected content in "Sent Items" and "Drafts" against its configuration, **bypassing configured DLP policies and sensitivity labels**. Detected on 2026-01-21; Microsoft says it only processed information the user was already entitled to see, and has rolled out a fix worldwide

## Attack chain

```mermaid
flowchart LR
    E["An ordinary task handed over by the user"]:::entry
    S0["agent misjudges the situation and escalates on its own"]:::step
    I["A destructive command is executed"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | BleepingComputer | <https://www.bleepingcomputer.com/news/microsoft/microsoft-says-bug-causes-copilot-to-summarize-confidential-emails/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-02-18` (raw: 2026-02-18, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`ROGUE`](../../taxonomy/types.md#rogue) Rogue agent action |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-02-18-microsoft-copilot-yue-quan-zong` |

<sub>**Why this classification:** Vulnerability disclosure with confirmed in-the-wild exploitation, so `real_harm: true`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Coding agent autonomous sabotage](../../topics/rogue-agents.md)

**Related records:**

- `2026-02-26` [Claude Code runs terraform destroy on all of DataTalks.Club's production](2026-02-26-claude-code-terraform-destroy-datatalks.md)<br>  <sub>Claude Code runs terraform destroy on all of DataTalks.Club's production</sub>
- `2026-02-23` [OpenClaw deletes mail despite repeated stop commands](2026-02-23-openclaw-shi-ting-zhi-zhi.md)<br>  <sub>OpenClaw deletes mail despite repeated stop commands</sub>
- `2026-03-02` [⚠️ Amazon hit by back-to-back outages from AI-generated code](../2026-03/2026-03-02-amazon-yin-sheng-cheng-dai.md)<br>  <sub>Amazon hit by back-to-back outages from AI-generated code</sub>
- `2026-03-18` [Meta internal AI agent data exposure](../2026-03/2026-03-18-meta-agent-nei-bu-shu.md)<br>  <sub>Meta internal AI agent data exposure</sub>

---

[← 2026-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-02/2026-02-18-microsoft-copilot-yue-quan-zong.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
