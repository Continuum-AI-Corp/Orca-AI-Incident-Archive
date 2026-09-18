---
id: 2026-05-04-braintrust-aws-zhang-hao-gong
lang: zh
source: incidents/2026-05/2026-05-04-braintrust-aws-zhang-hao-gong.md
title: "Braintrust 的 AWS 账号被攻陷，要求全体客户轮换 AI 密钥"
summary: |
  AI **评测**平台 Braintrust 发现可疑活动后确认一个 AWS 账号被未授权访问，**很可能暴露了存放在 Braintrust 中的组织级 AI 提供方 API key**（客户用它连接云端模型）。05-05 通知全部客户轮换。SecurityWeek：已确认 1 家客户受影响，另有 3 家报告 **AI 提供方用量异常飙升**
---

# Braintrust 的 AWS 账号被攻陷，要求全体客户轮换 AI 密钥

<sub>Braintrust's AWS account compromised, all customers told to rotate AI keys</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## 概要

AI **评测**平台 Braintrust 发现可疑活动后确认一个 AWS 账号被未授权访问，**很可能暴露了存放在 Braintrust 中的组织级 AI 提供方 API key**（客户用它连接云端模型）。05-05 通知全部客户轮换。SecurityWeek：已确认 1 家客户受影响，另有 3 家报告 **AI 提供方用量异常飙升**

## 攻击链

```mermaid
flowchart LR
    E["放在 agent 够得着的位置的凭据"]:::entry
    S0["agent 取用并调用"]:::step
    I["凭据被滥用"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | TechCrunch | <https://techcrunch.com/2026/05/06/ai-evaluation-startup-braintrust-confirms-breach-tells-every-customer-to-rotate-sensitive-keys/> |
| 2 | SecurityWeek | <https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-05-04`（原文：2026-05-04，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`CRED`](../../../../taxonomy/types.md#cred) 凭据滥用 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-05-04-braintrust-aws-zhang-hao-gong` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**同类条目**：

- `2026-05-19` [TrapDoor：跨三个生态投毒，专门污染 AI 助手配置](../../../2026-05/2026-05-19-trapdoor-poisons-agent-configs.md)<br>  <sub>TrapDoor: poisoning three ecosystems to corrupt AI assistant configs</sub>
- `2026-05-21` [Composio：agent 自动化本身成了提权路径](../../../2026-05/2026-05-21-composio-agent-automation-privesc.md)<br>  <sub>Composio: agent automation itself becomes the privilege-escalation path</sub>
- `2026-05-11` [TanStack npm "Mini Shai-Hulud"](../../../2026-05/2026-05-11-tanstack-npm-mini-shai.md)<br>  <sub>TanStack npm "Mini Shai-Hulud"</sub>
- `2026-05-18` [GitHub 内部 3,800 个仓库被攻陷](../../../2026-05/2026-05-18-github-3800-internal-repos.md)<br>  <sub>3,800 internal GitHub repositories compromised</sub>

---

[← English original](../../../2026-05/2026-05-04-braintrust-aws-zhang-hao-gong.md) · [2026-05 index](../../../2026-05/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
