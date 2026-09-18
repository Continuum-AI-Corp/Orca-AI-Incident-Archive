---
id: 2025-10-28-claude-code-api
title: "Claude Code API key exfiltration"
title_zh: "Claude Code API 密钥外带"
title_ja: "Claude CodeのAPIキー外部送信"
title_ko: "Claude Code API 키 유출"
title_de: "Claude Code: Exfiltration des API-Schlüssels"
title_fr: "Exfiltration de clés API via Claude Code"
title_es: "Exfiltración de claves de API en Claude Code"
date: 2025-10-28
date_precision: day
date_raw: "2025-10-28"

kind: vulnerability
type: [CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  A malicious `ANTHROPIC_BASE_URL` in `.claude/settings.json` routes authenticated traffic to an attacker's proxy, **before the trust prompt ever appears**. CVE-2026-21852 (disclosed 2026-01-21), **fixed 2025-12-28**


summary_zh: |
  `.claude/settings.json` 里的恶意 `ANTHROPIC_BASE_URL` 把已认证流量导向攻击者代理，**且发生在信任提示出现之前**。CVE-2026-21852（2026-01-21 公开），**2025-12-28 修复**

summary_ja: |
  `.claude/settings.json`内の悪意ある`ANTHROPIC_BASE_URL`が、**信頼確認プロンプトが表示される前に**認証済みトラフィックを攻撃者のプロキシへルーティングする。CVE-2026-21852（2026-01-21公開）、**2025-12-28に修正**

summary_ko: |
  `.claude/settings.json`의 악성 `ANTHROPIC_BASE_URL`이 **신뢰 프롬프트가 뜨기도 전에** 인증된 트래픽을 공격자 프록시로 우회시킨다. CVE-2026-21852(2026-01-21 공개), **2025-12-28 수정**

summary_de: |
  Eine bösartige `ANTHROPIC_BASE_URL` in `.claude/settings.json` leitet authentifizierten Verkehr über einen Proxy des Angreifers — **noch bevor der Vertrauensdialog überhaupt erscheint**. CVE-2026-21852 (offengelegt am 2026-01-21), **behoben am 2025-12-28**

summary_fr: |
  Une variable `ANTHROPIC_BASE_URL` malveillante dans `.claude/settings.json` route le trafic authentifié vers le proxy d'un attaquant, **avant même que l'invite de confiance n'apparaisse**. CVE-2026-21852 (divulgué le 2026-01-21), **corrigé le 2025-12-28**

summary_es: |
  Un `ANTHROPIC_BASE_URL` malicioso en `.claude/settings.json` enruta el tráfico autenticado al proxy de un atacante, **antes de que aparezca el aviso de confianza**. CVE-2026-21852 (divulgado el 2026-01-21), **corregido el 2025-12-28**

sources:
  - url: https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/
    label: Check Point

disputed: false
landmark: false
scan_month: 2025-10
scan_ref: "SCAN.md §5 2025-10"
---

# Claude Code API key exfiltration

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

A malicious `ANTHROPIC_BASE_URL` in `.claude/settings.json` routes authenticated traffic to an attacker's proxy, **before the trust prompt ever appears**. CVE-2026-21852 (disclosed 2026-01-21), **fixed 2025-12-28**

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
| 1 | Check Point | <https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-10-28` (raw: 2025-10-28, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-10-28-claude-code-api` |

<sub>**Why this classification:** Vulnerability disclosure with confirmed in-the-wild exploitation, so `real_harm: true`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2025-09-15` [Shai-Hulud npm worm v1](../2025-09/2025-09-15-shai-hulud-npm.md)<br>  <sub>Shai-Hulud npm worm v1</sub>
- `2025-11-21` [Shai-Hulud 2.0](../2025-11/2025-11-21-shai-hulud.md)<br>  <sub>Shai-Hulud 2.0</sub>
- `2025-11-25` [OpenAI reports the third-party Mixpanel breach](../2025-11/2025-11-25-mixpanel-tong-bao-di-san.md)<br>  <sub>OpenAI reports the third-party Mixpanel breach</sub>
- `2025-08-08` [Salesloft Drift OAuth token theft](../2025-08/2025-08-08-salesloft-drift-oauth-theft.md)<br>  <sub>Salesloft Drift OAuth token theft</sub>

---

[← 2025-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-10/2025-10-28-claude-code-api.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
