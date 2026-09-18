---
id: 2026-09-11-claude-scans-18m-android-apks
lang: zh
source: incidents/2026-09/2026-09-11-claude-scans-18m-android-apks.md
title: "用 Claude 扫描 180 万个安卓 App 找密钥"
summary: |
  Anthropic 九月报告中的一个具体案例：一名疑似法语系的 **ShinyHunters** 成员（handle **`frkoo`**）部署了一条凭据收割流水线，**横跨 10 台 AWS EC2 worker**，从多个应用商店下载并**扫描 180 万个安卓 APK 中的密钥**。账号已被移除、护栏已调整
---

# 用 Claude 扫描 180 万个安卓 App 找密钥

<sub>Claude used to scan 1.8 million Android apps for secrets</sub>

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

Anthropic 九月报告中的一个具体案例：一名疑似法语系的 **ShinyHunters** 成员（handle **`frkoo`**）部署了一条凭据收割流水线，**横跨 10 台 AWS EC2 worker**，从多个应用商店下载并**扫描 180 万个安卓 APK 中的密钥**。账号已被移除、护栏已调整

## 攻击链

```mermaid
flowchart LR
    E["攻击者 + 越狱话术"]:::entry
    S0["LLM 编排器驱动子 agent 集群"]:::step
    I["目标系统被攻陷"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/hackers-abused-claude-to-extract-secrets-from-18m-android-apps/> |
| 2 | Anthropic 报告 | <https://www.anthropic.com/threat-intelligence-report-september-2026> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-09-11`（原文：2026-09-11，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **严重** `critical` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-09-11-claude-scans-18m-android-apks` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `critical`：确认的真实损害达到多组织 / 政府 / 关键基础设施 / 供应链蠕虫级别，或属首次出现且有真实受害方的能力里程碑。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**同类条目**：

- `2026-09-10` [Anthropic 九月威胁情报报告](../../../2026-09/2026-09-10-anthropic-september-threat-report.md)<br>  <sub>Anthropic September threat intelligence report</sub>
- `2026-09-15` [PaperCut AI agent 蜂群攻击公开](../../../2026-09/2026-09-15-papercut-agent-swarm-disclosed.md)<br>  <sub>PaperCut AI agent swarm attack made public</sub>
- `2026-09-02` [Unit 42：AI agent 把两周的入侵工作压到 10 小时内](../../../2026-09/2026-09-02-unit-agent-liang-ru-qin.md)<br>  <sub>Unit 42: AI agents compress two weeks of intrusion work into 10 hours</sub>
- `2026-08-28` [PaperCut AI agent 蜂群战役启动](../../../2026-08/2026-08-28-papercut-agent-swarm-campaign-begins.md)<br>  <sub>PaperCut AI agent swarm campaign begins</sub>

---

[← English original](../../../2026-09/2026-09-11-claude-scans-18m-android-apks.md) · [2026-09 index](../../../2026-09/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
