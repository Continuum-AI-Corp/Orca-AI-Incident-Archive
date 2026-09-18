---
id: 2025-08-05-cursor-mcpoison
title: "Cursor MCPoison (CVE-2025-54136)"
title_zh: "Cursor MCPoison（CVE-2025-54136）"
title_ja: "Cursor MCPoison（CVE-2025-54136）"
title_ko: "Cursor MCPoison (CVE-2025-54136)"
title_de: "Cursor MCPoison (CVE-2025-54136)"
title_fr: "Cursor MCPoison (CVE-2025-54136)"
title_es: "Cursor MCPoison (CVE-2025-54136)"
date: 2025-08-05
date_precision: day
date_raw: "2025-08-05"

kind: vulnerability
type: [MCP]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Disclosed by Check Point Research, CVSS 8.8. Once a developer approves a harmless MCP config, the attacker can **silently swap in malicious commands without triggering re-approval** — an "approval means permanent trust" design flaw


summary_zh: |
  Check Point Research 披露，CVSS 8.8。开发者一旦批准了一个无害的 MCP 配置，攻击者可**静默替换为恶意命令而不触发重新批准** —— 「批准即永久信任」的设计缺陷

summary_ja: |
  Check Point Researchが公表、CVSS 8.8。開発者が無害なMCP設定を一度承認すると、攻撃者は**再承認をトリガーせずに悪意あるコマンドへ静かに差し替えられる**——「承認は恒久的な信頼を意味する」という設計上の欠陥

summary_ko: |
  Check Point Research가 공개했으며 CVSS 8.8. 개발자가 무해한 MCP 설정을 한 번 승인하면 **재승인 없이 악성 명령으로 조용히 바꿔치기**할 수 있다 — "승인은 영구 신뢰"라는 설계 결함이다

summary_de: |
  Offengelegt von Check Point Research, CVSS 8.8. Sobald ein Entwickler eine harmlose MCP-Konfiguration genehmigt hat, kann der Angreifer **still bösartige Befehle austauschen, ohne eine erneute Genehmigung auszulösen** — ein Designfehler nach dem Motto „Genehmigung bedeutet dauerhaftes Vertrauen“

summary_fr: |
  Divulguée par Check Point Research, CVSS 8.8. Une fois qu'un développeur approuve une configuration MCP inoffensive, l'attaquant peut **substituer silencieusement des commandes malveillantes sans déclencher de nouvelle approbation** — une faille de conception « approuver vaut confiance permanente »

summary_es: |
  Divulgado por Check Point Research, CVSS 8.8. Una vez que un desarrollador aprueba una configuración MCP inofensiva, el atacante puede **sustituirla silenciosamente por comandos maliciosos sin reactivar la aprobación** — un fallo de diseño de "aprobar significa confiar para siempre"

sources:
  - url: https://www.tenable.com/blog/faq-cve-2025-54135-cve-2025-54136-vulnerabilities-in-cursor-curxecute-mcpoison
    label: Tenable FAQ
  - url: https://www.darkreading.com/vulnerabilities-threats/rce-flaw-ai-coding-tool-supply-chain-risk
    label: Dark Reading

disputed: false
landmark: false
scan_month: 2025-08
scan_ref: "SCAN.md §5 2025-08"
---

# Cursor MCPoison (CVE-2025-54136)

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square)

## Summary

Disclosed by Check Point Research, CVSS 8.8. Once a developer approves a harmless MCP config, the attacker can **silently swap in malicious commands without triggering re-approval** — an "approval means permanent trust" design flaw

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
| 1 | Tenable FAQ | <https://www.tenable.com/blog/faq-cve-2025-54135-cve-2025-54136-vulnerabilities-in-cursor-curxecute-mcpoison> |
| 2 | Dark Reading | <https://www.darkreading.com/vulnerabilities-threats/rce-flaw-ai-coding-tool-supply-chain-risk> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-08-05` (raw: 2025-08-05, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-08-05-cursor-mcpoison` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-07-06` [Supabase MCP prompt injection dumps a private table](../2025-07/2025-07-06-supabase-mcp-ti-shi-zhu.md)<br>  <sub>Supabase MCP prompt injection dumps a private table</sub>
- `2025-09-03` [Claude Code MCP auto-enable bypass](../2025-09/2025-09-03-claude-code-mcp.md)<br>  <sub>Claude Code MCP auto-enable bypass</sub>
- `2025-09-25` [postmark-mcp malicious npm package](../2025-09/2025-09-25-postmark-mcp-npm.md)<br>  <sub>postmark-mcp malicious npm package</sub>
- `2025-07-01` [Anthropic Filesystem MCP sandbox escape](../2025-07/2025-07-01-anthropic-filesystem-mcp.md)<br>  <sub>Anthropic Filesystem MCP sandbox escape</sub>

---

[← 2025-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-08/2025-08-05-cursor-mcpoison.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
