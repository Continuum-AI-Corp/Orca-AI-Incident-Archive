---
id: 2026-06-30-guardfall-agent-shell
lang: zh
source: incidents/2026-06/2026-06-30-guardfall-agent-shell.md
title: "GuardFall：11 个开源 agent 中 10 个可绕过 shell 边界"
summary: |
  Adversa：根因是护栏比对**原始命令字符串**，而 bash 执行前会做引号去除、展开、命令替换 —— **检查的字符串和实际执行的指令不是同一个东西**。5 类绕过：`r''m`、`$IFS`、命令替换、base64 管道给 sh、`find -delete`。**只有 Continue 在默认 IDE 模式下从结构上堵住大部分**。⚠️ 实验室实证，非在野；且需满足「间接提示注入让 LLM 误判」+「自动执行模式开启或沙箱为 local」两个前提
---

# GuardFall：11 个开源 agent 中 10 个可绕过 shell 边界

<sub>GuardFall: 10 of 11 open-source agents can be pushed past their shell boundary</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## 概要

Adversa：根因是护栏比对**原始命令字符串**，而 bash 执行前会做引号去除、展开、命令替换 —— **检查的字符串和实际执行的指令不是同一个东西**。5 类绕过：`r''m`、`$IFS`、命令替换、base64 管道给 sh、`find -delete`。**只有 Continue 在默认 IDE 模式下从结构上堵住大部分**。⚠️ 实验室实证，非在野；且需满足「间接提示注入让 LLM 误判」+「自动执行模式开启或沙箱为 local」两个前提

## 攻击链

```mermaid
flowchart LR
    E["评测 / 容器环境"]:::entry
    S0["残留的出网路径"]:::step
    I["逃逸到真实系统<br/><i>（实验室演示 · 无真实受害方）</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Adversa | <https://adversa.ai/blog/opensource-ai-coding-agents-shell-injection-vulnerability/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-06-30`（原文：2026-06-30，精度 `day`） |
| 性质 | 研究演示 `research` |
| 类型 | [`SANDBOX`](../../../../taxonomy/types.md#sandbox) 沙箱逃逸 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-06-30-guardfall-agent-shell` |

<sub>**判定依据**：研究机构或厂商的受控演示，`real_harm: false`；收录是为了标记攻击面何时被公开。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[前沿模型自主越界](../../../../topics/eval-escapes.md)

**同类条目**：

- `2026-05-08` [Cline Kanban 跨源 WebSocket 劫持（CVE-2026-44211）](../../../2026-05/2026-05-08-cline-kanban-websocket.md)<br>  <sub>Cline Kanban cross-origin WebSocket hijack (CVE-2026-44211)</sub>
- `2026-07-01` [DuneSlide：Cursor 零点击沙箱逃逸](../../../2026-07/2026-07-01-duneslide-cursor-ling-dian-ji.md)<br>  <sub>DuneSlide: zero-click sandbox escape in Cursor</sub>
- `2026-07-09` [GhostApproval：6 款 AI 编码助手共有的审批绕过](../../../2026-07/2026-07-09-ghostapproval-kuan-bian-ma-zhu.md)<br>  <sub>GhostApproval: an approval bypass shared by six AI coding assistants</sub>
- `2026-07-01` [AWS Kiro：让它总结一个网页，就能拿到 RCE（CVE-2026-10591）](../../../2026-07/2026-07-01-aws-kiro-rce.md)<br>  <sub>AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)</sub>

---

[← English original](../../../2026-06/2026-06-30-guardfall-agent-shell.md) · [2026-06 index](../../../2026-06/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
