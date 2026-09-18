---
id: 2025-05-01-gitlab-duo-yuan-cheng-ti
lang: zh
source: incidents/2025-05/2025-05-01-gitlab-duo-yuan-cheng-ti.md
title: "GitLab Duo 远程提示注入"
summary: |
  Legit Security：merge request 中的隐藏指令可窃取私有项目源码、操纵他人看到的代码建议、外带**未披露的零日**。2025-02-12 报告；GitLab 确认 HTML 注入并承认提示注入为安全问题，补丁禁止 Duo 渲染指向 gitlab.com 以外域的 `<img>`/`<form>`
---

# GitLab Duo 远程提示注入

<sub>GitLab Duo remote prompt injection</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## 概要

Legit Security：merge request 中的隐藏指令可窃取私有项目源码、操纵他人看到的代码建议、外带**未披露的零日**。2025-02-12 报告；GitLab 确认 HTML 注入并承认提示注入为安全问题，补丁禁止 Duo 渲染指向 gitlab.com 以外域的 `<img>`/`<form>`

## 攻击链

```mermaid
flowchart LR
    E["外部内容<br/>邮件 · 文档 · Issue · 网页"]:::entry
    S0["agent 读取并当作指令执行"]:::step
    S1["经厂商可信域外带<br/>图片渲染 · API · 代理"]:::step
    I["数据落入攻击者手中"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Legit Security | <https://www.legitsecurity.com/blog/remote-prompt-injection-in-gitlab-duo> |
| 2 | THN | <https://thehackernews.com/2025/05/gitlab-duo-vulnerability-enabled.html> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-05-01`（原文：2025-05，精度 `month`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`IPI`](../../../../taxonomy/types.md#ipi) 间接提示注入 · [`EXFIL`](../../../../taxonomy/types.md#exfil) 数据外泄 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-05-01-gitlab-duo-yuan-cheng-ti` |

<sub>**判定依据**：真实事故，未见确认的具体受害方。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[零点击数据外泄链](../../../../topics/zero-click-exfil.md)

**同类条目**：

- `2025-05-26` [GitHub MCP "Toxic Agent Flow"](../../../2025-05/2025-05-26-github-mcp-toxic-agent.md)<br>  <sub>GitHub MCP "toxic agent flow"</sub>
- `2025-06-11` [EchoLeak（CVE-2025-32711）](../../../2025-06/2025-06-11-echoleak.md)<br>  <sub>EchoLeak (CVE-2025-32711)</sub>
- `2025-08-06` [AgentFlayer 零点击攻击集（Black Hat USA）](../../../2025-08/2025-08-06-agentflayer-black-hat-usa.md)<br>  <sub>AgentFlayer zero-click attack set (Black Hat USA)</sub>
- `2025-08-06` [SafeBreach "Invitation Is All You Need"](../../../2025-08/2025-08-06-safebreach-invitation-is-all.md)<br>  <sub>SafeBreach "Invitation Is All You Need"</sub>

---

[← English original](../../../2025-05/2025-05-01-gitlab-duo-yuan-cheng-ti.md) · [2025-05 index](../../../2025-05/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
