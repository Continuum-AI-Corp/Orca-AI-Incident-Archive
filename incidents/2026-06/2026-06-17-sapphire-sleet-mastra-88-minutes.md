---
id: 2026-06-17-sapphire-sleet-mastra-88-minutes
title: "Sapphire Sleet poisons every Mastra AI scope in 88 minutes"
title_zh: "Sapphire Sleet 88 分钟投毒 Mastra AI 全 scope"
title_ja: "Sapphire Sleetが88分でMastraのAIスコープすべてを汚染"
title_ko: "Sapphire Sleet, 88분 만에 모든 Mastra AI 스코프를 오염시키다"
title_de: "Sapphire Sleet vergiftet in 88 Minuten den gesamten Mastra-KI-Scope"
title_fr: "Sapphire Sleet empoisonne tout le périmètre Mastra AI en 88 minutes"
title_es: "Sapphire Sleet envenena todo el ámbito de Mastra AI en 88 minutos"
date: 2026-06-17
date_precision: day
date_raw: "2026-06-17"

kind: incident
type: [SUPPLY, CRED]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  North Korea-linked **Sapphire Sleet** compromised the npm account of **ehindero** — a **former Mastra contributor whose publish rights were never revoked**. With that account it published poisoned versions of **144 packages** under the `@mastra` scope within **88 minutes**, together exceeding **1.1 million** weekly downloads.
  The technique: each poisoned version injected a new dependency, **`easy-day-js`** (a typosquat of `dayjs`), whose postinstall hook fired on every developer machine running `npm install`. The attacker first published a harmless "bait" version 1.11.21, then shipped a weaponized 1.11.22 carrying an obfuscated dropper. The payload is a cross-platform infostealer that **targets 166 cryptocurrency wallet extensions** and opens a persistent backdoor on developer workstations and CI/CD.
  Microsoft attributes it to Sapphire Sleet with **high confidence**, citing infrastructure overlap, **tactical consistency with the Axios campaign**, and the group's established goal of stealing cryptocurrency to convert into hard currency


summary_zh: |
  朝鲜系 **Sapphire Sleet** 攻陷了 **ehindero** 的 npm 账号 —— 一名 **Mastra 的前贡献者，其发布权限从未被回收**。用该账号在 **88 分钟内**为 `@mastra` scope 下 **144 个包**发布投毒版本，合计周下载量超 **110 万**。
  手法：每个投毒版本注入新依赖 **`easy-day-js`**（`dayjs` 的 typosquat），postinstall 钩子在每台 `npm install` 的开发机上触发。攻击者先发布无害「诱饵」版 1.11.21，再发武器化版 1.11.22 投放混淆 dropper。载荷是跨平台信息窃取器，**瞄准 166 个加密货币钱包扩展**，并在开发者工作站与 CI/CD 上开持久后门。
  Microsoft 以**高置信度**归因 Sapphire Sleet，依据是基础设施重叠、**与 Axios 行动的手法一致**、以及该组织窃取加密货币换取硬通货的一贯目标

summary_ja: |
  北朝鮮関連の**Sapphire Sleet**が**ehindero**のnpmアカウントを侵害した——**元Mastraのコントリビューターで、公開権限が一度も取り消されていなかった**。そのアカウントで**`@mastra`スコープの144パッケージ**の汚染版を**88分以内に**公開し、合計で週間**110万回**以上のダウンロードに達した。
  手法：汚染版はそれぞれ新しい依存関係**`easy-day-js`**（`dayjs`のtyposquat）を注入し、そのpostinstallフックが`npm install`を実行するすべての開発者マシンで発火した。攻撃者はまず無害な「餌」バージョン1.11.21を公開し、次に難読化されたドロッパーを搭載した武器化版1.11.22を出荷した。ペイロードは**166種類の暗号資産ウォレット拡張機能を標的とする**クロスプラットフォームのインフォスティーラーで、開発者ワークステーションとCI/CDに永続的バックドアを開く。
  Microsoftはインフラの重なり、**Axiosキャンペーンとの戦術的一貫性**、暗号資産を窃取してハードカレンシーに換えるという同グループの確立された目標を根拠に、Sapphire Sleetに**高い確度**で帰属している

summary_ko: |
  북한 연계 **Sapphire Sleet**이 **ehindero**의 npm 계정을 침해했다 — 이는 **Mastra의 전 기여자로 게시 권한이 회수되지 않았던 인물**이다. 이 계정으로 **88분** 안에 `@mastra` 스코프의 **패키지 144개**에 오염된 버전을 게시했고, 주간 다운로드 수를 합치면 **110만 회**를 넘는다.
  수법: 오염된 버전마다 새 의존성 **`easy-day-js`**(`dayjs`의 타이포스쿼트)를 주입했고, 그 postinstall 훅이 `npm install`을 실행하는 모든 개발자 머신에서 작동했다. 공격자는 먼저 무해한 "미끼" 버전 1.11.21을 게시한 뒤 난독화된 드로퍼를 담은 무기화 버전 1.11.22를 배포했다. 페이로드는 **가상자산 지갑 확장 프로그램 166개를 겨냥**하고 개발자 워크스테이션과 CI/CD에 영구 백도어를 여는 크로스 플랫폼 정보 탈취기다.
  마이크로소프트는 인프라 중첩, **Axios 작전과의 전술적 일관성**, 가상자산을 탈취해 경화로 바꾸려는 조직의 기존 목표를 근거로 **높은 확신**으로 Sapphire Sleet에 귀속했다

summary_de: |
  Die mit Nordkorea verbundene Gruppe **Sapphire Sleet** kompromittierte das npm-Konto von **ehindero** — eines **ehemaligen Mastra-Mitwirkenden, dessen Veröffentlichungsrechte nie entzogen wurden**. Mit diesem Konto veröffentlichte sie innerhalb von **88 Minuten** vergiftete Versionen von **144 Paketen** im Scope `@mastra`, die zusammen mehr als **1.1 Millionen** wöchentliche Downloads erreichen.
  Die Technik: Jede vergiftete Version fügte eine neue Abhängigkeit hinzu, **`easy-day-js`** (ein Typosquat von `dayjs`), deren postinstall-Hook auf jedem Entwicklerrechner ausgelöst wurde, der `npm install` ausführte. Der Angreifer veröffentlichte zunächst eine harmlose „Köder“-Version 1.11.21 und lieferte dann eine bewaffnete 1.11.22 mit einem obfuskierten Dropper aus. Die Nutzlast ist ein plattformübergreifender Infostealer, der **auf 166 Krypto-Wallet-Erweiterungen abzielt** und auf Entwicklerarbeitsplätzen und in CI/CD eine persistente Backdoor öffnet.
  Microsoft schreibt es Sapphire Sleet mit **hoher Konfidenz** zu und verweist auf überlappende Infrastruktur, **taktische Übereinstimmung mit der Axios-Kampagne** und das etablierte Ziel der Gruppe, Kryptowährungen zu stehlen und in Hartwährung umzuwandeln

summary_fr: |
  Le groupe lié à la Corée du Nord **Sapphire Sleet** a compromis le compte npm de **ehindero** — **un ancien contributeur de Mastra dont les droits de publication n'ont jamais été révoqués**. Avec ce compte, il a publié en **88 minutes** des versions empoisonnées de **144 paquets** du périmètre `@mastra`, totalisant ensemble plus de **1,1 million** de téléchargements hebdomadaires.
  La technique : chaque version empoisonnée injectait une nouvelle dépendance, **`easy-day-js`** (un typosquat de `dayjs`), dont le hook postinstall se déclenchait sur chaque machine de développeur exécutant `npm install`. L'attaquant a d'abord publié une version « appât » inoffensive 1.11.21, puis livré une 1.11.22 weaponisée portant un dropper obfusqué. La charge est un infostealer multiplateforme qui **cible 166 extensions de portefeuilles de cryptomonnaies** et ouvre une backdoor persistante sur les postes de développeurs et les CI/CD.
  Microsoft l'attribue à Sapphire Sleet avec **un haut degré de confiance**, citant le chevauchement d'infrastructure, **la cohérence tactique avec la campagne Axios**, et l'objectif établi du groupe de voler des cryptomonnaies pour les convertir en monnaie fiduciaire

summary_es: |
  **Sapphire Sleet**, vinculado a Corea del Norte, comprometió la cuenta de npm de **ehindero** — un **antiguo colaborador de Mastra cuyos derechos de publicación nunca se revocaron**. Con esa cuenta publicó versiones envenenadas de **144 paquetes** del ámbito `@mastra` en **88 minutos**, que en conjunto suman más de **1.1 millones** de descargas semanales.
  La técnica: cada versión envenenada inyectaba una nueva dependencia, **`easy-day-js`** (un typosquat de `dayjs`), cuyo hook postinstall se disparaba en cada máquina de desarrollador que ejecutara `npm install`. El atacante publicó primero una versión "cebo" inofensiva, la 1.11.21, y luego lanzó una 1.11.22 armada con un dropper ofuscado. La carga útil es un infostealer multiplataforma que **ataca 166 extensiones de carteras de criptomonedas** y abre una puerta trasera persistente en estaciones de trabajo de desarrolladores y en CI/CD.
  Microsoft lo atribuye a Sapphire Sleet con **alta confianza**, citando la superposición de infraestructura, la **coherencia táctica con la campaña de Axios** y el objetivo ya establecido del grupo de robar criptomonedas para convertirlas en dinero fiduciario

sources:
  - url: https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/
    label: Microsoft
  - url: https://safedep.io/mastra-npm-scope-takeover-supply-chain-attack/
    label: safedep
  - url: https://www.securityweek.com/north-korean-hackers-blamed-for-mastra-npm-supply-chain-attack/
    label: SecurityWeek

disputed: false
landmark: true
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# Sapphire Sleet poisons every Mastra AI scope in 88 minutes

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

North Korea-linked **Sapphire Sleet** compromised the npm account of **ehindero** — a **former Mastra contributor whose publish rights were never revoked**. With that account it published poisoned versions of **144 packages** under the `@mastra` scope within **88 minutes**, together exceeding **1.1 million** weekly downloads.

The technique: each poisoned version injected a new dependency, **`easy-day-js`** (a typosquat of `dayjs`), whose postinstall hook fired on every developer machine running `npm install`. The attacker first published a harmless "bait" version 1.11.21, then shipped a weaponized 1.11.22 carrying an obfuscated dropper. The payload is a cross-platform infostealer that **targets 166 cryptocurrency wallet extensions** and opens a persistent backdoor on developer workstations and CI/CD.

Microsoft attributes it to Sapphire Sleet with **high confidence**, citing infrastructure overlap, **tactical consistency with the Axios campaign**, and the group's established goal of stealing cryptocurrency to convert into hard currency

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
| 1 | Microsoft | <https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/> |
| 2 | safedep | <https://safedep.io/mastra-npm-scope-takeover-supply-chain-attack/> |
| 3 | SecurityWeek | <https://www.securityweek.com/north-korean-hackers-blamed-for-mastra-npm-supply-chain-attack/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-17` (raw: 2026-06-17, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-17-sapphire-sleet-mastra-88-minutes` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-06-01` [Miasma worm](2026-06-01-miasma-worm.md)<br>  <sub>Miasma worm</sub>
- `2026-06-01` [Attackers simply ask Meta's AI support bot for Instagram accounts](2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br>  <sub>Attackers simply ask Meta's AI support bot for Instagram accounts</sub>
- `2026-06-04` [Claude Oceanus-v1-p illegally redistributed](2026-06-04-claude-oceanus-fei-fa-fen.md)<br>  <sub>Claude Oceanus-v1-p illegally redistributed</sub>
- `2026-06-13` [PromptSnatcher: ad-blocking extensions steal AI conversations](2026-06-13-promptsnatcher-guang-gao-lan-jie.md)<br>  <sub>PromptSnatcher: ad-blocking extensions steal AI conversations</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-17-sapphire-sleet-mastra-88-minutes.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
