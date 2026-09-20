---
id: 2026-09-17-plugin4shell-coding-agents
lang: zh
source: incidents/2026-09/2026-09-17-plugin4shell-coding-agents.md
title: "Plugin4Shell：零点击 RCE 链打击四款 AI 编码 agent"
summary: |
  **AIR Security 披露 Plugin4Shell**：一个影响四款主流 AI 编码 agent 的**零点击远程代码执行（RCE）**缺陷——**Claude Code、OpenAI Codex、GitHub Copilot 与 Gemini CLI**。该链路不攻击模型本身，而是**滥用托管 agent 插件的可信市场**并**绕过 SHA-pinning 防护**，使投毒插件能以开发者权限执行代码；**披露时四款产品中仍有两款无补丁可用**，暂无在野利用报告
---

# Plugin4Shell：零点击 RCE 链打击四款 AI 编码 agent

<sub>Plugin4Shell: a zero-click RCE chain hits four AI coding agents</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## 概要

**AIR Security 披露 Plugin4Shell**：一个影响四款主流 AI 编码 agent 的**零点击远程代码执行（RCE）**缺陷——**Claude Code、OpenAI Codex、GitHub Copilot 与 Gemini CLI**。该链路不攻击模型本身，而是**滥用托管 agent 插件的可信市场**并**绕过 SHA-pinning 防护**，使投毒插件能以开发者权限执行代码；**披露时四款产品中仍有两款无补丁可用**，暂无在野利用报告

## 攻击链

```mermaid
flowchart LR
    E["投毒插件发布到可信的 agent 插件市场"]:::entry
    S0["agent 加载插件；SHA-pinning 防护被绕过（Plugin4Shell）"]:::step
    I["以开发者权限实现零点击代码执行"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 详情

**机制。** Plugin4Shell 瞄准的是**插件供应链**而非模型本身：四款 agent 都会从开发者被训练去信任的市场加载扩展，而该链路**绕过了用于把扩展锁定到已审核版本的 SHA-pinning 控制**。恶意或被攻陷的插件随后在开发者环境中**无需任何用户交互**（「零点击」）执行——之所以被形容为「拿到王国的钥匙」，是因为编码 agent 通常持有源码访问权、凭证与 shell 权限。

**披露时的状态。** AIR Security 已向全部受影响厂商报告；据媒体报道，**研究发布时四款产品中仍有两款没有补丁**。暂无在野利用报告。

**为什么重要。** 它把 9 月的 agent 供应链发现潮（GitSpawn 的恶意 `.git/config`、RubyGems 的 GemStuffer 滥用）**从配置文件与注册表扩展到了插件市场**；且发生在 Hacktron 链展示 agent 周边工具可迅速触达生产系统之后数日。实操建议不变但范围更宽：对 agent 加载的内容做固定与校验、收窄其凭证、把插件市场当作未认证输入通道。

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | The Register | <https://www.theregister.com/security/2026/09/17/ai-coding-agents-0-click-rce-flaw-could-hand-attackers-keys-to-the-kingdom/5297335> |
| 2 | Help Net Security | <https://www.helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability/> |
| 3 | Cybersecurity News | <https://cybersecuritynews.com/plugin4shell-zero-click-rce/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-09-17`（原文：2026-09-17，精度 `day`） |
| 性质 | 漏洞披露 `vulnerability` |
| 类型 | [`SUPPLY`](../../../../taxonomy/types.md#supply) 供应链投毒 |
| 严重度 | **高** `high` |
| 可信度 | **B** — 研究机构或主流媒体，细节可核查 |
| 真实伤害 | 无 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-09-17-plugin4shell-coding-agents` |

<sub>**判定依据**：安全研究机构披露的漏洞；披露时无已知在野利用（两款产品未修复），因此 `real_harm: false`。定级 `high`：经由可信通道对四款广泛部署的 agent 实现零点击 RCE。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 供应链投毒](../../../../topics/agent-supply-chain.md)

**同类条目**：

- `2026-09-18` [研究员用 Claude 在漏洞赏金中攻破 OpenAI 内部系统](../../../2026-09/2026-09-18-hacktron-claude-openai-hack.md)<br>  <sub>Researchers used Claude to hack OpenAI's internal systems in a bug-bounty chain</sub>
- `2026-09-01` [GitSpawn：恶意 `.git/config` 让 7 款编码 agent 在联系模型之前就执行攻击者代码](../../../2026-09/2026-09-01-gitspawn-git-config-pre-model-rce.md)<br>  <sub>GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted</sub>
- `2026-09-11` [研究人员把 OpenAI agent 与 RubyGems「GemStuffer」战役关联起来](../../../2026-09/2026-09-11-rubygems-gemstuffer.md)<br>  <sub>Researchers link OpenAI agents to the RubyGems "GemStuffer" campaign</sub>

---

[← English original](../../../2026-09/2026-09-17-plugin4shell-coding-agents.md) · [2026-09 index](../../../2026-09/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
