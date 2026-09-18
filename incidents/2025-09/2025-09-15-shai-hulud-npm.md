---
id: 2025-09-15-shai-hulud-npm
title: "Shai-Hulud npm worm v1"
title_zh: "Shai-Hulud npm 蠕虫 v1"
title_ja: "Shai-Hulud npmワーム v1"
title_ko: "Shai-Hulud npm 웜 v1"
title_de: "Shai-Hulud npm-Wurm v1"
title_fr: "Le ver npm Shai-Hulud v1"
title_es: "Gusano npm Shai-Hulud v1"
date: 2025-09-15
date_precision: day
date_raw: "2025-09-15"

kind: incident
type: [SUPPLY, CRED]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **The first successful self-propagating attack in the npm ecosystem**. The postinstall script harvests secrets and exfiltrates them to public GitHub repositories the attackers created (named Shai-Hulud). CISA issued an alert on 09-23; **500+ packages** were affected. The theft targets explicitly include GitHub PATs, AWS/GCP/Azure keys, `ANTHROPIC_API_KEY`, Claude Code configs and `.mcp.json`. Wiz assesses it as sharing the same origin as s1ngularity


summary_zh: |
  **npm 生态首个成功自我传播的攻击**。postinstall 脚本收割密钥并外带到攻击者建的公开 GitHub 仓库（名为 Shai-Hulud）。CISA 09-23 发警报，**500+ 包**受影响。窃取目标明确包含 GitHub PAT、AWS/GCP/Azure 密钥、`ANTHROPIC_API_KEY`、Claude Code 配置与 `.mcp.json`。Wiz 评估与 s1ngularity 同源

summary_ja: |
  **npmエコシステムにおける初の自己増殖型攻撃の成功例**。postinstallスクリプトがシークレットを収集し、攻撃者が作成した公開GitHubリポジトリ（Shai-Huludという名前）へ外部送信する。CISAは09-23に警告を発出、**500以上のパッケージ**が影響を受けた。窃取対象にはGitHub PAT、AWS/GCP/Azureのキー、`ANTHROPIC_API_KEY`、Claude Codeの設定、`.mcp.json`が明示的に含まれる。Wizはs1ngularityと同一の起源を持つと評価している

summary_ko: |
  **npm 생태계에서 성공한 최초의 자기 전파 공격**. postinstall 스크립트가 비밀 정보를 수집해 공격자가 만든 공개 GitHub 저장소(Shai-Hulud라는 이름)로 유출한다. CISA는 09-23에 경보를 발령했고 **500개 이상의 패키지**가 영향을 받았다. 탈취 대상에는 GitHub PAT, AWS/GCP/Azure 키, `ANTHROPIC_API_KEY`, Claude Code 설정, `.mcp.json`이 명시적으로 포함된다. Wiz는 s1ngularity와 같은 출처로 평가했다

summary_de: |
  **Der erste erfolgreiche selbstverbreitende Angriff im npm-Ökosystem**. Das postinstall-Skript sammelt Secrets und exfiltriert sie in öffentliche GitHub-Repositories, die die Angreifer angelegt haben (mit dem Namen Shai-Hulud). CISA gab am 09-23 eine Warnung heraus; **500+ Pakete** waren betroffen. Zu den Diebstahlzielen gehören ausdrücklich GitHub-PATs, AWS/GCP/Azure-Schlüssel, `ANTHROPIC_API_KEY`, Claude-Code-Konfigurationen und `.mcp.json`. Wiz schätzt, dass es denselben Ursprung wie s1ngularity hat

summary_fr: |
  **La première attaque auto-propagatrice réussie dans l'écosystème npm**. Le script postinstall récolte des secrets et les exfiltre vers des dépôts GitHub publics créés par les attaquants (nommés Shai-Hulud). La CISA a émis une alerte le 09-23 ; **plus de 500 paquets** ont été touchés. Les cibles du vol incluent explicitement les PAT GitHub, les clés AWS/GCP/Azure, `ANTHROPIC_API_KEY`, les configurations Claude Code et `.mcp.json`. Wiz estime qu'il partage la même origine que s1ngularity

summary_es: |
  **El primer ataque autorreplicante exitoso en el ecosistema npm**. El script postinstall recolecta secretos y los exfiltra a repositorios públicos de GitHub creados por los atacantes (llamados Shai-Hulud). CISA emitió una alerta el 09-23; **más de 500 paquetes** se vieron afectados. Los objetivos del robo incluyen explícitamente PAT de GitHub, claves de AWS/GCP/Azure, `ANTHROPIC_API_KEY`, configuraciones de Claude Code y `.mcp.json`. Wiz evalúa que comparte el mismo origen que s1ngularity

sources:
  - url: https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack
    label: Wiz
  - url: https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem
    label: CISA

disputed: false
landmark: true
scan_month: 2025-09
scan_ref: "SCAN.md §5 2025-09"
---

# Shai-Hulud npm worm v1

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

**The first successful self-propagating attack in the npm ecosystem**. The postinstall script harvests secrets and exfiltrates them to public GitHub repositories the attackers created (named Shai-Hulud). CISA issued an alert on 09-23; **500+ packages** were affected. The theft targets explicitly include GitHub PATs, AWS/GCP/Azure keys, `ANTHROPIC_API_KEY`, Claude Code configs and `.mcp.json`. Wiz assesses it as sharing the same origin as s1ngularity

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
| 1 | Wiz | <https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack> |
| 2 | CISA | <https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-09-15` (raw: 2025-09-15, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-09-15-shai-hulud-npm` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-09-25` [postmark-mcp malicious npm package](2025-09-25-postmark-mcp-npm.md)<br>  <sub>postmark-mcp malicious npm package</sub>
- `2025-08-08` [Salesloft Drift OAuth token theft](../2025-08/2025-08-08-salesloft-drift-oauth-theft.md)<br>  <sub>Salesloft Drift OAuth token theft</sub>
- `2025-08-26` [Nx "s1ngularity"](../2025-08/2025-08-26-nx-s1ngularity.md)<br>  <sub>Nx "s1ngularity"</sub>
- `2025-08-28` [TransUnion leaks 4.4-4.5M people via a third-party app](../2025-08/2025-08-28-transunion-jing-di-san-fang.md)<br>  <sub>TransUnion leaks 4.4-4.5M people via a third-party app</sub>

---

[← 2025-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-09/2025-09-15-shai-hulud-npm.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
