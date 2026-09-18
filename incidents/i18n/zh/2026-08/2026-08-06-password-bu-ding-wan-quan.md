---
id: 2026-08-06-password-bu-ding-wan-quan
lang: zh
source: incidents/2026-08/2026-08-06-password-bu-ding-wan-quan.md
title: "1Password：AI 补丁完全修复率仅 26%"
summary: |
  Off-by-1 Labs：对 6 个需复杂修复的 CVE 用 2 个生成式 AI 模型产出 6,480 份补丁，剔除 400 份「抄上游」后统计 6,080 份 —— **在不改变行为的前提下彻底消除漏洞的平均只有 26.0%**，**53.9% 是漏洞仍在、引入新漏洞、或两者都有**。另 Checkmarx 的 SusViBes 基准：功能成功率 83–95%，但**安全且功能正确的只有 24–36%**，能跑的补丁里 **65–75% 复现了已被修复过的漏洞**
---

# 1Password：AI 补丁完全修复率仅 26%

<sub>1Password: AI patches fully fix only 26% of the time</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## 概要

Off-by-1 Labs：对 6 个需复杂修复的 CVE 用 2 个生成式 AI 模型产出 6,480 份补丁，剔除 400 份「抄上游」后统计 6,080 份 —— **在不改变行为的前提下彻底消除漏洞的平均只有 26.0%**，**53.9% 是漏洞仍在、引入新漏洞、或两者都有**。另 Checkmarx 的 SusViBes 基准：功能成功率 83–95%，但**安全且功能正确的只有 24–36%**，能跑的补丁里 **65–75% 复现了已被修复过的漏洞**

## 攻击链

```mermaid
flowchart LR
    E["监管或政策动作"]:::entry
    S0["落到厂商与使用方头上"]:::step
    I["合规要求发生变化"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | 1Password | <https://1password.com/blog/why-ai-generated-patches-still-require-human-review> |
| 2 | PDF | <https://1password.com/files/resources/frontier-models-vulnerability-patches-flawed.pdf> |
| 3 | Checkmarx | <https://checkmarx.com/blog/zombie-cves-put-to-rest-by-humans-dug-back-up-by-ai-agents/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-08-06`（原文：2026-08-06，精度 `day`） |
| 性质 | 威胁情报报告 `report` |
| 类型 | [`GOV`](../../../../taxonomy/types.md#gov) 治理 / 监管 |
| 严重度 | **信息** `info` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-08-06-password-bu-ding-wan-quan` |

<sub>**判定依据**：威胁情报报告，汇总多起事件，本身不作为单一事故计数，`severity` 记为 `info`。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[防御与治理](../../../../topics/defense.md)

**同类条目**：

- `2026-08-03` [CrowdStrike 2026 威胁狩猎报告](../../../2026-08/2026-08-03-crowdstrike-wei-xie-shou-lie.md)<br>  <sub>CrowdStrike 2026 threat hunting report</sub>
- `2026-08-04` [OSAA 发布 AI 事故共享框架 SAFE 草案（RFC）](../../../2026-08/2026-08-04-osaa-safe-rfc.md)<br>  <sub>OSAA publishes the SAFE draft for AI incident sharing (RFC)</sub>
- `2026-08-07` [OpenAI：下一代模型 Astra 可能达到网络能力 Critical](../../../2026-08/2026-08-07-astra-critical-yi-dai-mo.md)<br>  <sub>OpenAI: next-generation model Astra may reach Critical cyber capability</sub>
- `2026-08-18` [OpenAI 宣布放慢研发、暂停 RL 训练两周](../../../2026-08/2026-08-18-rl-xuan-bu-fang-man.md)<br>  <sub>OpenAI slows development and pauses RL training for two weeks</sub>

---

[← English original](../../../2026-08/2026-08-06-password-bu-ding-wan-quan.md) · [2026-08 index](../../../2026-08/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
