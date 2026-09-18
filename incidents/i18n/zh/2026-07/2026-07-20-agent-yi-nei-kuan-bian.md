---
id: 2026-07-20-agent-yi-nei-kuan-bian
lang: zh
source: incidents/2026-07/2026-07-20-agent-yi-nei-kuan-bian.md
title: "一周内 4 款编码 agent 爆 6 个沙箱逃逸"
summary: |
  Pillar Security：Cursor、OpenAI Codex CLI、Google Gemini CLI、Google Antigravity。共同模式：**agent 自己老实待在限制内，但改写了宿主之后会信任并执行的文件** —— Docker socket（三家共有，GHSA-v4xv-rqh3-w9mc）、Cursor 的 virtualenv 解释器（GHSA-p9g2-cr55-cw9c）、Git fsmonitor、工作区 `.claude` hook 配置（CVE-2026-48124）、Codex CLI 只信命令名不查参数的白名单、Antigravity 的 macOS Seatbelt 拒绝列表绕过与 `.vscode` 任务配置绕过安全模式。Cursor 3.0.0 / Codex CLI v0.95.0 修复；Google 视为普通漏洞但认为需社工或仓库信任前提。**无在野利用报告**
---

# 一周内 4 款编码 agent 爆 6 个沙箱逃逸

<sub>Six sandbox escapes across four coding agents in one week</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## 概要

Pillar Security：Cursor、OpenAI Codex CLI、Google Gemini CLI、Google Antigravity。共同模式：**agent 自己老实待在限制内，但改写了宿主之后会信任并执行的文件** —— Docker socket（三家共有，GHSA-v4xv-rqh3-w9mc）、Cursor 的 virtualenv 解释器（GHSA-p9g2-cr55-cw9c）、Git fsmonitor、工作区 `.claude` hook 配置（CVE-2026-48124）、Codex CLI 只信命令名不查参数的白名单、Antigravity 的 macOS Seatbelt 拒绝列表绕过与 `.vscode` 任务配置绕过安全模式。Cursor 3.0.0 / Codex CLI v0.95.0 修复；Google 视为普通漏洞但认为需社工或仓库信任前提。**无在野利用报告**

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
| 1 | Pillar Security | <https://www.pillar.security/blog/the-week-of-sandbox-escapes> |
| 2 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/cursor-codex-gemini-cli-antigravity-hit-by-sandbox-escapes/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-07-20`（原文：2026-07-20，精度 `day`） |
| 性质 | 研究演示 `research` |
| 类型 | [`SANDBOX`](../../../../taxonomy/types.md#sandbox) 沙箱逃逸 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-07-20-agent-yi-nei-kuan-bian` |

<sub>**判定依据**：研究机构或厂商的受控演示，`real_harm: false`；收录是为了标记攻击面何时被公开。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[前沿模型自主越界](../../../../topics/eval-escapes.md)

**同类条目**：

- `2026-07-01` [DuneSlide：Cursor 零点击沙箱逃逸](../../../2026-07/2026-07-01-duneslide-cursor-ling-dian-ji.md)<br>  <sub>DuneSlide: zero-click sandbox escape in Cursor</sub>
- `2026-07-09` [GhostApproval：6 款 AI 编码助手共有的审批绕过](../../../2026-07/2026-07-09-ghostapproval-kuan-bian-ma-zhu.md)<br>  <sub>GhostApproval: an approval bypass shared by six AI coding assistants</sub>
- `2026-07-01` [AWS Kiro：让它总结一个网页，就能拿到 RCE（CVE-2026-10591）](../../../2026-07/2026-07-01-aws-kiro-rce.md)<br>  <sub>AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)</sub>
- `2026-07-22` [SharedRoot：Claude Cowork 从 Linux VM 逃到 macOS 宿主](../../../2026-07/2026-07-22-sharedroot-claude-cowork-linux.md)<br>  <sub>SharedRoot: Claude Cowork escapes a Linux VM onto the macOS host</sub>

---

[← English original](../../../2026-07/2026-07-20-agent-yi-nei-kuan-bian.md) · [2026-07 index](../../../2026-07/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
