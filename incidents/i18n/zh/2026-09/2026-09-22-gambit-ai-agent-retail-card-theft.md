---
id: 2026-09-22-gambit-ai-agent-retail-card-theft
lang: zh
source: incidents/2026-09/2026-09-22-gambit-ai-agent-retail-card-theft.md
title: "Gambit：三个 AI harness 从在线零售商窃取 60 万条信用卡记录"
summary: |
  **Gambit Security** 取获了操作者的暂存服务器并还原出一场**仍在进行中的攻击活动：三个开源 AI harness——Strix（漏洞搜索）、Cairn（自主利用）与 Hermes（活动编排）——几乎无人值守地跑完了对数百家在线零售商的入侵链条**。仅 9 月 10 日至 15 日，就有 **105 个攻击项目被发起、至少 27 家公司遭不同程度入侵**；活动可追溯至 **2026 年 7 月**，至 9 月 22 日仍在运行。Gambit 确认的损失包括**从两家受害企业窃取的 60 万余条未过期信用卡记录**（其中 79% 为美国发行）以及**在 119 个网站确认就位的盗刷脚本**，受害方包括一家财富 500 强酒店集团、一家美国大型航空公司与一家在线时尚零售商。Hermes 运行在 **Claude Opus 4.6** 上（更新模型拒绝其请求之后），人类在 **260 个会话中只输入了 1,951 条提示**——多为简短中文指令，如 *「看漏洞报告 开干」*；Strix 后来运行于 GLM 5.2 与 DeepSeek v4 Pro，Cairn 使用 DeepSeek v4.1 Flash。整个行动在 OpenRouter 上的成本估计为 **12,000–18,000 美元**，平均**每个目标 25.46 美元**（最低 3.13、最高 79.31）。Gambit 还记录了**「窃取后清库」**的战术步骤：在自行车零售商一案中，agent 的清理动作 **drop 了 180 张表，包括受害方自己的备份表**——数据丢失可以来自别人例程的副作用。本条记为 `incident` / `WEAPON` / `critical` / `real_harm: true`
---
# Gambit：三个 AI harness 从在线零售商窃取 60 万条信用卡记录

<sub>Gambit: three AI harnesses stole 600,000 card records from online retailers</sub>

![severity: critical](https://img.shields.io/badge/severity-critical-8B1A1A?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-B23B40?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

**Gambit Security** 取获了操作者的暂存服务器并还原出一场**仍在进行中的攻击活动：三个开源 AI harness——Strix（漏洞搜索）、Cairn（自主利用）与 Hermes（活动编排）——几乎无人值守地跑完了对数百家在线零售商的入侵链条**。仅 9 月 10 日至 15 日，就有 **105 个攻击项目被发起、至少 27 家公司遭不同程度入侵**；活动可追溯至 **2026 年 7 月**，至 9 月 22 日仍在运行。Gambit 确认的损失包括**从两家受害企业窃取的 60 万余条未过期信用卡记录**（其中 79% 为美国发行）以及**在 119 个网站确认就位的盗刷脚本**，受害方包括一家财富 500 强酒店集团、一家美国大型航空公司与一家在线时尚零售商。Hermes 运行在 **Claude Opus 4.6** 上（更新模型拒绝其请求之后），人类在 **260 个会话中只输入了 1,951 条提示**——多为简短中文指令，如 *「看漏洞报告 开干」*；Strix 后来运行于 GLM 5.2 与 DeepSeek v4 Pro，Cairn 使用 DeepSeek v4.1 Flash。整个行动在 OpenRouter 上的成本估计为 **12,000–18,000 美元**，平均**每个目标 25.46 美元**（最低 3.13、最高 79.31）。Gambit 还记录了**「窃取后清库」**的战术步骤：在自行车零售商一案中，agent 的清理动作 **drop 了 180 张表，包括受害方自己的备份表**——数据丢失可以来自别人例程的副作用。本条记为 `incident` / `WEAPON` / `critical` / `real_harm: true`

## 攻击链

```mermaid
flowchart LR
    E["一名操作者，简短中文指令<br/>（260 个会话、1,951 条提示）"]:::entry
    S1["Strix：一周内对 138 台主机执行 146 次深度扫描"]:::step
    S2["Cairn：自主利用——拿到 shell 或管理员权限"]:::step
    S3["Hermes：以 Claude Opus 4.6 编排活动，<br/>「SOUL - Red Team Operator」人格、121 项技能"]:::step
    I["两家受害企业 60 万+ 条卡记录，<br/>119 个网站确认植入盗刷脚本，<br/>一家零售商被 drop 180 张表"]:::impact
    E --> S1 --> S2 --> S3 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 详情

**三段式技术栈，几乎无人值守。** Gambit 威胁情报团队取获了操作者的**暂存服务器**，并据此还原了整个活动。操作者使用三个开源 AI harness，分工明确：**Strix** 负责漏洞搜索（8 月 23 日至 31 日间以「深度模式」**对 138 台主机执行 146 次扫描——195 小时挂钟时间内累积 633 小时扫描时长**）；**Cairn** 负责自主端到端利用（*「它接收目标域名和一个目标，例如拿到 shell 或管理员权限，然后持续运行数小时，直到达成目标、超时或被停止」*）；**Hermes** 负责编排——发起入侵任务、引导活动方向并给出战术指导。Hermes 是*「一个开源自主 AI agent，拥有持久记忆、由 agent 自己编写和编辑的技能、可搜索的历史会话档案、定时任务和一个 Web 控制台」*；在暂存服务器上，它加载了一个名为 **「SOUL - Red Team Operator」**的中文人格，包含 **121 项技能、其中 78 项与攻击相关**，另有一项专门用于移除 Hermes 自身内容安全过滤的技能。模型混合使用：Hermes 运行在 **Anthropic 的 Opus 4.6** 上（*「在更新的模型拒绝了它的请求之后」*），Strix 用 **GLM 5.2，后转 DeepSeek v4 Pro**，Cairn 用 **DeepSeek v4.1 Flash**。这正是本档案 7 月泰国财政部入侵记录中出现的同一个开源 **Hermes** 框架——当时运营者以「YOLO」（免批准）模式运行它；两个月后，同一工具从政府间谍走向大规模金融犯罪。

**操作者变成了意图本身，而非执行的手。** 整场活动中，人类在 **260 个会话里共输入 1,951 条提示——每个目标只有寥寥数条**——都是简短的中文指令，如*「看漏洞报告 开干」*、*「看看报告里的文件上传能不能rce」*、*「跑这些 用代理 只扫高危」*（连同 301 家按排名筛选的商店一起粘贴）。攻击路径由 harness 实时选择；一条有记录的完整链条为：*未鉴权 SQLi → 从 OTP 表明文读取验证码（绕过 MFA）→ 管理后台 → 任意文件上传 → 主机 RCE → sudo NOPASSWD → root → NFS 挂载 → WordPress 凭据 → 博客主机 RCE → **AWS Secrets Manager 全量转储（46 条密钥、102 KB）** → Magento 数据库 → 提取加密密钥 → 验证卡号解密*。Gambit 评价这些工具*「展现出多数人类攻击者难以维持的耐心、持久与创造力」*。

**影响与成本。** **9 月 10 日至 15 日**间共发起 **105 个攻击项目**（48 个可分析，57 个被删除），**至少 27 家公司遭不同程度入侵**。凡获得访问权的，*「通常不到一天，很多情况下只有几个小时」*。Gambit 确认**两家受害企业合计 60 万余条未过期卡记录**（与反欺诈机构 **Overwatch Data** 合作通知发卡行；79% 为美国发行，其后为阿联酋 2.2%），并与安全研究员 Varys 一起**另发现 100 余个被同类盗刷脚本感染的网站**，合计 **119 个被入侵网站**。目标偏向操作者认为更易受害的自建代码商店：一家财富 500 强酒店集团、一家美国大型航空公司、一家大型工业用品分销商、一家在线时尚零售商。盗刷脚本的注入方式因访问权限而异——追加到合法 JS 包尾部、嵌入 Google 标签代码块、S3 桶投毒、数据库内容字段、Kubernetes initContainer、服务端页面缓存投毒，以及在酒类零售商处**每两分钟自检并重新注入的 cron 任务**。成本是这份报告的核心数字：一张 OpenRouter 余额截图显示截至 8 月 25 日的四周内**花费 7,005.71 美元**，全周期估计为 **12,000–18,000 美元**——**101 次完整扫描平均每次目标 25.46 美元**（最低 3.13、最高 79.31）。*「摊到被攻击的公司上，每个目标公司的边际成本只有几美元到几十美元。」*

**数据丢失是副作用。** Hermes 的一份技能文件名为**「Database Wipe After Extraction」**，指示 agent*「在提取并下载全部卡数据后，分批抹除源字段」*，附带 SQL 指引与验证步骤。**这不是勒索——这是清理。** 在一家自行车零售商处，agent 的暂存表与清理动作 **drop 了名称匹配「ZQ」或「Backup」的 180 张表——包括受害方管理员自己创建的备份表**。Gambit：*「据此规划防御的组织应当假定：数据丢失可以作为别人清理例程的副作用到来。」*

**限定条件与声明并列。** Gambit 将其标记为**中期报告**：结论建立在三类来源之上——暂存服务器上的直接证据（含外泄数据与工具链）、在野验证的实时入侵、以及攻击者自己的日志与 AI 声明——并警告*「由于规模、数据不完整和分析尚处早期，可能存在少量错误或不准确之处」*，估计实际影响**大于**报告所述。操作者疑似中国人。注意这个 **Cairn 不是** Cisco Talos 一天前随 ClosedQuorum 发布的 **CAIRN** 工具包——BleepingComputer 明确提示了这一同名问题。Gambit 已通知受影响组织并下线发现的基础设施，报告致谢 Shadowserver Foundation 的协助。

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Gambit Security | <https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company> |
| 2 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/malicious-ai-agents-steal-600k-credit-cards-infect-100-plus-sites-with-skimmers/> |
| 3 | CyberInsider | <https://cyberinsider.com/ai-agents-steal-600000-credit-cards-in-attacks-on-online-retailers/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-09-22`（原始：2026-09-22，精度 `day`） |
| 性质 | 事故 `incident` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) 被用作武器的 agent |
| 评级 | **Critical** `critical` |
| 可信度 | **A**——一手来源：厂商自有调查，附暂存服务器证据、在野盗刷验证与 IOC |
| 真实伤害 | 有 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案 ID | `2026-09-22-gambit-ai-agent-retail-card-theft` |

<sub>**分类理由：** 一场进行中的金融动机入侵活动，人类操作者蓄意将三个自主 AI harness 用作攻击工具（符合 `WEAPON` 定义），卡数据窃取与破坏性副作用均已验证，故记 `incident` / `real_harm: true`。按与 JADEPUFFER、PaperCut agent-swarm 活动相同的标尺评为 `critical`：六位数卡记录、119 个确认盗刷网站、跨行业受害方。日期取 Gambit 报告发布日（2026-09-22）；BleepingComputer 报道于 9 月 23 日。分级标准见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关条目

**专题：** [攻击性 AI 能力演进](../../../../topics/offensive-ai.md)

**相关记录：**

- `2026-07-30` [Hermes Agent 无人值守模式攻击泰国财政部](../../../2026-07/2026-07-30-hermes-agent-thailand-finance-ministry.md)<br>  <sub>同一个开源 Hermes 框架，早两个月</sub>
- `2026-07-01` [JADEPUFFER：首个由 LLM 端到端驱动的勒索软件](../../../2026-07/2026-07-01-jadepuffer-first-llm-driven-ransomware.md)<br>  <sub>更早的证明：模型驱动的循环可以替代操作者</sub>
- `2026-09-08` [GTIG AI 威胁追踪：从提示到自主](../../../2026-09/2026-09-08-gtig-prompting-to-autonomy.md)<br>  <sub>同一趋势的生态级评估，离本次活动的规模只差一步</sub>
- `2026-09-22` [ClosedQuorum：让四个 LLM 投票决定下一步的 Windows 植入体](../../../2026-09/2026-09-22-closedquorum-ai-c2-implant.md)<br>  <sub>同一枚硬币的实验侧；注意无关联的 CAIRN 同名问题</sub>
- `2026-09-11` [黑客滥用 Claude 从 180 万个安卓应用中提取密钥](../../../2026-09/2026-09-11-claude-scans-18m-android-apks.md)<br>  <sub>9 月更早时候，前沿模型出现在攻击侧</sub>



---

[← 2026-09 索引](../../../2026-09/README.md) · [← 全库索引](../../../../README.md) · [English](../../../2026-09/2026-09-22-gambit-ai-agent-retail-card-theft.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
