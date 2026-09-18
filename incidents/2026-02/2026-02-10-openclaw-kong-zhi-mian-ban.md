---
id: 2026-02-10-openclaw-kong-zhi-mian-ban
title: "15,200 OpenClaw control panels exposed"
title_zh: "15,200 个 OpenClaw 控制面板裸奔"
title_ja: "15,200のOpenClawコントロールパネルが露出"
title_ko: "OpenClaw 제어 패널 15,200개 노출"
title_de: "15,200 OpenClaw-Control-Panels exponiert"
title_fr: "15 200 panneaux de contrôle OpenClaw exposés"
title_es: "15,200 paneles de control de OpenClaw expuestos"
date: 2026-02-10
date_precision: day
date_raw: "2026-02-10"

kind: incident
type: [INFRA]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  SecurityScorecard STRIKE: binds to all network interfaces by default. CVE-2026-25253 (RCE), CVE-2026-25157 (SSH command injection) and CVE-2026-24763 (Docker sandbox escape) are widely unpatched. The agent holds cloud credentials, SSH keys and browser sessions, so a compromise means full loss of control over the host. **About 33.8% of the instances are linked to existing malicious activity (including APT groups)**. Recommendations: upgrade to 2026.2.1+, bind to 127.0.0.1, rotate all API keys


summary_zh: |
  SecurityScorecard STRIKE：默认绑定所有网卡。CVE-2026-25253(RCE)、CVE-2026-25157(SSH 命令注入)、CVE-2026-24763(Docker 沙箱逃逸) 大量未打补丁。agent 持有云凭据、SSH 密钥、浏览器会话，被攻陷即失去主机完全控制权。**约 33.8% 的实例与已有恶意活动（含 APT 组织）相关联**。建议升级至 2026.2.1+、绑定 127.0.0.1、轮换全部 API key

summary_ja: |
  SecurityScorecard STRIKE：デフォルトですべてのネットワークインターフェースにバインドする。CVE-2026-25253（RCE）、CVE-2026-25157（SSHコマンドインジェクション）、CVE-2026-24763（Dockerサンドボックス脱出）は広く未修正のまま。エージェントはクラウド認証情報、SSHキー、ブラウザセッションを保持するため、侵害されるとホストの完全な制御喪失を意味する。**約33.8%のインスタンスが既存の悪性活動（APTグループを含む）と関連している**。推奨事項：2026.2.1以降へアップグレード、127.0.0.1へのバインド、すべてのAPIキーのローテーション

summary_ko: |
  SecurityScorecard STRIKE: 기본적으로 모든 네트워크 인터페이스에 바인딩한다. CVE-2026-25253(RCE), CVE-2026-25157(SSH 명령 주입), CVE-2026-24763(Docker 샌드박스 탈출)이 광범위하게 미패치 상태다. 에이전트가 클라우드 자격 증명, SSH 키, 브라우저 세션을 보유하므로 침해되면 호스트 통제권을 완전히 잃는다. **인스턴스의 약 33.8%가 기존 악성 활동(APT 그룹 포함)과 연결되어 있다**. 권고: 2026.2.1 이상으로 업그레이드, 127.0.0.1에 바인딩, 모든 API 키 교체

summary_de: |
  SecurityScorecard STRIKE: bindet standardmäßig an alle Netzwerkschnittstellen. CVE-2026-25253 (RCE), CVE-2026-25157 (SSH-Command-Injection) und CVE-2026-24763 (Docker-Sandbox-Escape) sind weitgehend ungepatcht. Der Agent hält Cloud-Zugangsdaten, SSH-Schlüssel und Browsersitzungen, eine Kompromittierung bedeutet daher vollständigen Kontrollverlust über den Host. **Etwa 33.8% der Instanzen stehen in Verbindung mit bestehender bösartiger Aktivität (einschließlich APT-Gruppen)**. Empfehlungen: Upgrade auf 2026.2.1+, Binden an 127.0.0.1, Rotation aller API-Schlüssel

summary_fr: |
  SecurityScorecard STRIKE : se lie par défaut à toutes les interfaces réseau. CVE-2026-25253 (RCE), CVE-2026-25157 (injection de commande SSH) et CVE-2026-24763 (évasion de bac à sable Docker) restent largement non corrigés. L'agent détient des identifiants cloud, des clés SSH et des sessions de navigateur, si bien qu'une compromission signifie la perte totale du contrôle de l'hôte. **Environ 33,8 % des instances sont liées à une activité malveillante existante (y compris des groupes APT)**. Recommandations : passer à la version 2026.2.1+, se lier à 127.0.0.1, faire tourner toutes les clés API

summary_es: |
  SecurityScorecard STRIKE: se enlaza a todas las interfaces de red por defecto. CVE-2026-25253 (RCE), CVE-2026-25157 (inyección de comandos SSH) y CVE-2026-24763 (escape del sandbox de Docker) siguen sin parchear en gran medida. El agente posee credenciales de nube, claves SSH y sesiones de navegador, así que un compromiso significa la pérdida total del control del host. **Alrededor del 33.8% de las instancias están vinculadas a actividad maliciosa existente (incluidos grupos APT)**. Recomendaciones: actualizar a 2026.2.1+, enlazar a 127.0.0.1, rotar todas las claves de API

sources:
  - url: https://cybersecuritynews.com/openclaw-control-panels-exposed/
    label: CybersecurityNews

disputed: false
landmark: true
scan_month: 2026-02
scan_ref: "SCAN.md §6 2026-02"
---

# 15,200 OpenClaw control panels exposed

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

SecurityScorecard STRIKE: binds to all network interfaces by default. CVE-2026-25253 (RCE), CVE-2026-25157 (SSH command injection) and CVE-2026-24763 (Docker sandbox escape) are widely unpatched. The agent holds cloud credentials, SSH keys and browser sessions, so a compromise means full loss of control over the host. **About 33.8% of the instances are linked to existing malicious activity (including APT groups)**. Recommendations: upgrade to 2026.2.1+, bind to 127.0.0.1, rotate all API keys

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
| 1 | CybersecurityNews | <https://cybersecuritynews.com/openclaw-control-panels-exposed/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-02-10` (raw: 2026-02-10, precision `day`) |
| Kind | Incident `incident` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-02-10-openclaw-kong-zhi-mian-ban` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-02-28` [CodeWall breaches McKinsey's internal "Lilli" AI platform](2026-02-28-codewall-breaches-mckinsey-lilli.md)<br>  <sub>CodeWall breaches McKinsey's internal "Lilli" AI platform</sub>
- `2026-02-25` [OpenClaw ClawJacked (CVE-2026-25253)](2026-02-25-openclaw-clawjacked.md)<br>  <sub>OpenClaw ClawJacked (CVE-2026-25253)</sub>
- `2026-01-26` [Clawdbot gateways exposed at scale](../2026-01/2026-01-26-clawdbot-wang-guan-gui-mo.md)<br>  <sub>Clawdbot gateways exposed at scale</sub>
- `2026-01-29` [OpenClaw Control UI WebSocket hijack RCE](../2026-01/2026-01-29-openclaw-control-ui-websocket.md)<br>  <sub>OpenClaw Control UI WebSocket hijack RCE</sub>

---

[← 2026-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-02/2026-02-10-openclaw-kong-zhi-mian-ban.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
