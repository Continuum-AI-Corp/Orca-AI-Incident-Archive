---
id: 2025-11-05-gtig-promptflux-promptsteal
lang: zh
source: incidents/2025-11/2025-11-05-gtig-promptflux-promptsteal.md
title: "GTIG：PROMPTFLUX / PROMPTSTEAL"
summary: |
  **首次发现在运行时调用 LLM 的恶意软件家族**。**PROMPTSTEAL** 由俄 **APT28（FROZENLAKE）** 在**对乌克兰的实战中**使用，经 Hugging Face API 调 **Qwen2.5-Coder-32B-Instruct** 动态生成命令；**PROMPTFLUX**（2025-06 首见）为 VBScript dropper，调 Gemini API 请求混淆与规避技术，**仍在开发/测试阶段，不具备实际攻陷能力**。另发现攻击者用「CTF 参赛学生」「安全研究员」等托词绕过 Gemini 护栏
---

# GTIG：PROMPTFLUX / PROMPTSTEAL

<sub>GTIG: PROMPTFLUX / PROMPTSTEAL</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

**首次发现在运行时调用 LLM 的恶意软件家族**。**PROMPTSTEAL** 由俄 **APT28（FROZENLAKE）** 在**对乌克兰的实战中**使用，经 Hugging Face API 调 **Qwen2.5-Coder-32B-Instruct** 动态生成命令；**PROMPTFLUX**（2025-06 首见）为 VBScript dropper，调 Gemini API 请求混淆与规避技术，**仍在开发/测试阶段，不具备实际攻陷能力**。另发现攻击者用「CTF 参赛学生」「安全研究员」等托词绕过 Gemini 护栏

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
| 1 | GTIG PDF | <https://services.google.com/fh/files/misc/advances-in-threat-actor-usage-of-ai-tools-en.pdf> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-11-05`（原文：2025-11-05，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-11-05-gtig-promptflux-promptsteal` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**同类条目**：

- `2025-11-13` [GTG-1002：首起 AI 自主编排的网络间谍行动](../../../2025-11/2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md)<br>  <sub>GTG-1002: first AI-orchestrated cyber-espionage campaign</sub>
- `2025-11-03` [SesameOp](../../../2025-11/2025-11-03-sesameop.md)<br>  <sub>SesameOp</sub>
- `2025-12-28` [墨西哥政府入侵行动启动](../../../2025-12/2025-12-28-mexico-government-intrusion-begins.md)<br>  <sub>Mexico government intrusion campaign begins</sub>
- `2025-10-07` [OpenAI 十月威胁报告](../../../2025-10/2025-10-07-shi-wei-xie-bao-gao.md)<br>  <sub>OpenAI October threat report</sub>

---

[← English original](../../../2025-11/2025-11-05-gtig-promptflux-promptsteal.md) · [2025-11 index](../../../2025-11/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
