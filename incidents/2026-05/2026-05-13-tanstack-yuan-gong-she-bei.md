---
id: 2026-05-13-tanstack-yuan-gong-she-bei
title: "OpenAI staff devices compromised via the TanStack incident"
title_zh: "OpenAI 员工设备因 TanStack 事件被攻陷"
title_ja: "TanStackインシデントでOpenAI従業員のデバイスが侵害"
title_ko: "TanStack 사건으로 OpenAI 직원 기기 침해"
title_de: "Geräte von OpenAI-Mitarbeitern über den TanStack-Vorfall kompromittiert"
title_fr: "Des appareils d'employés d'OpenAI compromis via l'incident TanStack"
title_es: "Comprometen dispositivos de empleados de OpenAI a través del incidente de TanStack"
date: 2026-05-13
date_precision: day
date_raw: "2026-05-13"

kind: incident
type: [SUPPLY]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Some repository credentials and **Windows/macOS/iOS code-signing certificates** were exposed; no customer data or IP was compromised, and certificates were rotated preventively (macOS users must update the app by 2026-06-12)


summary_zh: |
  部分仓库凭据与 **Windows/macOS/iOS 代码签名证书**暴露；未见客户数据或 IP 受损，预防性轮换证书（macOS 用户须在 2026-06-12 前更新应用）

summary_ja: |
  一部のリポジトリ認証情報と**Windows/macOS/iOSのコード署名証明書**が露出した。顧客データやIPは侵害されておらず、証明書は予防的にローテーションされた（macOSユーザーは2026-06-12までにアプリを更新する必要がある）

summary_ko: |
  일부 저장소 자격 증명과 **Windows/macOS/iOS 코드 서명 인증서**가 노출되었다. 고객 데이터나 지식재산은 침해되지 않았고 인증서는 예방적으로 교체되었다(macOS 사용자는 2026-06-12까지 앱을 업데이트해야 한다)

summary_de: |
  Einige Repository-Zugangsdaten und **Code-Signaturzertifikate für Windows/macOS/iOS** wurden exponiert; keine Kundendaten und kein geistiges Eigentum wurden kompromittiert, und die Zertifikate wurden vorsorglich rotiert (macOS-Nutzer müssen die App bis zum 2026-06-12 aktualisieren)

summary_fr: |
  Certains identifiants de dépôt et **certificats de signature de code Windows/macOS/iOS** ont été exposés ; aucune donnée client ni propriété intellectuelle n'a été compromise, et les certificats ont été renouvelés par précaution (les utilisateurs macOS doivent mettre à jour l'application avant le 2026-06-12)

summary_es: |
  Se expusieron algunas credenciales de repositorios y **certificados de firma de código de Windows/macOS/iOS**; no se comprometieron datos de clientes ni propiedad intelectual, y los certificados se rotaron de forma preventiva (los usuarios de macOS deben actualizar la app antes del 2026-06-12)

sources:
  - url: https://openai.com/ja-JP/index/our-response-to-the-tanstack-npm-supply-chain-attack/
    label: OpenAI

disputed: false
landmark: false
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# OpenAI staff devices compromised via the TanStack incident

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## Summary

Some repository credentials and **Windows/macOS/iOS code-signing certificates** were exposed; no customer data or IP was compromised, and certificates were rotated preventively (macOS users must update the app by 2026-06-12)

## Attack chain

```mermaid
flowchart LR
    E["Poisoned package / repository / agent config"]:::entry
    S0["Developer or agent installs it automatically"]:::step
    I["Credential theft and self-propagation"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | OpenAI | <https://openai.com/ja-JP/index/our-response-to-the-tanstack-npm-supply-chain-attack/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-13` (raw: 2026-05-13, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-13-tanstack-yuan-gong-she-bei` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-05-19` [TrapDoor: poisoning three ecosystems to corrupt AI assistant configs](2026-05-19-trapdoor-poisons-agent-configs.md)<br>  <sub>TrapDoor: poisoning three ecosystems to corrupt AI assistant configs</sub>
- `2026-05-21` [Composio: agent automation itself becomes the privilege-escalation path](2026-05-21-composio-agent-automation-privesc.md)<br>  <sub>Composio: agent automation itself becomes the privilege-escalation path</sub>
- `2026-05-11` [TanStack npm "Mini Shai-Hulud"](2026-05-11-tanstack-npm-mini-shai.md)<br>  <sub>TanStack npm "Mini Shai-Hulud"</sub>
- `2026-05-18` [3,800 internal GitHub repositories compromised](2026-05-18-github-3800-internal-repos.md)<br>  <sub>3,800 internal GitHub repositories compromised</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-13-tanstack-yuan-gong-she-bei.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
