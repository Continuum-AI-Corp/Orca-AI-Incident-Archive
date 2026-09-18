---
id: 2026-04-30-tui-chu-gao-ji-zhang
title: "OpenAI launches Advanced Account Security"
title_zh: "OpenAI 推出「高级账户安全」"
title_ja: "OpenAIがAdvanced Account Securityを開始"
title_ko: "OpenAI, 고급 계정 보안 출시"
title_de: "OpenAI führt Advanced Account Security ein"
title_fr: "OpenAI lance la Advanced Account Security"
title_es: "OpenAI lanza la Seguridad de Cuenta Avanzada"
date: 2026-04-30
date_precision: day
date_raw: "2026-04-30"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Mandatory passkey/FIDO hardware keys, removal of email/SMS account recovery, shorter sessions, session visualisation; **enabling it automatically opts the account out of model training**. Built with Yubico


summary_zh: |
  强制 passkey/FIDO 硬件密钥、取消邮件/短信找回、缩短会话、会话可视化；**启用后自动排除模型训练**。与 Yubico 合作

summary_ja: |
  パスキー／FIDOハードウェアキーの必須化、メール／SMSによるアカウント復旧の廃止、セッションの短縮、セッションの可視化。**有効化するとアカウントが自動的にモデル学習からオプトアウトされる**。Yubicoと共同で構築

summary_ko: |
  패스키/FIDO 하드웨어 키 의무화, 이메일/SMS 계정 복구 제거, 세션 단축, 세션 시각화. **활성화하면 계정이 자동으로 모델 학습에서 제외된다**. Yubico와 함께 만들었다

summary_de: |
  Verpflichtende Passkey-/FIDO-Hardware-Schlüssel, Abschaffung der Konto-Wiederherstellung per E-Mail/SMS, kürzere Sitzungen, Sitzungsvisualisierung; **wer es aktiviert, nimmt das Konto automatisch vom Modelltraining aus**. Entwickelt mit Yubico

summary_fr: |
  Clés matérielles passkey/FIDO obligatoires, suppression de la récupération de compte par e-mail/SMS, sessions plus courtes, visualisation des sessions ; **l'activation exclut automatiquement le compte de l'entraînement des modèles**. Développé avec Yubico

summary_es: |
  Claves de hardware passkey/FIDO obligatorias, eliminación de la recuperación de cuenta por correo/SMS, sesiones más cortas, visualización de sesiones; **activarla excluye automáticamente la cuenta del entrenamiento de modelos**. Desarrollada con Yubico

sources:
  - url: https://openai.com/ja-JP/index/advanced-account-security/
    label: OpenAI

disputed: false
landmark: false
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# OpenAI launches Advanced Account Security

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Mandatory passkey/FIDO hardware keys, removal of email/SMS account recovery, shorter sessions, session visualisation; **enabling it automatically opts the account out of model training**. Built with Yubico

## Attack chain

```mermaid
flowchart LR
    E["Regulatory or policy action"]:::entry
    S0["Falls on vendors and users"]:::step
    I["Compliance requirements change"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | OpenAI | <https://openai.com/ja-JP/index/advanced-account-security/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-04-30` (raw: 2026-04-30, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-04-30-tui-chu-gao-ji-zhang` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-04-07` [Claude Mythos Preview cyber capability disclosure, Project Glasswing formed](2026-04-07-claude-mythos-preview-project.md)<br>  <sub>Claude Mythos Preview cyber capability disclosure, Project Glasswing formed</sub>
- `2026-04-13` [UK AISI independently evaluates Claude Mythos Preview](2026-04-13-uk-aisi-claude-mythos.md)<br>  <sub>UK AISI independently evaluates Claude Mythos Preview</sub>
- `2026-04-14` [Vidoc reproduces Mythos's findings with public models](2026-04-14-vidoc-mythos-yong-gong-kai.md)<br>  <sub>Vidoc reproduces Mythos's findings with public models</sub>
- `2026-05-12` [Brazilian labour court sanctions lawyers over prompt injection](../2026-05/2026-05-12-brazil-labor-court-prompt-injection-sanction.md)<br>  <sub>Brazilian labour court sanctions lawyers over prompt injection</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-30-tui-chu-gao-ji-zhang.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
