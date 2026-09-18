---
id: 2025-05-26-github-mcp-toxic-agent
title: "GitHub MCP \"toxic agent flow\""
title_zh: "GitHub MCP \"Toxic Agent Flow\""
title_ja: "GitHub MCPの「toxic agent flow」"
title_ko: "GitHub MCP \"독성 에이전트 흐름\""
title_de: "GitHub MCP „Toxic Agent Flow“"
title_fr: "« Toxic agent flow » du MCP de GitHub"
title_es: "\"Toxic agent flow\" en GitHub MCP"
date: 2025-05-26
date_precision: day
date_raw: "2025-05-26"

kind: research
type: [MCP, EXFIL]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Invariant Labs: instructions planted in a public issue made the agent write **private repository source code** into a public PR


summary_zh: |
  Invariant Labs：在公开 issue 里埋指令，agent 读取后把**私有仓库源码**写进公开 PR

summary_ja: |
  Invariant Labs：公開イシューに仕込まれた指示により、エージェントが**非公開リポジトリのソースコード**を公開PRに書き出した

summary_ko: |
  Invariant Labs: 공개 이슈에 심어둔 지시로 에이전트가 **비공개 저장소 소스 코드**를 공개 PR에 작성하게 만들었다

summary_de: |
  Invariant Labs: In einem öffentlichen Issue platzierte Anweisungen brachten den Agenten dazu, **Quellcode aus privaten Repositories** in einen öffentlichen PR zu schreiben

summary_fr: |
  Invariant Labs : des instructions plantées dans une issue publique ont poussé l'agent à écrire du **code source d'un dépôt privé** dans une PR publique

summary_es: |
  Invariant Labs: instrucciones plantadas en un issue público hicieron que el agente escribiera **código fuente de un repositorio privado** en un PR público

sources:
  - url: https://github.com/invariantlabs-ai/mcp-injection-experiments
    label: Reproduction code

disputed: false
landmark: true
scan_month: 2025-05
scan_ref: "SCAN.md §5 2025-05"
---

# GitHub MCP "toxic agent flow"

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

Invariant Labs: instructions planted in a public issue made the agent write **private repository source code** into a public PR

## Attack chain

```mermaid
flowchart LR
    E["Malicious MCP server or tool description"]:::entry
    S0["The agent toolchain loads and trusts it"]:::step
    S1["Exfiltration via the vendor's trusted domain<br/>image rendering · API · proxy"]:::step
    I["Data ends up with the attacker<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Reproduction code | <https://github.com/invariantlabs-ai/mcp-injection-experiments> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-05-26` (raw: 2025-05-26, precision `day`) |
| Kind | Research demo `research` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-05-26-github-mcp-toxic-agent` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md) · [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2025-05-01` [GitLab Duo remote prompt injection](2025-05-01-gitlab-duo-yuan-cheng-ti.md)<br>  <sub>GitLab Duo remote prompt injection</sub>
- `2025-06-11` [EchoLeak (CVE-2025-32711)](../2025-06/2025-06-11-echoleak.md)<br>  <sub>EchoLeak (CVE-2025-32711)</sub>
- `2025-06-13` [MCP Inspector unauthenticated RCE](../2025-06/2025-06-13-mcp-inspector-rce.md)<br>  <sub>MCP Inspector unauthenticated RCE</sub>
- `2025-04-01` [First systematic disclosure of MCP tool-poisoning attacks](../2025-04/2025-04-01-mcp-tpa-gong-ju-tou.md)<br>  <sub>First systematic disclosure of MCP tool-poisoning attacks</sub>

---

[← 2025-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-05/2025-05-26-github-mcp-toxic-agent.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
