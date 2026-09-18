---
id: 2025-12-01-anthropic-git-mcp-server
lang: zh
source: incidents/2025-12/2025-12-01-anthropic-git-mcp-server.md
title: "Anthropic Git MCP Server 三连 CVE"
summary: |
  Anthropic **2025-09 接受报告、2025-12 发布修复、2026-01 公开**。CVE-2025-68143：`git_init` 接受任意文件系统路径且不校验，可把任何目录变成 git 仓库；CVE-2025-68145：`--repository` 限定在后续调用中未被校验，可越界访问系统上任意仓库；CVE-2025-68144：`git_diff` / `git_checkout` 把用户可控参数直接传给 GitPython。与 filesystem MCP server 并用时可执行代码、删除任意文件、把任意文件塞进 LLM 上下文
---

# Anthropic Git MCP Server 三连 CVE

<sub>Three CVEs in Anthropic's Git MCP Server</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square)

> [!WARNING]
> **本条存在争议或未完全证实的事实**，正文中的各方说法并列保留，请勿单独引用其中一方。

## 概要

Anthropic **2025-09 接受报告、2025-12 发布修复、2026-01 公开**。CVE-2025-68143：`git_init` 接受任意文件系统路径且不校验，可把任何目录变成 git 仓库；CVE-2025-68145：`--repository` 限定在后续调用中未被校验，可越界访问系统上任意仓库；CVE-2025-68144：`git_diff` / `git_checkout` 把用户可控参数直接传给 GitPython。与 filesystem MCP server 并用时可执行代码、删除任意文件、把任意文件塞进 LLM 上下文

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
| 1 | The Register | <https://www.theregister.com/security/2026/01/20/anthropic-quietly-fixed-flaws-in-its-git-mcp-server/4676059> |
| 2 | THN | <https://thehackernews.com/2026/01/three-flaws-in-anthropic-mcp-git-server.html> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-12-01`（原文：2025-12 修复 / 2026-01 披露，精度 `month`） |
| 性质 | 漏洞披露 `vulnerability` |
| 类型 | [`MCP`](../../../../taxonomy/types.md#mcp) MCP / 工具链 |
| 严重度 | **中** `medium` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-12-01-anthropic-git-mcp-server` |

<sub>**判定依据**：漏洞披露，截至归档未见在野利用证据，故 `real_harm: false`。 判 `medium`：受控演示、中等缺陷，或单用户 / 单机范围的事故。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 供应链投毒](../../../../topics/agent-supply-chain.md)

**同类条目**：

- `2025-12-06` [IDEsaster](../../../2025-12/2025-12-06-idesaster.md)<br>  <sub>IDEsaster</sub>
- `2025-12-01` [MCP TypeScript SDK DNS 重绑定](../../../2025-12/2025-12-01-mcp-typescript-sdk-dns.md)<br>  <sub>MCP TypeScript SDK DNS rebinding</sub>
- `2025-10-22` [Shadow Escape：首个经 MCP 的零点击 agent 攻击](../../../2025-10/2025-10-22-shadow-escape-mcp-agent.md)<br>  <sub>Shadow Escape: first zero-click agent attack over MCP</sub>
- `2025-10-01` [Framelink Figma MCP RCE](../../../2025-10/2025-10-01-framelink-figma-mcp-rce.md)<br>  <sub>Framelink Figma MCP RCE</sub>

---

[← English original](../../../2025-12/2025-12-01-anthropic-git-mcp-server.md) · [2025-12 index](../../../2025-12/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
