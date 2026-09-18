---
id: 2025-12-28-mexico-government-intrusion-begins
lang: zh
source: incidents/2025-12/2025-12-28-mexico-government-intrusion-begins.md
title: "墨西哥政府入侵行动启动"
summary: |
  墨西哥政府入侵战役的起点——攻击者开始用 Claude Code 对政府网段做持续侦察，整条战役到 2026-02 才被完整还原。
---

# 墨西哥政府入侵行动启动

<sub>Mexico government intrusion campaign begins</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

墨西哥政府入侵战役的起点——攻击者开始用 Claude Code 对政府网段做持续侦察，整条战役到 2026-02 才被完整还原。

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
| 1 | Bloomberg | <https://www.bloomberg.com/news/articles/2026-02-25/hacker-used-anthropic-s-claude-to-steal-sensitive-mexican-data> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-12-28`（原文：2025-12-末，精度 `part`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **中** `medium` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [拉美](../../../../regions/latam.md) |
| 档案编号 | `2025-12-28-mexico-government-intrusion-begins` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `medium`：受控演示、中等缺陷，或单用户 / 单机范围的事故。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**同类条目**：

- `2025-11-13` [GTG-1002：首起 AI 自主编排的网络间谍行动](../../../2025-11/2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md)<br>  <sub>GTG-1002: first AI-orchestrated cyber-espionage campaign</sub>
- `2025-11-03` [SesameOp](../../../2025-11/2025-11-03-sesameop.md)<br>  <sub>SesameOp</sub>
- `2025-11-05` [GTIG：PROMPTFLUX / PROMPTSTEAL](../../../2025-11/2025-11-05-gtig-promptflux-promptsteal.md)<br>  <sub>GTIG: PROMPTFLUX / PROMPTSTEAL</sub>
- `2026-01-01` [墨西哥某供水公司 OT 网络被 Claude Code 侦察喷洒](../../../2026-01/2026-01-01-ot-claude-code.md)<br>  <sub>Claude Code sprays credentials at a Mexican water utility's OT network</sub>

---

[← English original](../../../2025-12/2025-12-28-mexico-government-intrusion-begins.md) · [2025-12 index](../../../2025-12/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
