---
id: 2025-11-21-shai-hulud
title: "Shai-Hulud 2.0"
title_zh: "Shai-Hulud 2.0"
title_ja: "Shai-Hulud 2.0"
title_ko: "Shai-Hulud 2.0"
title_de: "Shai-Hulud 2.0"
title_fr: "Shai-Hulud 2.0"
title_es: "Shai-Hulud 2.0"
date: 2025-11-21
date_end: 2025-11-24
date_precision: day
date_raw: "2025-11-21→24"

kind: incident
type: [SUPPLY, CRED]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  The second wave of the self-replicating worm: **796 unique npm packages** backdoored, **25,000+ repositories / about 350 users** affected (Zapier, ENS Domains, PostHog, Postman and others). It now runs at the **preinstall stage** (before dependency resolution), hitting build systems nearly 100% of the time with no user interaction required


summary_zh: |
  第二波自我复制蠕虫，**796 个唯一 npm 包**被后门化，**25,000+ 仓库 / 约 350 个用户**受影响（Zapier、ENS Domains、PostHog、Postman 等）。改在 **preinstall 阶段**执行（依赖解析前），在构建系统上近乎 100% 命中、无需任何用户交互

summary_ja: |
  自己複製ワームの第2波：**796個の固有のnpmパッケージ**にバックドアが仕込まれ、**25,000以上のリポジトリ／約350ユーザー**が影響を受けた（Zapier、ENS Domains、PostHog、Postmanなど）。今回は**preinstall段階**（依存関係解決の前）で実行され、ユーザー操作なしでほぼ100%の確率でビルドシステムに到達する

summary_ko: |
  자기 복제 웜의 두 번째 파도: **서로 다른 npm 패키지 796개**에 백도어가 심어졌고 **저장소 25,000개 이상 / 사용자 약 350명**이 영향을 받았다(Zapier, ENS Domains, PostHog, Postman 등). 이제 **preinstall 단계**(의존성 해석 전)에서 실행되어 사용자 상호작용 없이 거의 100%의 확률로 빌드 시스템을 감염시킨다

summary_de: |
  Die zweite Welle des selbstreplizierenden Wurms: **796 eindeutige npm-Pakete** mit Backdoor versehen, **25,000+ Repositories / etwa 350 Nutzer** betroffen (Zapier, ENS Domains, PostHog, Postman und andere). Er läuft nun in der **preinstall-Phase** (vor der Abhängigkeitsauflösung) und trifft Build-Systeme nahezu zu 100%, ohne dass eine Nutzerinteraktion nötig ist

summary_fr: |
  La deuxième vague du ver auto-répliquant : **796 paquets npm uniques** backdoorés, **plus de 25 000 dépôts / environ 350 utilisateurs** touchés (Zapier, ENS Domains, PostHog, Postman et d'autres). Il s'exécute désormais à l'étape **preinstall** (avant la résolution des dépendances), frappant les systèmes de build dans près de 100 % des cas sans aucune interaction de l'utilisateur

summary_es: |
  La segunda ola del gusano autorreplicante: **796 paquetes npm únicos** con puerta trasera, **más de 25,000 repositorios / unos 350 usuarios** afectados (Zapier, ENS Domains, PostHog, Postman y otros). Ahora se ejecuta en la **etapa de preinstall** (antes de la resolución de dependencias), alcanzando los sistemas de compilación casi el 100% de las veces sin requerir interacción del usuario

sources:
  - url: https://www.wiz.io/blog/shai-hulud-2-0-ongoing-supply-chain-attack
    label: Wiz
  - url: https://unit42.paloaltonetworks.com/npm-supply-chain-attack/
    label: Unit 42
  - url: https://securitylabs.datadoghq.com/articles/shai-hulud-2.0-npm-worm/
    label: Datadog

disputed: false
landmark: true
scan_month: 2025-11
scan_ref: "SCAN.md §5 2025-11"
---

# Shai-Hulud 2.0

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

The second wave of the self-replicating worm: **796 unique npm packages** backdoored, **25,000+ repositories / about 350 users** affected (Zapier, ENS Domains, PostHog, Postman and others). It now runs at the **preinstall stage** (before dependency resolution), hitting build systems nearly 100% of the time with no user interaction required

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
| 1 | Wiz | <https://www.wiz.io/blog/shai-hulud-2-0-ongoing-supply-chain-attack> |
| 2 | Unit 42 | <https://unit42.paloaltonetworks.com/npm-supply-chain-attack/> |
| 3 | Datadog | <https://securitylabs.datadoghq.com/articles/shai-hulud-2.0-npm-worm/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-11-21` → `2025-11-24` (raw: 2025-11-21→24, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-11-21-shai-hulud` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-11-25` [OpenAI reports the third-party Mixpanel breach](2025-11-25-mixpanel-tong-bao-di-san.md)<br>  <sub>OpenAI reports the third-party Mixpanel breach</sub>
- `2025-10-28` [Claude Code API key exfiltration](../2025-10/2025-10-28-claude-code-api.md)<br>  <sub>Claude Code API key exfiltration</sub>
- `2025-12-15` ["Privacy" browser extensions resell AI conversations](../2025-12/2025-12-15-yin-si-liu-lan-qi.md)<br>  <sub>"Privacy" browser extensions resell AI conversations</sub>
- `2025-12-30` [Chrome extensions steal ChatGPT and DeepSeek conversations](../2025-12/2025-12-30-chrome-chatgpt-deepseek.md)<br>  <sub>Chrome extensions steal ChatGPT and DeepSeek conversations</sub>

---

[← 2025-11 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-11/2025-11-21-shai-hulud.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
