---
id: 2026-06-15-unc6508-redcap-jing-ru-qin
lang: zh
source: incidents/2026-06/2026-06-15-unc6508-redcap-jing-ru-qin.md
title: "UNC6508 经 REDCap 入侵北美研究机构"
summary: |
  GTIG 高置信度归因中国相关行为者。目标含国家/州/民间医疗机构、学术中心、军方医疗机构；收集国防信息、印太军作战、AI、无人机系统、医学研究。最早入侵 2023-09，某机构活动持续到 2025-11。植入 INFINITERED 改写 REDCap 正规文件、每次升级自我重注入存活 1 年+。滥用合规规则 **"Patroit"** 用正则匹配收发邮件并静默 BCC 到攻击者 Gmail —— **GTIG 称中国相关行为者中前所未见**
---

# UNC6508 经 REDCap 入侵北美研究机构

<sub>UNC6508 breaches North American research institutions via REDCap</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

GTIG 高置信度归因中国相关行为者。目标含国家/州/民间医疗机构、学术中心、军方医疗机构；收集国防信息、印太军作战、AI、无人机系统、医学研究。最早入侵 2023-09，某机构活动持续到 2025-11。植入 INFINITERED 改写 REDCap 正规文件、每次升级自我重注入存活 1 年+。滥用合规规则 **"Patroit"** 用正则匹配收发邮件并静默 BCC 到攻击者 Gmail —— **GTIG 称中国相关行为者中前所未见**

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
| 1 | Google Cloud | <https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-06-15`（原文：2026-06-15，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [美国](../../../../regions/us.md) |
| 档案编号 | `2026-06-15-unc6508-redcap-jing-ru-qin` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**同类条目**：

- `2026-06-02` [CleverHans Lab 自适应 AI 蠕虫 PoC](../../../2026-06/2026-06-02-cleverhans-lab-poc.md)<br>  <sub>CleverHans Lab adaptive AI worm PoC</sub>
- `2026-06-24` [macOS.Gaslight：恶意软件反过来对 AI 分析师做提示注入](../../../2026-06/2026-06-24-macos-gaslight-e-yi-ruan-jian.md)<br>  <sub>macOS.Gaslight: malware prompt-injects the AI analyst</sub>
- `2026-06-03` [Anthropic《LLM ATT&CK Navigator》](../../../2026-06/2026-06-03-anthropic-llm-att-ck.md)<br>  <sub>Anthropic, "LLM ATT&CK Navigator"</sub>
- `2026-06-09` [Anthropic：N-day 实为「N-hour」](../../../2026-06/2026-06-09-anthropic-day-hour.md)<br>  <sub>Anthropic: N-day is really "N-hour"</sub>

---

[← English original](../../../2026-06/2026-06-15-unc6508-redcap-jing-ru-qin.md) · [2026-06 index](../../../2026-06/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
