---
id: 2026-01-26-clawdbot-wang-guan-gui-mo
title: "Clawdbot gateways exposed at scale"
title_zh: "Clawdbot 网关大规模裸奔"
title_ja: "Clawdbotのゲートウェイが大規模に露出"
title_ko: "Clawdbot 게이트웨이 대규모 노출"
title_de: "Clawdbot-Gateways in großem Umfang exponiert"
title_fr: "Les passerelles Clawdbot exposées à grande échelle"
title_es: "Gateways de Clawdbot expuestos a gran escala"
date: 2026-01-26
date_precision: day
date_raw: "2026-01-26"

kind: incident
type: [INFRA, CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Behind a reverse proxy `X-Forwarded-For` is not handled correctly, so the "auto-approve localhost" check is fooled → **900+ instances** expose the Control UI to unauthenticated remote access, leaking Anthropic/Slack/Telegram API keys and months of conversation history, with **RCE as root** possible. Recommendations: configure `gateway.trustedProxies`, enable password authentication, rotate all credentials


summary_zh: |
  反向代理下未正确处理 `X-Forwarded-For`，「localhost 自动批准」误判 → **900+ 实例**可无认证远程访问 Control UI，泄露 Anthropic/Slack/Telegram API key、数月对话历史，并可 **root 权限 RCE**。建议：配置 `gateway.trustedProxies`、启用密码认证、轮换全部凭据

summary_ja: |
  リバースプロキシの背後では`X-Forwarded-For`が正しく処理されないため、「localhostを自動承認」のチェックが欺かれ、**900以上のインスタンス**がControl UIを未認証のリモートアクセスにさらし、Anthropic/Slack/TelegramのAPIキーと数か月分の会話履歴が漏えい、**rootでのRCE**も可能。推奨事項：`gateway.trustedProxies`の設定、パスワード認証の有効化、すべての認証情報のローテーション

summary_ko: |
  리버스 프록시 뒤에서 `X-Forwarded-For`가 올바르게 처리되지 않아 "localhost 자동 승인" 검사가 속는다 → **900개 이상 인스턴스**가 Control UI를 무인증 원격 접근에 노출해 Anthropic/Slack/Telegram API 키와 수개월치 대화 기록이 유출되었고, **root 권한 RCE**도 가능했다. 권고: `gateway.trustedProxies` 설정, 비밀번호 인증 활성화, 모든 자격 증명 교체

summary_de: |
  Hinter einem Reverse Proxy wird `X-Forwarded-For` nicht korrekt behandelt, sodass die Prüfung „localhost automatisch genehmigen“ getäuscht wird → **900+ Instanzen** legen die Control UI für nicht authentifizierten Fernzugriff offen, wodurch Anthropic-/Slack-/Telegram-API-Schlüssel und monatelanger Unterhaltungsverlauf preisgegeben werden, mit möglicher **RCE als root**. Empfehlungen: `gateway.trustedProxies` konfigurieren, Passwortauthentifizierung aktivieren, alle Zugangsdaten rotieren

summary_fr: |
  Derrière un reverse proxy, `X-Forwarded-For` n'est pas traité correctement, ce qui trompe la vérification « auto-approuver localhost » → **plus de 900 instances** exposent la Control UI à un accès distant non authentifié, laissant fuiter des clés API Anthropic/Slack/Telegram et des mois d'historique de conversations, avec un **RCE en root** possible. Recommandations : configurer `gateway.trustedProxies`, activer l'authentification par mot de passe, faire tourner tous les identifiants

summary_es: |
  Detrás de un proxy inverso, `X-Forwarded-For` no se maneja correctamente, así que la comprobación de "aprobación automática de localhost" se engaña → **más de 900 instancias** exponen la Control UI a acceso remoto sin autenticación, filtrando claves de API de Anthropic/Slack/Telegram y meses de historial de conversaciones, con posibilidad de **RCE como root**. Recomendaciones: configurar `gateway.trustedProxies`, habilitar autenticación por contraseña, rotar todas las credenciales

sources:
  - url: https://cybersecuritynews.com/clawdbot-chats-exposed/
    label: CybersecurityNews
  - url: https://x.com/theonejvo/status/2015401219746128322
    label: Original discovery (X)

disputed: false
landmark: true
scan_month: 2026-01
scan_ref: "SCAN.md §6 2026-01"
---

# Clawdbot gateways exposed at scale

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

Behind a reverse proxy `X-Forwarded-For` is not handled correctly, so the "auto-approve localhost" check is fooled → **900+ instances** expose the Control UI to unauthenticated remote access, leaking Anthropic/Slack/Telegram API keys and months of conversation history, with **RCE as root** possible. Recommendations: configure `gateway.trustedProxies`, enable password authentication, rotate all credentials

## Attack chain

```mermaid
flowchart LR
    E["Agent infrastructure exposed to the internet"]:::entry
    S0["Unauthenticated access"]:::step
    S1["agent retrieves and uses them"]:::step
    I["Credential abuse"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | CybersecurityNews | <https://cybersecuritynews.com/clawdbot-chats-exposed/> |
| 2 | Original discovery (X) | <https://x.com/theonejvo/status/2015401219746128322> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-01-26` (raw: 2026-01-26, precision `day`) |
| Kind | Incident `incident` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-01-26-clawdbot-wang-guan-gui-mo` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-01-31` [Moltbook database fully open](2026-01-31-moltbook-open-database.md)<br>  <sub>Moltbook database fully open</sub>
- `2026-01-29` [OpenClaw Control UI WebSocket hijack RCE](2026-01-29-openclaw-control-ui-websocket.md)<br>  <sub>OpenClaw Control UI WebSocket hijack RCE</sub>
- `2026-01-31` [Step Finance treasury drained](2026-01-31-step-finance-jin-ku-dao.md)<br>  <sub>Step Finance treasury drained</sub>
- `2026-02-28` [CodeWall breaches McKinsey's internal "Lilli" AI platform](../2026-02/2026-02-28-codewall-breaches-mckinsey-lilli.md)<br>  <sub>CodeWall breaches McKinsey's internal "Lilli" AI platform</sub>

---

[← 2026-01 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-01/2026-01-26-clawdbot-wang-guan-gui-mo.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
