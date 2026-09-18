---
id: 2025-08-06-agentflayer-black-hat-usa
lang: zh
source: incidents/2025-08/2025-08-06-agentflayer-black-hat-usa.md
title: "AgentFlayer 零点击攻击集（Black Hat USA）"
summary: |
  Zenity Labs（Tamir Ishay Sharbat）一次性打穿 **ChatGPT Connectors、Copilot Studio、Salesforce Einstein、Cursor+Jira、Gemini**。典型手法：共享一个含约 300 词 1px 白字的文档，用户说一句「总结一下」，agent 就去 Google Drive / SharePoint 搜 API key 并经图片渲染 URL 外带到攻击者 Azure Blob
---

# AgentFlayer 零点击攻击集（Black Hat USA）

<sub>AgentFlayer zero-click attack set (Black Hat USA)</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## 概要

Zenity Labs（Tamir Ishay Sharbat）一次性打穿 **ChatGPT Connectors、Copilot Studio、Salesforce Einstein、Cursor+Jira、Gemini**。典型手法：共享一个含约 300 词 1px 白字的文档，用户说一句「总结一下」，agent 就去 Google Drive / SharePoint 搜 API key 并经图片渲染 URL 外带到攻击者 Azure Blob

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
| 1 | Zenity Labs | <https://labs.zenity.io/p/agentflayer-chatgpt-connectors-0click-attack-5b41> |
| 2 | HackRead | <https://hackread.com/agentflayer-0-click-exploit-chatgpt-connectors-steal-data/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-08-06`（原文：2025-08-06，精度 `day`） |
| 性质 | 研究演示 `research` |
| 类型 | [`IPI`](../../../../taxonomy/types.md#ipi) 间接提示注入 · [`EXFIL`](../../../../taxonomy/types.md#exfil) 数据外泄 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-08-06-agentflayer-black-hat-usa` |

<sub>**判定依据**：研究机构或厂商的受控演示，`real_harm: false`；收录是为了标记攻击面何时被公开。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[零点击数据外泄链](../../../../topics/zero-click-exfil.md)

**同类条目**：

- `2025-08-06` [SafeBreach "Invitation Is All You Need"](../../../2025-08/2025-08-06-safebreach-invitation-is-all.md)<br>  <sub>SafeBreach "Invitation Is All You Need"</sub>
- `2025-08-01` ["Man in the Prompt" 浏览器扩展攻击](../../../2025-08/2025-08-01-man-prompt-liu-lan-qi.md)<br>  <sub>"Man in the Prompt" browser-extension attack</sub>
- `2025-09-18` [ShadowLeak](../../../2025-09/2025-09-18-shadowleak.md)<br>  <sub>ShadowLeak</sub>
- `2025-09-19` [Notion 3.0 agent「致命三元组」](../../../2025-09/2025-09-19-notion-agent-zhi-ming-san.md)<br>  <sub>Notion 3.0 agent hits the lethal trifecta</sub>

---

[← English original](../../../2025-08/2025-08-06-agentflayer-black-hat-usa.md) · [2025-08 index](../../../2025-08/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
