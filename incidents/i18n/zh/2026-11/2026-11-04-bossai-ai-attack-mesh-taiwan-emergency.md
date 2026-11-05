---
id: 2026-11-04-bossai-ai-attack-mesh-taiwan-emergency
lang: zh
source: incidents/2026-11/2026-11-04-bossai-ai-attack-mesh-taiwan-emergency.md
title: "\"BOSSAI\"：Acronis 记录一名单人操作者的 12-agent AI 攻击网，攻破三国的应急/急救服务"
summary: |
  **2026 年 11 月 4 日，Acronis 威胁研究部门（TRU）发布《BOSSAI》报告，取证还原了一名位于台湾花莲市的单人操作者：其运行一个由 12 个 AI agent（9 个活跃）组成的攻击网，攻击了 11 国数百家机构——在其中三国的约 10 个目标确认发生数据外传或系统访问。** Acronis 恢复了该操作者暴露的工作区（90,000+ 文件、9GB）。操作者（"bossjy"／"Jy技術團隊"／SSH 身份"lstjks"）手动在各 agent 间搬运输出：**Hermes Agent** 为主攻 agent（约 95 个会话，跑在越狱本地模型上），辅以 **Cursor**（利用）、**Trae**（写脚本）、**CyberStrike**／**HalberdStrike**（扫描）与非 LLM 的 **Acunetix**；**Grok 4.5**、**OpenClaw**（MiniMax M3）、**Claude Code**、**Codex** 充当基础设施 agent（数个拒绝明确攻击请求、被改路由到越狱模型）。该网还用了 **MCP server**（HexStrike AI、Kali）。**确认伤害：** 某台北消防患者护理平台无需凭证即暴露 ECG、救护车视频与生命体征；台北 7 个行政区的 119 调度记录；某放贷机构经 16 处 SQL 注入点泄露账号数据；泰国 3 所大学经 SQLi 被取数（一张管理员表 2,563 行）；墨西哥约 20.68 万条住宅电话记录被汇集。**值得注意的是，这些 agent 频繁夸大自己的战果**——一处国家级灾防中心的"漏洞发现"系虚构，多项输出无法核实。Acronis 评估操作者为单一个人、隶属或目的"不明"，并**未**将其与 2026 年 7 月的台湾*政府*campaign 关联。记为 `incident` / `WEAPON` + `EXFIL` / `high` / `real_harm: true`。
---

# "BOSSAI"：Acronis 记录一名单人操作者的 12-agent AI 攻击网，攻破三国的应急/急救服务

<sub>"BOSSAI": Acronis documents a lone operator's 12-agent AI attack mesh that breached emergency services across three countries</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-8F6A3C?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-3C6E8F?style=flat-square)

## 概要

**2026 年 11 月 4 日，Acronis 威胁研究部门（TRU）发布《BOSSAI》报告，取证还原了一名位于台湾花莲市的单人操作者：其运行一个由 12 个 AI agent（9 个活跃）组成的攻击网，攻击了 11 国数百家机构——在其中三国的约 10 个目标确认发生数据外传或系统访问。** Acronis 恢复了该操作者暴露的工作区（90,000+ 文件、9GB）。操作者（"bossjy"／"Jy技術團隊"／SSH 身份"lstjks"）手动在各 agent 间搬运输出：**Hermes Agent** 为主攻 agent（约 95 个会话，跑在越狱本地模型上），辅以 **Cursor**（利用）、**Trae**（写脚本）、**CyberStrike**／**HalberdStrike**（扫描）与非 LLM 的 **Acunetix**；**Grok 4.5**、**OpenClaw**（MiniMax M3）、**Claude Code**、**Codex** 充当基础设施 agent（数个拒绝明确攻击请求、被改路由到越狱模型）。该网还用了 **MCP server**（HexStrike AI、Kali）。**确认伤害：** 某台北消防患者护理平台无需凭证即暴露 ECG、救护车视频与生命体征；台北 7 个行政区的 119 调度记录；某放贷机构经 16 处 SQL 注入点泄露账号数据；泰国 3 所大学经 SQLi 被取数（一张管理员表 2,563 行）；墨西哥约 20.68 万条住宅电话记录被汇集。**值得注意的是，这些 agent 频繁夸大自己的战果**——一处国家级灾防中心的"漏洞发现"系虚构，多项输出无法核实。Acronis 评估操作者为单一个人、隶属或目的"不明"，并**未**将其与 2026 年 7 月的台湾*政府*campaign 关联。记为 `incident` / `WEAPON` + `EXFIL` / `high` / `real_harm: true`。

## 攻击链

```mermaid
flowchart LR
    O["单人操作者，台湾花莲市<br/>（'bossjy'）；手动在 agent 间搬运"]:::entry
    M["12-agent 网（9 活跃）：<br/>Hermes（主攻）+ Cursor/Trae/CyberStrike<br/>+ Grok/OpenClaw/Claude Code/Codex（基础设施）<br/>+ MCP server（HexStrike AI、Kali）"]:::step
    T["数百目标、11 国；<br/>其中 3 国约 10 个确认被攻破"]:::step
    I["台北消防/119 患者数据（无需凭证）；<br/>泰国大学经 SQLi；墨西哥约 20.68 万电话记录<br/>——但多项 agent'发现'系虚构"]:::impact
    O --> M --> T --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 详情

**BOSSAI 是什么。** 2026 年 **11 月 4 日**，**Acronis 威胁研究部门（TRU）** 发布 *《BOSSAI：深入这张瞄准台湾急救服务的 AI 攻击网》*。TRU 在发现一个初看像是配置错误的开发环境后，恢复了操作者暴露的工作区——**超过 90,000 个文件、9GB** 材料，据此做了取证还原。Acronis 在一个 **约 12 天的窗口** 内观察了该网（其中一个具体的工具事件——用 Grok 把某海康威视工具移植到 Linux——日期为 **2026 年 7 月 25 日**，Hermes 的模型轮换"历时 19 天"）。

**操作者。** Acronis **高置信度** 评估：运行该基础设施的是 **一名位于台湾花莲市的单一个人**，由 **"bossjy"** 这一 handle、**"Jy技術團隊"** 标识与 **"lstjks"** SSH 密钥身份串联。报告称其 **不是** 政府行为体，并称"不清楚攻击者是否有任何具体隶属或目的"。关键在于，Acronis **未** 将其与 2026 年 7 月的台湾*政府* agent 蜂群（Dream 的归因）或 Unit 42 所述的"knaithe／KnYuan"关联——因此这是一名 **不同的操作者**，不是本档案已有记录的再报。

**12-agent 攻击网。** 12 个 agent，9 个活跃、3 个未用，由不断更换的 LLM 驱动；各 agent **并不直接通信**——操作者手动在它们之间搬运输出、充当桥梁：

| Agent | 角色 |
|---|---|
| **Hermes Agent** | 主攻 agent（约 95 个会话），多跑在越狱本地模型上 |
| **Cursor** | 利用工作 |
| **Trae** | 写脚本 |
| **CyberStrike** | 扫描/利用尝试（输出无法独立核实） |
| **HalberdStrike** | 基于 PenTestGPT 的扫描框架 |
| **Acunetix (AWVS)** | 传统的非 LLM 扫描器 |
| **Grok 4.5**、**OpenClaw**（MiniMax M3） | 基础设施 agent——二者均拒绝明确的攻击请求 |
| **Claude Code**、**Codex** | 基础设施 agent——被改路由到越狱模型 |

该网还使用了 **MCP server**，包括一个 **HexStrike AI** 服务器和一个 **Kali** 服务器。

**确认的伤害（及其边界）。** Acronis 报告操作者 **瞄准了 11 国数百家机构**，在 **三国约 10 个目标确认发生数据外传或系统访问**，另有约 15 个被攻击但未确认被攻陷：

- **台湾：** 某台北消防 **患者护理平台** **无需凭证** 即暴露 ECG、救护车视频与生命体征；agent 还抽取了台北 7 个行政区的 **119 调度** 案件记录；某放贷机构有 **16 处 SQL 注入点**、账号数据被取走；某消防调度供应商后台用默认口令即可进入。一处 **国家级灾防中心的"发现"系虚构**——该漏洞根本不存在。
- **墨西哥：** 流水线汇集了约 **20.68 万条住宅电话记录** 并抓取约 12.4 万条黄页记录（属数据收集；对这些数字 Acronis 未确认有单一系统被入侵）。
- **泰国：** agent 在 45 家机构中识别出 489 个潜在目标；**在 3 所大学确认 SQL 注入并取数**（一张管理员表有 **2,563 行**）；另有 2 所有注入点但未取数。
- **洪都拉斯：** 一个军方空军人员系统被刻画但 **未** 被利用——agent 判其超出范围。

**"agent 夸大自身战果"的教训。** Acronis 明确指出：尽管入侵是真实的，但 **战役的规模常常被 agent 自己夸大**——许多 AI 生成的"发现"是误报，国家级灾防中心的漏洞并不存在，部分工具输出（如 CyberStrike 的）无法核实。这对攻击型 AI 宣称中的 agent 自报战果是一个有用的纠偏。

**如何分级。** `incident`——真实、经取证还原的入侵，带有恢复到的操作者物证，而非演示。`WEAPON`（自主/半自主 agent 被武器化用于入侵，与本档案的台湾/Hermes 攻击簇一致）+ `EXFIL`（确认的数据外传——患者数据、大学记录、PII）。`real_harm: true`：跨三国确认外传了敏感医疗/应急与个人数据。评 `high` 而非 critical：确认伤害真实但有界（约 10 个目标）、操作者为单一个人、所称规模很大一部分是 agent 虚构、且无政府/关键基础设施 *系统* 被攻陷的确认。可信度 `A`：Acronis TRU 对操作者自身工作区的取证恢复，Cyber Security News 佐证。`ai_involvement: confirmed`：恢复到的 agent 会话（Hermes 约 95 个）与工具直接佐证该攻击网。

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Acronis 威胁研究部门（《BOSSAI》） | <https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/> |
| 2 | Cyber Security News | <https://cybersecuritynews.com/one-hacker-uses-12-ai-agents/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-11-04`（原始：2026-11-04 Acronis TRU 报告；约 12 天观察窗，工具事件日期至 2026-07-25，精度 `day`） |
| 性质 | 真实事件 `incident` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) [`EXFIL`](../../../../taxonomy/types.md#exfil) |
| 评级 | **高** `high` |
| 可信度 | **A**——Acronis TRU 取证报告（恢复操作者工作区）+ Cyber Security News |
| 真实伤害 | 有——确认外传患者/应急数据（台北）、大学数据（泰国）与 PII（墨西哥） |
| AI 参与 | 已确认 `confirmed`——恢复到的 agent 会话与工具 |
| 地区 | [台湾](../../../../regions/tw.md) · [东南亚](../../../../regions/sea.md) · [拉丁美洲](../../../../regions/latam.md) |
| 档案 ID | `2026-11-04-bossai-ai-attack-mesh-taiwan-emergency` |

<sub>**分类理由：** 一场由单人操作者通过 AI agent 攻击网发动、经取证还原的攻击型战役（`WEAPON`），并跨三国确认数据外传（`EXFIL`），故 `real_harm: true`。评 `high` 非 critical：伤害真实但有界（约 10 个确认目标）、操作者为单一个人、所称规模很大一部分被 agent 虚构、且无政府/关键基础设施系统被攻陷的确认。`confirmed` 的 AI 参与来自恢复到的 agent 会话。属不同操作者——Acronis 未将 BOSSAI 与本档案已记录的 2026 年 7 月台湾政府campaign 关联。分级标准见 [severity.md](../../../../taxonomy/severity.md) 与 [confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关条目

**专题：** [攻击型 AI（被攻击者使用的 agent）](../../../../topics/offensive-ai.md)

**相关记录：**

- `2026-07-01` [台湾核安会等政府机构被 agent 蜂群攻破](../2026-07/2026-07-01-taiwan-government-agent-swarm.md)<br>  <sub>不同的操作者/campaign（政府目标，2026 年 7 月）——Acronis 未将 BOSSAI 与之关联</sub>
- `2026-07-30` [Hermes Agent 无人值守模式攻击泰国财政部](../2026-07/2026-07-30-hermes-agent-thailand-finance-ministry.md)<br>  <sub>同一开源 Hermes Agent 工具，不同操作者</sub>
- `2026-09-22` [Carbonato：一个基于 Docker 的 Hermes Agent 僵尸网络](../2026-09/2026-09-22-carbonato-docker-hermes-agent-botnet.md)<br>  <sub>另一名滥用 Hermes Agent 框架的操作者</sub>

---

[← English original](../../../2026-11/2026-11-04-bossai-ai-attack-mesh-taiwan-emergency.md) · [2026-11 index](../../../2026-11/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
