---
id: 2025-12-15-yin-si-liu-lan-qi
title: "\"Privacy\" browser extensions resell AI conversations"
title_zh: "「隐私」浏览器扩展倒卖 AI 对话"
title_ja: "「プライバシー」ブラウザ拡張機能がAI会話を転売"
title_ko: "\"프라이버시\" 브라우저 확장, AI 대화를 재판매"
title_de: "„Datenschutz“-Browser-Erweiterungen verkaufen KI-Unterhaltungen weiter"
title_fr: "Des extensions de navigateur « vie privée » revendent les conversations IA"
title_es: "Extensiones de navegador \"de privacidad\" revenden conversaciones de IA"
date: 2025-12-15
date_precision: day
date_raw: "2025-12-15"

kind: incident
type: [CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Koi Security: Urban VPN and others, about 8 million users


summary_zh: |
  Koi Security：Urban VPN 等，约 800 万用户

summary_ja: |
  Koi Security：Urban VPNなど、約800万人のユーザー

summary_ko: |
  Koi Security: Urban VPN 등, 사용자 약 800만 명

summary_de: |
  Koi Security: Urban VPN und andere, etwa 8 Millionen Nutzer

summary_fr: |
  Koi Security : Urban VPN et d'autres, environ 8 millions d'utilisateurs

summary_es: |
  Koi Security: Urban VPN y otras, unos 8 millones de usuarios

sources:
  - url: https://www.koi.ai/blog/urban-vpn-browser-extension-ai-conversations-data-collection
    label: Koi

disputed: false
landmark: false
scan_month: 2025-12
scan_ref: "SCAN.md §5 2025-12"
---

# "Privacy" browser extensions resell AI conversations

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

Koi Security: Urban VPN and others, about 8 million users

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
| 1 | Koi | <https://www.koi.ai/blog/urban-vpn-browser-extension-ai-conversations-data-collection> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-12-15` (raw: 2025-12-15, precision `day`) |
| Kind | Incident `incident` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-12-15-yin-si-liu-lan-qi` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2025-12-30` [Chrome extensions steal ChatGPT and DeepSeek conversations](2025-12-30-chrome-chatgpt-deepseek.md)<br>  <sub>Chrome extensions steal ChatGPT and DeepSeek conversations</sub>
- `2025-11-21` [Shai-Hulud 2.0](../2025-11/2025-11-21-shai-hulud.md)<br>  <sub>Shai-Hulud 2.0</sub>
- `2026-01-31` [Moltbook database fully open](../2026-01/2026-01-31-moltbook-open-database.md)<br>  <sub>Moltbook database fully open</sub>
- `2025-11-25` [OpenAI reports the third-party Mixpanel breach](../2025-11/2025-11-25-mixpanel-tong-bao-di-san.md)<br>  <sub>OpenAI reports the third-party Mixpanel breach</sub>

---

[← 2025-12 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-12/2025-12-15-yin-si-liu-lan-qi.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
