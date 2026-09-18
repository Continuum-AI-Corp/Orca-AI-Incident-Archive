---
id: 2026-03-30-axios-npm-compromised
title: "Axios npm package compromised"
title_zh: "Axios npm 包被攻陷"
title_ja: "Axios npmパッケージが侵害される"
title_ko: "Axios npm 패키지 침해"
title_de: "Axios npm-Paket kompromittiert"
title_fr: "Le paquet npm Axios compromis"
title_es: "El paquete npm Axios comprometido"
date: 2026-03-30
date_precision: day
date_raw: "2026-03-30"

kind: incident
type: [SUPPLY]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  v1.14.1 and 0.30.4 were seeded with a malicious dependency `plain-crypto-js@4.2.1` that drops the cross-platform RAT **WAVESHAPER.V2** via postinstall (separate platform payloads in PowerShell/C++/Python). Attribution to North Korea-linked **UNC1069**. **Deepfakes were used to social-engineer the maintainer during the attack**. The malicious versions were live for about 3 hours; the package gets 100M+ weekly downloads


summary_zh: |
  v1.14.1 与 0.30.4 被植入恶意依赖 `plain-crypto-js@4.2.1`，经 postinstall 投放跨平台 RAT **WAVESHAPER.V2**（PowerShell/C++/Python 分平台载荷）。归因朝鲜系 **UNC1069**。**攻击过程中使用深度伪造对维护者做社工**。恶意版本存活约 3 小时，该包周下载量 1 亿+

summary_ja: |
  v1.14.1と0.30.4に悪性依存関係`plain-crypto-js@4.2.1`が仕込まれ、postinstall経由でクロスプラットフォームRAT**WAVESHAPER.V2**をドロップする（PowerShell/C++/Pythonのプラットフォーム別ペイロード）。帰属は北朝鮮関連の**UNC1069**。**攻撃中、メンテナーへのソーシャルエンジニアリングにディープフェイクが使われた**。悪性バージョンは約3時間公開されていた。このパッケージは週間1億回以上ダウンロードされる

summary_ko: |
  v1.14.1과 0.30.4에 악성 의존성 `plain-crypto-js@4.2.1`이 심어졌고, postinstall로 크로스 플랫폼 RAT **WAVESHAPER.V2**를 설치한다(플랫폼별 PowerShell/C++/Python 페이로드). 북한 연계 **UNC1069**으로 귀속되었다. **공격 중 유지관리자를 소셜 엔지니어링하는 데 딥페이크가 사용되었다**. 악성 버전은 약 3시간 동안 유통되었고, 이 패키지는 주당 1억 회 이상 다운로드된다

summary_de: |
  v1.14.1 und 0.30.4 wurden mit einer bösartigen Abhängigkeit `plain-crypto-js@4.2.1` versehen, die per postinstall den plattformübergreifenden RAT **WAVESHAPER.V2** ablegt (getrennte Plattform-Nutzlasten in PowerShell/C++/Python). Zuschreibung an die mit Nordkorea verbundene Gruppe **UNC1069**. **Während des Angriffs wurden Deepfakes eingesetzt, um den Maintainer per Social Engineering zu manipulieren**. Die bösartigen Versionen waren etwa 3 Stunden lang online; das Paket verzeichnet 100M+ wöchentliche Downloads

summary_fr: |
  Les versions 1.14.1 et 0.30.4 ont été ensemencées avec une dépendance malveillante `plain-crypto-js@4.2.1` qui dépose le RAT multiplateforme **WAVESHAPER.V2** via postinstall (charges séparées par plateforme en PowerShell/C++/Python). Attribution au groupe lié à la Corée du Nord **UNC1069**. **Des deepfakes ont servi à manipuler le mainteneur par ingénierie sociale pendant l'attaque**. Les versions malveillantes sont restées en ligne environ 3 heures ; le paquet est téléchargé plus de 100 millions de fois par semaine

summary_es: |
  Las versiones v1.14.1 y 0.30.4 fueron sembradas con una dependencia maliciosa `plain-crypto-js@4.2.1` que instala el RAT multiplataforma **WAVESHAPER.V2** mediante postinstall (cargas separadas por plataforma en PowerShell/C++/Python). Atribuido a **UNC1069**, vinculado a Corea del Norte. **Se usaron deepfakes para hacer ingeniería social con el mantenedor durante el ataque**. Las versiones maliciosas estuvieron activas unas 3 horas; el paquete recibe más de 100M de descargas semanales

sources:
  - url: https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package/?hl=en
    label: Google Cloud
  - url: https://www.elastic.co/security-labs/axios-one-rat-to-rule-them-all
    label: Elastic
  - url: https://github.com/axios/axios/issues/10636
    label: "axios#10636"

disputed: false
landmark: true
scan_month: 2026-03
scan_ref: "SCAN.md §6 2026-03"
---

# Axios npm package compromised

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## Summary

v1.14.1 and 0.30.4 were seeded with a malicious dependency `plain-crypto-js@4.2.1` that drops the cross-platform RAT **WAVESHAPER.V2** via postinstall (separate platform payloads in PowerShell/C++/Python). Attribution to North Korea-linked **UNC1069**. **Deepfakes were used to social-engineer the maintainer during the attack**. The malicious versions were live for about 3 hours; the package gets 100M+ weekly downloads

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
| 1 | Google Cloud | <https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package/?hl=en> |
| 2 | Elastic | <https://www.elastic.co/security-labs/axios-one-rat-to-rule-them-all> |
| 3 | axios#10636 | <https://github.com/axios/axios/issues/10636> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-03-30` (raw: 2026-03-30, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-03-30-axios-npm-compromised` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-03-01` [Hades: a sustained campaign turning AI coding assistants into the attack surface](2026-03-01-hades-campaign-ai-coding-assistants.md)<br>  <sub>Hades: a sustained campaign turning AI coding assistants into the attack surface</sub>
- `2026-03-24` [Backdoored LiteLLM release](2026-03-24-litellm-backdoored-release.md)<br>  <sub>Backdoored LiteLLM release</sub>
- `2026-03-02` [Sustained supply-chain compromise across the Trivy ecosystem](2026-03-02-trivy-sheng-tai-chi-xu.md)<br>  <sub>Sustained supply-chain compromise across the Trivy ecosystem</sub>
- `2026-02-09` [Clinejection](../2026-02/2026-02-09-clinejection.md)<br>  <sub>Clinejection</sub>

---

[← 2026-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-03/2026-03-30-axios-npm-compromised.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
