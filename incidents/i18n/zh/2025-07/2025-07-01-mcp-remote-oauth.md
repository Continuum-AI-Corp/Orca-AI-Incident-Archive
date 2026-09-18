---
id: 2025-07-01-mcp-remote-oauth
lang: zh
source: incidents/2025-07/2025-07-01-mcp-remote-oauth.md
title: "mcp-remote OAuth 命令注入"
summary: |
  CVE-2025-6514，恶意 MCP server 可在客户端执行任意命令
---

# mcp-remote OAuth 命令注入

<sub>mcp-remote OAuth command injection</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square)

## 概要

CVE-2025-6514，恶意 MCP server 可在客户端执行任意命令

## 攻击链

```mermaid
flowchart LR
    E["恶意 MCP 服务器或工具描述"]:::entry
    S0["agent 工具链加载并信任"]:::step
    I["未授权工具调用<br/><i>（漏洞已披露 · 未见在野利用）</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | IPA 2025-12 号 | <https://www.ipa.go.jp/digital/ai/security/ai-security-bulletin.html> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-07-01`（原文：2025-07，精度 `month`） |
| 性质 | 漏洞披露 `vulnerability` |
| 类型 | [`MCP`](../../../../taxonomy/types.md#mcp) MCP / 工具链 |
| 严重度 | **中** `medium` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-07-01-mcp-remote-oauth` |

<sub>**判定依据**：漏洞披露，截至归档未见在野利用证据，故 `real_harm: false`。 判 `medium`：受控演示、中等缺陷，或单用户 / 单机范围的事故。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 供应链投毒](../../../../topics/agent-supply-chain.md)

**同类条目**：

- `2025-07-06` [Supabase MCP 提示注入泄库](../../../2025-07/2025-07-06-supabase-mcp-ti-shi-zhu.md)<br>  <sub>Supabase MCP prompt injection dumps a private table</sub>
- `2025-07-01` [Anthropic Filesystem MCP 沙箱逃逸](../../../2025-07/2025-07-01-anthropic-filesystem-mcp.md)<br>  <sub>Anthropic Filesystem MCP sandbox escape</sub>
- `2025-06-13` [MCP Inspector 未认证 RCE](../../../2025-06/2025-06-13-mcp-inspector-rce.md)<br>  <sub>MCP Inspector unauthenticated RCE</sub>
- `2025-08-05` [Cursor MCPoison（CVE-2025-54136）](../../../2025-08/2025-08-05-cursor-mcpoison.md)<br>  <sub>Cursor MCPoison (CVE-2025-54136)</sub>

---

[← English original](../../../2025-07/2025-07-01-mcp-remote-oauth.md) · [2025-07 index](../../../2025-07/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
