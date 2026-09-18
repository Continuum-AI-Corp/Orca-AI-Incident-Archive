---
id: 2025-06-13-mcp-inspector-rce
title: "MCP Inspector unauthenticated RCE"
title_zh: "MCP Inspector 未认证 RCE"
title_ja: "MCP Inspectorの認証不要RCE"
title_ko: "MCP Inspector 무인증 RCE"
title_de: "MCP Inspector: nicht authentifizierte RCE"
title_fr: "RCE non authentifiée dans MCP Inspector"
title_es: "RCE sin autenticación en MCP Inspector"
date: 2025-06-13
date_precision: day
date_raw: "2025-06-13"

kind: vulnerability
type: [MCP]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Oligo Security found CVE-2025-49596, **CVSS 9.4**. Chained with the browser "0.0.0.0 Day" + CSRF — **simply visiting a malicious website could execute arbitrary code on a developer's machine**. Anthropic fixed it in v0.14.1 (2025-06-13): the proxy server now requires a session token and validates Host/Origin


summary_zh: |
  Oligo Security 发现 CVE-2025-49596，**CVSS 9.4**。与浏览器 "0.0.0.0 Day" + CSRF 链式利用 —— **访问一个恶意网站即可在开发者机器上执行任意代码**。Anthropic 于 v0.14.1（2025-06-13）修复：代理服务器要求会话令牌、校验 Host/Origin

summary_ja: |
  Oligo SecurityがCVE-2025-49596を発見、**CVSS 9.4**。ブラウザの「0.0.0.0 Day」＋CSRFと組み合わせると、**悪意あるWebサイトを訪れるだけで開発者のマシン上で任意コードが実行可能**。Anthropicはv0.14.1（2025-06-13）で修正：プロキシサーバーがセッショントークンを要求し、Host/Originを検証するようになった

summary_ko: |
  Oligo Security는 CVE-2025-49596(**CVSS 9.4**)을 발견했다. 브라우저 "0.0.0.0 Day" + CSRF와 연계되어 **악성 웹사이트를 방문하기만 해도 개발자 머신에서 임의 코드를 실행할 수 있었다**. Anthropic은 v0.14.1(2025-06-13)에서 수정했으며, 이제 프록시 서버는 세션 토큰을 요구하고 Host/Origin을 검증한다

summary_de: |
  Oligo Security fand CVE-2025-49596, **CVSS 9.4**. Verkettet mit dem Browser-„0.0.0.0 Day“ + CSRF — **der bloße Besuch einer bösartigen Website konnte beliebigen Code auf dem Rechner eines Entwicklers ausführen**. Anthropic behob es in v0.14.1 (2025-06-13): Der Proxy-Server verlangt nun ein Session-Token und validiert Host/Origin

summary_fr: |
  Oligo Security a trouvé CVE-2025-49596, **CVSS 9.4**. Enchaînée avec le « 0.0.0.0 Day » des navigateurs + CSRF — **une simple visite sur un site malveillant pouvait exécuter du code arbitraire sur la machine d'un développeur**. Anthropic l'a corrigé en v0.14.1 (2025-06-13) : le serveur proxy exige désormais un jeton de session et valide Host/Origin

summary_es: |
  Oligo Security encontró CVE-2025-49596, **CVSS 9.4**. Encadenado con el "0.0.0.0 Day" del navegador + CSRF — **bastaba con visitar un sitio web malicioso para ejecutar código arbitrario en la máquina de un desarrollador**. Anthropic lo corrigió en la v0.14.1 (2025-06-13): el servidor proxy ahora requiere un token de sesión y valida Host/Origin

sources:
  - url: https://www.oligo.security/blog/critical-rce-vulnerability-in-anthropic-mcp-inspector-cve-2025-49596
    label: Oligo
  - url: https://github.com/advisories/GHSA-7f8r-222p-6f5g
    label: GHSA

disputed: false
landmark: false
scan_month: 2025-06
scan_ref: "SCAN.md §5 2025-06"
---

# MCP Inspector unauthenticated RCE

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square)

## Summary

Oligo Security found CVE-2025-49596, **CVSS 9.4**. Chained with the browser "0.0.0.0 Day" + CSRF — **simply visiting a malicious website could execute arbitrary code on a developer's machine**. Anthropic fixed it in v0.14.1 (2025-06-13): the proxy server now requires a session token and validates Host/Origin

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
| 1 | Oligo | <https://www.oligo.security/blog/critical-rce-vulnerability-in-anthropic-mcp-inspector-cve-2025-49596> |
| 2 | GHSA | <https://github.com/advisories/GHSA-7f8r-222p-6f5g> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-06-13` (raw: 2025-06-13, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-06-13-mcp-inspector-rce` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-06-04` [Asana MCP server cross-tenant data exposure](2025-06-04-asana-mcp-server.md)<br>  <sub>Asana MCP server cross-tenant data exposure</sub>
- `2025-06-13` [Smithery.ai path traversal](2025-06-13-smithery-ai-lu-jing-chuan-yue.md)<br>  <sub>Smithery.ai path traversal</sub>
- `2025-07-06` [Supabase MCP prompt injection dumps a private table](../2025-07/2025-07-06-supabase-mcp-ti-shi-zhu.md)<br>  <sub>Supabase MCP prompt injection dumps a private table</sub>
- `2025-05-26` [GitHub MCP "toxic agent flow"](../2025-05/2025-05-26-github-mcp-toxic-agent.md)<br>  <sub>GitHub MCP "toxic agent flow"</sub>

---

[← 2025-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-06/2025-06-13-mcp-inspector-rce.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
