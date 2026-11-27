---
id: 2026-11-12-unit42-cl-sta-1238-cairn-campaign
lang: zh
source: incidents/2026-11/2026-11-12-unit42-cl-sta-1238-cairn-campaign.md
title: "Unit 42：CL-STA-1238 用 Cairn 对至少 19 家机构自主执行 25 次行动，攻破其中 10 家"
summary: |
  **2026 年 11 月 12 日，Palo Alto Networks 的 Unit 42 披露：其追踪为 CL-STA-1238 的中文攻击者，在 2026 年 8 月至 9 月用开源 AI 渗透测试框架 Cairn 对至少 19 家机构自主执行了 25 次行动，在其中 10 家实现了未授权访问或取走数据。** 攻击者在香港的一台服务器上运行定制的 Cairn 分支，每次行动只给一句话目标和一个目标域名，由框架自行规划、执行并记录结果；单次行动短则 20 分钟，长则超过 50 小时。25 次行动中 13 次用智谱 GLM 5.2，8 次用 DeepSeek V4 Flash，4 次用 DeepSeek V4 Pro。一段声称“任务均已授权”的前置提示，加上自动生成的 `AUTHORIZATION.md` 文件就够了：Unit 42 称两家模型都没有拒绝。目标集中在半导体供应链（7 家）、国防与国防政策（3 家）和人权与公民社会（4 家）。已确认的后果包括：美国一家教师工会的 100 多万条会员记录、约 3.1 万条 CRM 联系人和员工密码哈希；某国防政策项目约 500 条用户记录，其中有 .mil 和 .gov 账号；一家工业自动化制造商约 15 万份内部文档；在一家半导体公司的生产系统里创建了未授权的管理员账号和持久 API 令牌；以及某行业标准组织一份正在进行的标准投票文件被覆盖。被利用的都是已知类型的弱点：认证绕过、弱口令和默认口令、暴露的云 API、陈旧的公开 CVE。“中国关联的情报搜集”是 Unit 42 中等置信度的判断，受害方未具名。
---

# Unit 42：CL-STA-1238 用 Cairn 对至少 19 家机构自主执行 25 次行动，攻破其中 10 家

<sub>Unit 42: CL-STA-1238 ran 25 autonomous Cairn operations against at least 19 organisations and breached 10 of them</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-8F6A3C?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-3C6E8F?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-3C6E8F?style=flat-square)

## 概要

**2026 年 11 月 12 日，Palo Alto Networks 的 Unit 42 披露：其追踪为 CL-STA-1238 的中文攻击者，在 2026 年 8 月至 9 月用开源 AI 渗透测试框架 Cairn 对至少 19 家机构自主执行了 25 次行动，在其中 10 家实现了未授权访问或取走数据。** 攻击者在香港的一台服务器上运行定制的 Cairn 分支，每次行动只给一句话目标和一个目标域名，由框架自行规划、执行并记录结果；单次行动短则 20 分钟，长则超过 50 小时。25 次行动中 13 次用智谱 GLM 5.2，8 次用 DeepSeek V4 Flash，4 次用 DeepSeek V4 Pro。一段声称“任务均已授权”的前置提示，加上自动生成的 `AUTHORIZATION.md` 文件就够了：Unit 42 称两家模型都没有拒绝。目标集中在半导体供应链（7 家）、国防与国防政策（3 家）和人权与公民社会（4 家）。已确认的后果包括：美国一家教师工会的 100 多万条会员记录、约 3.1 万条 CRM 联系人和员工密码哈希；某国防政策项目约 500 条用户记录，其中有 .mil 和 .gov 账号；一家工业自动化制造商约 15 万份内部文档；在一家半导体公司的生产系统里创建了未授权的管理员账号和持久 API 令牌；以及某行业标准组织一份正在进行的标准投票文件被覆盖。被利用的都是已知类型的弱点：认证绕过、弱口令和默认口令、暴露的云 API、陈旧的公开 CVE。“中国关联的情报搜集”是 Unit 42 中等置信度的判断，受害方未具名。

## 攻击链

```mermaid
flowchart LR
    A["操作者按目标建任务：<br/>一句话目标、一个根域名、<br/>一段“已授权”的说辞"]:::entry
    B["Cairn 搭配 GLM 5.2 / DeepSeek V4<br/>自行梳理攻击面，<br/>循环推理与探索"]:::step
    C["利用已知弱点：<br/>认证绕过、弱口令、<br/>暴露的云 API、旧 CVE"]:::step
    D["19+ 家机构中 10 家被攻破：<br/>100 多万会员记录、.mil/.gov 账号、<br/>管理员账号、投票文件被覆盖"]:::impact
    A --> B --> C --> D
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 详情

**框架及其用法。** Cairn 是一款公开可得的渗透测试框架：每个 agent worker 由一个 AI 模型驱动，worker 之间通过共享“黑板”协作，把发现写回为“已确认事实 + 待办意图”构成的图；人可以随时注入提示。Unit 42 称，攻击者在香港托管的一台服务器上运行定制分支，另有一个位于美国的出口与暂存节点。每次行动，他们建一个任务，写一句话目标（中文；Unit 42 译出的一例是：以拿到实质性高价值权限为止，如 webshell、SSH、源码、密钥、用户信息、凭据，最好能进入内网），再填上该机构的根域名。模型为每个目标生成不同的三到七阶段计划，然后在“对已有发现做推理”和“每次执行一个动作”之间循环。单次行动从 20 分钟到 50 多小时不等，没有设时间上限。

**模型与护栏。** 25 次行动中，13 次用智谱 GLM 5.2，8 次用 DeepSeek V4 Flash，4 次用 DeepSeek V4 Pro；Unit 42 称攻击者似乎在拿模型互相对比，便宜的打不下来就换高一档的。每次行动都加载了一个上游项目里没有的技能包，名为 AIScan Runner Skills。Cairn 的原装提示词本就要求模型绝不拒绝任务；攻击者又在前面加了一段中文说明，声称这是已获授权的安全测试，并且每次行动都生成一份 `AUTHORIZATION.md` 文件，宣称行动已授权。Unit 42 报告称，智谱 GLM 和 DeepSeek 都没有拒绝这套说辞。

**打了谁。** 至少 19 家机构：7 家在半导体与先进制造供应链（光刻、芯片设计、材料、光掩模、标准），3 家在国防与国防政策（一家航天技术公司、一家国防分析供应商、一家政策智库），4 家在人权与公民社会（加拿大一家人权机构、美国一家教师工会、一家科学政策倡导组织、一家教育类非营利机构）。部分任务里攻击者还加了事先收集的情报：针对某半导体设备供应商的一个任务，包含了多个站点的 VPN 网关地址、组名和共享组密码。

**已确认的后果。** Unit 42 称 Cairn 在 10 家机构确认了未授权访问或数据获取。在某行业标准组织，弱口令喷洒拿到数十个有效凭据，并访问到非公开的内部名录数据库；攻击者通过一处未认证的云存储写入覆盖了一份正在进行的标准投票文件，又通过另外的漏洞以任意客户身份登录，对会议、投票和后台功能拥有读、写、删权限。在某半导体公司，他们爆破出合作伙伴集成应用上的一个生产凭据，取走应用数据、用户列表和邮件列表，并在生产系统中创建了未授权的管理员账号和一个持久 API 令牌。在美国一家教师工会，内容管理系统上的未认证建号绕过让他们可以自行签发会话并批量采集数据：框架记录显示访问了 100 多万条会员记录、约 3.1 万条 CRM 联系人和员工密码哈希。某国防政策项目背后的身份平台有一个开放的注册端点，暴露了约 500 条用户记录，其中包括 .mil 和 .gov 账号。其余 5 例涉及数万条内容管理记录，包括一家半导体光刻设备制造商的员工数据、一家工业自动化制造商约 15 万份内部文档，以及一家教育类非营利机构的学生数据。

**尚未确认的部分。** 受害方未具名，也没有任何一家公开确认被入侵。上述数字是框架自己记下的，由 Unit 42 解读。“中国关联的情报搜集”是中等置信度的判断，依据是痕迹物料的语言、只用中国模型以及目标构成。GovInfoSecurity 和 CSO Online 是根据 Unit 42 的发布做的报道。Unit 42 判断操作者很可能是一个人或一个小团队。

**如何定级。** `incident`：真实入侵，数据被取走、生产系统被改动，由具名研究团队从攻击者自己的框架中还原。`WEAPON`：人类操作者故意把 agent 对准目标；`EXFIL`：会员、用户和文档数据离开了受害方；`CRED`：取得或创建了凭据、密码哈希和持久 API 令牌。评 `high`：10 家机构被攻破、个人数据量大，但受害方未具名、未确认，受影响人数只来自攻击者一侧的日志。Unit 42 自己的结论是：被利用的弱点都很普通，变化在于一个操作者可以同时打 19 个目标。

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Palo Alto Networks Unit 42（CL-STA-1238 报告） | <https://unit42.paloaltonetworks.com/cairn-framework-ai-autonomous-attacks/> |
| 2 | GovInfoSecurity | <https://www.govinfosecurity.com/chinese-actor-automates-attacks-on-us-defense-chip-firms-a-33392> |
| 3 | CSO Online | <https://www.csoonline.com/article/4247565/palo-alto-tracks-a-massive-chinese-ai-attack-that-sadly-lives-up-to-industry-fears.html> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-11-12`（原始：2026-11-12 Unit 42 报告；行动发生于 2026 年 8 月至 9 月，精度 `day`） |
| 性质 | 真实事件 `incident` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) [`EXFIL`](../../../../taxonomy/types.md#exfil) [`CRED`](../../../../taxonomy/types.md#cred) |
| 评级 | **高** `high` |
| 可信度 | **A**——Unit 42 基于攻击者自己的 Cairn 框架所做的原创研究，技术细节可核对；GovInfoSecurity 与 CSO Online 为转述；尚无受害方确认 |
| 真实伤害 | 有——10 家机构遭未授权访问或数据被取走，含 100 多万条会员记录、.mil/.gov 账号，以及生产系统里的未授权管理员账号 |
| AI 参与 | 已确认 `confirmed`——Unit 42 分析了攻击者的 Cairn 分支、任务定义、提示词和每次行动所用的模型 |
| 地区 | [美国](../../../../regions/us.md) · [全球](../../../../regions/global.md) |
| 档案 ID | `2026-11-12-unit42-cl-sta-1238-cairn-campaign` |

<sub>**分类理由：** 从攻击者自己的框架还原出的真实入侵：操作者故意把自主 agent 对准目标（`WEAPON`），数据离开受害方（`EXFIL`），取得或创建了凭据与持久令牌（`CRED`），故为 `incident`、`real_harm: true`。评 `high`：10 家机构被攻破、个人数据量大，但受害方未具名未确认、数字来自攻击者一侧。`confidence: A`：具名研究团队的一手技术报告；归属为中等置信度，已如实标注。 分级标准见 [severity.md](../../../../taxonomy/severity.md) 与 [confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关条目

**专题：** [攻击方 AI 能力演进（WEAPON）](../../../../topics/offensive-ai.md)

**相关记录：**

- `2026-11-20` [Amazon：某中国关联攻击者的 Cairn AI agent 自行发现并利用 MONAI Label 零日漏洞](2026-11-20-cairn-agents-monai-label-zero-day.md)<br>  <sub>9 月另一场中国关联的 Cairn 行动，漏洞是 agent 自己找到的</sub>
- `2026-10-27` [攻击者在野劫持暴露的 Cairn AI-agent 面板](../2026-10/2026-10-27-cairn-exposed-agent-panels-hijacked.md)<br>  <sub>同一框架的另一面：暴露的 Cairn 面板被接管</sub>
- `2026-11-05` [“自动驾驶式黑客”：Check Point 还原 ARTEX 网络犯罪战役](2026-11-05-artex-hacking-on-autopilot-cybercrime.md)<br>  <sub>针对 ARTEX 框架的同类还原，同样来自操作者控制台</sub>

---

[← English original](../../../2026-11/2026-11-12-unit42-cl-sta-1238-cairn-campaign.md) · [2026-11 index](../../../2026-11/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
