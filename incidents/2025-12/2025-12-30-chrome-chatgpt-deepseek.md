---
id: 2025-12-30-chrome-chatgpt-deepseek
title: "Chrome extensions steal ChatGPT and DeepSeek conversations"
title_zh: "Chrome 扩展窃取 ChatGPT/DeepSeek 对话"
title_ja: "Chrome拡張機能がChatGPTとDeepSeekの会話を窃取"
title_ko: "Chrome 확장 프로그램, ChatGPT와 DeepSeek 대화 탈취"
title_de: "Chrome-Erweiterungen stehlen ChatGPT- und DeepSeek-Unterhaltungen"
title_fr: "Des extensions Chrome volent les conversations ChatGPT et DeepSeek"
title_es: "Extensiones de Chrome roban conversaciones de ChatGPT y DeepSeek"
date: 2025-12-30
date_precision: day
date_raw: "2025-12-30"

kind: incident
type: [CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  ox.security: about 900,000 users; together with the 12-15 incident, about **8.9 million users** affected


summary_zh: |
  ox.security：约 90 万用户；与 12-15 事件合计约 **890 万用户**受影响

summary_ja: |
  ox.security：約90万人のユーザー。12-15のインシデントと合わせ、約**890万人**が影響を受けた

summary_ko: |
  ox.security: 사용자 약 90만 명. 12-15 사건과 합치면 약 **890만 명**이 영향을 받았다

summary_de: |
  ox.security: etwa 900,000 Nutzer; zusammen mit dem Vorfall vom 12-15 sind etwa **8.9 Millionen Nutzer** betroffen

summary_fr: |
  ox.security : environ 900 000 utilisateurs ; avec l'incident du 12-15, environ **8,9 millions d'utilisateurs** touchés

summary_es: |
  ox.security: unos 900,000 usuarios; junto con el incidente del 12-15, unos **8.9 millones de usuarios** afectados

sources:
  - url: https://www.ox.security/blog/malicious-chrome-extensions-steal-chatgpt-deepseek-conversations/
    label: ox.security

disputed: false
landmark: false
scan_month: 2025-12
scan_ref: "SCAN.md §5 2025-12"
---

# Chrome extensions steal ChatGPT and DeepSeek conversations

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

ox.security: about 900,000 users; together with the 12-15 incident, about **8.9 million users** affected

## Attack chain

```mermaid
flowchart LR
    E["Credentials within an agent's reach"]:::entry
    S0["The agent picks them up and calls out"]:::step
    I["Credentials are abused"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | ox.security | <https://www.ox.security/blog/malicious-chrome-extensions-steal-chatgpt-deepseek-conversations/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-12-30` (raw: 2025-12-30, precision `day`) |
| Kind | Incident `incident` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-12-30-chrome-chatgpt-deepseek` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2025-12-15` ["Privacy" browser extensions resell AI conversations](2025-12-15-yin-si-liu-lan-qi.md)<br>  <sub>"Privacy" browser extensions resell AI conversations</sub>
- `2025-11-21` [Shai-Hulud 2.0](../2025-11/2025-11-21-shai-hulud.md)<br>  <sub>Shai-Hulud 2.0</sub>
- `2026-01-31` [Moltbook database fully open](../2026-01/2026-01-31-moltbook-open-database.md)<br>  <sub>Moltbook database fully open</sub>
- `2025-11-25` [OpenAI reports the third-party Mixpanel breach](../2025-11/2025-11-25-mixpanel-tong-bao-di-san.md)<br>  <sub>OpenAI reports the third-party Mixpanel breach</sub>

---

[← 2025-12 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-12/2025-12-30-chrome-chatgpt-deepseek.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
