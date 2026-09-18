---
id: 2025-04-01-gpt-mcp-jing-gong-ju
lang: zh
source: incidents/2025-04/2025-04-01-gpt-mcp-jing-gong-ju.md
title: "GPT-4.1 经 MCP 工具投毒被越狱"
summary: |
  研究者用被投毒的 MCP 工具描述越狱 GPT-4.1，使其在用户无感知的情况下访问并外带未授权数据。
---

# GPT-4.1 经 MCP 工具投毒被越狱

<sub>GPT-4.1 jailbroken through a poisoned MCP tool</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square)

## 概要

研究者用被投毒的 MCP 工具描述越狱 GPT-4.1，使其在用户无感知的情况下访问并外带未授权数据。

## 攻击链

```mermaid
flowchart LR
    E["恶意 MCP 服务器或工具描述"]:::entry
    S0["agent 工具链加载并信任"]:::step
    I["未授权工具调用<br/><i>（实验室演示 · 无真实受害方）</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | OWASP Q2'25 | <https://genai.owasp.org/2025/07/14/owasp-gen-ai-incident-exploit-round-up-q225/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-04-01`（原文：2025-04，精度 `month`） |
| 性质 | 研究演示 `research` |
| 类型 | [`MCP`](../../../../taxonomy/types.md#mcp) MCP / 工具链 |
| 严重度 | **中** `medium` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-04-01-gpt-mcp-jing-gong-ju` |

<sub>**判定依据**：研究机构或厂商的受控演示，`real_harm: false`；收录是为了标记攻击面何时被公开。 判 `medium`：受控演示、中等缺陷，或单用户 / 单机范围的事故。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 供应链投毒](../../../../topics/agent-supply-chain.md)

**同类条目**：

- `2025-04-01` [MCP 工具投毒攻击（TPA）首次系统披露](../../../2025-04/2025-04-01-mcp-tpa-gong-ju-tou.md)<br>  <sub>First systematic disclosure of MCP tool-poisoning attacks</sub>
- `2025-05-26` [GitHub MCP "Toxic Agent Flow"](../../../2025-05/2025-05-26-github-mcp-toxic-agent.md)<br>  <sub>GitHub MCP "toxic agent flow"</sub>
- `2025-06-13` [MCP Inspector 未认证 RCE](../../../2025-06/2025-06-13-mcp-inspector-rce.md)<br>  <sub>MCP Inspector unauthenticated RCE</sub>
- `2025-06-04` [Asana MCP server 跨租户数据暴露](../../../2025-06/2025-06-04-asana-mcp-server.md)<br>  <sub>Asana MCP server cross-tenant data exposure</sub>

---

[← English original](../../../2025-04/2025-04-01-gpt-mcp-jing-gong-ju.md) · [2025-04 index](../../../2025-04/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
