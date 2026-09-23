---
id: 2026-09-08-gtig-prompting-to-autonomy
lang: zh
source: incidents/2026-09/2026-09-08-gtig-prompting-to-autonomy.md
title: "GTIG AI 威胁追踪：从提示到自主"
summary: |
  **谷歌威胁情报小组（GTIG）**发布 2026 年第二季度 **AI 威胁追踪**报告，描述*「走在前面的攻击者正从基础提示转向 agent 化 AI 工作流与 AI 驱动的自动化」*。案例沿这条阶梯展开：**UNC6780** 攻陷开发者账号，把合法 MCP 服务器（如 `tiktoken_mcp`）的「投毒分叉」发布到 PyPI；其 **DUSTMAKER** 窃密程序会从 GitHub Actions 运行器进程内存中提取 OIDC 令牌，以合法身份发布带*「有效的、加密签名的 SLSA Build 3 证明」*的后门包——*「这些包会通过 AI 编程 agent 的自动信任检查」*。一个疑似经济动机的攻击者用 AI 编程聊天机器人、一段提示加预置的 markdown agent 指令，在**不到六小时**内策划并执行了一场大规模凭证收割行动：从受害者的云基础设施中窃得数千条凭证，扫描、排障与 IP 轮换全部自主完成。国家背景组织贯穿全篇：中国背景的 **UNC6508** 瞄准专有 AI 研究；朝鲜的 **MIDNIGHT NEPTUNE** 与伊朗的 **CALANQUE ION** 把商用 LLM 嵌进行动链条；GTIG 还处置了一个用 Gemini 设计自动化渗透测试框架的中国相关行为体。报告也记录了今年的 **LLMJacking** 市场——被盗 AI 账号与被劫持算力——以及针对 LLM 的「拒绝诱饵」：DUSTMAKER 的加载器以生物武器与核武器相关文本开头，*「很可能意在让 LLM 安全扫描器失败或跳过分析」*
---

# GTIG AI 威胁追踪：从提示到自主

<sub>GTIG AI threat tracker: from prompting to autonomy</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

**谷歌威胁情报小组（GTIG）**发布 2026 年第二季度 **AI 威胁追踪**报告，描述*「走在前面的攻击者正从基础提示转向 agent 化 AI 工作流与 AI 驱动的自动化」*。案例沿这条阶梯展开：**UNC6780** 攻陷开发者账号，把合法 MCP 服务器（如 `tiktoken_mcp`）的「投毒分叉」发布到 PyPI；其 **DUSTMAKER** 窃密程序会从 GitHub Actions 运行器进程内存中提取 OIDC 令牌，以合法身份发布带*「有效的、加密签名的 SLSA Build 3 证明」*的后门包——*「这些包会通过 AI 编程 agent 的自动信任检查」*。一个疑似经济动机的攻击者用 AI 编程聊天机器人、一段提示加预置的 markdown agent 指令，在**不到六小时**内策划并执行了一场大规模凭证收割行动：从受害者的云基础设施中窃得数千条凭证，扫描、排障与 IP 轮换全部自主完成。国家背景组织贯穿全篇：中国背景的 **UNC6508** 瞄准专有 AI 研究；朝鲜的 **MIDNIGHT NEPTUNE** 与伊朗的 **CALANQUE ION** 把商用 LLM 嵌进行动链条；GTIG 还处置了一个用 Gemini 设计自动化渗透测试框架的中国相关行为体。报告也记录了今年的 **LLMJacking** 市场——被盗 AI 账号与被劫持算力——以及针对 LLM 的「拒绝诱饵」：DUSTMAKER 的加载器以生物武器与核武器相关文本开头，*「很可能意在让 LLM 安全扫描器失败或跳过分析」*

## 攻击链

```mermaid
flowchart LR
    E["攻击者越过提示阶段，进入 agent 化工作流"]:::entry
    S0["AI 编程聊天机器人 + 一段提示 + markdown agent 指令：扫描、收割、IP 轮换"]:::step
    I["不到六小时收割数千条凭证<br/><i>（报告级发现；未具名单一受害者）</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 详情

**定调：提示阶段已经过去。** GTIG 的基线是自己 2026 年 5 月的攻击性 AI 滥用报告；本追踪报告讲的是此后发生的变化。*「自我们 2026 年 5 月的报告发布以来……GTIG 观察到走在前面的攻击者正从基础提示转向 agent 化 AI 工作流与 AI 驱动的自动化。」* 首要后果是速度：agent 压缩了防守方传统的响应窗口；报告的第二季度趋势清单勾勒出它出现的位置——围绕 AI 编程工具加速的软件供应链风险、对专有 AI 资产的直接瞄准（*「从模型权重到云算力配额」*）、攻击各阶段的 agent 化自动化，以及 AI 作为贯穿生命周期的影响力倍增器。报告对这一边界说得很明确：*「GTIG 尚未观察到攻击者在真实目标上部署完全自主的攻击管线」*，并把本季度的变化描述为*「战术的渐进成熟与 AI 能力的层层叠加」*。

**供应链：UNC6780 与 DUSTMAKER。** UNC6780 的打法是*「用多种手法欺骗 AI 编程助手与大语言模型（LLM）安全扫描器」*：攻陷合法开发者账号，把真实 MCP 服务器（报告点名 `tiktoken_mcp`）的投毒分叉发布到 PyPI，其中的恶意工作区钩子在*「资产被下载或克隆时」*被自动引入。其 DUSTMAKER 凭据窃取程序会探测自己是否运行在 CI/CD 环境，从 GitHub Actions 运行器的进程内存里提取 OIDC 令牌，并据此把自身认证为可信发布者——发布带*「有效的、加密签名的 SLSA Build 3 证明」*的被污染包，*「这些包会通过 AI 编程 agent 的自动信任检查」*。同一款恶意软件还携带针对 LLM 的拒绝诱饵：DUSTMAKER 的 JavaScript 加载器以生物武器与核武器相关文本开头，*「很可能意在让 LLM 安全扫描器失败或跳过分析」*——几天后 ESET 把这一手法命名为 GuardBreaker。

**六小时行动与「Recon」C2。** 报告中被引用最多的案例：一个疑似经济动机的攻击者攻陷某组织的云基础设施，部署了自主的多 agent 攻击框架，然后用*「一个 AI 编程聊天机器人、一段提示和一组 agent 指令，在不到六小时内计划、构建并执行了一场大规模凭据收割行动」*。借助预置的 markdown 指令集充当行动手册，agent 执行自动化扫描与凭据收割——*「窃取了数千条第三方凭据」*——同时*「无需人工干预地」*完成实时排障与 IP 轮换逻辑，*「显著降低了人工介入带来的延迟」*，并借受害者自己的合法 IP 段转发攻击流量。相关发现：一台暴露的 C2 服务器承载着名为「Recon」的自动化侦察与凭据管理框架，目录列表里满是 agent 化配置文件（`AGENTS.md`、`KNOWLEDGE.md`、`agentic_vuln_research.md`）。本条保留一处边界：这场六小时行动可能与本档案 9 月 16 日 **Mandiant** 报告中的某个案例是同一起入侵——两者都涉及把云环境的失陷改造成 AI 辅助的凭据收割平台——但两份报告互未引用，无法确认重合。

**目标、行为体与市场。** GTIG 的归因贯穿全图：中国背景的 **UNC6508** 瞄准学术、医疗与军事机构的专有 AI 研究，并曾攻陷云环境部署本地的开源权重 LLM 基础设施；朝鲜集群 **MIDNIGHT NEPTUNE** 用商用 LLM 与开源权重模型辅助社会工程与自动化后门开发，服务加密货币窃取；伊朗的 **CALANQUE ION**（原 APT42）用 Gemini 做侦察与话术准备。GTIG 另单独处置了一个用 Gemini 设计动态自动化渗透测试框架的中国背景组织，以及*「谷歌首次因 Gemini 被滥用而采取法律行动」*的「Outsider Enterprise」——一家中国网络犯罪服务商，运营者用 Gemini 批量生成钓鱼工具包代码。在犯罪侧，报告记录了走向成熟的 **LLMJacking** 市场：被盗的开发者凭据、购入的 AI 账号，以及被劫持来运行未授权高性能计算的云基础设施；朝鲜 IT 工作者集群还在批量注册 API 账号。本条记为 `report`、严重度 `info`：它不聚焦任何单一受害者或事件——它是本档案同期的其他条目所处的「现状全景」。

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Google Threat Intelligence Group | <https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai> |
| 2 | ThreatOps | <https://www.threatops.tech/threat-pulse/gtig-adversarial-ai-agent-enabled-operations-september-2026> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-09-08`（原文：2026-09-08，精度 `day`） |
| 性质 | 威胁情报报告 `report` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **信息** `info` |
| 可信度 | **A** —— 一手来源：报告本身，出自谷歌自己的威胁情报团队 |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-09-08-gtig-prompting-to-autonomy` |

<sub>**判定依据：** 厂商威胁报告而非单一事件——严重度记 `info`、不做 `real_harm` 评估，与本档案对 5 月 GTIG 追踪及 CrowdStrike、Mandiant 报告的处理一致。日期按谷歌 RSS 的 GMT 时间戳（2026 年 9 月 8 日 14:00 UTC）；博文页面在部分时区显示为 9 月 9 日。分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题：** [攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**相关条目：**

- `2026-08-27` [GuardBreaker：亲俄组织在恶意脚本里埋入「造核武器」请求，让 AI 分析半途拒绝](../../../2026-08/2026-08-27-guardbreaker-uac-0099.md)<br>  <sub>本报告记录于 DUSTMAKER 的拒绝诱饵手法，同季度被用于实战</sub>
- `2026-09-16` [Mandiant 2026 AI 报告：失控 agent 烧掉 5 万美元账单，AI 辅助入侵登场](../../../2026-09/2026-09-16-mandiant-ai-risk-resilience-2026.md)<br>  <sub>其案例研究可能与这场六小时行动是同一起入侵</sub>
- `2026-05-12` [GTIG AI 威胁追踪（2026 版）](../../../2026-05/2026-05-12-gtig-wei-xie-zhui-zong.md)<br>  <sub>本追踪更新的 5 月基线</sub>
- `2025-11-13` [GTG-1002：首起 AI 自主编排的网络间谍行动](../../../2025-11/2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md)<br>  <sub>谷歌首次记录国家行动中的 agent 自主性</sub>

---

[← 2026-09 索引](../../../2026-09/README.md) · [← 全库索引](../../../../README.md) · [English](../../../2026-09/2026-09-08-gtig-prompting-to-autonomy.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
