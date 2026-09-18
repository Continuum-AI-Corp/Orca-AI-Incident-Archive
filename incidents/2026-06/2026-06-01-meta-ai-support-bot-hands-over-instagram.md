---
id: 2026-06-01-meta-ai-support-bot-hands-over-instagram
title: "Attackers simply ask Meta's AI support bot for Instagram accounts"
title_zh: "黑客直接「请求」Meta AI 客服机器人交出 Instagram 账号"
title_ja: "攻撃者はMetaのAIサポートボットにInstagramアカウントを頼むだけ"
title_ko: "공격자들, Meta AI 지원 봇에 그냥 Instagram 계정을 요구하다"
title_de: "Angreifer bitten Metas KI-Support-Bot einfach um Instagram-Konten"
title_fr: "Les attaquants demandent simplement des comptes Instagram au bot de support IA de Meta"
title_es: "Los atacantes simplemente piden cuentas de Instagram al bot de soporte de IA de Meta"
date: 2026-06-01
date_precision: day
date_raw: "2026-06-01"

kind: incident
type: [IPI, CRED]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Attackers used prompt injection to make the AI bind an attacker-controlled email to the target account, **bypassing two-factor authentication**. A textbook "confused deputy" problem — the AI's checks on the attacker's identity were not designed well enough. **About 34,000 accounts** (04-17 → 05-31, 44 days) were taken over and resold by an organized operation; a username alone was enough to start. Meta patched this urgently on **05-29** and restricted the account-recovery API


summary_zh: |
  用提示注入诱导 AI 把攻击者邮箱绑定到目标账户，**绕过两因素认证**。典型「混淆代理人(confused deputy)」问题 —— AI 对攻击者身份校验设计不足。**约 34,000 个账户**（04-17 → 05-31，共 44 天）被有组织接管转卖；仅需用户名即可发起。Meta 于 **05-29** 紧急修补并限制账号恢复 API

summary_ja: |
  攻撃者はプロンプトインジェクションを使い、AIに攻撃者制御のメールアドレスを標的アカウントに紐づけさせ、**二要素認証をバイパス**した。典型的な「confused deputy」問題——AIの攻撃者本人確認が十分に設計されていなかった。**約34,000アカウント**（04-17 → 05-31の44日間）が乗っ取られ、組織的な操作で転売された。ユーザー名だけで開始できた。Metaは**05-29**に緊急修正し、アカウント復旧APIを制限した

summary_ko: |
  공격자들은 프롬프트 인젝션으로 AI가 공격자가 제어하는 이메일을 대상 계정에 연결하게 해 **2단계 인증을 우회**했다. 교과서적인 "혼동된 대리인(confused deputy)" 문제로, AI의 공격자 신원 확인이 충분히 설계되지 않았다. **약 34,000개 계정**(04-17 → 05-31, 44일)이 조직적으로 탈취되어 재판매되었다. 사용자 이름만으로 시작할 수 있었다. Meta는 **05-29** 긴급 패치하고 계정 복구 API를 제한했다

summary_de: |
  Angreifer nutzten Prompt-Injection, um die KI dazu zu bringen, eine vom Angreifer kontrollierte E-Mail an das Zielkonto zu binden, und **umgingen so die Zwei-Faktor-Authentifizierung**. Ein Lehrbuchfall des „Confused Deputy“ — die Prüfungen der KI zur Identität des Angreifers waren nicht gut genug entworfen. **Etwa 34,000 Konten** (04-17 → 05-31, 44 Tage) wurden übernommen und von einer organisierten Operation weiterverkauft; ein bloßer Benutzername genügte für den Anfang. Meta patchte dies am **05-29** dringend und beschränkte die Konto-Wiederherstellungs-API

summary_fr: |
  Les attaquants ont utilisé une injection de prompt pour faire lier par l'IA une adresse e-mail contrôlée par eux au compte cible, **contournant l'authentification à deux facteurs**. Un problème classique de « confused deputy » — les vérifications de l'identité de l'attaquant par l'IA n'étaient pas assez bien conçues. **Environ 34 000 comptes** (04-17 → 05-31, 44 jours) ont été pris et revendus par une opération organisée ; un simple nom d'utilisateur suffisait pour commencer. Meta a corrigé en urgence le **05-29** et restreint l'API de récupération de compte

summary_es: |
  Los atacantes usaron una inyección de prompt para que la IA vinculara un correo controlado por el atacante a la cuenta objetivo, **eludiendo la autenticación de dos factores**. Un caso de manual del problema del "delegado confundido" — las comprobaciones de la IA sobre la identidad del atacante no estaban bien diseñadas. **Unas 34,000 cuentas** (04-17 → 05-31, 44 días) fueron tomadas y revendidas por una operación organizada; bastaba con un nombre de usuario para empezar. Meta lo parcheó urgentemente el **05-29** y restringió la API de recuperación de cuentas

sources:
  - url: https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/
    label: Krebs
  - url: https://www.404media.co/hackers-simply-asked-meta-ai-to-give-them-access-to-high-profile-instagram-accounts-it-worked/
    label: 404 Media
  - url: https://arstechnica.com/ai/2026/06/meta-ai-support-chatbot-gave-hackers-access-to-notable-instagram-accounts/
    label: Ars Technica

disputed: false
landmark: true
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# Attackers simply ask Meta's AI support bot for Instagram accounts

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

Attackers used prompt injection to make the AI bind an attacker-controlled email to the target account, **bypassing two-factor authentication**. A textbook "confused deputy" problem — the AI's checks on the attacker's identity were not designed well enough. **About 34,000 accounts** (04-17 → 05-31, 44 days) were taken over and resold by an organized operation; a username alone was enough to start. Meta patched this urgently on **05-29** and restricted the account-recovery API

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["The agent picks it up and calls it"]:::step
    I["Credential abuse"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Krebs | <https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/> |
| 2 | 404 Media | <https://www.404media.co/hackers-simply-asked-meta-ai-to-give-them-access-to-high-profile-instagram-accounts-it-worked/> |
| 3 | Ars Technica | <https://arstechnica.com/ai/2026/06/meta-ai-support-chatbot-gave-hackers-access-to-notable-instagram-accounts/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-01` (raw: 2026-06-01, precision `day`) |
| Kind | Incident `incident` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-01-meta-ai-support-bot-hands-over-instagram` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-06-01` [Miasma worm](2026-06-01-miasma-worm.md)<br>  <sub>Miasma worm</sub>
- `2026-06-17` [Sapphire Sleet poisons every Mastra AI scope in 88 minutes](2026-06-17-sapphire-sleet-mastra-88-minutes.md)<br>  <sub>Sapphire Sleet poisons every Mastra AI scope in 88 minutes</sub>
- `2026-06-04` [Claude Oceanus-v1-p illegally redistributed](2026-06-04-claude-oceanus-fei-fa-fen.md)<br>  <sub>Claude Oceanus-v1-p illegally redistributed</sub>
- `2026-06-13` [PromptSnatcher: ad-blocking extensions steal AI conversations](2026-06-13-promptsnatcher-guang-gao-lan-jie.md)<br>  <sub>PromptSnatcher: ad-blocking extensions steal AI conversations</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-01-meta-ai-support-bot-hands-over-instagram.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
