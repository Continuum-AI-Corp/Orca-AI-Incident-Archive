---
id: 2026-02-25-openclaw-clawjacked
title: "OpenClaw ClawJacked (CVE-2026-25253)"
title_zh: "OpenClaw ClawJacked（CVE-2026-25253）"
title_ja: "OpenClaw ClawJacked（CVE-2026-25253）"
title_ko: "OpenClaw ClawJacked (CVE-2026-25253)"
title_de: "OpenClaw ClawJacked (CVE-2026-25253)"
title_fr: "OpenClaw ClawJacked (CVE-2026-25253)"
title_es: "OpenClaw ClawJacked (CVE-2026-25253)"
date: 2026-02-25
date_precision: day
date_raw: "2026-02-25"

kind: incident
type: [INFRA]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Oasis Security: a cross-origin WebSocket can connect to the local gateway with no rate limiting and no device approval → full control of the agent (interact, export config, enumerate connected devices, read logs). At disclosure **42,665 instances were exposed** (SecurityScorecard gives a different figure of 40,214, of which 35.4% were vulnerable)


summary_zh: |
  Oasis Security：跨源 WebSocket 连本地网关，无速率限制、无设备批准 → 完全控制 agent（交互、导出配置、枚举已连设备、读日志）。披露时 **42,665 个实例暴露**（SecurityScorecard 另称 40,214 台，35.4% 存在漏洞）

summary_ja: |
  Oasis Security：クロスオリジンのWebSocketがレート制限もデバイス承認もなくローカルゲートウェイに接続できる→エージェントの完全制御（操作、設定の持ち出し、接続デバイスの列挙、ログの読み取り）。公表時点で**42,665インスタンスが露出**（SecurityScorecardは40,214という別の数字を挙げ、うち35.4%が脆弱だったとしている）

summary_ko: |
  Oasis Security: 교차 출처 WebSocket이 속도 제한도 기기 승인도 없이 로컬 게이트웨이에 접속할 수 있다 → 에이전트 완전 장악(상호작용, 설정 내보내기, 연결 기기 열거, 로그 읽기). 공개 시점에 **42,665개 인스턴스가 노출**되었다(SecurityScorecard는 40,214개, 그중 35.4%가 취약하다는 다른 수치를 제시했다)

summary_de: |
  Oasis Security: Ein Cross-Origin-WebSocket kann sich ohne Rate Limiting und ohne Gerätefreigabe mit dem lokalen Gateway verbinden → vollständige Kontrolle über den Agenten (Interagieren, Konfiguration exportieren, verbundene Geräte auflisten, Logs lesen). Zum Zeitpunkt der Offenlegung waren **42,665 Instanzen exponiert** (SecurityScorecard nennt eine abweichende Zahl von 40,214, davon 35.4% verwundbar)

summary_fr: |
  Oasis Security : un WebSocket cross-origin peut se connecter à la passerelle locale sans limitation de débit ni approbation d'appareil → contrôle total de l'agent (interaction, export de configuration, énumération des appareils connectés, lecture des journaux). Au moment de la divulgation, **42 665 instances étaient exposées** (SecurityScorecard donne un chiffre différent : 40 214, dont 35,4 % vulnérables)

summary_es: |
  Oasis Security: un WebSocket de origen cruzado puede conectarse al gateway local sin límite de tasa y sin aprobación de dispositivo → control total del agente (interactuar, exportar la configuración, enumerar dispositivos conectados, leer registros). En el momento de la divulgación **42,665 instancias estaban expuestas** (SecurityScorecard da una cifra distinta, 40,214, de las cuales el 35.4% eran vulnerables)

sources:
  - url: https://rafter.so/blog/incidents/ai-agent-security-timeline-2025-2026
    label: Rafter timeline
  - url: https://adversa.ai/blog/openclaw-security-101-vulnerabilities-hardening-2026/
    label: adversa

disputed: false
landmark: false
scan_month: 2026-02
scan_ref: "SCAN.md §6 2026-02"
---

# OpenClaw ClawJacked (CVE-2026-25253)

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

Oasis Security: a cross-origin WebSocket can connect to the local gateway with no rate limiting and no device approval → full control of the agent (interact, export config, enumerate connected devices, read logs). At disclosure **42,665 instances were exposed** (SecurityScorecard gives a different figure of 40,214, of which 35.4% were vulnerable)

## Attack chain

```mermaid
flowchart LR
    E["Agent infrastructure exposed to the internet"]:::entry
    S0["Unauthenticated access"]:::step
    I["RCE / data leak"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Rafter timeline | <https://rafter.so/blog/incidents/ai-agent-security-timeline-2025-2026> |
| 2 | adversa | <https://adversa.ai/blog/openclaw-security-101-vulnerabilities-hardening-2026/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-02-25` (raw: 2026-02-25, precision `day`) |
| Kind | Incident `incident` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-02-25-openclaw-clawjacked` |

<sub>**Why this classification:** Real incident without a confirmed specific victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-02-28` [CodeWall breaches McKinsey's internal "Lilli" AI platform](2026-02-28-codewall-breaches-mckinsey-lilli.md)<br>  <sub>CodeWall breaches McKinsey's internal "Lilli" AI platform</sub>
- `2026-02-10` [15,200 OpenClaw control panels exposed](2026-02-10-openclaw-kong-zhi-mian-ban.md)<br>  <sub>15,200 OpenClaw control panels exposed</sub>
- `2026-01-26` [Clawdbot gateways exposed at scale](../2026-01/2026-01-26-clawdbot-wang-guan-gui-mo.md)<br>  <sub>Clawdbot gateways exposed at scale</sub>
- `2026-01-29` [OpenClaw Control UI WebSocket hijack RCE](../2026-01/2026-01-29-openclaw-control-ui-websocket.md)<br>  <sub>OpenClaw Control UI WebSocket hijack RCE</sub>

---

[← 2026-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-02/2026-02-25-openclaw-clawjacked.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
