---
id: 2025-08-26-nx-s1ngularity
lang: zh
source: incidents/2025-08/2025-08-26-nx-s1ngularity.md
title: "Nx \"s1ngularity\""
summary: |
  **首个把 AI CLI 武器化的恶意软件**：检测本机是否装了 Claude Code / Gemini CLI / Amazon Q，然后**指挥这些 agent 去扫描并收集凭据**。窃取 GitHub token、SSH 密钥、钱包与密钥，写入攻击者创建的公开仓库。影响 **2,180 个 GitHub 账号、7,200 个仓库**
---

# Nx "s1ngularity"

<sub>Nx "s1ngularity"</sub>

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## 概要

**首个把 AI CLI 武器化的恶意软件**：检测本机是否装了 Claude Code / Gemini CLI / Amazon Q，然后**指挥这些 agent 去扫描并收集凭据**。窃取 GitHub token、SSH 密钥、钱包与密钥，写入攻击者创建的公开仓库。影响 **2,180 个 GitHub 账号、7,200 个仓库**

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
| 1 | Wiz | <https://www.wiz.io/blog/s1ngularity-supply-chain-attack> |
| 2 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/ai-powered-malware-hit-2-180-github-accounts-in-s1ngularity-attack/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-08-26`（原文：2025-08-26，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`SUPPLY`](../../../../taxonomy/types.md#supply) 供应链投毒 · [`CRED`](../../../../taxonomy/types.md#cred) 凭据滥用 |
| 严重度 | **严重** `critical` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-08-26-nx-s1ngularity` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `critical`：确认的真实损害达到多组织 / 政府 / 关键基础设施 / 供应链蠕虫级别，或属首次出现且有真实受害方的能力里程碑。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 供应链投毒](../../../../topics/agent-supply-chain.md)

**同类条目**：

- `2025-08-08` [Salesloft Drift OAuth 令牌窃取](../../../2025-08/2025-08-08-salesloft-drift-oauth-theft.md)<br>  <sub>Salesloft Drift OAuth token theft</sub>
- `2025-08-28` [TransUnion 经第三方应用泄露 440–450 万人数据](../../../2025-08/2025-08-28-transunion-jing-di-san-fang.md)<br>  <sub>TransUnion leaks 4.4-4.5M people via a third-party app</sub>
- `2025-07-13` [Amazon Q Developer 扩展被投毒](../../../2025-07/2025-07-13-amazon-q-extension-poisoned.md)<br>  <sub>Amazon Q Developer extension poisoned</sub>
- `2025-09-15` [Shai-Hulud npm 蠕虫 v1](../../../2025-09/2025-09-15-shai-hulud-npm.md)<br>  <sub>Shai-Hulud npm worm v1</sub>

---

[← English original](../../../2025-08/2025-08-26-nx-s1ngularity.md) · [2025-08 index](../../../2025-08/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
