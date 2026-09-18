---
id: 2025-08-26-nx-s1ngularity
title: "Nx \"s1ngularity\""
title_zh: "Nx \"s1ngularity\""
title_ja: "Nx「s1ngularity」"
title_ko: "Nx \"s1ngularity\""
title_de: "Nx „s1ngularity“"
title_fr: "Nx « s1ngularity »"
title_es: "Nx \"s1ngularity\""
date: 2025-08-26
date_precision: day
date_raw: "2025-08-26"

kind: incident
type: [SUPPLY, CRED]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **The first malware to weaponize AI CLIs**: it checks whether Claude Code / Gemini CLI / Amazon Q are installed locally, then **directs those agents to scan for and collect credentials**. It steals GitHub tokens, SSH keys, wallets and private keys and writes them into public repositories the attackers created. Affected **2,180 GitHub accounts and 7,200 repositories**


summary_zh: |
  **首个把 AI CLI 武器化的恶意软件**：检测本机是否装了 Claude Code / Gemini CLI / Amazon Q，然后**指挥这些 agent 去扫描并收集凭据**。窃取 GitHub token、SSH 密钥、钱包与密钥，写入攻击者创建的公开仓库。影响 **2,180 个 GitHub 账号、7,200 个仓库**

summary_ja: |
  **AI CLIを兵器化した初のマルウェア**：Claude Code／Gemini CLI／Amazon Qがローカルにインストールされているかを確認し、**それらのエージェントに認証情報の探索・収集を指示する**。GitHubトークン、SSHキー、ウォレット、秘密鍵を窃取し、攻撃者が作成した公開リポジトリに書き込む。**2,180のGitHubアカウントと7,200のリポジトリ**が影響を受けた

summary_ko: |
  **AI CLI를 무기화한 최초의 악성코드**: 로컬에 Claude Code / Gemini CLI / Amazon Q가 설치되어 있는지 확인한 뒤 **그 에이전트들에게 자격 증명을 스캔·수집하도록 지시**한다. GitHub 토큰, SSH 키, 지갑, 개인 키를 탈취해 공격자가 만든 공개 저장소에 기록한다. **GitHub 계정 2,180개와 저장소 7,200개**가 영향을 받았다

summary_de: |
  **Die erste Malware, die KI-CLIs als Waffe einsetzt**: Sie prüft, ob Claude Code / Gemini CLI / Amazon Q lokal installiert sind, und **weist diese Agenten an, nach Zugangsdaten zu suchen und sie zu sammeln**. Sie stiehlt GitHub-Token, SSH-Schlüssel, Wallets und private Schlüssel und schreibt sie in öffentliche Repositories, die die Angreifer angelegt haben. Betroffen: **2,180 GitHub-Konten und 7,200 Repositories**

summary_fr: |
  **Le premier malware à weaponiser les CLI d'IA** : il vérifie si Claude Code / Gemini CLI / Amazon Q sont installés localement, puis **ordonne à ces agents de rechercher et collecter des identifiants**. Il vole des jetons GitHub, des clés SSH, des portefeuilles et des clés privées et les écrit dans des dépôts publics créés par les attaquants. **2 180 comptes GitHub et 7 200 dépôts** touchés

summary_es: |
  **El primer malware que convirtió las CLI de IA en armas**: comprueba si Claude Code / Gemini CLI / Amazon Q están instalados localmente y luego **dirige a esos agentes a buscar y recolectar credenciales**. Roba tokens de GitHub, claves SSH, carteras y claves privadas y las escribe en repositorios públicos creados por los atacantes. Afectó a **2,180 cuentas de GitHub y 7,200 repositorios**

sources:
  - url: https://www.wiz.io/blog/s1ngularity-supply-chain-attack
    label: Wiz
  - url: https://www.bleepingcomputer.com/news/security/ai-powered-malware-hit-2-180-github-accounts-in-s1ngularity-attack/
    label: BleepingComputer

disputed: false
landmark: true
scan_month: 2025-08
scan_ref: "SCAN.md §5 2025-08"
---

# Nx "s1ngularity"

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

**The first malware to weaponize AI CLIs**: it checks whether Claude Code / Gemini CLI / Amazon Q are installed locally, then **directs those agents to scan for and collect credentials**. It steals GitHub tokens, SSH keys, wallets and private keys and writes them into public repositories the attackers created. Affected **2,180 GitHub accounts and 7,200 repositories**

## Attack chain

```mermaid
flowchart LR
    E["Poisoned package / repository / agent config"]:::entry
    S0["Developer or agent installs it automatically"]:::step
    S1["The agent retrieves and uses it"]:::step
    I["Credential abuse"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Wiz | <https://www.wiz.io/blog/s1ngularity-supply-chain-attack> |
| 2 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/ai-powered-malware-hit-2-180-github-accounts-in-s1ngularity-attack/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-08-26` (raw: 2025-08-26, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-08-26-nx-s1ngularity` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-08-08` [Salesloft Drift OAuth token theft](2025-08-08-salesloft-drift-oauth-theft.md)<br>  <sub>Salesloft Drift OAuth token theft</sub>
- `2025-08-28` [TransUnion leaks 4.4-4.5M people via a third-party app](2025-08-28-transunion-jing-di-san-fang.md)<br>  <sub>TransUnion leaks 4.4-4.5M people via a third-party app</sub>
- `2025-07-13` [Amazon Q Developer extension poisoned](../2025-07/2025-07-13-amazon-q-extension-poisoned.md)<br>  <sub>Amazon Q Developer extension poisoned</sub>
- `2025-09-15` [Shai-Hulud npm worm v1](../2025-09/2025-09-15-shai-hulud-npm.md)<br>  <sub>Shai-Hulud npm worm v1</sub>

---

[← 2025-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-08/2025-08-26-nx-s1ngularity.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
