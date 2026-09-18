---
id: 2026-03-16-cellshock-biao-ge-gong-ju
lang: zh
source: incidents/2026-03/2026-03-16-cellshock-biao-ge-gong-ju.md
title: "AI 表格工具数据外泄（CellShock）"
summary: |
  PromptArmor：外部数据集里埋指令，诱导 Claude for Excel / Ramp Sheets AI 生成 **`=IMAGE()` 公式**把机密数据发往攻击者服务器。**滥用的是表格的正常功能，所以绕过所有防护**。Anthropic 与 Ramp 引入了警告与用户确认，但仍不充分
---

# AI 表格工具数据外泄（CellShock）

<sub>CellShock: data exfiltration through an AI spreadsheet tool</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## 概要

PromptArmor：外部数据集里埋指令，诱导 Claude for Excel / Ramp Sheets AI 生成 **`=IMAGE()` 公式**把机密数据发往攻击者服务器。**滥用的是表格的正常功能，所以绕过所有防护**。Anthropic 与 Ramp 引入了警告与用户确认，但仍不充分

## 攻击链

```mermaid
flowchart LR
    E["外部内容<br/>邮件 · 文档 · Issue · 网页"]:::entry
    S0["agent 读取并当作指令执行"]:::step
    S1["经厂商可信域外带<br/>图片渲染 · API · 代理"]:::step
    I["数据落入攻击者手中<br/><i>（实验室演示 · 无真实受害方）</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | PromptArmor CellShock | <https://www.promptarmor.com/resources/cellshock-claude-ai-is-excel-lent-at-stealing-data> |
| 2 | PromptArmor Ramp | <https://www.promptarmor.com/resources/ramps-sheets-ai-exfiltrates-financials> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-03-16`（原文：2026-03-16，精度 `day`） |
| 性质 | 研究演示 `research` |
| 类型 | [`IPI`](../../../../taxonomy/types.md#ipi) 间接提示注入 · [`EXFIL`](../../../../taxonomy/types.md#exfil) 数据外泄 |
| 严重度 | **中** `medium` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-03-16-cellshock-biao-ge-gong-ju` |

<sub>**判定依据**：研究机构或厂商的受控演示，`real_harm: false`；收录是为了标记攻击面何时被公开。 判 `medium`：受控演示、中等缺陷，或单用户 / 单机范围的事故。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[零点击数据外泄链](../../../../topics/zero-click-exfil.md)

**同类条目**：

- `2026-03-01` [Claudy Day：claude.ai 三漏洞链](../../../2026-03/2026-03-01-claudy-day-claude-ai.md)<br>  <sub>Claudy Day: a three-flaw chain in claude.ai</sub>
- `2026-02-09` [Clinejection](../../../2026-02/2026-02-09-clinejection.md)<br>  <sub>Clinejection</sub>
- `2026-04-01` [Claude Code GitHub Action 三 CVE：一个 PR 标题偷走 API key](../../../2026-04/2026-04-01-claude-code-github-action.md)<br>  <sub>Three CVEs in the Claude Code GitHub Action: a PR title steals your API key</sub>
- `2026-04-15` [ShareLeak（CVE-2026-21520）+ PipeLeak](../../../2026-04/2026-04-15-shareleak-pipeleak.md)<br>  <sub>ShareLeak (CVE-2026-21520) and PipeLeak</sub>

---

[← English original](../../../2026-03/2026-03-16-cellshock-biao-ge-gong-ju.md) · [2026-03 index](../../../2026-03/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
