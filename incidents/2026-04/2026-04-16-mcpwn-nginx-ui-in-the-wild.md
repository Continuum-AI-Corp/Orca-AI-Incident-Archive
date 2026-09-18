---
id: 2026-04-16-mcpwn-nginx-ui-in-the-wild
title: "MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild"
title_zh: "MCPwn（CVE-2026-33032）：nginx-ui 的 MCP 端点在野被打"
title_ja: "MCPwn（CVE-2026-33032）：nginx-uiのMCPエンドポイントが実悪用される"
title_ko: "MCPwn (CVE-2026-33032): nginx-ui MCP 엔드포인트 실제 공격"
title_de: "MCPwn (CVE-2026-33032): nginx-ui-MCP-Endpunkt in freier Wildbahn angegriffen"
title_fr: "MCPwn (CVE-2026-33032) : le point de terminaison MCP de nginx-ui frappé en conditions réelles"
title_es: "MCPwn (CVE-2026-33032): el endpoint MCP de nginx-ui golpeado en entornos reales"
date: 2026-04-16
date_precision: day
date_raw: "2026-04-16"

kind: incident
type: [MCP, INFRA]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **CVSS 9.8, exploited in the wild**, named by Pluto Security. The root cause is strikingly plain: nginx-ui's MCP integration exposes two endpoints; `/mcp` gets both an IP allowlist and authentication enforced by middleware, while **`/mcp_message` applies only the IP allowlist — and that allowlist is empty by default, so the middleware let every connection through**. An unauthenticated remote attacker can thus take full control of the managed Nginx server. About **2,600–2,700** instances are reachable from the cloud, and a PoC was published after disclosure


summary_zh: |
  **CVSS 9.8，在野利用**，由 Pluto Security 命名。根因极其朴素：nginx-ui 的 MCP 集成暴露两个端点，`/mcp` 同时经中间件强制 IP 白名单 + 认证，而 **`/mcp_message` 只应用 IP 白名单 —— 而该白名单默认为空，于是中间件放行了所有连接**。未认证远程攻击者由此完全接管被管理的 Nginx 服务器。云上可达实例约 **2,600–2,700 台**，PoC 在披露后公开

summary_ja: |
  **CVSS 9.8、実悪用あり**。Pluto Securityが命名。根本原因は驚くほど単純：nginx-uiのMCP連携は2つのエンドポイントを公開しており、`/mcp`にはIP許可リストと認証がミドルウェアで適用される一方、**`/mcp_message`にはIP許可リストしか適用されない——しかもその許可リストはデフォルトで空のため、ミドルウェアはすべての接続を通してしまった**。これにより未認証のリモート攻撃者が管理下のNginxサーバーを完全に制御できる。約**2,600〜2,700**のインスタンスがクラウドから到達可能で、公表後にPoCが公開された

summary_ko: |
  **CVSS 9.8, 실제 악용 중**이며 Pluto Security가 명명했다. 근본 원인은 놀랄 만큼 단순하다: nginx-ui의 MCP 통합은 두 개의 엔드포인트를 노출하는데, `/mcp`에는 IP 허용 목록과 미들웨어 인증이 모두 적용되지만 **`/mcp_message`에는 IP 허용 목록만 적용되고 그 목록이 기본값으로 비어 있어 미들웨어가 모든 연결을 통과시켰다**. 따라서 무인증 원격 공격자가 관리 대상 Nginx 서버를 완전히 장악할 수 있다. 클라우드에서 접근 가능한 인스턴스는 약 **2,600~2,700개**이며, 공개 후 PoC가 게시되었다

summary_de: |
  **CVSS 9.8, in freier Wildbahn ausgenutzt**, benannt von Pluto Security. Die Ursache ist verblüffend simpel: Die MCP-Integration von nginx-ui stellt zwei Endpunkte bereit; `/mcp` erhält sowohl eine IP-Positivliste als auch eine per Middleware erzwungene Authentifizierung, während **`/mcp_message` nur die IP-Positivliste anwendet — und diese Positivliste ist standardmäßig leer, sodass die Middleware jede Verbindung durchließ**. Ein nicht authentifizierter Angreifer aus der Ferne kann so die vollständige Kontrolle über den verwalteten Nginx-Server übernehmen. Etwa **2,600–2,700** Instanzen sind aus der Cloud erreichbar, und nach der Offenlegung wurde ein PoC veröffentlicht

summary_fr: |
  **CVSS 9.8, exploité en conditions réelles**, nommé par Pluto Security. La cause racine est d'une simplicité frappante : l'intégration MCP de nginx-ui expose deux points de terminaison ; `/mcp` bénéficie à la fois d'une liste d'IP autorisées et d'une authentification imposée par un middleware, tandis que **`/mcp_message` n'applique que la liste d'IP autorisées — et cette liste est vide par défaut, si bien que le middleware laissait passer toutes les connexions**. Un attaquant distant non authentifié peut ainsi prendre le contrôle total du serveur Nginx géré. Environ **2 600 à 2 700** instances sont joignables depuis le cloud, et un PoC a été publié après la divulgation

summary_es: |
  **CVSS 9.8, explotado en entornos reales**, nombrado por Pluto Security. La causa raíz es llamativamente simple: la integración MCP de nginx-ui expone dos endpoints; `/mcp` recibe tanto una lista de IP permitidas como autenticación aplicada por middleware, mientras que **`/mcp_message` solo aplica la lista de IP permitidas — y esa lista está vacía por defecto, así que el middleware dejó pasar todas las conexiones**. Un atacante remoto sin autenticación puede así tomar el control total del servidor Nginx gestionado. Unas **2,600–2,700** instancias son alcanzables desde la nube, y se publicó un PoC tras la divulgación

sources:
  - url: https://thehackernews.com/2026/04/critical-nginx-ui-vulnerability-cve.html
    label: THN
  - url: https://www.esentire.com/security-advisories/nginx-ui-authentication-bypass-vulnerability-cve-2026-33032-exploited
    label: eSentire
  - url: https://www.picussecurity.com/resource/blog/cve-2026-33032-mcpwn-how-a-missing-middleware-call-in-nginx-ui-hands-attackers-full-web-server-takeover
    label: Picus

disputed: false
landmark: true
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

**CVSS 9.8, exploited in the wild**, named by Pluto Security. The root cause is strikingly plain: nginx-ui's MCP integration exposes two endpoints; `/mcp` gets both an IP allowlist and authentication enforced by middleware, while **`/mcp_message` applies only the IP allowlist — and that allowlist is empty by default, so the middleware let every connection through**. An unauthenticated remote attacker can thus take full control of the managed Nginx server. About **2,600–2,700** instances are reachable from the cloud, and a PoC was published after disclosure

## Attack chain

```mermaid
flowchart LR
    E["Malicious MCP server or tool description"]:::entry
    S0["The agent toolchain loads and trusts it"]:::step
    S1["Unauthenticated access"]:::step
    I["RCE / data leak"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | THN | <https://thehackernews.com/2026/04/critical-nginx-ui-vulnerability-cve.html> |
| 2 | eSentire | <https://www.esentire.com/security-advisories/nginx-ui-authentication-bypass-vulnerability-cve-2026-33032-exploited> |
| 3 | Picus | <https://www.picussecurity.com/resource/blog/cve-2026-33032-mcpwn-how-a-missing-middleware-call-in-nginx-ui-hands-attackers-full-web-server-takeover> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-04-16` (raw: 2026-04-16, precision `day`) |
| Kind | Incident `incident` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain · [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-04-16-mcpwn-nginx-ui-in-the-wild` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md) · [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-04-07` [Flowise CVE-2025-59528 exploited in the wild](2026-04-07-flowise-ye-li-yong.md)<br>  <sub>Flowise CVE-2025-59528 exploited in the wild</sub>
- `2026-04-15` [Windsurf zero-click MCP RCE (CVE-2026-30615)](2026-04-15-windsurf-mcp-rce.md)<br>  <sub>Windsurf zero-click MCP RCE (CVE-2026-30615)</sub>
- `2026-04-23` [OpenClaw "Claw Chain": four chained flaws, 245,000 servers exposed](2026-04-23-openclaw-claw-chain.md)<br>  <sub>OpenClaw "Claw Chain": four chained flaws, 245,000 servers exposed</sub>
- `2026-04-01` [Google Vertex AI "Double Agent" permission abuse](2026-04-01-google-vertex-double-agent.md)<br>  <sub>Google Vertex AI "Double Agent" permission abuse</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-16-mcpwn-nginx-ui-in-the-wild.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
