---
id: 2026-09-17-plugin4shell-coding-agents
title: "Plugin4Shell: a zero-click RCE chain hits four AI coding agents"
title_zh: "Plugin4Shell：零点击 RCE 链打击四款 AI 编码 agent"
title_ja: "Plugin4Shell：4つのAIコーディングエージェントを襲うゼロクリックRCE"
title_ko: "Plugin4Shell: 4개 AI 코딩 에이전트를 노린 제로클릭 RCE 체인"
title_de: "Plugin4Shell: Zero-Click-RCE-Kette trifft vier KI-Coding-Agenten"
title_fr: "Plugin4Shell : une chaîne RCE sans clic touche quatre agents de codage IA"
title_es: "Plugin4Shell: una cadena RCE sin clic golpea a cuatro agentes de código de IA"
date: 2026-09-17
date_precision: day
date_raw: "2026-09-17"

kind: vulnerability
type: [SUPPLY]
severity: high
confidence: B
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **AIR Security discloses Plugin4Shell**, a **zero-click remote code execution** flaw affecting four major AI coding agents — **Claude Code, OpenAI Codex, GitHub Copilot and Gemini CLI**: instead of attacking the model, the chain **abuses the trusted plugin marketplaces** that host agent extensions and **bypasses SHA-pinning safeguards**, so a poisoned plugin can execute code with the developer's privileges; **two of the four products had no patch available at disclosure**, and no in-the-wild exploitation has been reported


summary_zh: |
  **AIR Security 披露 Plugin4Shell**：一个影响四款主流 AI 编码 agent 的**零点击远程代码执行（RCE）**缺陷——**Claude Code、OpenAI Codex、GitHub Copilot 与 Gemini CLI**。该链路不攻击模型本身，而是**滥用托管 agent 插件的可信市场**并**绕过 SHA-pinning 防护**，使投毒插件能以开发者权限执行代码；**披露时四款产品中仍有两款无补丁可用**，暂无在野利用报告

summary_ja: |
  **AIR SecurityがPlugin4Shellを公表**：4つの主要AIコーディングエージェント——**Claude Code、OpenAI Codex、GitHub Copilot、Gemini CLI**——に影響する**ゼロクリックRCE**。モデルではなく**エージェント拡張を配る信頼済みプラグインマーケットプレイスを悪用**し、**SHAピン留めを回避**。汚染プラグインが開発者権限でコード実行可能になる。**開示時点で4製品中2つにパッチなし**、実被害の報告はない

summary_ko: |
  **AIR Security가 Plugin4Shell을 공개**했다: 4개 주요 AI 코딩 에이전트 — **Claude Code, OpenAI Codex, GitHub Copilot, Gemini CLI** — 에 영향을 주는 **제로클릭 RCE**. 모델이 아니라 **에이전트 확장을 배포하는 신뢰된 플러그인 마켓플레이스를 악용**하고 **SHA 고정을 우회**해, 오염된 플러그인이 개발자 권한으로 코드를 실행할 수 있다. **공개 시점에 4개 중 2개는 패치가 없었고**, 실제 악용 보고는 없다

summary_de: |
  **AIR Security veröffentlicht Plugin4Shell**: eine **Zero-Click-RCE**-Lücke in vier großen KI-Coding-Agenten — **Claude Code, OpenAI Codex, GitHub Copilot und Gemini CLI**. Die Kette greift nicht das Modell an, sondern **missbraucht die vertrauenswürdigen Plugin-Marktplätze** der Agenten und **umgeht SHA-Pinning**, sodass ein vergiftetes Plugin mit Entwicklerrechten Code ausführen kann; **zwei der vier Produkte hatten zur Offenlegung keinen Patch**, In-the-Wild-Ausnutzung ist nicht bekannt

summary_fr: |
  **AIR Security divulgue Plugin4Shell**, une faille d'**exécution de code à distance sans clic** touchant quatre agents de codage IA majeurs — **Claude Code, OpenAI Codex, GitHub Copilot et Gemini CLI** : la chaîne **exploite les places de marché de plugins de confiance** des agents et **contourne le SHA-pinning**, permettant à un plugin piégé d'exécuter du code avec les privilèges du développeur ; **deux des quatre produits n'avaient pas de correctif à la divulgation**, sans exploitation observée

summary_es: |
  **AIR Security divulga Plugin4Shell**, una falla de **ejecución remota de código sin clic** que afecta a cuatro agentes de código IA — **Claude Code, OpenAI Codex, GitHub Copilot y Gemini CLI**: la cadena **abusa de los mercados de plugins de confianza** de los agentes y **elude el SHA-pinning**, de modo que un plugin envenenado puede ejecutar código con privilegios del desarrollador; **dos de los cuatro productos no tenían parche al divulgarse**, sin explotación observada

sources:
  - url: https://www.theregister.com/security/2026/09/17/ai-coding-agents-0-click-rce-flaw-could-hand-attackers-keys-to-the-kingdom/5297335
    label: The Register
  - url: https://www.helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability/
    label: Help Net Security
  - url: https://cybersecuritynews.com/plugin4shell-zero-click-rce/
    label: Cybersecurity News

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# Plugin4Shell: a zero-click RCE chain hits four AI coding agents

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## Summary

**AIR Security discloses Plugin4Shell**, a **zero-click remote code execution** flaw affecting four major AI coding agents — **Claude Code, OpenAI Codex, GitHub Copilot and Gemini CLI**: instead of attacking the model, the chain **abuses the trusted plugin marketplaces** that host agent extensions and **bypasses SHA-pinning safeguards**, so a poisoned plugin can execute code with the developer's privileges; **two of the four products had no patch available at disclosure**, and no in-the-wild exploitation has been reported

## Attack chain

```mermaid
flowchart LR
    E["Poisoned plugin published to a trusted agent marketplace"]:::entry
    S0["Agent loads it; SHA-pinning safeguard bypassed (Plugin4Shell)"]:::step
    I["Zero-click code execution with the developer's privileges"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The mechanism.** Plugin4Shell targets the **plugin supply chain** rather than the model: the four agents all load extensions from marketplaces that developers are trained to trust, and the chain **bypasses the SHA-pinning controls** meant to lock an extension to a reviewed version. A malicious or compromised plugin then executes **without any user interaction** ("zero-click") in the developer's environment — the "keys to the kingdom" framing, since coding agents routinely hold source access, credentials and shell permissions.

**Status at disclosure.** AIR Security reported the issue to all affected vendors; **two of the four products still had no patch available** when the research was published, according to coverage. No in-the-wild exploitation has been reported.

**Why it matters.** It extends the September wave of agent-supply-chain findings (GitSpawn's malicious `.git/config`, RubyGems' GemStuffer abuse) from **config files and registries to plugin marketplaces**, and it lands days after the Hacktron chain showed how quickly agent-adjacent tooling can reach production systems. The practical guidance is unchanged but now wider: pin and verify what agents load, scope their credentials, and treat the marketplace as an unauthenticated input channel.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | The Register | <https://www.theregister.com/security/2026/09/17/ai-coding-agents-0-click-rce-flaw-could-hand-attackers-keys-to-the-kingdom/5297335> |
| 2 | Help Net Security | <https://www.helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability/> |
| 3 | Cybersecurity News | <https://cybersecuritynews.com/plugin4shell-zero-click-rce/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-17` (raw: 2026-09-17, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning |
| Severity | **High** `high` |
| Confidence | **B** — research organisation or mainstream media, with checkable detail |
| Real harm | no |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-17-plugin4shell-coding-agents` |

<sub>**Why this classification:** Vulnerability disclosure from a security research organisation; no known exploitation in the wild at disclosure (two products unpatched), so `real_harm: false`. Graded `high`: zero-click RCE across four widely deployed agents via a trusted channel. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-09-18` [Researchers used Claude to hack OpenAI's internal systems in a bug-bounty chain](2026-09-18-hacktron-claude-openai-hack.md)<br>  <sub>Researchers used Claude to hack OpenAI's internal systems in a bug-bounty chain</sub>
- `2026-09-01` [GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted](2026-09-01-gitspawn-git-config-pre-model-rce.md)<br>  <sub>GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted</sub>
- `2026-09-11` [Researchers link OpenAI agents to the RubyGems "GemStuffer" campaign](2026-09-11-rubygems-gemstuffer.md)<br>  <sub>Researchers link OpenAI agents to the RubyGems "GemStuffer" campaign</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-17-plugin4shell-coding-agents.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
