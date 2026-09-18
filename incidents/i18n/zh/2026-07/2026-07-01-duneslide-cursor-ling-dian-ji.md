---
id: 2026-07-01-duneslide-cursor-ling-dian-ji
lang: zh
source: incidents/2026-07/2026-07-01-duneslide-cursor-ling-dian-ji.md
title: "DuneSlide：Cursor 零点击沙箱逃逸"
summary: |
  Cato AI Labs，两个 CVE 均 **CVSS 9.8**：
  **CVE-2026-50548** 滥用 `run_terminal_cmd` 工具的可选参数 `working_directory` —— 沙箱允许写入命令的工作目录，而**这个目录可以由 agent 自己不受限制地设定**，提示注入把它指向项目外的系统路径即可
  **CVE-2026-50549** 路径解析的**回退逻辑**缺陷：写文件前 Cursor 会解析符号链接确认真实目标在项目内，但**这个检查失败时它转而信任符号链接自己声明的路径**而非直接阻止
  CVE 于 06-05 分配，**Cursor 3.0（04-02 发布）已修复**，3.0 之前全部受影响
  ⚠️ **CVE-2026-50549 与 2026-07-09 Wiz「GhostApproval」中 Cursor 的修复编号是同一个** —— 两支团队独立发现了同一符号链接缺陷，**入库时应合并或标注 `duplicate_of`，不要重复计数**
---

# DuneSlide：Cursor 零点击沙箱逃逸

<sub>DuneSlide: zero-click sandbox escape in Cursor</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## 概要

Cato AI Labs，两个 CVE 均 **CVSS 9.8**：

**CVE-2026-50548** 滥用 `run_terminal_cmd` 工具的可选参数 `working_directory` —— 沙箱允许写入命令的工作目录，而**这个目录可以由 agent 自己不受限制地设定**，提示注入把它指向项目外的系统路径即可

**CVE-2026-50549** 路径解析的**回退逻辑**缺陷：写文件前 Cursor 会解析符号链接确认真实目标在项目内，但**这个检查失败时它转而信任符号链接自己声明的路径**而非直接阻止

CVE 于 06-05 分配，**Cursor 3.0（04-02 发布）已修复**，3.0 之前全部受影响

⚠️ **CVE-2026-50549 与 2026-07-09 Wiz「GhostApproval」中 Cursor 的修复编号是同一个** —— 两支团队独立发现了同一符号链接缺陷，**入库时应合并或标注 `duplicate_of`，不要重复计数**

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
| 1 | Cato Networks | <https://www.catonetworks.com/blog/duneslide-two-critical-rce-vulnerabilities/> |
| 2 | THN | <https://thehackernews.com/2026/07/critical-cursor-flaws-could-let-prompt.html> |
| 3 | SecurityWeek | <https://www.securityweek.com/critical-cursor-ai-ide-flaws-could-lead-to-os-level-remote-code-execution/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-07-01`（原文：2026-07-01，精度 `day`） |
| 性质 | 研究演示 `research` |
| 类型 | [`SANDBOX`](../../../../taxonomy/types.md#sandbox) 沙箱逃逸 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-07-01-duneslide-cursor-ling-dian-ji` |

<sub>**判定依据**：研究机构或厂商的受控演示，`real_harm: false`；收录是为了标记攻击面何时被公开。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[前沿模型自主越界](../../../../topics/eval-escapes.md)

**同类条目**：

- `2026-07-09` [GhostApproval：6 款 AI 编码助手共有的审批绕过](../../../2026-07/2026-07-09-ghostapproval-kuan-bian-ma-zhu.md)<br>  <sub>GhostApproval: an approval bypass shared by six AI coding assistants</sub>
- `2026-07-01` [AWS Kiro：让它总结一个网页，就能拿到 RCE（CVE-2026-10591）](../../../2026-07/2026-07-01-aws-kiro-rce.md)<br>  <sub>AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)</sub>
- `2026-07-20` [一周内 4 款编码 agent 爆 6 个沙箱逃逸](../../../2026-07/2026-07-20-agent-yi-nei-kuan-bian.md)<br>  <sub>Six sandbox escapes across four coding agents in one week</sub>
- `2026-07-22` [SharedRoot：Claude Cowork 从 Linux VM 逃到 macOS 宿主](../../../2026-07/2026-07-22-sharedroot-claude-cowork-linux.md)<br>  <sub>SharedRoot: Claude Cowork escapes a Linux VM onto the macOS host</sub>

---

[← English original](../../../2026-07/2026-07-01-duneslide-cursor-ling-dian-ji.md) · [2026-07 index](../../../2026-07/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
