---
id: 2026-02-09-clinejection
title: "Clinejection"
title_zh: "Clinejection"
title_ja: "Clinejection"
title_ko: "Clinejection"
title_de: "Clinejection"
title_fr: "Clinejection"
title_es: "Clinejection"
date: 2026-02-09
date_precision: day
date_raw: "2026-02-09"

kind: incident
type: [SUPPLY, IPI]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **The most elegant agent supply-chain attack to date**: a prompt injection planted in a GitHub issue **title** → manipulated the `claude-code-action` automatic triage flow → arbitrary code execution → poisoned the GitHub Actions cache → stole publishing credentials such as `VSCE_PAT` → **a malicious Cline CLI was actually published**. **Exploited for real, not a PoC**


summary_zh: |
  **迄今最优雅的 agent 供应链攻击**：在 GitHub issue **标题**里埋提示注入 → 操纵 `claude-code-action` 自动分诊流程 → 任意代码执行 → 污染 GitHub Actions 缓存 → 窃取 `VSCE_PAT` 等发布凭据 → **真的发布了恶意 Cline CLI**。**实际被利用，非 PoC**

summary_ja: |
  **これまでで最もエレガントなエージェントサプライチェーン攻撃**：GitHubイシューの**タイトル**に仕込まれたプロンプトインジェクション→`claude-code-action`の自動トリアージフローを操作→任意コード実行→GitHub Actionsキャッシュを汚染→`VSCE_PAT`などの公開用認証情報を窃取→**悪性のCline CLIが実際に公開された**。**実際に悪用されており、PoCではない**

summary_ko: |
  **지금까지 가장 정교한 에이전트 공급망 공격**: GitHub 이슈 **제목**에 심은 프롬프트 인젝션 → `claude-code-action` 자동 분류 흐름 조작 → 임의 코드 실행 → GitHub Actions 캐시 오염 → `VSCE_PAT` 등 게시 자격 증명 탈취 → **실제로 악성 Cline CLI가 게시되었다**. **PoC가 아닌 실제 악용**

summary_de: |
  **Der eleganteste Agent-Supply-Chain-Angriff bisher**: Eine in den **Titel** eines GitHub-Issues gepflanzte Prompt-Injection → manipulierte den automatischen Triage-Ablauf von `claude-code-action` → beliebige Codeausführung → vergiftete den GitHub-Actions-Cache → stahl Veröffentlichungs-Zugangsdaten wie `VSCE_PAT` → **eine bösartige Cline CLI wurde tatsächlich veröffentlicht**. **Real ausgenutzt, kein PoC**

summary_fr: |
  **L'attaque de chaîne d'approvisionnement d'agent la plus élégante à ce jour** : une injection de prompt plantée dans le **titre** d'une issue GitHub → a manipulé le flux de triage automatique `claude-code-action` → exécution de code arbitraire → empoisonnement du cache GitHub Actions → vol d'identifiants de publication comme `VSCE_PAT` → **une CLI Cline malveillante a réellement été publiée**. **Exploitée pour de vrai, pas un PoC**

summary_es: |
  **El ataque de cadena de suministro de agentes más elegante hasta la fecha**: una inyección de prompt plantada en el **título** de un issue de GitHub → manipuló el flujo automático de triaje de `claude-code-action` → ejecución de código arbitrario → envenenó la caché de GitHub Actions → robó credenciales de publicación como `VSCE_PAT` → **se publicó realmente una CLI de Cline maliciosa**. **Explotado de verdad, no es un PoC**

sources:
  - url: https://adnanthekhan.com/posts/clinejection/#pre-publication
    label: adnanthekhan

disputed: false
landmark: true
scan_month: 2026-02
scan_ref: "SCAN.md §6 2026-02"
---

# Clinejection

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square)

## Summary

**The most elegant agent supply-chain attack to date**: a prompt injection planted in a GitHub issue **title** → manipulated the `claude-code-action` automatic triage flow → arbitrary code execution → poisoned the GitHub Actions cache → stole publishing credentials such as `VSCE_PAT` → **a malicious Cline CLI was actually published**. **Exploited for real, not a PoC**

## Attack chain

```mermaid
flowchart LR
    E["Poisoned packages / repositories / agent config"]:::entry
    S0["Developer or agent installs it automatically"]:::step
    S1["agent reads it and executes it as instructions"]:::step
    I["Acts beyond its authority as the attacker intends"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | adnanthekhan | <https://adnanthekhan.com/posts/clinejection/#pre-publication> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-02-09` (raw: 2026-02-09, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning · [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-02-09-clinejection` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md) · [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-02-01` [ClawHavoc campaign](2026-02-01-clawhavoc-zhan-yi.md)<br>  <sub>ClawHavoc campaign</sub>
- `2026-03-01` [Hades: a sustained campaign turning AI coding assistants into the attack surface](../2026-03/2026-03-01-hades-campaign-ai-coding-assistants.md)<br>  <sub>Hades: a sustained campaign turning AI coding assistants into the attack surface</sub>
- `2026-03-24` [Backdoored LiteLLM release](../2026-03/2026-03-24-litellm-backdoored-release.md)<br>  <sub>Backdoored LiteLLM release</sub>
- `2026-03-30` [Axios npm package compromised](../2026-03/2026-03-30-axios-npm-compromised.md)<br>  <sub>Axios npm package compromised</sub>

---

[← 2026-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-02/2026-02-09-clinejection.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
