---
id: 2026-05-11-tanstack-npm-mini-shai
title: "TanStack npm \"Mini Shai-Hulud\""
title_zh: "TanStack npm \"Mini Shai-Hulud\""
title_ja: "TanStack npmの「Mini Shai-Hulud」"
title_ko: "TanStack npm \"Mini Shai-Hulud\""
title_de: "TanStack npm „Mini Shai-Hulud“"
title_fr: "« Mini Shai-Hulud » sur npm TanStack"
title_es: "TanStack npm \"Mini Shai-Hulud\""
date: 2026-05-11
date_precision: day
date_raw: "2026-05-11"

kind: incident
type: [SUPPLY, CRED]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **TeamPCP** used GitHub Actions cache poisoning plus OIDC token extraction to compromise **42 `@tanstack/*` packages**, producing malicious packages **with valid SLSA provenance**. They included a "dead man's switch" that destroys the home directory and editor-persistence hooks. **In the malware, TeamPCP added a note saying the software was AI-developed**, and later open-sourced its worm on GitHub


summary_zh: |
  **TeamPCP** 用 GitHub Actions 缓存污染 + OIDC token 提取，攻陷 **42 个 `@tanstack/*` 包**，生成**带有效 SLSA 证明**的恶意包。含破坏 home 目录的「死亡开关」与编辑器持久化钩子。**TeamPCP 在恶意软件里附言称该软件由 AI 开发**，并随后在 GitHub 开源了自己的蠕虫

summary_ja: |
  **TeamPCP**がGitHub ActionsのキャッシュポイズニングとOIDCトークン抽出を組み合わせて**42個の`@tanstack/*`パッケージ**を侵害し、**有効なSLSA provenanceを備えた**悪性パッケージを生成した。ホームディレクトリを破壊する「デッドマンズスイッチ」とエディタの永続化フックも含まれていた。**マルウェア内でTeamPCPはソフトウェアがAI開発である旨の注記を追加**し、後にワームをGitHubでオープンソース化した

summary_ko: |
  **TeamPCP**는 GitHub Actions 캐시 오염과 OIDC 토큰 추출로 **`@tanstack/*` 패키지 42개**를 침해해 **유효한 SLSA 출처 증명까지 갖춘** 악성 패키지를 만들어냈다. 여기에는 홈 디렉터리를 파괴하는 "데드맨 스위치"와 편집기 지속성 훅이 포함되었다. **악성코드 안에서 TeamPCP는 이 소프트웨어가 AI로 개발되었다는 메모를 남겼고**, 이후 자사 웜을 GitHub에 오픈소스로 공개했다

summary_de: |
  **TeamPCP** nutzte Cache-Poisoning in GitHub Actions plus OIDC-Token-Extraktion, um **42 `@tanstack/*`-Pakete** zu kompromittieren, und erzeugte bösartige Pakete **mit gültiger SLSA-Provenienz**. Sie enthielten einen „Dead Man's Switch“, der das Home-Verzeichnis zerstört, sowie Persistenz-Hooks für Editoren. **In der Malware hinterließ TeamPCP einen Hinweis, die Software sei KI-entwickelt**, und veröffentlichte seinen Wurm später als Open Source auf GitHub

summary_fr: |
  **TeamPCP** a utilisé l'empoisonnement du cache GitHub Actions plus l'extraction de jetons OIDC pour compromettre **42 paquets `@tanstack/*`**, produisant des paquets malveillants **avec une provenance SLSA valide**. Ils incluaient un « dead man's switch » qui détruit le répertoire home et des hooks de persistance pour l'éditeur. **Dans le malware, TeamPCP a ajouté une note indiquant que le logiciel était développé par IA**, et a ensuite publié son ver en open source sur GitHub

summary_es: |
  **TeamPCP** usó envenenamiento de la caché de GitHub Actions más extracción de tokens OIDC para comprometer **42 paquetes `@tanstack/*`**, produciendo paquetes maliciosos **con procedencia SLSA válida**. Incluían un "interruptor de hombre muerto" que destruye el directorio home y hooks de persistencia en editores. **En el malware, TeamPCP añadió una nota diciendo que el software fue desarrollado con IA**, y después publicó su gusano como código abierto en GitHub

sources:
  - url: https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx
    label: TanStack advisory
  - url: https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem
    label: StepSecurity
  - url: https://www.theregister.com/security/2026/05/13/malware-crew-teampcp-open-sources-its-shai-hulud-worm-on-github/5239319
    label: The Register

disputed: false
landmark: true
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# TanStack npm "Mini Shai-Hulud"

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

**TeamPCP** used GitHub Actions cache poisoning plus OIDC token extraction to compromise **42 `@tanstack/*` packages**, producing malicious packages **with valid SLSA provenance**. They included a "dead man's switch" that destroys the home directory and editor-persistence hooks. **In the malware, TeamPCP added a note saying the software was AI-developed**, and later open-sourced its worm on GitHub

## Attack chain

```mermaid
flowchart LR
    E["Poisoned package / repository / agent config"]:::entry
    S0["Developer or agent installs it automatically"]:::step
    S1["The agent picks them up and calls out"]:::step
    I["Credentials are abused"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | TanStack advisory | <https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx> |
| 2 | StepSecurity | <https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem> |
| 3 | The Register | <https://www.theregister.com/security/2026/05/13/malware-crew-teampcp-open-sources-its-shai-hulud-worm-on-github/5239319> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-11` (raw: 2026-05-11, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-11-tanstack-npm-mini-shai` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-05-19` [TrapDoor: poisoning three ecosystems to corrupt AI assistant configs](2026-05-19-trapdoor-poisons-agent-configs.md)<br>  <sub>TrapDoor: poisoning three ecosystems to corrupt AI assistant configs</sub>
- `2026-05-21` [Composio: agent automation itself becomes the privilege-escalation path](2026-05-21-composio-agent-automation-privesc.md)<br>  <sub>Composio: agent automation itself becomes the privilege-escalation path</sub>
- `2026-05-18` [3,800 internal GitHub repositories compromised](2026-05-18-github-3800-internal-repos.md)<br>  <sub>3,800 internal GitHub repositories compromised</sub>
- `2026-05-04` [Braintrust's AWS account compromised, all customers told to rotate AI keys](2026-05-04-braintrust-aws-zhang-hao-gong.md)<br>  <sub>Braintrust's AWS account compromised, all customers told to rotate AI keys</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-11-tanstack-npm-mini-shai.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
