---
id: 2026-01-12-superhuman-jian-jie-ti-shi
title: "Superhuman AI indirect prompt injection"
title_zh: "Superhuman AI 间接提示注入"
title_ja: "Superhuman AIの間接プロンプトインジェクション"
title_ko: "Superhuman AI 간접 프롬프트 인젝션"
title_de: "Superhuman AI: indirekte Prompt-Injection"
title_fr: "Injection indirecte de prompt dans Superhuman AI"
title_es: "Inyección indirecta de prompt en Superhuman AI"
date: 2026-01-12
date_precision: day
date_raw: "2026-01-12"

kind: incident
type: [IPI, EXFIL]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  PromptArmor: zero-interaction exfiltration of inbox data via **Google Forms prefill links** plus automatic Markdown image rendering, which bypasses CSP. Superhuman's security team fixed it quickly (including Superhuman Go)


summary_zh: |
  PromptArmor：零交互外带收件箱数据，经 **Google 表单预填链接** + Markdown 图片自动渲染绕过 CSP。Superhuman 安全团队快速修复（含 Superhuman Go）

summary_ja: |
  PromptArmor：**Google Formsのプリフィルリンク**とCSPをバイパスするMarkdown画像の自動レンダリングにより、操作ゼロで受信トレイのデータを外部送信。Superhumanのセキュリティチームは迅速に修正した（Superhuman Goを含む）

summary_ko: |
  PromptArmor: **Google Forms 사전 채우기 링크**와 CSP를 우회하는 Markdown 이미지 자동 렌더링을 통해 상호작용 없이 받은편지함 데이터를 유출했다. Superhuman 보안팀은 신속히 수정했다(Superhuman Go 포함)

summary_de: |
  PromptArmor: Exfiltration von Postfachdaten ohne jede Interaktion über **Google-Forms-Prefill-Links** plus automatisches Markdown-Bild-Rendering, das CSP umgeht. Das Sicherheitsteam von Superhuman behob es schnell (einschließlich Superhuman Go)

summary_fr: |
  PromptArmor : exfiltration sans interaction des données de la boîte de réception via des **liens de préremplissage Google Forms** plus le rendu automatique des images Markdown, qui contourne la CSP. L'équipe sécurité de Superhuman a corrigé rapidement (y compris Superhuman Go)

summary_es: |
  PromptArmor: exfiltración de datos de la bandeja de entrada con cero interacción mediante **enlaces de prellenado de Google Forms** más el renderizado automático de imágenes Markdown, que elude el CSP. El equipo de seguridad de Superhuman lo corrigió rápidamente (incluido Superhuman Go)

sources:
  - url: https://www.promptarmor.com/resources/superhuman-ai-exfiltrates-emails
    label: PromptArmor

disputed: false
landmark: true
scan_month: 2026-01
scan_ref: "SCAN.md §6 2026-01"
---

# Superhuman AI indirect prompt injection

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

PromptArmor: zero-interaction exfiltration of inbox data via **Google Forms prefill links** plus automatic Markdown image rendering, which bypasses CSP. Superhuman's security team fixed it quickly (including Superhuman Go)

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["agent reads it and executes it as instructions"]:::step
    S1["Exfiltrated via vendor-trusted domains<br/>image rendering · APIs · proxies"]:::step
    I["Data ends up in the attacker's hands"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | PromptArmor | <https://www.promptarmor.com/resources/superhuman-ai-exfiltrates-emails> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-01-12` (raw: 2026-01-12, precision `day`) |
| Kind | Incident `incident` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-01-12-superhuman-jian-jie-ti-shi` |

<sub>**Why this classification:** Real incident without a confirmed specific victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-01-12` [Claude Cowork ships with known vulnerabilities](2026-01-12-claude-cowork-dai-zhe-zhi.md)<br>  <sub>Claude Cowork ships with known vulnerabilities</sub>
- `2026-01-14` [Microsoft Copilot Personal "Reprompt"](2026-01-14-microsoft-copilot-personal-reprompt.md)<br>  <sub>Microsoft Copilot Personal "Reprompt"</sub>
- `2026-01-07` [Four productivity tools hit the lethal trifecta in nine days](2026-01-07-lethal-trifecta-four-tools.md)<br>  <sub>Four productivity tools hit the lethal trifecta in nine days</sub>
- `2026-02-09` [Clinejection](../2026-02/2026-02-09-clinejection.md)<br>  <sub>Clinejection</sub>

---

[← 2026-01 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-01/2026-01-12-superhuman-jian-jie-ti-shi.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
