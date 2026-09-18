---
id: 2025-10-02-cometjacking
lang: zh
source: incidents/2025-10/2025-10-02-cometjacking.md
title: "CometJacking"
summary: |
  LayerX：URL 的 `collection` 参数即可携带指令，让 Perplexity Comet 去查**记忆和已连接服务**（Gmail、日历）并外带，**无需凭据或用户交互**。2025-08-27/28 报告 Perplexity，初次回应「无安全影响」
---

# CometJacking

<sub>CometJacking</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## 概要

LayerX：URL 的 `collection` 参数即可携带指令，让 Perplexity Comet 去查**记忆和已连接服务**（Gmail、日历）并外带，**无需凭据或用户交互**。2025-08-27/28 报告 Perplexity，初次回应「无安全影响」

## 攻击链

```mermaid
flowchart LR
    E["外部内容<br/>邮件 · 文档 · Issue · 网页"]:::entry
    S0["agent 读取并当作指令执行"]:::step
    S1["经厂商可信域外带<br/>图片渲染 · API · 代理"]:::step
    I["数据落入攻击者手中<br/><i>（实验室演示 · 无真实受害方）</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | PPC Land 汇总 | <https://ppc.land/comet-browser-faces-multiple-security-vulnerabilities-from-prompt-injection/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-10-02`（原文：2025-10-02，精度 `day`） |
| 性质 | 研究演示 `research` |
| 类型 | [`IPI`](../../../../taxonomy/types.md#ipi) 间接提示注入 · [`EXFIL`](../../../../taxonomy/types.md#exfil) 数据外泄 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-10-02-cometjacking` |

<sub>**判定依据**：研究机构或厂商的受控演示，`real_harm: false`；收录是为了标记攻击面何时被公开。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[零点击数据外泄链](../../../../topics/zero-click-exfil.md)

**同类条目**：

- `2025-10-22` [Shadow Escape：首个经 MCP 的零点击 agent 攻击](../../../2025-10/2025-10-22-shadow-escape-mcp-agent.md)<br>  <sub>Shadow Escape: first zero-click agent attack over MCP</sub>
- `2025-10-08` [CamoLeak（GitHub Copilot Chat）](../../../2025-10/2025-10-08-camoleak-github-copilot-chat.md)<br>  <sub>CamoLeak (GitHub Copilot Chat)</sub>
- `2025-10-31` [Agent Session Smuggling：A2A 协议上的 agent 互骗](../../../2025-10/2025-10-31-agent-session-smuggling-a2a.md)<br>  <sub>Agent Session Smuggling: agents deceiving agents over A2A</sub>
- `2025-10-21` [Brave 披露 Comet 截图型注入](../../../2025-10/2025-10-21-brave-comet-pi-lu-jie.md)<br>  <sub>Brave discloses screenshot-based injection in Comet</sub>

---

[← English original](../../../2025-10/2025-10-02-cometjacking.md) · [2025-10 index](../../../2025-10/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
