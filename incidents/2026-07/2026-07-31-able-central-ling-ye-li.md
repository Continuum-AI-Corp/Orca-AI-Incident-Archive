---
id: 2026-07-31-able-central-ling-ye-li
title: "N-able N-central zero-day exploited in the wild"
title_zh: "N-able N-central 零日在野利用"
title_ja: "N-able N-centralのゼロデイが実悪用される"
title_ko: "N-able N-central 제로데이 실제 악용"
title_de: "N-able N-central: Zero-Day in freier Wildbahn ausgenutzt"
title_fr: "Un zero-day de N-able N-central exploité en conditions réelles"
title_es: "Zero-day de N-able N-central explotado en entornos reales"
date: 2026-07-31
date_precision: day
date_raw: "2026-07-31"

kind: incident
type: [OTHER]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Adlumin MDR detected exploitation of an unknown flaw in a customer environment; the attacker used Take Control to connect to managed endpoints and registered a **Cloudflare tunnel** for persistence. CVE-2026-18556 / 18577; two hotfixes on 08-02 and 08-06


summary_zh: |
  Adlumin MDR 在客户环境检测到未知漏洞被利用；攻击者用 Take Control 连接受管端点并注册 **Cloudflare 隧道**持久化。CVE-2026-18556 / 18577，08-02 与 08-06 两次热修复

summary_ja: |
  Adlumin MDRが顧客環境で未知の欠陥の悪用を検知。攻撃者はTake Controlを使って管理対象エンドポイントに接続し、永続化のために**Cloudflareトンネル**を登録した。CVE-2026-18556 / 18577。08-02と08-06に2件のホットフィックス

summary_ko: |
  Adlumin MDR이 고객 환경에서 알려지지 않은 결함의 악용을 탐지했다. 공격자는 Take Control로 관리 대상 엔드포인트에 접속하고 지속성을 위해 **Cloudflare 터널**을 등록했다. CVE-2026-18556 / 18577이며 08-02와 08-06에 핫픽스 2건이 배포되었다

summary_de: |
  Adlumin MDR erkannte die Ausnutzung einer unbekannten Schwachstelle in einer Kundenumgebung; der Angreifer nutzte Take Control, um sich mit verwalteten Endpunkten zu verbinden, und registrierte einen **Cloudflare-Tunnel** zur Persistenz. CVE-2026-18556 / 18577; zwei Hotfixes am 08-02 und 08-06

summary_fr: |
  Adlumin MDR a détecté l'exploitation d'une faille inconnue dans l'environnement d'un client ; l'attaquant a utilisé Take Control pour se connecter à des endpoints gérés et a enregistré un **tunnel Cloudflare** pour la persistance. CVE-2026-18556 / 18577 ; deux correctifs à chaud les 08-02 et 08-06

summary_es: |
  Adlumin MDR detectó la explotación de un fallo desconocido en el entorno de un cliente; el atacante usó Take Control para conectarse a los endpoints gestionados y registró un **túnel de Cloudflare** para persistencia. CVE-2026-18556 / 18577; dos hotfixes el 08-02 y el 08-06

sources:
  - url: https://www.n-able.com/blog/n-central-security-update-august-2-2026
    label: "N-able"

disputed: false
landmark: false
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# N-able N-central zero-day exploited in the wild

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

Adlumin MDR detected exploitation of an unknown flaw in a customer environment; the attacker used Take Control to connect to managed endpoints and registered a **Cloudflare tunnel** for persistence. CVE-2026-18556 / 18577; two hotfixes on 08-02 and 08-06

## Attack chain

```mermaid
flowchart LR
    E["Entry point"]:::entry
    S0["Process"]:::step
    I["Result"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | N-able | <https://www.n-able.com/blog/n-central-security-update-august-2-2026> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-31` (raw: 2026-07-31, precision `day`) |
| Kind | Incident `incident` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-07-31-able-central-ling-ye-li` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-31-able-central-ling-ye-li.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
