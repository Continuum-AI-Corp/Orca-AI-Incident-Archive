---
id: 2026-06-24-macos-gaslight-e-yi-ruan-jian
lang: zh
source: incidents/2026-06/2026-06-24-macos-gaslight-e-yi-ruan-jian.md
title: "macOS.Gaslight：恶意软件反过来对 AI 分析师做提示注入"
summary: |
  SentinelLABS：朝鲜相关 Rust 植入体内含 **3.5KB 数据块**，用 Markdown 代码围栏和 `{{DATA}}` 令牌**模仿 LLM 分析平台的提示结构**，排布 **38 条伪造系统消息**（token 过期、内存不足、磁盘耗尽、连续失败）与伪装的漏洞/静态分析警告，目的是让 LLM 辅助的初步分类**中止、打断或拒绝**。比 2025 年 Check Point 那个单条指令的 Windows 样本高一个量级。C2 走 Telegram Bot API
---

# macOS.Gaslight：恶意软件反过来对 AI 分析师做提示注入

<sub>macOS.Gaslight: malware prompt-injects the AI analyst</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

SentinelLABS：朝鲜相关 Rust 植入体内含 **3.5KB 数据块**，用 Markdown 代码围栏和 `{{DATA}}` 令牌**模仿 LLM 分析平台的提示结构**，排布 **38 条伪造系统消息**（token 过期、内存不足、磁盘耗尽、连续失败）与伪装的漏洞/静态分析警告，目的是让 LLM 辅助的初步分类**中止、打断或拒绝**。比 2025 年 Check Point 那个单条指令的 Windows 样本高一个量级。C2 走 Telegram Bot API

## 攻击链

```mermaid
flowchart LR
    E["攻击者 + 越狱话术"]:::entry
    S0["LLM 编排器驱动子 agent 集群"]:::step
    I["目标系统被攻陷<br/><i>（实验室演示 · 无真实受害方）</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | SentinelLABS | <https://www.sentinelone.com/labs/macos-gaslight-rust-backdoor-turns-prompt-injection-on-the-analyst-not-the-sandbox/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-06-24`（原文：2026-06-24，精度 `day`） |
| 性质 | 研究演示 `research` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **中** `medium` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-06-24-macos-gaslight-e-yi-ruan-jian` |

<sub>**判定依据**：研究机构或厂商的受控演示，`real_harm: false`；收录是为了标记攻击面何时被公开。 判 `medium`：受控演示、中等缺陷，或单用户 / 单机范围的事故。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**同类条目**：

- `2026-06-15` [UNC6508 经 REDCap 入侵北美研究机构](../../../2026-06/2026-06-15-unc6508-redcap-jing-ru-qin.md)<br>  <sub>UNC6508 breaches North American research institutions via REDCap</sub>
- `2026-06-02` [CleverHans Lab 自适应 AI 蠕虫 PoC](../../../2026-06/2026-06-02-cleverhans-lab-poc.md)<br>  <sub>CleverHans Lab adaptive AI worm PoC</sub>
- `2026-06-03` [Anthropic《LLM ATT&CK Navigator》](../../../2026-06/2026-06-03-anthropic-llm-att-ck.md)<br>  <sub>Anthropic, "LLM ATT&CK Navigator"</sub>
- `2026-06-09` [Anthropic：N-day 实为「N-hour」](../../../2026-06/2026-06-09-anthropic-day-hour.md)<br>  <sub>Anthropic: N-day is really "N-hour"</sub>

---

[← English original](../../../2026-06/2026-06-24-macos-gaslight-e-yi-ruan-jian.md) · [2026-06 index](../../../2026-06/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
