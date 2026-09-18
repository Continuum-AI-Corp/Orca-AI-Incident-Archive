---
id: 2025-11-25-mixpanel-tong-bao-di-san
title: "OpenAI reports the third-party Mixpanel breach"
title_zh: "OpenAI 通报 Mixpanel 第三方泄露"
title_ja: "OpenAIが第三者Mixpanelの侵害を報告"
title_ko: "OpenAI, 서드파티 Mixpanel 침해 통보"
title_de: "OpenAI meldet den Vorfall beim Drittanbieter Mixpanel"
title_fr: "OpenAI signale la violation de données du tiers Mixpanel"
title_es: "OpenAI informa de la brecha de Mixpanel, un tercero"
date: 2025-11-25
date_precision: part
date_raw: "late 2025-11"

kind: incident
type: [CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  On **11-09** Mixpanel discovered an attacker exporting a dataset; the source was **SMS phishing** against its employee accounts. **No OpenAI systems were compromised**; no conversations, API requests, passwords, credentials, API keys or payment information leaked; what leaked was contact metadata such as names, emails, approximate location, browser/OS, and organization/user IDs


summary_zh: |
  Mixpanel **11-09** 发现攻击者导出数据集，源头是针对其员工账号的**短信钓鱼**。**非 OpenAI 系统被攻破**；无对话、API 请求、密码、凭据、API key、支付信息泄露；泄露的是姓名、邮箱、大致位置、浏览器/OS、组织/用户 ID 等联系元数据

summary_ja: |
  **11-09**にMixpanelが攻撃者によるデータセットの持ち出しを発見。侵入元は従業員アカウントに対する**SMSフィッシング**だった。**OpenAIのシステムは侵害されていない**。会話、APIリクエスト、パスワード、認証情報、APIキー、支払い情報の漏えいはなく、漏れたのは氏名、メール、おおよその所在地、ブラウザ/OS、組織/ユーザーIDなどの連絡先メタデータだった

summary_ko: |
  **11-09** Mixpanel은 공격자가 데이터셋을 내보내고 있는 것을 발견했다. 경로는 직원 계정을 겨냥한 **SMS 피싱**이었다. **OpenAI 시스템은 침해되지 않았고**, 대화, API 요청, 비밀번호, 자격 증명, API 키, 결제 정보는 유출되지 않았다. 유출된 것은 이름, 이메일, 대략적 위치, 브라우저/OS, 조직/사용자 ID 같은 연락처 메타데이터였다

summary_de: |
  Am **11-09** entdeckte Mixpanel, dass ein Angreifer einen Datensatz exportierte; die Quelle war **SMS-Phishing** gegen Mitarbeiterkonten. **Keine OpenAI-Systeme wurden kompromittiert**; es gelangten keine Unterhaltungen, API-Anfragen, Passwörter, Zugangsdaten, API-Schlüssel oder Zahlungsinformationen nach außen; preisgegeben wurden Kontakt-Metadaten wie Namen, E-Mails, ungefährer Standort, Browser/Betriebssystem sowie Organisations-/Nutzer-IDs

summary_fr: |
  Le **11-09**, Mixpanel a découvert qu'un attaquant exportait un jeu de données ; la source était du **hameçonnage par SMS** contre ses comptes employés. **Aucun système d'OpenAI n'a été compromis** ; aucune conversation, requête API, mot de passe, identifiant, clé API ou information de paiement n'a fuité ; ce qui a fuité, ce sont des métadonnées de contact comme les noms, e-mails, localisation approximative, navigateur/OS et ID d'organisation/utilisateur

summary_es: |
  El **11-09** Mixpanel descubrió a un atacante exportando un conjunto de datos; el origen fue **phishing por SMS** contra las cuentas de sus empleados. **Ningún sistema de OpenAI fue comprometido**; no se filtraron conversaciones, solicitudes de API, contraseñas, credenciales, claves de API ni información de pago; lo filtrado fueron metadatos de contacto como nombres, correos, ubicación aproximada, navegador/SO e identificadores de organización/usuario

sources:
  - url: https://openai.com/index/mixpanel-incident/
    label: OpenAI
  - url: https://techcrunch.com/2025/12/02/a-data-breach-at-analytics-giant-mixpanel-leaves-a-lot-of-open-questions/
    label: TechCrunch

disputed: false
landmark: false
scan_month: 2025-11
scan_ref: "SCAN.md §5 2025-11"
---

# OpenAI reports the third-party Mixpanel breach

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

On **11-09** Mixpanel discovered an attacker exporting a dataset; the source was **SMS phishing** against its employee accounts. **No OpenAI systems were compromised**; no conversations, API requests, passwords, credentials, API keys or payment information leaked; what leaked was contact metadata such as names, emails, approximate location, browser/OS, and organization/user IDs

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
| 1 | OpenAI | <https://openai.com/index/mixpanel-incident/> |
| 2 | TechCrunch | <https://techcrunch.com/2025/12/02/a-data-breach-at-analytics-giant-mixpanel-leaves-a-lot-of-open-questions/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-11-25` (raw: late 2025-11, precision `part`) |
| Kind | Incident `incident` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-11-25-mixpanel-tong-bao-di-san` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2025-11-21` [Shai-Hulud 2.0](2025-11-21-shai-hulud.md)<br>  <sub>Shai-Hulud 2.0</sub>
- `2025-10-28` [Claude Code API key exfiltration](../2025-10/2025-10-28-claude-code-api.md)<br>  <sub>Claude Code API key exfiltration</sub>
- `2025-12-15` ["Privacy" browser extensions resell AI conversations](../2025-12/2025-12-15-yin-si-liu-lan-qi.md)<br>  <sub>"Privacy" browser extensions resell AI conversations</sub>
- `2025-12-30` [Chrome extensions steal ChatGPT and DeepSeek conversations](../2025-12/2025-12-30-chrome-chatgpt-deepseek.md)<br>  <sub>Chrome extensions steal ChatGPT and DeepSeek conversations</sub>

---

[← 2025-11 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-11/2025-11-25-mixpanel-tong-bao-di-san.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
