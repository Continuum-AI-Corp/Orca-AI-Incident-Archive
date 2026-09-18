---
id: 2026-06-03-anthropic-llm-att-ck
lang: zh
source: incidents/2026-06/2026-06-03-anthropic-llm-att-ck.md
title: "Anthropic《LLM ATT&CK Navigator》"
summary: |
  分析 2025-03 → 2026-03 的 **832 个滥用账号**。关键发现：攻击者用 AI 的重心从「准备阶段」（写恶意软件）转向**「入侵后阶段」**（横移、窃凭据）；中高风险行为者占比一年内从 **33% 升到 56%**，主因是 agent 对攻击阶段的自主串联。结论：MITRE ATT&CK 捕捉不了这些自主行为，风险评估需从「技能/手法数量」转向**「编排能力」**
---

# Anthropic《LLM ATT&CK Navigator》

<sub>Anthropic, "LLM ATT&CK Navigator"</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

分析 2025-03 → 2026-03 的 **832 个滥用账号**。关键发现：攻击者用 AI 的重心从「准备阶段」（写恶意软件）转向**「入侵后阶段」**（横移、窃凭据）；中高风险行为者占比一年内从 **33% 升到 56%**，主因是 agent 对攻击阶段的自主串联。结论：MITRE ATT&CK 捕捉不了这些自主行为，风险评估需从「技能/手法数量」转向**「编排能力」**

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
| 1 | red.anthropic.com | <https://red.anthropic.com/2026/attack-navigator/> |
| 2 | Anthropic | <https://www.anthropic.com/news/AI-enabled-cyber-threats-mitre-attack> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-06-03`（原文：2026-06-03，精度 `day`） |
| 性质 | 威胁情报报告 `report` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **信息** `info` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-06-03-anthropic-llm-att-ck` |

<sub>**判定依据**：威胁情报报告，汇总多起事件，本身不作为单一事故计数，`severity` 记为 `info`。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**同类条目**：

- `2026-06-15` [UNC6508 经 REDCap 入侵北美研究机构](../../../2026-06/2026-06-15-unc6508-redcap-jing-ru-qin.md)<br>  <sub>UNC6508 breaches North American research institutions via REDCap</sub>
- `2026-06-02` [CleverHans Lab 自适应 AI 蠕虫 PoC](../../../2026-06/2026-06-02-cleverhans-lab-poc.md)<br>  <sub>CleverHans Lab adaptive AI worm PoC</sub>
- `2026-06-24` [macOS.Gaslight：恶意软件反过来对 AI 分析师做提示注入](../../../2026-06/2026-06-24-macos-gaslight-e-yi-ruan-jian.md)<br>  <sub>macOS.Gaslight: malware prompt-injects the AI analyst</sub>
- `2026-06-09` [Anthropic：N-day 实为「N-hour」](../../../2026-06/2026-06-09-anthropic-day-hour.md)<br>  <sub>Anthropic: N-day is really "N-hour"</sub>

---

[← English original](../../../2026-06/2026-06-03-anthropic-llm-att-ck.md) · [2026-06 index](../../../2026-06/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
