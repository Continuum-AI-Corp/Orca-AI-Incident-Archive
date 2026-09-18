---
id: 2026-06-28-langflow-yong-yu-men-luo
title: "Langflow CVE-2026-33017 used for Monero mining"
title_zh: "Langflow CVE-2026-33017 被用于门罗币挖矿"
title_ja: "Langflow CVE-2026-33017がMoneroマイニングに悪用される"
title_ko: "Langflow CVE-2026-33017, 모네로 채굴에 악용"
title_de: "Langflow CVE-2026-33017 für Monero-Mining ausgenutzt"
title_fr: "CVE-2026-33017 de Langflow utilisé pour du minage de Monero"
title_es: "CVE-2026-33017 de Langflow usado para minar Monero"
date: 2026-06-28
date_precision: day
date_raw: "2026-06-28"

kind: vulnerability
type: [INFRA]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Trend Micro: unauthenticated RCE → `isp.sh` → a Go-based `lambsys` (placed at `/var/tmp/.xlamb`) that **walks private keys, known_hosts and ssh-agent keys to spread worm-style**, kills competing miners, disables AppArmor/SELinux/firewalls/the Alibaba Cloud monitoring agent, persists via cron and a resident script, and deploys a modified XMRig. **A single IoC traced 19 days of continuous exploitation**


summary_zh: |
  Trend Micro：未认证 RCE → `isp.sh` → Go 语言 `lambsys`（置于 `/var/tmp/.xlamb`），**遍历私钥、known_hosts、ssh-agent 密钥蠕虫式扩散**，停掉竞争矿工，禁用 AppArmor/SELinux/防火墙/阿里云监控代理，cron + 常驻脚本持久化，部署改版 XMRig。**单个 IoC 追踪到 19 天的持续利用**

summary_ja: |
  Trend Micro：認証不要のRCE → `isp.sh` → Go製の`lambsys`（`/var/tmp/.xlamb`に配置）が、**秘密鍵、known_hosts、ssh-agentの鍵を走査してワーム状に拡散**し、競合するマイナーを停止させ、AppArmor/SELinux/ファイアウォール/Alibaba Cloud監視エージェントを無効化し、cronと常駐スクリプトで永続化し、改造版XMRigを展開する。**単一のIoCから19日間の継続的な悪用が判明した**

summary_ko: |
  Trend Micro: 무인증 RCE → `isp.sh` → Go 기반 `lambsys`(`/var/tmp/.xlamb`에 배치)가 **개인 키, known_hosts, ssh-agent 키를 훑어 웜처럼 확산**하고, 경쟁 채굴기를 종료하며 AppArmor/SELinux/방화벽/알리바바 클라우드 모니터링 에이전트를 비활성화하고 cron과 상주 스크립트로 지속되며 수정된 XMRig를 배포한다. **IoC 하나로 19일간의 연속 악용이 추적되었다**

summary_de: |
  Trend Micro: nicht authentifizierte RCE → `isp.sh` → ein Go-basiertes `lambsys` (platziert unter `/var/tmp/.xlamb`), das **private Schlüssel, known_hosts und ssh-agent-Schlüssel durchgeht, um sich wurmartig zu verbreiten**, konkurrierende Miner beendet, AppArmor/SELinux/Firewalls und den Monitoring-Agenten von Alibaba Cloud deaktiviert, sich über cron und ein residentes Skript persistiert und eine modifizierte XMRig einsetzt. **Ein einziger IoC führte zu 19 Tagen kontinuierlicher Ausnutzung**

summary_fr: |
  Trend Micro : RCE non authentifiée → `isp.sh` → un `lambsys` en Go (placé à `/var/tmp/.xlamb`) qui **parcourt les clés privées, known_hosts et clés ssh-agent pour se propager façon ver**, tue les mineurs concurrents, désactive AppArmor/SELinux/pare-feux/l'agent de surveillance Alibaba Cloud, persiste via cron et un script résident, et déploie un XMRig modifié. **Un seul IoC a permis de tracer 19 jours d'exploitation continue**

summary_es: |
  Trend Micro: RCE sin autenticación → `isp.sh` → un `lambsys` basado en Go (colocado en `/var/tmp/.xlamb`) que **recorre claves privadas, known_hosts y claves de ssh-agent para propagarse como un gusano**, mata a los mineros competidores, desactiva AppArmor/SELinux/firewalls y el agente de monitoreo de Alibaba Cloud, persiste mediante cron y un script residente, y despliega un XMRig modificado. **Un único IoC permitió rastrear 19 días de explotación continua**

sources:
  - url: https://www.trendmicro.com/en_us/research/26/f/from-langflow-to-monero-inside-cve-2026-33017-cryptominer.html
    label: Trend Micro

disputed: false
landmark: false
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# Langflow CVE-2026-33017 used for Monero mining

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

Trend Micro: unauthenticated RCE → `isp.sh` → a Go-based `lambsys` (placed at `/var/tmp/.xlamb`) that **walks private keys, known_hosts and ssh-agent keys to spread worm-style**, kills competing miners, disables AppArmor/SELinux/firewalls/the Alibaba Cloud monitoring agent, persists via cron and a resident script, and deploys a modified XMRig. **A single IoC traced 19 days of continuous exploitation**

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
| 1 | Trend Micro | <https://www.trendmicro.com/en_us/research/26/f/from-langflow-to-monero-inside-cve-2026-33017-cryptominer.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-28` (raw: 2026-06-28, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-28-langflow-yong-yu-men-luo` |

<sub>**Why this classification:** Vulnerability disclosure; in-the-wild exploitation is confirmed, so `real_harm: true`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-06-08` [LiteLLM CVE-2026-42271 MCP endpoint takeover](2026-06-08-litellm-mcp-duan-dian-jie.md)<br>  <sub>LiteLLM CVE-2026-42271 MCP endpoint takeover</sub>
- `2026-06-29` [DifyTap: four flaws leave 1M+ AI apps open to cross-tenant eavesdropping](2026-06-29-difytap-lou-dong-rang-wan.md)<br>  <sub>DifyTap: four flaws leave 1M+ AI apps open to cross-tenant eavesdropping</sub>
- `2026-06-17` [Vertex AI SDK bucket takeover leads to cross-tenant RCE](2026-06-17-vertex-sdk-rce.md)<br>  <sub>Vertex AI SDK bucket takeover leads to cross-tenant RCE</sub>
- `2026-06-18` [AutoJack: one web page from AutoGen Studio to the host](2026-06-18-autojack-autogen-studio.md)<br>  <sub>AutoJack: one web page from AutoGen Studio to the host</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-28-langflow-yong-yu-men-luo.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
