---
id: 2026-06-09-anthropic-day-hour
lang: zh
source: incidents/2026-06/2026-06-09-anthropic-day-hour.md
title: "Anthropic：N-day 实为「N-hour」"
summary: |
  只给补丁 diff + 严重度 + 修复前后构建：Firefox 的 18 个 SpiderMonkey 漏洞 → Claude Mythos Preview 做出 **14 个 PoC**，其中 **8 个在约 12 小时内**做成可读沙箱外文件的代码执行利用（**第一个不到 1 小时**，而对应的 Firefox 148 发布在 18 天后）。闭源 Windows：2026 年 1–2 月的 21 个内核提权漏洞 → **18 个 PoC、8 条完整提权链**，总成本约 **$15,700（单个约 $2,000）**。**微软评为「不太可能被利用」的 14 个里有 13 个也做出了 PoC**。同时指出 Windows Autopatch 铺到 9 成要 7 天、强制重启在第 11 天
---

# Anthropic：N-day 实为「N-hour」

<sub>Anthropic: N-day is really "N-hour"</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

只给补丁 diff + 严重度 + 修复前后构建：Firefox 的 18 个 SpiderMonkey 漏洞 → Claude Mythos Preview 做出 **14 个 PoC**，其中 **8 个在约 12 小时内**做成可读沙箱外文件的代码执行利用（**第一个不到 1 小时**，而对应的 Firefox 148 发布在 18 天后）。闭源 Windows：2026 年 1–2 月的 21 个内核提权漏洞 → **18 个 PoC、8 条完整提权链**，总成本约 **$15,700（单个约 $2,000）**。**微软评为「不太可能被利用」的 14 个里有 13 个也做出了 PoC**。同时指出 Windows Autopatch 铺到 9 成要 7 天、强制重启在第 11 天

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
| 1 | red.anthropic.com | <https://red.anthropic.com/2026/n-days/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-06-09`（原文：2026-06-09，精度 `day`） |
| 性质 | 威胁情报报告 `report` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **信息** `info` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-06-09-anthropic-day-hour` |

<sub>**判定依据**：威胁情报报告，汇总多起事件，本身不作为单一事故计数，`severity` 记为 `info`。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**同类条目**：

- `2026-06-15` [UNC6508 经 REDCap 入侵北美研究机构](../../../2026-06/2026-06-15-unc6508-redcap-jing-ru-qin.md)<br>  <sub>UNC6508 breaches North American research institutions via REDCap</sub>
- `2026-06-02` [CleverHans Lab 自适应 AI 蠕虫 PoC](../../../2026-06/2026-06-02-cleverhans-lab-poc.md)<br>  <sub>CleverHans Lab adaptive AI worm PoC</sub>
- `2026-06-24` [macOS.Gaslight：恶意软件反过来对 AI 分析师做提示注入](../../../2026-06/2026-06-24-macos-gaslight-e-yi-ruan-jian.md)<br>  <sub>macOS.Gaslight: malware prompt-injects the AI analyst</sub>
- `2026-06-03` [Anthropic《LLM ATT&CK Navigator》](../../../2026-06/2026-06-03-anthropic-llm-att-ck.md)<br>  <sub>Anthropic, "LLM ATT&CK Navigator"</sub>

---

[← English original](../../../2026-06/2026-06-09-anthropic-day-hour.md) · [2026-06 index](../../../2026-06/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
