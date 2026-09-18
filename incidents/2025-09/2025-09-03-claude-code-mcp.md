---
id: 2025-09-03-claude-code-mcp
title: "Claude Code MCP auto-enable bypass"
title_zh: "Claude Code MCP 自动启用绕过"
title_ja: "Claude Code MCPの自動有効化バイパス"
title_ko: "Claude Code MCP 자동 활성화 우회"
title_de: "Claude Code: Umgehung der MCP-Autoaktivierung"
title_fr: "Contournement de l'activation automatique MCP dans Claude Code"
title_es: "Omisión de la activación automática de MCP en Claude Code"
date: 2025-09-03
date_precision: day
date_raw: "2025-09-03"

kind: vulnerability
type: [MCP]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  CVE-2025-59536 (published 2025-10-03): a project-level `.mcp.json` setting `enableAllProjectMcpServers: true` silently activates attacker endpoints; fixed 09-22


summary_zh: |
  CVE-2025-59536（2025-10-03 公开），项目级 `.mcp.json` 设 `enableAllProjectMcpServers: true` 静默激活攻击者端点；09-22 修复

summary_ja: |
  CVE-2025-59536（2025-10-03公開）：プロジェクト直下の`.mcp.json`に`enableAllProjectMcpServers: true`を設定すると、攻撃者のエンドポイントが静かに有効化される。09-22に修正

summary_ko: |
  CVE-2025-59536(2025-10-03 공개): 프로젝트 수준 `.mcp.json`에서 `enableAllProjectMcpServers: true`를 설정하면 공격자 엔드포인트가 조용히 활성화된다. 09-22 수정

summary_de: |
  CVE-2025-59536 (veröffentlicht 2025-10-03): Eine projektweite `.mcp.json` mit `enableAllProjectMcpServers: true` aktiviert still Endpunkte des Angreifers; behoben am 09-22

summary_fr: |
  CVE-2025-59536 (publié le 2025-10-03) : un fichier projet `.mcp.json` avec `enableAllProjectMcpServers: true` active silencieusement des points de terminaison d'attaquant ; corrigé le 09-22

summary_es: |
  CVE-2025-59536 (publicado el 2025-10-03): un `.mcp.json` a nivel de proyecto que define `enableAllProjectMcpServers: true` activa silenciosamente endpoints del atacante; corregido el 09-22

sources:
  - url: https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/
    label: Check Point

disputed: false
landmark: false
scan_month: 2025-09
scan_ref: "SCAN.md §5 2025-09"
---

# Claude Code MCP auto-enable bypass

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square)

## Summary

CVE-2025-59536 (published 2025-10-03): a project-level `.mcp.json` setting `enableAllProjectMcpServers: true` silently activates attacker endpoints; fixed 09-22

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
| 1 | Check Point | <https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-09-03` (raw: 2025-09-03, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-09-03-claude-code-mcp` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-09-25` [postmark-mcp malicious npm package](2025-09-25-postmark-mcp-npm.md)<br>  <sub>postmark-mcp malicious npm package</sub>
- `2025-08-05` [Cursor MCPoison (CVE-2025-54136)](../2025-08/2025-08-05-cursor-mcpoison.md)<br>  <sub>Cursor MCPoison (CVE-2025-54136)</sub>
- `2025-10-22` [Shadow Escape: first zero-click agent attack over MCP](../2025-10/2025-10-22-shadow-escape-mcp-agent.md)<br>  <sub>Shadow Escape: first zero-click agent attack over MCP</sub>
- `2025-10-01` [Framelink Figma MCP RCE](../2025-10/2025-10-01-framelink-figma-mcp-rce.md)<br>  <sub>Framelink Figma MCP RCE</sub>

---

[← 2025-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-09/2025-09-03-claude-code-mcp.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
