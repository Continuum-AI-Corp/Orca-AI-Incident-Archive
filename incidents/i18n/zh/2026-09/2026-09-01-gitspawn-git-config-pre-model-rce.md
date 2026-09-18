---
id: 2026-09-01-gitspawn-git-config-pre-model-rce
lang: zh
source: incidents/2026-09/2026-09-01-gitspawn-git-config-pre-model-rce.md
title: "GitSpawn：恶意 .git/config 让 7 款编码 agent 在联系模型之前就执行攻击者代码"
summary: |
  **8 个 Git 配置类缺陷**让被克隆的仓库能通过 **7 款 AI 编码 agent**（含 Claude Code、Codex、Cursor）执行命令，**披露时仍有 4 家未修**。
  最要命的性质：**在恶意仓库里跑某些命令时，攻击者代码的执行发生在「没有提交任何提示、没有调用模型、没有工具批准、没有信任提示」之前 —— 命令在 agent 联系模型之前就已经执行了**。研究者演示把一个仅涉及配置的凭据泄露升级为完整 RCE，收割了 136 个密钥
---

# GitSpawn：恶意 .git/config 让 7 款编码 agent 在联系模型之前就执行攻击者代码

<sub>GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted</sub>

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## 概要

**8 个 Git 配置类缺陷**让被克隆的仓库能通过 **7 款 AI 编码 agent**（含 Claude Code、Codex、Cursor）执行命令，**披露时仍有 4 家未修**。

最要命的性质：**在恶意仓库里跑某些命令时，攻击者代码的执行发生在「没有提交任何提示、没有调用模型、没有工具批准、没有信任提示」之前 —— 命令在 agent 联系模型之前就已经执行了**。研究者演示把一个仅涉及配置的凭据泄露升级为完整 RCE，收割了 136 个密钥

## 攻击链

```mermaid
flowchart LR
    E["被投毒的包 / 仓库 / agent 配置"]:::entry
    S0["开发者或 agent 自动安装"]:::step
    S1["残留的出网路径"]:::step
    I["逃逸到真实系统<br/><i>（实验室演示 · 无真实受害方）</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | THN | <https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-09-01`（原文：2026-09-01，精度 `day`） |
| 性质 | 研究演示 `research` |
| 类型 | [`SUPPLY`](../../../../taxonomy/types.md#supply) 供应链投毒 · [`SANDBOX`](../../../../taxonomy/types.md#sandbox) 沙箱逃逸 |
| 严重度 | **严重** `critical` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-09-01-gitspawn-git-config-pre-model-rce` |

<sub>**判定依据**：研究机构或厂商的受控演示，`real_harm: false`；收录是为了标记攻击面何时被公开。 判 `critical` 但 `real_harm: false`：适用第三条触发条件——**这项研究推翻了一项已被广泛部署的防护假设**，其意义不在于已经造成了多少损失。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 供应链投毒](../../../../topics/agent-supply-chain.md) · [前沿模型自主越界](../../../../topics/eval-escapes.md)

**同类条目**：

- `2026-08-04` [CHAINDROP npm 蠕虫](../../../2026-08/2026-08-04-chaindrop-npm-ru-chong.md)<br>  <sub>CHAINDROP npm worm</sub>
- `2026-08-26` [Trail of Bits：虚拟机关不住有网络能力的 agent](../../../2026-08/2026-08-26-trailofbits-vm-cannot-contain-networked-agents.md)<br>  <sub>Trail of Bits: VMs won't contain cyber-capable agents</sub>
- `2026-08-17` [AI 找到了 AI 参与写的漏洞：Snowflake 的 Jira 令牌](../../../2026-08/2026-08-17-snowflake-jira-zhao-dao-can.md)<br>  <sub>AI finds a flaw AI helped write: Snowflake's Jira token</sub>
- `2026-07-01` [DuneSlide：Cursor 零点击沙箱逃逸](../../../2026-07/2026-07-01-duneslide-cursor-ling-dian-ji.md)<br>  <sub>DuneSlide: zero-click sandbox escape in Cursor</sub>

---

[← English original](../../../2026-09/2026-09-01-gitspawn-git-config-pre-model-rce.md) · [2026-09 index](../../../2026-09/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
