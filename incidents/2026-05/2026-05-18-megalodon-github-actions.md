---
id: 2026-05-18-megalodon-github-actions
title: "Megalodon: malicious Actions injected into 5,500+ GitHub repositories"
title_zh: "Megalodon：5,500+ GitHub 仓库被注入恶意 Actions"
title_ja: "Megalodon：5,500以上のGitHubリポジトリに悪性Actionsが注入"
title_ko: "Megalodon: GitHub 저장소 5,500개 이상에 악성 Actions 주입"
title_de: "Megalodon: bösartige Actions in 5,500+ GitHub-Repositories eingeschleust"
title_fr: "Megalodon : des Actions malveillantes injectées dans plus de 5 500 dépôts GitHub"
title_es: "Megalodon: Actions maliciosas inyectadas en más de 5,500 repositorios de GitHub"
date: 2026-05-18
date_precision: day
date_raw: "2026-05-18"

kind: incident
type: [SUPPLY]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  A dual payload: the automatically executing `SysDiag` plus a dormant backdoor `Optimize-Build` triggered by `workflow_dispatch`, stealing CI/CD environment variables, cloud credentials and OIDC tokens to an external C2. The blast radius included several npm packages commonly used by AI applications, among them `@tiledesk/tiledesk-server`


summary_zh: |
  双载荷：自动执行的 `SysDiag` + `workflow_dispatch` 触发的休眠后门 `Optimize-Build`，窃取 CI/CD 环境变量、云凭据、OIDC token 到外部 C2。波及 `@tiledesk/tiledesk-server` 等多个 AI 应用常用 npm 包

summary_ja: |
  二重ペイロード：自動実行される`SysDiag`と、`workflow_dispatch`で起動する休眠バックドア`Optimize-Build`。CI/CD環境変数、クラウド認証情報、OIDCトークンを外部C2へ窃取する。影響範囲にはAIアプリケーションでよく使われるnpmパッケージも含まれ、`@tiledesk/tiledesk-server`などが該当する

summary_ko: |
  이중 페이로드: 자동 실행되는 `SysDiag`와 `workflow_dispatch`로 작동하는 휴면 백도어 `Optimize-Build`로, CI/CD 환경 변수, 클라우드 자격 증명, OIDC 토큰을 외부 C2로 탈취한다. 영향 범위에는 AI 애플리케이션에서 흔히 쓰이는 여러 npm 패키지가 포함되었고 그중 하나가 `@tiledesk/tiledesk-server`다

summary_de: |
  Eine doppelte Nutzlast: das automatisch ausgeführte `SysDiag` plus eine schlafende Backdoor `Optimize-Build`, die durch `workflow_dispatch` ausgelöst wird und CI/CD-Umgebungsvariablen, Cloud-Zugangsdaten und OIDC-Token an einen externen C2 stiehlt. Der Wirkungsradius umfasste mehrere npm-Pakete, die häufig in KI-Anwendungen genutzt werden, darunter `@tiledesk/tiledesk-server`

summary_fr: |
  Une double charge : le `SysDiag` à exécution automatique plus une backdoor dormante `Optimize-Build` déclenchée par `workflow_dispatch`, volant des variables d'environnement CI/CD, des identifiants cloud et des jetons OIDC vers un C2 externe. Le rayon d'impact inclut plusieurs paquets npm couramment utilisés par des applications d'IA, dont `@tiledesk/tiledesk-server`

summary_es: |
  Una carga útil doble: el `SysDiag` de ejecución automática más una puerta trasera latente `Optimize-Build` activada por `workflow_dispatch`, que roba variables de entorno de CI/CD, credenciales de nube y tokens OIDC hacia un C2 externo. El radio de impacto incluyó varios paquetes npm usados habitualmente por aplicaciones de IA, entre ellos `@tiledesk/tiledesk-server`

sources:
  - url: https://safedep.io/megalodon-mass-github-repo-backdooring-ci-workflows/
    label: safedep

disputed: false
landmark: true
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# Megalodon: malicious Actions injected into 5,500+ GitHub repositories

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## Summary

A dual payload: the automatically executing `SysDiag` plus a dormant backdoor `Optimize-Build` triggered by `workflow_dispatch`, stealing CI/CD environment variables, cloud credentials and OIDC tokens to an external C2. The blast radius included several npm packages commonly used by AI applications, among them `@tiledesk/tiledesk-server`

## Attack chain

```mermaid
flowchart LR
    E["Poisoned package / repository / agent config"]:::entry
    S0["Developer or agent installs it automatically"]:::step
    I["Credential theft and self-propagation"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | safedep | <https://safedep.io/megalodon-mass-github-repo-backdooring-ci-workflows/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-18` (raw: 2026-05-18, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-18-megalodon-github-actions` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-05-19` [TrapDoor: poisoning three ecosystems to corrupt AI assistant configs](2026-05-19-trapdoor-poisons-agent-configs.md)<br>  <sub>TrapDoor: poisoning three ecosystems to corrupt AI assistant configs</sub>
- `2026-05-21` [Composio: agent automation itself becomes the privilege-escalation path](2026-05-21-composio-agent-automation-privesc.md)<br>  <sub>Composio: agent automation itself becomes the privilege-escalation path</sub>
- `2026-05-11` [TanStack npm "Mini Shai-Hulud"](2026-05-11-tanstack-npm-mini-shai.md)<br>  <sub>TanStack npm "Mini Shai-Hulud"</sub>
- `2026-05-18` [3,800 internal GitHub repositories compromised](2026-05-18-github-3800-internal-repos.md)<br>  <sub>3,800 internal GitHub repositories compromised</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-18-megalodon-github-actions.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
