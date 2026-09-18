---
id: 2025-08-08-salesloft-drift-oauth-theft
title: "Salesloft Drift OAuth token theft"
title_zh: "Salesloft Drift OAuth 令牌窃取"
title_ja: "Salesloft DriftのOAuthトークン窃取"
title_ko: "Salesloft Drift OAuth 토큰 탈취"
title_de: "Salesloft Drift: Diebstahl von OAuth-Token"
title_fr: "Vol de jetons OAuth de Salesloft Drift"
title_es: "Robo de tokens OAuth de Salesloft Drift"
date: 2025-08-08
date_end: 2025-08-18
date_precision: day
date_raw: "2025-08-08→18"

kind: incident
type: [SUPPLY, CRED]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  UNC6395 stole the OAuth tokens of the Drift AI chat agent, impersonated a trusted app and, over 10 days, systematically exported **700+ organizations'** Salesforce / Google Workspace / Slack data. Victims include Cloudflare, Google, PagerDuty, Palo Alto Networks, Proofpoint, SpyCloud, Tanium and Zscaler. **No exploit, no phishing — the trust chain of the AI integration itself was broken through**. GTIG published its report on 08-26


summary_zh: |
  UNC6395 盗取 Drift AI 聊天代理的 OAuth token，冒充可信应用，10 天内系统性导出 **700+ 组织**的 Salesforce / Google Workspace / Slack 数据。受害者含 Cloudflare、Google、PagerDuty、Palo Alto Networks、Proofpoint、SpyCloud、Tanium、Zscaler。**无 exploit、无钓鱼 —— AI 集成的信任链本身被打穿**。GTIG 08-26 发报告

summary_ja: |
  UNC6395がDrift AIチャットエージェントのOAuthトークンを窃取し、信頼されたアプリになりすまして、10日間にわたり**700社超の組織**のSalesforce／Google Workspace／Slackデータを体系的に持ち出した。被害者にはCloudflare、Google、PagerDuty、Palo Alto Networks、Proofpoint、SpyCloud、Tanium、Zscalerが含まれる。**エクスプロイトもフィッシングもなし——AI連携そのものの信頼チェーンが突破された**。GTIGは08-26にレポートを公開

summary_ko: |
  UNC6395는 Drift AI 챗 에이전트의 OAuth 토큰을 탈취해 신뢰된 앱으로 위장하고, 10일에 걸쳐 **700개 이상 조직**의 Salesforce / Google Workspace / Slack 데이터를 체계적으로 내보냈다. 피해자에는 Cloudflare, Google, PagerDuty, Palo Alto Networks, Proofpoint, SpyCloud, Tanium, Zscaler가 포함된다. **익스플로잇도 피싱도 없었다 — AI 통합 자체의 신뢰 체인이 뚫렸다**. GTIG는 08-26에 보고서를 발표했다

summary_de: |
  UNC6395 stahl die OAuth-Token des Drift-KI-Chat-Agenten, gab sich als vertrauenswürdige App aus und exportierte über 10 Tage systematisch die Salesforce-/Google-Workspace-/Slack-Daten von **700+ Organisationen**. Zu den Opfern gehören Cloudflare, Google, PagerDuty, Palo Alto Networks, Proofpoint, SpyCloud, Tanium und Zscaler. **Kein Exploit, kein Phishing — die Vertrauenskette der KI-Integration selbst wurde durchbrochen**. GTIG veröffentlichte seinen Bericht am 08-26

summary_fr: |
  UNC6395 a volé les jetons OAuth de l'agent conversationnel IA Drift, s'est fait passer pour une application de confiance et a, pendant 10 jours, exporté méthodiquement les données Salesforce / Google Workspace / Slack de **plus de 700 organisations**. Parmi les victimes : Cloudflare, Google, PagerDuty, Palo Alto Networks, Proofpoint, SpyCloud, Tanium et Zscaler. **Aucun exploit, aucun phishing — c'est la chaîne de confiance de l'intégration IA elle-même qui a été brisée**. GTIG a publié son rapport le 08-26

summary_es: |
  UNC6395 robó los tokens OAuth del agente de chat con IA Drift, suplantó una aplicación de confianza y, durante 10 días, exportó sistemáticamente datos de Salesforce / Google Workspace / Slack de **más de 700 organizaciones**. Entre las víctimas hay Cloudflare, Google, PagerDuty, Palo Alto Networks, Proofpoint, SpyCloud, Tanium y Zscaler. **Sin exploit ni phishing — se rompió la cadena de confianza de la propia integración de IA**. GTIG publicó su informe el 08-26

sources:
  - url: https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift
    label: Google Cloud/Mandiant
  - url: https://thehackernews.com/2025/08/salesloft-oauth-breach-via-drift-ai.html
    label: THN
  - url: https://www.finra.org/rules-guidance/guidance/salesloft-drift-AI-supply-chain-attack
    label: FINRA

disputed: false
landmark: true
scan_month: 2025-08
scan_ref: "SCAN.md §5 2025-08"
---

# Salesloft Drift OAuth token theft

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

UNC6395 stole the OAuth tokens of the Drift AI chat agent, impersonated a trusted app and, over 10 days, systematically exported **700+ organizations'** Salesforce / Google Workspace / Slack data. Victims include Cloudflare, Google, PagerDuty, Palo Alto Networks, Proofpoint, SpyCloud, Tanium and Zscaler. **No exploit, no phishing — the trust chain of the AI integration itself was broken through**. GTIG published its report on 08-26

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

## Details

In many general security reports this event is filed as an "OAuth leak", but the essence is that **the AI chat agent was granted long-lived, high-privilege cross-SaaS tokens because its job requires them**. Once that AI vendor is taken down, the 700-plus enterprises connected to it fall with it.
This is the most typical structural risk of the agent era: **an agent's value comes from the breadth of its permissions, and that breadth is the blast radius.**

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Google Cloud/Mandiant | <https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift> |
| 2 | THN | <https://thehackernews.com/2025/08/salesloft-oauth-breach-via-drift-ai.html> |
| 3 | FINRA | <https://www.finra.org/rules-guidance/guidance/salesloft-drift-AI-supply-chain-attack> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-08-08` → `2025-08-18` (raw: 2025-08-08→18, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-08-08-salesloft-drift-oauth-theft` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-08-26` [Nx "s1ngularity"](2025-08-26-nx-s1ngularity.md)<br>  <sub>Nx "s1ngularity"</sub>
- `2025-08-28` [TransUnion leaks 4.4-4.5M people via a third-party app](2025-08-28-transunion-jing-di-san-fang.md)<br>  <sub>TransUnion leaks 4.4-4.5M people via a third-party app</sub>
- `2025-07-13` [Amazon Q Developer extension poisoned](../2025-07/2025-07-13-amazon-q-extension-poisoned.md)<br>  <sub>Amazon Q Developer extension poisoned</sub>
- `2025-09-15` [Shai-Hulud npm worm v1](../2025-09/2025-09-15-shai-hulud-npm.md)<br>  <sub>Shai-Hulud npm worm v1</sub>

---

[← 2025-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-08/2025-08-08-salesloft-drift-oauth-theft.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
