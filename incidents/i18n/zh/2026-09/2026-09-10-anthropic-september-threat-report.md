---
id: 2026-09-10-anthropic-september-threat-report
lang: zh
source: incidents/2026-09/2026-09-10-anthropic-september-threat-report.md
title: "Anthropic 九月威胁情报报告"
summary: |
  Anthropic 九月威胁情报报告：多个国家背景行为方把 Claude 用于入侵链各环节，涉及 30 万条身份记录，并首次记录模型被用于受害方筛选与勒索文案生成。
---

# Anthropic 九月威胁情报报告

<sub>Anthropic September threat intelligence report</sub>

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

Anthropic 九月威胁情报报告：多个国家背景行为方把 Claude 用于入侵链各环节，涉及 30 万条身份记录，并首次记录模型被用于受害方筛选与勒索文案生成。

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

## 详情

覆盖 **2025-12 → 2026-08**，横跨七大危害领域（网络行动、影响力行动、监控、诈骗欺诈、生物滥用、常规武器、蒸馏），涉及至少 10 个国家的行为者。
**涉事模型为 Claude Haiku / Sonnet / Opus；除一起非法蒸馏案外，未发现 Fable 或 Mythos 级模型被滥用。**

| 编号 | 归因 | 时间 | 用 Claude 做什么 | 规模 |
|---|---|---|---|---|
| **GTG-20006** | 俄罗斯国家支持（疑为 Midnight Blizzard） | 2025-12→2026-08 | 自动化侦察、钓鱼基建、恶意软件规避、凭据收集、数据外带、维持持久访问 | **20+ 个组织**：乌克兰与欧洲政府、军用无人机制造商、外交使团、国防组织、酒店 WiFi。外带数百 GB，含 **30 万+ 国民身份记录** |
| **GTG-50014** | ShinyHunters 关联（含法语系操作者） | 2025-12→2026-08 | 凭据验证、供应链侦察、令牌生成、批量数据导出、跨租户访问、API 认证工具 | 科技供应商、航空、能源、SaaS、零售、Web3；**200+ 下游客户组织**受影响。TB 级外带，数百万支付记录，**部分入侵在数小时内完成** |
| **GTG-10007** | 中文使用者（疑在湖南长沙；大学生与安全公司人员） | 2025-12→2026-08 | 自主二进制逆向、漏洞假设形成、利用代码开发、侦察编排、恶意软件开发、情报收集平台运营 | 约 **50 个组织**（教育、零售、能源、科技、医疗、金融、制造）+ 全球政府机构。**单月发现十余个零日**，外带数百 MB 学生数据 |
| **GTG-50020** | 俄语系逐利型 | 2026-05→06 | **对评测沙箱做提示注入**、自动化渗透流程、账号工厂自动化、KYC 拦截伪装 | 先打酒店预订/金融科技平台，**随后转向 AI 厂商本身**，4 天内针对约 **30 家 AI 公司**，试图获取预发布模型访问（未成功）。单一受害者被外带约 26 GB |
| **GTG-50029** | 单一法语系政治动机行为者 | 2026-02→07 | 定制扫描器、API key 校验、利用代码编写调试、自研 "fafsearch" 人肉搜索平台、凭据收集自动化 | 欧洲政党、媒体、智库、SaaS 提供商；追踪 **42 个实体**、内部访问 **14 个**。外带 12–26 GB，某政治平台 14 万条记录，人肉库数千万行 |
| **GTG-04001** | 俄罗斯国家关联（评估为 Politology / Africa Corps / SVR） | 至 2026 年中 | 每日内容生成、合同起草、HR 评分系统、员工评估自动化、**伪造政府文件**、监控行动管理 | 中非共和国信息空间；**每日 98.9 FM 电台广播** + 多个国家媒体与 Telegram 分发。Breakout Scale **Category Four** |
| **GTG-54002** | LKM Company（法国数字广告公司） | 2025 年中→2025-09 | 批量生成文章、改写真新闻加政治倾向、伪造署名、结构化 JSON 输出流水线 | 约 **70 个伪造新闻站**、**8,913+ 篇文章、20 种语言**、250+ 个虚假 X 账号，覆盖六大洲 |
| **GTG-84005** | BBS Bilisim Teknolojileri（伊斯坦布尔科技公司） | 至 2026 年中 | 用人口普查与选举数据建选民定向系统、虚假账号网络管理、合成新闻改写流水线、伪造档案 | 马来西亚全部 **222 个国会选区**；约 1,000 个虚假 X 账号 |
| **GTG-24015** | 俄罗斯国有/国资媒体（Sputnik、RIA Novosti、RT） | 至 2026 年中 | 编辑部新闻台自动化、内容生产、文章润色、生成诽谤性主张、制造「验证闭环」 | 摩尔多瓦、拉美、非洲及全球受众；针对摩尔多瓦总统 Maia Sandu 的不实指控（2025-09 选举前）。4 个账号被移除 |
| **GTG-50021** | 俄/乌语系（化名 "kl1zy"） | — | 代理搭建、凭据收集工具 | 欺诈性转售 Claude 访问，静默代理到其他模型，窃取凭据 |
| **GTG-15001** | 中国的 App 工作室 | 2026-04 | 运营 **20+ 个约会 App** 的 AI 人格网络 | **4,700+ 个 AI 人格**，两周内与**至少 25,000 名真人**对话，交换约 **236 万条消息**；AI 人格与真实零工按约 **3:1** 混入同一匹配流，**人格被要求绝不透露自己是自动化的** |
| **蒸馏** | 中国的 **7 家实验室** | 2026-02 起 | 非法蒸馏 Anthropic 的通用模型 | 全部针对通用可得模型 |

**跨案的三条趋势**：
1. AI 在网络行动中**越来越自主**，从助手变成执行者与协调者；多 agent 系统承担侦察、利用、外带
2. **攻击运行在 agent 框架上，而 API key 就是战利品** —— 攻击者开始「靠 AI 资源就地取材」，攻陷 AI 厂商、评测方、套壳服务，把 API key 拿来复用和转售
3. **一个人 + AI ≈ 一支国家级团队**（GTG-50029 单人打 42 个实体即是明证）

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Anthropic | <https://www.anthropic.com/threat-intelligence-report-september-2026> |
| 2 | 报告 PDF | <https://www-cdn.anthropic.com/e50be2e51e7695dc4b1366a37a245a597377d3b5/Anthropic-Detecting-and-countering-091026.pdf> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-09-10`（原文：2026-09-10，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **严重** `critical` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-09-10-anthropic-september-threat-report` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `critical`：确认的真实损害达到多组织 / 政府 / 关键基础设施 / 供应链蠕虫级别，或属首次出现且有真实受害方的能力里程碑。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**同类条目**：

- `2026-09-11` [用 Claude 扫描 180 万个安卓 App 找密钥](../../../2026-09/2026-09-11-claude-scans-18m-android-apks.md)<br>  <sub>Claude used to scan 1.8 million Android apps for secrets</sub>
- `2026-09-15` [PaperCut AI agent 蜂群攻击公开](../../../2026-09/2026-09-15-papercut-agent-swarm-disclosed.md)<br>  <sub>PaperCut AI agent swarm attack made public</sub>
- `2026-09-02` [Unit 42：AI agent 把两周的入侵工作压到 10 小时内](../../../2026-09/2026-09-02-unit-agent-liang-ru-qin.md)<br>  <sub>Unit 42: AI agents compress two weeks of intrusion work into 10 hours</sub>
- `2026-08-28` [PaperCut AI agent 蜂群战役启动](../../../2026-08/2026-08-28-papercut-agent-swarm-campaign-begins.md)<br>  <sub>PaperCut AI agent swarm campaign begins</sub>

---

[← English original](../../../2026-09/2026-09-10-anthropic-september-threat-report.md) · [2026-09 index](../../../2026-09/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
