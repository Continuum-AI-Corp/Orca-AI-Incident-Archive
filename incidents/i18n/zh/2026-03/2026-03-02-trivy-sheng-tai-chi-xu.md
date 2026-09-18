---
id: 2026-03-02-trivy-sheng-tai-chi-xu
lang: zh
source: incidents/2026-03/2026-03-02-trivy-sheng-tai-chi-xu.md
title: "Trivy 生态持续性供应链攻陷"
summary: |
  攻破 GitHub 仓库凭据，分发恶意二进制(v0.69.4)、容器镜像、GitHub Actions（trivy-action、setup-trivy）。**其中针对 OpenVSX 上 Trivy VS Code 扩展的是 AI 辅助攻击 —— 利用受害者本机的 AI 编码助手把系统数据外带**。波及 Checkmarx KICS、LiteLLM、Telnyx、Axios
---

# Trivy 生态持续性供应链攻陷

<sub>Sustained supply-chain compromise across the Trivy ecosystem</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## 概要

攻破 GitHub 仓库凭据，分发恶意二进制(v0.69.4)、容器镜像、GitHub Actions（trivy-action、setup-trivy）。**其中针对 OpenVSX 上 Trivy VS Code 扩展的是 AI 辅助攻击 —— 利用受害者本机的 AI 编码助手把系统数据外带**。波及 Checkmarx KICS、LiteLLM、Telnyx、Axios

## 攻击链

```mermaid
flowchart LR
    E["被投毒的包 / 仓库 / agent 配置"]:::entry
    S0["开发者或 agent 自动安装"]:::step
    I["凭据窃取与自我传播"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Aqua 公告 | <https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23> |
| 2 | Socket | <https://socket.dev/blog/unauthorized-ai-agent-execution-code-published-to-openvsx-in-aqua-trivy-vs-code-extension> |
| 3 | Trend Micro | <https://www.trendmicro.com/ja_jp/jp-security/26/d/expertview-20260409-01.html> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-03-02`（原文：2026-03-02，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`SUPPLY`](../../../../taxonomy/types.md#supply) 供应链投毒 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-03-02-trivy-sheng-tai-chi-xu` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 供应链投毒](../../../../topics/agent-supply-chain.md)

**同类条目**：

- `2026-03-01` [Hades：把 AI 编码助手本身变成攻击面的持续战役](../../../2026-03/2026-03-01-hades-campaign-ai-coding-assistants.md)<br>  <sub>Hades: a sustained campaign turning AI coding assistants into the attack surface</sub>
- `2026-03-24` [LiteLLM 后门版本](../../../2026-03/2026-03-24-litellm-backdoored-release.md)<br>  <sub>Backdoored LiteLLM release</sub>
- `2026-03-30` [Axios npm 包被攻陷](../../../2026-03/2026-03-30-axios-npm-compromised.md)<br>  <sub>Axios npm package compromised</sub>
- `2026-02-09` [Clinejection](../../../2026-02/2026-02-09-clinejection.md)<br>  <sub>Clinejection</sub>

---

[← English original](../../../2026-03/2026-03-02-trivy-sheng-tai-chi-xu.md) · [2026-03 index](../../../2026-03/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
