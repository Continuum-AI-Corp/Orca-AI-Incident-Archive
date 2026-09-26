---
id: 2026-09-21-meta-muse-not-a-mused-dictation-hijack
lang: zh
source: incidents/2026-09/2026-09-21-meta-muse-not-a-mused-dictation-hijack.md
title: "Not-a-Mused：一个未公开的 Muse 设置项把语音输入重定向，并把 agent 的令牌交给攻击者"
summary: |
  **Patrick Wardle 展示：Meta 面向 macOS 的 Muse 助手里有一个隐藏配置项——`endo_voyager_dictation_endpoint`——它决定语音输入被发送到哪里，存于应用偏好设置中，任何以登录用户身份运行的进程都可改写，且无需额外权限。** 把它指向攻击者的地址，Muse 的麦克风输入与转写文本就离开设备：攻击者可以*「读取用户的语音内容、追加 Muse 信任并执行的额外指令，并捕获用于登录用户 Muse 账户的令牌」*——随后读取该账户的聊天记录，并在**该账户登录的任何设备**上驱动这个助手（Wardle 让 iPhone 端上报了精确位置、执行蓝牙扫描并列出可下发的智能家居指令）。Muse 是 Meta 本月在美国推出的个人 agent，持有用户授予的跨文件、邮件、消息、日历与购物的访问权限；Wardle 称把它*「变成终极后门易如反掌」*。它无法自行攻入一台 Mac——需要先以用户身份执行代码，或用 ClickFix 手法——也没有攻破 macOS 的应用隔离或 Meta 的云端隔离。Wardle 未事先通知 Meta 就公开；Meta 随后推送了他所称的「修复」，但未发布公告
---

# Not-a-Mused：一个未公开的 Muse 设置项把语音输入重定向，并把 agent 的令牌交给攻击者

<sub>Not-a-Mused: an undocumented Muse setting redirects dictation and hands the agent's token to an attacker</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-3C6E8F?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-3C6E8F?style=flat-square)

## 概要

**Patrick Wardle 展示：Meta 面向 macOS 的 Muse 助手里有一个隐藏配置项——`endo_voyager_dictation_endpoint`——它决定语音输入被发送到哪里，存于应用偏好设置中，任何以登录用户身份运行的进程都可改写，且无需额外权限。** 把它指向攻击者的地址，Muse 的麦克风输入与转写文本就离开设备：攻击者可以*「读取用户的语音内容、追加 Muse 信任并执行的额外指令，并捕获用于登录用户 Muse 账户的令牌」*——随后读取该账户的聊天记录，并在**该账户登录的任何设备**上驱动这个助手（Wardle 让 iPhone 端上报了精确位置、执行蓝牙扫描并列出可下发的智能家居指令）。Muse 是 Meta 本月在美国推出的个人 agent，持有用户授予的跨文件、邮件、消息、日历与购物的访问权限；Wardle 称把它*「变成终极后门易如反掌」*。它无法自行攻入一台 Mac——需要先以用户身份执行代码，或用 ClickFix 手法——也没有攻破 macOS 的应用隔离或 Meta 的云端隔离。Wardle 未事先通知 Meta 就公开；Meta 随后推送了他所称的「修复」，但未发布公告。

## 攻击链

```mermaid
flowchart LR
    E["攻击者已能以用户身份执行代码<br/>（或用 ClickFix 骗用户跑一条命令）"]:::entry
    S1["改写未公开配置项<br/>endo_voyager_dictation_endpoint"]:::step
    S2["Muse 把音频与转写文本<br/>发往攻击者端点"]:::step
    I["读取语音内容、注入受信任指令、<br/>捕获 Muse 令牌——可在任意设备操控"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 详情

**发现内容。** Wardle 于 2026 年 9 月 21 日发布了概念验证 *not-a-mused*。该设置*「未公开，且决定 Muse 把语音输入发送到哪里」*；它存于 Mac 应用的偏好设置中，名为 `endo_voyager_dictation_endpoint`，*「任何以登录用户身份运行的程序都能把它指向攻击者控制的地址，无需额外权限。」* 此后*「语音输入不再发往 Meta。当用户说出一条提示时，音频与文本会流向攻击者在同台 Mac 上运行的一个小程序。」* 在此基础上他演示了三件事：*「读取用户说的语音内容、追加 Muse 信任并执行的额外指令，并捕获用于登录用户 Muse 账户的令牌，然后用它读取该账户的聊天记录并直接控制这个助手。」*

**为什么 agent 才是战利品。** macOS 通常会阻止一个应用读取另一个应用的文件、麦克风、摄像头或已保存的登录信息，因此普通恶意软件的能力有限。*「而一个能悄悄操纵 Muse 的攻击者，则得到用户允许该应用去做的一切」*——并且由于一个 Muse 账户可以在多台设备上登录，持有令牌的攻击者可以从任何地方下令：Wardle*「用它指挥自己 iPhone 上的 Muse 应用上报精确位置、执行附近设备的蓝牙扫描，并列出它可以下发的智能家居指令。」* 在他的测试中，助手只起草消息而没有自行发送。安全软件可能不会察觉，因为这些命令来自 Muse——*「一个正常签名过的应用。」*

**它做不到什么，以及披露方式。** 它没有攻破 macOS 的应用隔离：*「Muse 是随被重定向的语音输入一起把令牌发出去的，攻击之所以成立，是让 Muse 用它本来就有的访问权限去行动。」* 它也没有表明 Meta 的云端隔离被攻破；缺陷位于 Mac 客户端。它*「无法自行攻入一台 Mac」*——需要以登录用户身份执行代码，可通过 ClickFix 手法达成。Wardle 刻意未先向 Meta 报告，选择了完全披露；Meta 随后推送了他所称的「修复」，The Hacker News*「无法确认」*其具体内容，且未发布安全公告。Wardle 称他在更多 AI 助手中发现了缺陷，将于 11 月在 Objective by the Sea 会议上公布。

**背景与定级。** Muse 本月在美国推出，用户授予它跨文件、邮件、消息、日历、购物与智能家居的广泛权限——这正是档案把 **agent 客户端**视为 agent 基础设施的原因：助手把权限集中于一身，因此任何能操纵客户端的东西都会继承这些权限。记为 `vulnerability` / `INFRA` + `CRED` / `medium` / `real_harm: false`：这是一次单机上的受控演示，需要先有立足点，且无确认受害者，因此未进入 `high` 档。可信度 **A**：研究者公开发布的概念验证，加英文与中文的独立报道。

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | The Hacker News（2026-09-22） | <https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html> |
| 2 | Patrick Wardle——「not-a-mused」概念验证（2026-09-21） | <https://github.com/pwardle/not-a-mused> |
| 3 | IT之家（中文报道，2026-09-25） | <https://finance.sina.com.cn/tech/digi/2026-09-25/doc-iniszmmz7778318.shtml> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-09-21`（原始：PoC 2026-09-21 / The Hacker News 2026-09-22，精度 `day`） |
| 性质 | 漏洞披露 `vulnerability` |
| 类型 | [`INFRA`](../../../../taxonomy/types.md#infra) [`CRED`](../../../../taxonomy/types.md#cred) |
| 评级 | **Medium** `medium` |
| 可信度 | **A**——研究者公开的概念验证加独立报道 |
| 真实伤害 | 无——一次演示，无确认受害者 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [美国](../../../../regions/us.md)——Muse 在美国推出 |
| 档案 ID | `2026-09-21-meta-muse-not-a-mused-dictation-hijack` |

<sub>**分类理由：** 被暴露的资产是 agent 自身的客户端运行时及其配置面（`INFRA`），被拿走的是登录令牌加下发受信任指令的能力（`CRED`）。`vulnerability` 且 `real_harm: false`，因为这是一次无已知利用的概念验证。按档案阶梯评 `medium` 而非 `high`：一次受控的单机演示，且额外要求攻击者已能以用户身份执行代码——`high` 需要确认损害、CVSS 9+ 缺陷，或不预设立足点的能力演示。日期取 PoC 发布日（2026-09-21）。分级标准见 [severity.md](../../../../taxonomy/severity.md) 与 [confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关条目

**专题：** [Agent 基础设施暴露（INFRA）](../../../../topics/agent-infra.md)

**相关记录：**

- `2026-09-16` [BragJack：一个浏览器扩展劫持五大浏览器里的 AI agent](2026-09-16-bragjack-browser-agents.md)<br>  <sub>同一形状的问题，出现在浏览器攻击面：操纵客户端，继承它的权限</sub>
- `2026-09-15` [Codex 沙箱逃逸](2026-09-15-codex-sandbox-escapes.md)<br>  <sub>边界问题的另一面——agent 被允许触及什么</sub>
- `2026-09-18` [智谱 ZCode agent 静默上传整个仓库](2026-09-18-zcode-silent-upload.md)<br>  <sub>当 agent 客户端本身就是泄露通道</sub>

---

[← 2026-09 索引](../../../2026-09/README.md) · [← 全库索引](../../../../README.md) · [English](../../../2026-09/2026-09-21-meta-muse-not-a-mused-dictation-hijack.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
