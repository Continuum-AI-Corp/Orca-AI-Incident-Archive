---
id: 2026-01-01-ot-claude-code
lang: zh
source: incidents/2026-01/2026-01-01-ot-claude-code.md
title: "墨西哥某供水公司 OT 网络被 Claude Code 侦察喷洒"
summary: |
  墨西哥战役的一个分支：Claude Code 对某供水公司的 OT 网络做了侦察与凭据喷洒，属关键基础设施接触。
---

# 墨西哥某供水公司 OT 网络被 Claude Code 侦察喷洒

<sub>Claude Code sprays credentials at a Mexican water utility's OT network</sub>

![severity: low](https://img.shields.io/badge/severity-low-8C6A6A?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

墨西哥战役的一个分支：Claude Code 对某供水公司的 OT 网络做了侦察与凭据喷洒，属关键基础设施接触。

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
| 1 | SOCRadar | <https://socradar.io/blog/mexican-government-breach-claude-chatgpt/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-01-01`（原文：2026-01-01，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **低** `low` |
| 可信度 | **B** — 研究机构或主流媒体，有可核查细节 |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [拉美](../../../../regions/latam.md) |
| 档案编号 | `2026-01-01-ot-claude-code` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `low`：背景性条目，保留用于时间线连续性。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**同类条目**：

- `2026-02-20` [AI 增强型威胁方批量攻陷 600+ FortiGate](../../../2026-02/2026-02-20-fortigate-600-devices-compromised.md)<br>  <sub>AI-augmented actor compromises 600+ FortiGate devices</sub>
- `2026-02-25` [墨西哥 9 个政府机构被攻陷](../../../2026-02/2026-02-25-mexico-nine-agencies-breached.md)<br>  <sub>Nine Mexican government agencies breached</sub>
- `2026-02-28` [CodeWall 攻破麦肯锡 "Lilli" 内部 AI 平台](../../../2026-02/2026-02-28-codewall-breaches-mckinsey-lilli.md)<br>  <sub>CodeWall breaches McKinsey's internal "Lilli" AI platform</sub>
- `2025-12-28` [墨西哥政府入侵行动启动](../../../2025-12/2025-12-28-mexico-government-intrusion-begins.md)<br>  <sub>Mexico government intrusion campaign begins</sub>

---

[← English original](../../../2026-01/2026-01-01-ot-claude-code.md) · [2026-01 index](../../../2026-01/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
