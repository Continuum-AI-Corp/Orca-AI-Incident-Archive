---
id: 2026-05-12-gtig-wei-xie-zhui-zong
lang: zh
source: incidents/2026-05/2026-05-12-gtig-wei-xie-zhui-zong.md
title: "GTIG AI 威胁追踪（2026 版）"
summary: |
  见 [§7.5](#75-攻击方使用-ai-的能力演进weapon) 完整拆解。新增 **PROMPTSPY**（调 Gemini API 自主操作安卓 UI 的后门）、UNC2814 / APT45 / APT27 / UNC6201 / UNC5673 等中国系行为者的 AI 使用画像、LLM 访问混淆产业（CLIProxyAPI、Claude-Relay-Service 等）
---

# GTIG AI 威胁追踪（2026 版）

<sub>GTIG AI threat tracker, 2026 edition</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

见 [§7.5](#75-攻击方使用-ai-的能力演进weapon) 完整拆解。新增 **PROMPTSPY**（调 Gemini API 自主操作安卓 UI 的后门）、UNC2814 / APT45 / APT27 / UNC6201 / UNC5673 等中国系行为者的 AI 使用画像、LLM 访问混淆产业（CLIProxyAPI、Claude-Relay-Service 等）

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
| 1 | GTIG | <https://cloud.google.com/blog/ja/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-05-12`（原文：2026-05-12，精度 `day`） |
| 性质 | 威胁情报报告 `report` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **信息** `info` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-05-12-gtig-wei-xie-zhui-zong` |

<sub>**判定依据**：威胁情报报告，汇总多起事件，本身不作为单一事故计数，`severity` 记为 `info`。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**同类条目**：

- `2026-05-10` [首起在野的「LLM agent 自主完成入侵后全流程」](../../../2026-05/2026-05-10-first-in-wild-autonomous-llm-post-exploitation.md)<br>  <sub>First in-the-wild LLM agent running the full post-exploitation chain</sub>
- `2026-04-08` [Aurora 勒索软件用 Cursor Agent 做实战](../../../2026-04/2026-04-08-aurora-cursor-agent.md)<br>  <sub>Aurora ransomware operators use Cursor Agent in live intrusions</sub>
- `2026-06-15` [UNC6508 经 REDCap 入侵北美研究机构](../../../2026-06/2026-06-15-unc6508-redcap-jing-ru-qin.md)<br>  <sub>UNC6508 breaches North American research institutions via REDCap</sub>
- `2026-06-02` [CleverHans Lab 自适应 AI 蠕虫 PoC](../../../2026-06/2026-06-02-cleverhans-lab-poc.md)<br>  <sub>CleverHans Lab adaptive AI worm PoC</sub>

---

[← English original](../../../2026-05/2026-05-12-gtig-wei-xie-zhui-zong.md) · [2026-05 index](../../../2026-05/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
