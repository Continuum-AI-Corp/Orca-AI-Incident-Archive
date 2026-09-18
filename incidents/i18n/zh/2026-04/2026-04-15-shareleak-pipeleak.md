---
id: 2026-04-15-shareleak-pipeleak
lang: zh
source: incidents/2026-04/2026-04-15-shareleak-pipeleak.md
title: "ShareLeak（CVE-2026-21520）+ PipeLeak"
summary: |
  **Capsule Security** 发现（**v1 误记为 Zenity、误置于 2026-08**）。ShareLeak：Copilot Studio 把 SharePoint 表单提交内容**未经任何净化**直接与 agent 系统指令拼接，注入的伪 system 角色消息指挥 agent 查询已连接的 SharePoint 列表取 PII/线索/CRM 数据，经 Outlook 发到指定地址。CVSS 7.5，**补丁 2026-01-15 部署**。PipeLeak：Salesforce Agentforce 的同类问题，**Salesforce 未分配 CVE、未发公告**。VentureBeat 指出：**即使安全机制标记了攻击，数据仍然被带走了**
---

# ShareLeak（CVE-2026-21520）+ PipeLeak

<sub>ShareLeak (CVE-2026-21520) and PipeLeak</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

> [!WARNING]
> **本条存在争议或未完全证实的事实**，正文中的各方说法并列保留，请勿单独引用其中一方。

## 概要

**Capsule Security** 发现（**v1 误记为 Zenity、误置于 2026-08**）。ShareLeak：Copilot Studio 把 SharePoint 表单提交内容**未经任何净化**直接与 agent 系统指令拼接，注入的伪 system 角色消息指挥 agent 查询已连接的 SharePoint 列表取 PII/线索/CRM 数据，经 Outlook 发到指定地址。CVSS 7.5，**补丁 2026-01-15 部署**。PipeLeak：Salesforce Agentforce 的同类问题，**Salesforce 未分配 CVE、未发公告**。VentureBeat 指出：**即使安全机制标记了攻击，数据仍然被带走了**

## 攻击链

```mermaid
flowchart LR
    E["外部内容<br/>邮件 · 文档 · Issue · 网页"]:::entry
    S0["agent 读取并当作指令执行"]:::step
    S1["经厂商可信域外带<br/>图片渲染 · API · 代理"]:::step
    I["数据落入攻击者手中<br/><i>（漏洞已披露 · 未见在野利用）</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | VentureBeat | <https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook> |
| 2 | Capsule Security | <https://www.capsulesecurity.io/blog-post/shareleak-taking-the-wheel-of-microsofts-copilot-studio-cve-2026-21520> |
| 3 | Dark Reading | <https://www.darkreading.com/cloud-security/microsoft-salesforce-patch-ai-agent-data-leak-flaws> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-04-15`（原文：2026-04-15，精度 `day`） |
| 性质 | 漏洞披露 `vulnerability` |
| 类型 | [`IPI`](../../../../taxonomy/types.md#ipi) 间接提示注入 · [`EXFIL`](../../../../taxonomy/types.md#exfil) 数据外泄 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-04-15-shareleak-pipeleak` |

<sub>**判定依据**：漏洞披露，截至归档未见在野利用证据，故 `real_harm: false`。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[零点击数据外泄链](../../../../topics/zero-click-exfil.md)

**同类条目**：

- `2026-04-01` [Claude Code GitHub Action 三 CVE：一个 PR 标题偷走 API key](../../../2026-04/2026-04-01-claude-code-github-action.md)<br>  <sub>Three CVEs in the Claude Code GitHub Action: a PR title steals your API key</sub>
- `2026-04-17` [Meta AI 客服机器人被骗交出 Instagram 账号](../../../2026-04/2026-04-17-meta-instagram-ke-fu-ji.md)<br>  <sub>Meta AI support bot tricked into handing over an Instagram account</sub>
- `2026-04-07` [GrafanaGhost 间接提示注入](../../../2026-04/2026-04-07-grafanaghost-jian-jie-ti-shi.md)<br>  <sub>GrafanaGhost indirect prompt injection</sub>
- `2026-03-01` [Claudy Day：claude.ai 三漏洞链](../../../2026-03/2026-03-01-claudy-day-claude-ai.md)<br>  <sub>Claudy Day: a three-flaw chain in claude.ai</sub>

---

[← English original](../../../2026-04/2026-04-15-shareleak-pipeleak.md) · [2026-04 index](../../../2026-04/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
