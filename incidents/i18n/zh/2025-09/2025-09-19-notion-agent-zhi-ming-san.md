---
id: 2025-09-19-notion-agent-zhi-ming-san
lang: zh
source: incidents/2025-09/2025-09-19-notion-agent-zhi-ming-san.md
title: "Notion 3.0 agent「致命三元组」"
summary: |
  CodeIntegrity：伪装成客户反馈报告的 PDF，内含白底白字的隐藏提示，诱导 agent 用 `functions.search()` 的 **URL 参数能力**（该工具同时支持搜索词和 URL）把私有 Notion 页面外带。**任何被骗去「总结一份看起来无害的 PDF」的用户，都成了整个团队私有数据的泄露通道**
---

# Notion 3.0 agent「致命三元组」

<sub>Notion 3.0 agent hits the lethal trifecta</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## 概要

CodeIntegrity：伪装成客户反馈报告的 PDF，内含白底白字的隐藏提示，诱导 agent 用 `functions.search()` 的 **URL 参数能力**（该工具同时支持搜索词和 URL）把私有 Notion 页面外带。**任何被骗去「总结一份看起来无害的 PDF」的用户，都成了整个团队私有数据的泄露通道**

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
| 1 | CodeIntegrity | <https://www.codeintegrity.ai/blog/notion> |
| 2 | Simon Willison | <https://simonwillison.net/2025/Sep/19/notion-lethal-trifecta/> |
| 3 | Schneier | <https://www.schneier.com/blog/archives/2025/09/abusing-notions-ai-agent-for-data-theft.html> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-09-19`（原文：2025-09-19，精度 `day`） |
| 性质 | 研究演示 `research` |
| 类型 | [`IPI`](../../../../taxonomy/types.md#ipi) 间接提示注入 · [`EXFIL`](../../../../taxonomy/types.md#exfil) 数据外泄 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-09-19-notion-agent-zhi-ming-san` |

<sub>**判定依据**：研究机构或厂商的受控演示，`real_harm: false`；收录是为了标记攻击面何时被公开。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[零点击数据外泄链](../../../../topics/zero-click-exfil.md)

**同类条目**：

- `2025-09-18` [ShadowLeak](../../../2025-09/2025-09-18-shadowleak.md)<br>  <sub>ShadowLeak</sub>
- `2025-09-25` [ForcedLeak（Salesforce Agentforce）](../../../2025-09/2025-09-25-forcedleak-salesforce-agentforce.md)<br>  <sub>ForcedLeak (Salesforce Agentforce)</sub>
- `2025-09-30` [Gemini "Trifecta"](../../../2025-09/2025-09-30-gemini-trifecta.md)<br>  <sub>Gemini "Trifecta"</sub>
- `2025-08-06` [AgentFlayer 零点击攻击集（Black Hat USA）](../../../2025-08/2025-08-06-agentflayer-black-hat-usa.md)<br>  <sub>AgentFlayer zero-click attack set (Black Hat USA)</sub>

---

[← English original](../../../2025-09/2025-09-19-notion-agent-zhi-ming-san.md) · [2025-09 index](../../../2025-09/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
