---
id: 2026-03-10-azure-mcp-server-ssrf
title: "Azure MCP Server SSRF privilege escalation (CVE-2026-26118)"
title_zh: "Azure MCP Server SSRF 提权（CVE-2026-26118）"
title_ja: "Azure MCP ServerのSSRF権限昇格（CVE-2026-26118）"
title_ko: "Azure MCP Server SSRF 권한 상승 (CVE-2026-26118)"
title_de: "Azure MCP Server: SSRF-Rechteerweiterung (CVE-2026-26118)"
title_fr: "Élévation de privilèges par SSRF dans Azure MCP Server (CVE-2026-26118)"
title_es: "Escalada de privilegios por SSRF en Azure MCP Server (CVE-2026-26118)"
date: 2026-03-10
date_precision: day
date_raw: "2026-03-10"

kind: vulnerability
type: [MCP]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **CVSS 8.8**. Submit a **malicious URL in place of a normal Azure resource identifier** to an Azure MCP Server tool that accepts user parameters, and the MCP Server makes an outbound request to that URL, **possibly carrying its own managed identity token along with it** — a low-privilege attacker can thus capture that token and escalate privileges without administrator rights


summary_zh: |
  **CVSS 8.8**。向接受用户参数的 Azure MCP Server 工具提交一个**恶意 URL 顶替正常的 Azure 资源标识符**，MCP Server 就会向该 URL 发出站请求，**并可能把自己的托管身份令牌一起带上** —— 低权限攻击者由此在无需管理员权限的情况下捕获该令牌并提权

summary_ja: |
  **CVSS 8.8**。ユーザーパラメータを受け付けるAzure MCP Serverのツールに、**通常のAzureリソース識別子の代わりに悪意あるURLを**投入すると、MCP ServerがそのURLへ外向きリクエストを行い、**自身のマネージドIDトークンも一緒に持ち出される可能性がある**——低権限の攻撃者がこのトークンを奪取し、管理者権限なしで権限昇格できる

summary_ko: |
  **CVSS 8.8**. 사용자 매개변수를 받는 Azure MCP Server 도구에 **정상적인 Azure 리소스 식별자 대신 악성 URL**을 전달하면, MCP Server가 그 URL로 외부 요청을 보내며 **자신의 관리 ID 토큰까지 함께 실어 보낼 수 있다** — 낮은 권한의 공격자가 그 토큰을 가로채 관리자 권한 없이 권한을 상승시킬 수 있다

summary_de: |
  **CVSS 8.8**. Übergibt man an ein Tool des Azure MCP Server, das Nutzerparameter akzeptiert, **eine bösartige URL anstelle einer normalen Azure-Ressourcenkennung**, sendet der MCP Server eine ausgehende Anfrage an diese URL und **führt dabei möglicherweise sein eigenes Managed-Identity-Token mit** — ein Angreifer mit geringen Rechten kann dieses Token so abfangen und ohne Administratorrechte Rechte erweitern

summary_fr: |
  **CVSS 8.8**. Il suffit de soumettre une **URL malveillante à la place d'un identifiant de ressource Azure normal** à un outil Azure MCP Server acceptant des paramètres utilisateur pour que le MCP Server effectue une requête sortante vers cette URL, **en emportant possiblement son propre jeton d'identité managée** — un attaquant à faibles privilèges peut ainsi capturer ce jeton et élever ses privilèges sans droits d'administrateur

summary_es: |
  **CVSS 8.8**. Envía una **URL maliciosa en lugar de un identificador normal de recurso de Azure** a una herramienta del Azure MCP Server que acepta parámetros del usuario, y el MCP Server hace una solicitud saliente a esa URL, **posiblemente llevando consigo su propio token de identidad administrada** — un atacante con pocos privilegios puede así capturar ese token y escalar privilegios sin derechos de administrador

sources:
  - url: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26118
    label: MSRC
  - url: https://nvd.nist.gov/vuln/detail/CVE-2026-26118
    label: NVD

disputed: false
landmark: false
scan_month: 2026-03
scan_ref: "SCAN.md §6 2026-03"
---

# Azure MCP Server SSRF privilege escalation (CVE-2026-26118)

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square)

## Summary

**CVSS 8.8**. Submit a **malicious URL in place of a normal Azure resource identifier** to an Azure MCP Server tool that accepts user parameters, and the MCP Server makes an outbound request to that URL, **possibly carrying its own managed identity token along with it** — a low-privilege attacker can thus capture that token and escalate privileges without administrator rights

## Attack chain

```mermaid
flowchart LR
    E["Malicious MCP server or tool description"]:::entry
    S0["The agent toolchain loads and trusts it"]:::step
    I["Unauthorized tool calls<br/><i>(flaw disclosed, no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | MSRC | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26118> |
| 2 | NVD | <https://nvd.nist.gov/vuln/detail/CVE-2026-26118> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-03-10` (raw: 2026-03-10, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-03-10-azure-mcp-server-ssrf` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-04-16` [MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild](../2026-04/2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br>  <sub>MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild</sub>
- `2026-04-15` [Windsurf zero-click MCP RCE (CVE-2026-30615)](../2026-04/2026-04-15-windsurf-mcp-rce.md)<br>  <sub>Windsurf zero-click MCP RCE (CVE-2026-30615)</sub>
- `2026-05-07` [TrustFall: RCE on a single keypress](../2026-05/2026-05-07-trustfall-rce-yi-ci-hui.md)<br>  <sub>TrustFall: RCE on a single keypress</sub>
- `2026-06-12` [Agentjacking: one public DSN hijacks AI coding agents](../2026-06/2026-06-12-agentjacking-public-dsn.md)<br>  <sub>Agentjacking: one public DSN hijacks AI coding agents</sub>

---

[← 2026-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-03/2026-03-10-azure-mcp-server-ssrf.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
