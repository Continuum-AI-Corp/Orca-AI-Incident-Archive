---
id: 2026-05-07-semantic-kernel-shell
lang: zh
source: incidents/2026-05/2026-05-07-semantic-kernel-shell.md
title: "Semantic Kernel：提示注入变成 shell"
summary: |
  Microsoft 自曝两个 agent 框架 RCE：
  **CVE-2026-26030**（CVSS 9.8，Python SDK < 1.39.4）`InMemoryVectorStore` 的 filter 把**攻击者可控的向量库字段送进 Python `eval()`** —— 构造一个恶意 filter 即可执行任意代码
  **CVE-2026-25592**（.NET）`SessionsPythonPlugin` 中，**开发者误把内部方法 `DownloadFileAsync` 打上了 `[KernelFunction]` 标注**，等于告诉模型「这是你可以调用的工具」——**检索到一份文档就足以在运行 agent 的宿主上启动进程**
  修复：python-1.39.4 / .NET 1.71.0。**「手滑加一个标注就把宿主功能变成模型可调工具」是 agent 框架特有的新缺陷类型**
---

# Semantic Kernel：提示注入变成 shell

<sub>Semantic Kernel: prompt injection turns into a shell</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## 概要

Microsoft 自曝两个 agent 框架 RCE：

**CVE-2026-26030**（CVSS 9.8，Python SDK < 1.39.4）`InMemoryVectorStore` 的 filter 把**攻击者可控的向量库字段送进 Python `eval()`** —— 构造一个恶意 filter 即可执行任意代码

**CVE-2026-25592**（.NET）`SessionsPythonPlugin` 中，**开发者误把内部方法 `DownloadFileAsync` 打上了 `[KernelFunction]` 标注**，等于告诉模型「这是你可以调用的工具」——**检索到一份文档就足以在运行 agent 的宿主上启动进程**

修复：python-1.39.4 / .NET 1.71.0。**「手滑加一个标注就把宿主功能变成模型可调工具」是 agent 框架特有的新缺陷类型**

## 攻击链

```mermaid
flowchart LR
    E["暴露在公网的 agent 基础设施"]:::entry
    S0["未认证访问"]:::step
    I["RCE / 数据泄露<br/><i>（实验室演示 · 无真实受害方）</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Microsoft | <https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-05-07`（原文：2026-05-07，精度 `day`） |
| 性质 | 研究演示 `research` |
| 类型 | [`INFRA`](../../../../taxonomy/types.md#infra) agent 基础设施暴露 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-05-07-semantic-kernel-shell` |

<sub>**判定依据**：研究机构或厂商的受控演示，`real_harm: false`；收录是为了标记攻击面何时被公开。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 基础设施暴露](../../../../topics/agent-infra.md)

**同类条目**：

- `2026-05-28` [BadHost（CVE-2026-48710）](../../../2026-05/2026-05-28-badhost.md)<br>  <sub>BadHost (CVE-2026-48710)</sub>
- `2026-04-16` [MCPwn（CVE-2026-33032）：nginx-ui 的 MCP 端点在野被打](../../../2026-04/2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br>  <sub>MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild</sub>
- `2026-04-07` [Flowise CVE-2025-59528 在野利用](../../../2026-04/2026-04-07-flowise-ye-li-yong.md)<br>  <sub>Flowise CVE-2025-59528 exploited in the wild</sub>
- `2026-04-23` [OpenClaw「Claw Chain」四漏洞链，24.5 万台服务器暴露](../../../2026-04/2026-04-23-openclaw-claw-chain.md)<br>  <sub>OpenClaw "Claw Chain": four chained flaws, 245,000 servers exposed</sub>

---

[← English original](../../../2026-05/2026-05-07-semantic-kernel-shell.md) · [2026-05 index](../../../2026-05/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
