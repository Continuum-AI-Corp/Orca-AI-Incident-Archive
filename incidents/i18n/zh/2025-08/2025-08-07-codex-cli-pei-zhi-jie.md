---
id: 2025-08-07-codex-cli-pei-zhi-jie
lang: zh
source: incidents/2025-08/2025-08-07-codex-cli-pei-zhi-jie.md
title: "OpenAI Codex CLI 配置劫持"
summary: |
  CVE-2025-61260，CVSS 9.8。Codex 自动加载项目本地 `.env` 与 `.codex/config.toml` 而不需用户确认，可嵌入立即执行的任意命令。影响 ≤ v0.23.0，08-20 修复
---

# OpenAI Codex CLI 配置劫持

<sub>OpenAI Codex CLI config hijack</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## 概要

CVE-2025-61260，CVSS 9.8。Codex 自动加载项目本地 `.env` 与 `.codex/config.toml` 而不需用户确认，可嵌入立即执行的任意命令。影响 ≤ v0.23.0，08-20 修复

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
| 1 | GHSA-xrxf-jgv3-qmrm | <https://github.com/advisories/GHSA-xrxf-jgv3-qmrm> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-08-07`（原文：2025-08-07，精度 `day`） |
| 性质 | 漏洞披露 `vulnerability` |
| 类型 | [`SANDBOX`](../../../../taxonomy/types.md#sandbox) 沙箱逃逸 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-08-07-codex-cli-pei-zhi-jie` |

<sub>**判定依据**：漏洞披露，截至归档未见在野利用证据，故 `real_harm: false`。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[前沿模型自主越界](../../../../topics/eval-escapes.md)

**同类条目**：

- `2025-08-01` [Cursor CurXecute（CVE-2025-54135）](../../../2025-08/2025-08-01-cursor-curxecute.md)<br>  <sub>Cursor CurXecute (CVE-2025-54135)</sub>
- `2025-07-21` [Claude Code hooks RCE](../../../2025-07/2025-07-21-claude-code-hooks-rce.md)<br>  <sub>Claude Code hooks RCE</sub>
- `2025-07-28` [Gemini CLI 静默代码执行](../../../2025-07/2025-07-28-gemini-cli-jing-mo-dai.md)<br>  <sub>Gemini CLI silent code execution</sub>
- `2025-12-06` [IDEsaster](../../../2025-12/2025-12-06-idesaster.md)<br>  <sub>IDEsaster</sub>

---

[← English original](../../../2025-08/2025-08-07-codex-cli-pei-zhi-jie.md) · [2025-08 index](../../../2025-08/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
