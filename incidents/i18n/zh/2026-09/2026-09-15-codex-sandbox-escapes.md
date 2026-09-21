---
id: 2026-09-15-codex-sandbox-escapes
lang: zh
source: incidents/2026-09/2026-09-15-codex-sandbox-escapes.md
title: "OpenAI Codex 沙箱的两种逃逸：Heapjack 与 Overpatch"
summary: |
  **Oren Yomtov（Accomplish AI）**披露 **OpenAI Codex** 沙箱的两种逃逸方式，均于 **8 月 12 日**上报、8 天内修复。**Heapjack**：Codex Desktop 会安装一个未沙箱化的原生 `node_repl` 工具，其可信与不可信两个 V8 上下文**共享同一内存堆**——不可信代码从堆快照中读出信任令牌，伪造请求写入通往原生父进程的管道，从而**在 read-only（最严格）模式下取得未沙箱化的命令执行**：无审批提示、界面无任何显示；打开别人的仓库、问一个问题，仓库作者就能在你的机器上执行代码。**Overpatch**：Codex CLI 的 `apply_patch` 会为补丁中每个路径的父目录授予写权限——命名 `/tmp` 即把授权扩大到整个磁盘，再经软链向 `.zshrc` 追加一行，下个终端就会执行。修复版本：Codex Desktop **26.818.21641**、Codex CLI **0.149.0**
---

# OpenAI Codex 沙箱的两种逃逸：Heapjack 与 Overpatch

<sub>Two ways out of the OpenAI Codex sandbox: Heapjack and Overpatch</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## 概要

**Oren Yomtov（Accomplish AI）**披露 **OpenAI Codex** 沙箱的两种逃逸方式，均于 **8 月 12 日**上报、8 天内修复。**Heapjack**：Codex Desktop 会安装一个未沙箱化的原生 `node_repl` 工具，其可信与不可信两个 V8 上下文**共享同一内存堆**——不可信代码从堆快照中读出信任令牌，伪造请求写入通往原生父进程的管道，从而**在 read-only（最严格）模式下取得未沙箱化的命令执行**：无审批提示、界面无任何显示；打开别人的仓库、问一个问题，仓库作者就能在你的机器上执行代码。**Overpatch**：Codex CLI 的 `apply_patch` 会为补丁中每个路径的父目录授予写权限——命名 `/tmp` 即把授权扩大到整个磁盘，再经软链向 `.zshrc` 追加一行，下个终端就会执行。修复版本：Codex Desktop **26.818.21641**、Codex CLI **0.149.0**

## 攻击链

```mermaid
flowchart LR
    E["Codex 处理一个恶意仓库或补丁"]:::entry
    S0["Heapjack 从共享堆中读出信任令牌 / Overpatch 自行扩大写权限"]:::step
    I["在开发者机器上获得未沙箱化的命令执行<br/><i>（已修复，无已知利用）</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 详情

**Heapjack：与不可信代码同居一个堆的密钥。** Codex Desktop 在**安装时**就把 `[mcp_servers.node_repl]` 写进全局 `~/.codex/config.toml`——没有选择加入、没有关闭开关，因此普通的 Codex CLI 用户也会继承这个工具。`node_repl` 是一个原生、**未沙箱化**的 Rust 程序，它把 Node 进程启动在沙箱**内部**；而这个进程里并存着两个 V8 上下文：持有 OpenAI 自身代码的可信上下文，与运行 agent 代码的不可信上下文。可信上下文用每次运行随机生成的令牌证明身份——但两个上下文共享同一个堆，令牌不过是堆里的一串字符。攻击者用 `v8.getHeapSnapshot()` 取快照，把所有形如 UUID 的字符串拿去试探通往原生父进程的管道，并以「not authorized」与真实校验错误之间的差别作为判定预言机。拿到令牌后，不可信代码把伪造的请求写进同一条管道，父进程照单执行：概念验证调用了系统 `open` 命令，把应用启动在 Codex 进程树之外。同一枚令牌还能连接任意 Unix socket（Docker 守护进程 socket 是现成的目标），以及调用一个可编辑全局配置文件的工具。这一切都运行在 **read-only**——最严格的沙箱模式——没有任何审批提示，界面上也没有任何显示。

**Overpatch：权限从攻击者输入里推导出来。** 在开源 Codex CLI 的 `workspace-write` 模式下，agent 只能写项目文件夹内的文件，指向 `$HOME` 的命令会被拒绝。但 Codex 自带的文件编辑工具 `apply_patch` 会**为补丁中每个路径的父目录授予写权限**——因此一个只是写着 `/tmp` 的补丁，就把授权扩大到了磁盘根目录。可用的利用补丁包含两处修改：一处通过软链把一行内容追加进主目录的 `.zshrc`，另一处只是命名 `/tmp`、不做别的事。删掉第二处，写入会被拒绝；带着它，开发者下一次打开的终端就会执行攻击者的那一行——不经过任何沙箱。

**为何重要。** 两个漏洞形状相同：**执行边界的执行者本身就在被执行的边界之内**——`apply_patch` 从被交给它的输入里自行推导权限，`node_repl` 则把区分可信与不可信的密钥和不可信代码放在同一块内存里。这正是 Pillar Security 在 2026 年 7 月于 Cursor、Codex、Gemini CLI 与 Antigravity 上演示过的那一类问题，也是 Accomplish 给出的答案：把整个 agent 运行在 VM 里，真实凭据根本不进入客户机。OpenAI 修复了两个漏洞——Codex Desktop **26.818.21641**、Codex CLI **0.149.0**——但未发布公开公告，因此本条记为 `B` 级。没有证据显示任一漏洞曾被在野利用。

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Accomplish | <https://accomplish.ai/blog/escaping-the-openai-codex-sandbox-twice/> |
| 2 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/researchers-escape-openai-codex-sandbox-to-run-commands-on-host/> |
| 3 | 51CTO | <https://www.51cto.com/article/856105.html> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-09-15`（原文：2026-09-15，精度 `day`） |
| 性质 | 研究实证 `research` |
| 类型 | [`SANDBOX`](../../../../taxonomy/types.md#sandbox) 沙箱逃逸 |
| 严重度 | **高** `high` |
| 可信度 | **B** — 研究机构或主流媒体，细节可核查 |
| 真实伤害 | 无 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-09-15-codex-sandbox-escapes` |

<sub>**判定依据**：安全研究机构的协调披露，`real_harm: false`；本条标记该攻击面公开的时间点。因无 CVE 或厂商公告可锚定，记为 `B`。定级 `high`：具有标志性的能力实证——从广泛部署的编码 agent 的最严格沙箱中两次逃逸。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[前沿模型自主越界](../../../../topics/eval-escapes.md)

**同类条目**：

- `2026-07-20` [一周内 4 款编码 agent 爆 6 个沙箱逃逸](../../../2026-07/2026-07-20-agent-yi-nei-kuan-bian.md)<br>  <sub>Six sandbox escapes across four coding agents in one week</sub>
- `2026-07-01` [DuneSlide：Cursor 零点击沙箱逃逸](../../../2026-07/2026-07-01-duneslide-cursor-ling-dian-ji.md)<br>  <sub>DuneSlide: zero-click sandbox escape in Cursor</sub>
- `2026-07-09` [GhostApproval：6 款 AI 编码助手共有的审批绕过](../../../2026-07/2026-07-09-ghostapproval-kuan-bian-ma-zhu.md)<br>  <sub>GhostApproval: an approval bypass shared by six AI coding assistants</sub>

---

[← English original](../../../2026-09/2026-09-15-codex-sandbox-escapes.md) · [2026-09 index](../../../2026-09/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
