---
id: 2026-09-08-chatgpt-gmail-sha-xiang-que
lang: zh
source: incidents/2026-09/2026-09-08-chatgpt-gmail-sha-xiang-que.md
title: "ChatGPT 沙箱缺陷让受害者的 Gmail 数据流进攻击者账号"
summary: |
  Check Point Research（工作时间标注为 **2026-06**）：ChatGPT **代码执行沙箱**的一个弱点 —— **每个容器都能触达 OpenAI 用于包管理的同一个内部 JFrog Artifactory 实例**，构成隐蔽信道。攻击者把指令埋进共享对话、恶意提示或自定义 GPT 配置中，受害者的会话就会在处理正常请求的同时执行隐藏任务，把已连接应用的数据发给攻击者**且不在聊天输出中显示**，**全程无任何确认提示**。
  影响范围不止 Gmail —— 受害者会话已授权的一切（Google Drive、Microsoft Teams、GitHub 连接器）都在内。**唯一可见迹象是一个事后才记录的「Talked to Gmail」小标签**。OpenAI 已修复并下线了涉事内部服务
  💡 **注意：JFrog Artifactory 同时也是 2026-07 OpenAI agent 逃逸的出口** —— 同一个组件在半年内两次成为 AI 基础设施的薄弱点
---

# ChatGPT 沙箱缺陷让受害者的 Gmail 数据流进攻击者账号

<sub>ChatGPT sandbox flaw pipes a victim's Gmail data into the attacker's account</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## 概要

Check Point Research（工作时间标注为 **2026-06**）：ChatGPT **代码执行沙箱**的一个弱点 —— **每个容器都能触达 OpenAI 用于包管理的同一个内部 JFrog Artifactory 实例**，构成隐蔽信道。攻击者把指令埋进共享对话、恶意提示或自定义 GPT 配置中，受害者的会话就会在处理正常请求的同时执行隐藏任务，把已连接应用的数据发给攻击者**且不在聊天输出中显示**，**全程无任何确认提示**。

影响范围不止 Gmail —— 受害者会话已授权的一切（Google Drive、Microsoft Teams、GitHub 连接器）都在内。**唯一可见迹象是一个事后才记录的「Talked to Gmail」小标签**。OpenAI 已修复并下线了涉事内部服务

💡 **注意：JFrog Artifactory 同时也是 2026-07 OpenAI agent 逃逸的出口** —— 同一个组件在半年内两次成为 AI 基础设施的薄弱点

## 攻击链

```mermaid
flowchart LR
    E["agent 可访问的敏感数据"]:::entry
    S0["经厂商可信域外带<br/>图片渲染 · API · 代理"]:::step
    I["数据落入攻击者手中<br/><i>（实验室演示 · 无真实受害方）</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | THN | <https://thehackernews.com/2026/09/chatgpt-flaw-let-planted-prompt-send.html> |
| 2 | CSO Online | <https://www.csoonline.com/article/4220203/chatgpt-flaw-lets-attackers-pull-gmail-data-across-accounts-via-a-hidden-channel.html> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-09-08`（原文：2026-09-08，精度 `day`） |
| 性质 | 研究演示 `research` |
| 类型 | [`EXFIL`](../../../../taxonomy/types.md#exfil) 数据外泄 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-09-08-chatgpt-gmail-sha-xiang-que` |

<sub>**判定依据**：研究机构或厂商的受控演示，`real_harm: false`；收录是为了标记攻击面何时被公开。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[零点击数据外泄链](../../../../topics/zero-click-exfil.md)

**同类条目**：

- `2026-08-19` [Grok「密码学上下文注入」：加密的指令，明文的数据](../../../2026-08/2026-08-19-grok-mi-ma-xue-wen.md)<br>  <sub>Grok "cryptographic context injection": encrypted instructions, plaintext data</sub>
- `2026-08-18` [CoSnitch（CVE-2026-24301）](../../../2026-08/2026-08-18-cosnitch.md)<br>  <sub>CoSnitch (CVE-2026-24301)</sub>
- `2026-07-07` [GitLost：GitHub Agentic Workflows 泄露私有仓库](../../../2026-07/2026-07-07-gitlost-github-agentic-workflows.md)<br>  <sub>GitLost: GitHub Agentic Workflows leak private repositories</sub>
- `2026-06-15` [SearchLeak（CVE-2026-42824）](../../../2026-06/2026-06-15-searchleak.md)<br>  <sub>SearchLeak (CVE-2026-42824)</sub>

---

[← English original](../../../2026-09/2026-09-08-chatgpt-gmail-sha-xiang-que.md) · [2026-09 index](../../../2026-09/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
