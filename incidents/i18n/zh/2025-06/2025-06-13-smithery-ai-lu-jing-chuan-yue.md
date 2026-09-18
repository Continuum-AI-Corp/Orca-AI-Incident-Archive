---
id: 2025-06-13-smithery-ai-lu-jing-chuan-yue
lang: zh
source: incidents/2025-06/2025-06-13-smithery-ai-lu-jing-chuan-yue.md
title: "Smithery.ai 路径穿越"
summary: |
  MCP 托管平台泄露 Fly.io token，威胁数千下游 server
---

# Smithery.ai 路径穿越

<sub>Smithery.ai path traversal</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## 概要

MCP 托管平台泄露 Fly.io token，威胁数千下游 server

## 攻击链

```mermaid
flowchart LR
    E["恶意 MCP 服务器或工具描述"]:::entry
    S0["agent 工具链加载并信任"]:::step
    S1["agent 取用并调用"]:::step
    I["凭据被滥用<br/><i>（漏洞已披露 · 未见在野利用）</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | 安全内参 2025 盘点 | <https://www.secrss.com/articles/86614> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-06-13`（原文：2025-06-13，精度 `day`） |
| 性质 | 漏洞披露 `vulnerability` |
| 类型 | [`MCP`](../../../../taxonomy/types.md#mcp) MCP / 工具链 · [`CRED`](../../../../taxonomy/types.md#cred) 凭据滥用 |
| 严重度 | **中** `medium` |
| 可信度 | **B** — 研究机构或主流媒体，有可核查细节 |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-06-13-smithery-ai-lu-jing-chuan-yue` |

<sub>**判定依据**：漏洞披露，截至归档未见在野利用证据，故 `real_harm: false`。 判 `medium`：受控演示、中等缺陷，或单用户 / 单机范围的事故。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 供应链投毒](../../../../topics/agent-supply-chain.md)

**同类条目**：

- `2025-06-13` [MCP Inspector 未认证 RCE](../../../2025-06/2025-06-13-mcp-inspector-rce.md)<br>  <sub>MCP Inspector unauthenticated RCE</sub>
- `2025-06-30` [McDonald's McHire「Olivia」招聘机器人](../../../2025-06/2025-06-30-mcdonald-mchire-olivia.md)<br>  <sub>McDonald's McHire "Olivia" hiring bot</sub>
- `2025-06-04` [Asana MCP server 跨租户数据暴露](../../../2025-06/2025-06-04-asana-mcp-server.md)<br>  <sub>Asana MCP server cross-tenant data exposure</sub>
- `2025-07-06` [Supabase MCP 提示注入泄库](../../../2025-07/2025-07-06-supabase-mcp-ti-shi-zhu.md)<br>  <sub>Supabase MCP prompt injection dumps a private table</sub>

---

[← English original](../../../2025-06/2025-06-13-smithery-ai-lu-jing-chuan-yue.md) · [2025-06 index](../../../2025-06/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
