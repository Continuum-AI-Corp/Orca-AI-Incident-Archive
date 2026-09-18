---
id: 2026-06-01-miasma-worm
title: "Miasma worm"
title_zh: "Miasma 蠕虫"
title_ja: "Miasmaワーム"
title_ko: "Miasma 웜"
title_de: "Miasma-Wurm"
title_fr: "Le ver Miasma"
title_es: "El gusano Miasma"
date: 2026-06-01
date_precision: day
date_raw: "2026-06-01"

kind: incident
type: [SUPPLY, CRED]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  A Mini Shai-Hulud variant that punched through Red Hat's official npm channel. It triggers at npm install time using the **"Phantom Gyp"** trick in `binding.gyp`, and plants persistence hooks in VS Code / Cursor / **Claude Code**. It steals cloud, Kubernetes and repository credentials and sends them to an attacker-controlled GitHub account


summary_zh: |
  Mini Shai-Hulud 变种，打穿 Red Hat 官方 npm 渠道。用 `binding.gyp` 的 **"Phantom Gyp"** 技巧在 npm 安装时触发，并在 VS Code / Cursor / **Claude Code** 中植入持久化钩子。窃取云、Kubernetes、仓库凭据送往攻击者 GitHub 账号

summary_ja: |
  Red Hat公式のnpmチャネルを突破したMini Shai-Huludの変種。`binding.gyp`の**「Phantom Gyp」**トリックでnpm install時に発火し、VS Code／Cursor／**Claude Code**に永続化フックを仕込む。クラウド、Kubernetes、リポジトリの認証情報を窃取し、攻撃者制御のGitHubアカウントへ送信する

summary_ko: |
  Red Hat의 공식 npm 채널까지 뚫은 Mini Shai-Hulud 변종이다. `binding.gyp`의 **"Phantom Gyp"** 수법으로 npm install 시점에 작동하며, VS Code / Cursor / **Claude Code**에 지속성 훅을 심는다. 클라우드, Kubernetes, 저장소 자격 증명을 탈취해 공격자가 제어하는 GitHub 계정으로 보낸다

summary_de: |
  Eine Variante von Mini Shai-Hulud, die durch den offiziellen npm-Kanal von Red Hat drang. Er wird zum Zeitpunkt von npm install über den Trick **„Phantom Gyp“** in `binding.gyp` ausgelöst und pflanzt Persistenz-Hooks in VS Code / Cursor / **Claude Code**. Er stiehlt Cloud-, Kubernetes- und Repository-Zugangsdaten und sendet sie an ein vom Angreifer kontrolliertes GitHub-Konto

summary_fr: |
  Une variante de Mini Shai-Hulud qui a percé le canal npm officiel de Red Hat. Il se déclenche à l'installation npm avec l'astuce **« Phantom Gyp »** dans `binding.gyp`, et plante des hooks de persistance dans VS Code / Cursor / **Claude Code**. Il vole des identifiants cloud, Kubernetes et de dépôts et les envoie à un compte GitHub contrôlé par l'attaquant

summary_es: |
  Una variante de Mini Shai-Hulud que atravesó el canal oficial de npm de Red Hat. Se activa al instalar con npm usando el truco **"Phantom Gyp"** en `binding.gyp`, y planta hooks de persistencia en VS Code / Cursor / **Claude Code**. Roba credenciales de nube, Kubernetes y repositorios y las envía a una cuenta de GitHub controlada por el atacante

sources:
  - url: https://arstechnica.com/security/2026/06/dozens-of-red-hat-packages-backdoored-through-its-offical-npm-channel/
    label: Ars Technica
  - url: https://www.stepsecurity.io/blog/binding-gyp-npm-supply-chain-attack-spreads-like-worm
    label: StepSecurity
  - url: https://safedep.io/miasma-worm-ai-coding-agent-config-injection/
    label: safedep

disputed: false
landmark: true
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# Miasma worm

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

A Mini Shai-Hulud variant that punched through Red Hat's official npm channel. It triggers at npm install time using the **"Phantom Gyp"** trick in `binding.gyp`, and plants persistence hooks in VS Code / Cursor / **Claude Code**. It steals cloud, Kubernetes and repository credentials and sends them to an attacker-controlled GitHub account

## Attack chain

```mermaid
flowchart LR
    E["Poisoned package / repository / agent config"]:::entry
    S0["Developer or agent installs it automatically"]:::step
    S1["The agent picks it up and calls it"]:::step
    I["Credential abuse"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Ars Technica | <https://arstechnica.com/security/2026/06/dozens-of-red-hat-packages-backdoored-through-its-offical-npm-channel/> |
| 2 | StepSecurity | <https://www.stepsecurity.io/blog/binding-gyp-npm-supply-chain-attack-spreads-like-worm> |
| 3 | safedep | <https://safedep.io/miasma-worm-ai-coding-agent-config-injection/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-01` (raw: 2026-06-01, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-01-miasma-worm` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-06-01` [Attackers simply ask Meta's AI support bot for Instagram accounts](2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br>  <sub>Attackers simply ask Meta's AI support bot for Instagram accounts</sub>
- `2026-06-17` [Sapphire Sleet poisons every Mastra AI scope in 88 minutes](2026-06-17-sapphire-sleet-mastra-88-minutes.md)<br>  <sub>Sapphire Sleet poisons every Mastra AI scope in 88 minutes</sub>
- `2026-06-04` [Claude Oceanus-v1-p illegally redistributed](2026-06-04-claude-oceanus-fei-fa-fen.md)<br>  <sub>Claude Oceanus-v1-p illegally redistributed</sub>
- `2026-06-13` [PromptSnatcher: ad-blocking extensions steal AI conversations](2026-06-13-promptsnatcher-guang-gao-lan-jie.md)<br>  <sub>PromptSnatcher: ad-blocking extensions steal AI conversations</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-01-miasma-worm.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
