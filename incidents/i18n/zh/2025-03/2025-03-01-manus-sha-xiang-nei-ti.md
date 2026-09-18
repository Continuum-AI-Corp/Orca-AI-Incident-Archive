---
id: 2025-03-01-manus-sha-xiang-nei-ti
lang: zh
source: incidents/2025-03/2025-03-01-manus-sha-xiang-nei-ti.md
title: "Manus AI 沙箱内提示与运行时代码泄露"
summary: |
  用户只要让 Manus 输出内部目录（如 `/opt/.manus/`）的内容，即可取回部分系统提示与运行时代码。联合创始人兼首席科学家季逸超回应称**用户本就可直接访问沙箱**、每个会话沙箱隔离、沙箱内代码只负责接收指令因此只做了轻度混淆，并称工具设计本就不保密。
  💡 收录理由：这是 2025 年上半年少见的**中国 agent 产品自身的边界问题**，且厂商回应把「沙箱可访问」当作设计前提 —— 与后来 OpenClaw 的风险模型同源
---

# Manus AI 沙箱内提示与运行时代码泄露

<sub>Manus AI leaks in-sandbox prompts and runtime code</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## 概要

用户只要让 Manus 输出内部目录（如 `/opt/.manus/`）的内容，即可取回部分系统提示与运行时代码。联合创始人兼首席科学家季逸超回应称**用户本就可直接访问沙箱**、每个会话沙箱隔离、沙箱内代码只负责接收指令因此只做了轻度混淆，并称工具设计本就不保密。

💡 收录理由：这是 2025 年上半年少见的**中国 agent 产品自身的边界问题**，且厂商回应把「沙箱可访问」当作设计前提 —— 与后来 OpenClaw 的风险模型同源

## 攻击链

```mermaid
flowchart LR
    E["评测 / 容器环境"]:::entry
    S0["残留的出网路径"]:::step
    I["逃逸到真实系统<br/><i>（漏洞已披露 · 未见在野利用）</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | AIBase | <https://www.aibase.com/news/16138> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-03-01`（原文：2025-03，精度 `month`） |
| 性质 | 漏洞披露 `vulnerability` |
| 类型 | [`SANDBOX`](../../../../taxonomy/types.md#sandbox) 沙箱逃逸 |
| 严重度 | **中** `medium` |
| 可信度 | **B** — 研究机构或主流媒体，有可核查细节 |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [中国](../../../../regions/cn.md) |
| 档案编号 | `2025-03-01-manus-sha-xiang-nei-ti` |

<sub>**判定依据**：漏洞披露，截至归档未见在野利用证据，故 `real_harm: false`。 判 `medium`：受控演示、中等缺陷，或单用户 / 单机范围的事故。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[前沿模型自主越界](../../../../topics/eval-escapes.md)

**同类条目**：

- `2025-01-31` [GitHub Copilot 双漏洞](../../../2025-01/2025-01-31-github-copilot-shuang-lou-dong.md)<br>  <sub>Two GitHub Copilot flaws</sub>
- `2025-07-21` [Claude Code hooks RCE](../../../2025-07/2025-07-21-claude-code-hooks-rce.md)<br>  <sub>Claude Code hooks RCE</sub>
- `2025-07-28` [Gemini CLI 静默代码执行](../../../2025-07/2025-07-28-gemini-cli-jing-mo-dai.md)<br>  <sub>Gemini CLI silent code execution</sub>
- `2025-08-01` [Cursor CurXecute（CVE-2025-54135）](../../../2025-08/2025-08-01-cursor-curxecute.md)<br>  <sub>Cursor CurXecute (CVE-2025-54135)</sub>

---

[← English original](../../../2025-03/2025-03-01-manus-sha-xiang-nei-ti.md) · [2025-03 index](../../../2025-03/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
