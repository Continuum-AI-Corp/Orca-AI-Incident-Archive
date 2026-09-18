---
id: 2026-05-11-tanstack-npm-mini-shai
lang: zh
source: incidents/2026-05/2026-05-11-tanstack-npm-mini-shai.md
title: "TanStack npm \"Mini Shai-Hulud\""
summary: |
  **TeamPCP** 用 GitHub Actions 缓存污染 + OIDC token 提取，攻陷 **42 个 `@tanstack/*` 包**，生成**带有效 SLSA 证明**的恶意包。含破坏 home 目录的「死亡开关」与编辑器持久化钩子。**TeamPCP 在恶意软件里附言称该软件由 AI 开发**，并随后在 GitHub 开源了自己的蠕虫
---

# TanStack npm "Mini Shai-Hulud"

<sub>TanStack npm "Mini Shai-Hulud"</sub>

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## 概要

**TeamPCP** 用 GitHub Actions 缓存污染 + OIDC token 提取，攻陷 **42 个 `@tanstack/*` 包**，生成**带有效 SLSA 证明**的恶意包。含破坏 home 目录的「死亡开关」与编辑器持久化钩子。**TeamPCP 在恶意软件里附言称该软件由 AI 开发**，并随后在 GitHub 开源了自己的蠕虫

## 攻击链

```mermaid
flowchart LR
    E["被投毒的包 / 仓库 / agent 配置"]:::entry
    S0["开发者或 agent 自动安装"]:::step
    S1["agent 取用并调用"]:::step
    I["凭据被滥用"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | TanStack 公告 | <https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx> |
| 2 | StepSecurity | <https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem> |
| 3 | The Register | <https://www.theregister.com/security/2026/05/13/malware-crew-teampcp-open-sources-its-shai-hulud-worm-on-github/5239319> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-05-11`（原文：2026-05-11，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`SUPPLY`](../../../../taxonomy/types.md#supply) 供应链投毒 · [`CRED`](../../../../taxonomy/types.md#cred) 凭据滥用 |
| 严重度 | **严重** `critical` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-05-11-tanstack-npm-mini-shai` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `critical`：确认的真实损害达到多组织 / 政府 / 关键基础设施 / 供应链蠕虫级别，或属首次出现且有真实受害方的能力里程碑。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 供应链投毒](../../../../topics/agent-supply-chain.md)

**同类条目**：

- `2026-05-19` [TrapDoor：跨三个生态投毒，专门污染 AI 助手配置](../../../2026-05/2026-05-19-trapdoor-poisons-agent-configs.md)<br>  <sub>TrapDoor: poisoning three ecosystems to corrupt AI assistant configs</sub>
- `2026-05-21` [Composio：agent 自动化本身成了提权路径](../../../2026-05/2026-05-21-composio-agent-automation-privesc.md)<br>  <sub>Composio: agent automation itself becomes the privilege-escalation path</sub>
- `2026-05-18` [GitHub 内部 3,800 个仓库被攻陷](../../../2026-05/2026-05-18-github-3800-internal-repos.md)<br>  <sub>3,800 internal GitHub repositories compromised</sub>
- `2026-05-04` [Braintrust 的 AWS 账号被攻陷，要求全体客户轮换 AI 密钥](../../../2026-05/2026-05-04-braintrust-aws-zhang-hao-gong.md)<br>  <sub>Braintrust's AWS account compromised, all customers told to rotate AI keys</sub>

---

[← English original](../../../2026-05/2026-05-11-tanstack-npm-mini-shai.md) · [2026-05 index](../../../2026-05/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
