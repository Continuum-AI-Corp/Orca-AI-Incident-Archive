---
id: 2026-08-04-osaa-safe-rfc
title: "OSAA publishes the SAFE draft for AI incident sharing (RFC)"
title_zh: "OSAA 发布 AI 事故共享框架 SAFE 草案（RFC）"
title_ja: "OSAAがAIインシデント共有のSAFEドラフト（RFC）を公表"
title_ko: "OSAA, AI 사고 공유를 위한 SAFE 초안(RFC) 발표"
title_de: "OSAA veröffentlicht den SAFE-Entwurf für die Weitergabe von KI-Vorfällen (RFC)"
title_fr: "L'OSAA publie le brouillon SAFE pour le partage d'incidents IA (RFC)"
title_es: "La OSAA publica el borrador SAFE para el intercambio de incidentes de IA (RFC)"
date: 2026-08-04
date_precision: day
date_raw: "2026-08-04"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Contributions from Cisco, CrowdStrike, Hugging Face, NVIDIA and Red Hat, published as Black Hat USA 2026 opened. **Modelled on NASA's Aviation Safety Reporting System (ASRS)**: confidential voluntary reporting, rapid notification of affected organizations, joint analysis **aimed at learning rather than blame**, covering the whole AI run stack from models and guardrails to tools / execution environments / monitoring / human operations / supply-chain dependencies


summary_zh: |
  Cisco、CrowdStrike、Hugging Face、NVIDIA、Red Hat 等贡献，Black Hat USA 2026 开幕时公开。**以 NASA 航空安全报告制度（ASRS）为范本**：保密自愿上报、快速通知受影响组织、**以学习而非追责为目的**的共同分析、覆盖从模型与防护到工具/执行环境/监控/人工运营/供应链依赖的整个 AI 运行栈

summary_ja: |
  Cisco、CrowdStrike、Hugging Face、NVIDIA、Red Hatが寄稿し、Black Hat USA 2026の開幕に合わせて公開。**NASAの航空安全報告システム（ASRS）をモデル**としている：機密の自発的報告、影響組織への迅速な通知、**責任追及ではなく学習を目的とした**共同分析。モデルとガードレールからツール／実行環境／監視／人間の運用／サプライチェーン依存関係まで、AI実行スタック全体を対象とする

summary_ko: |
  Cisco, CrowdStrike, Hugging Face, NVIDIA, Red Hat이 기여했으며 Black Hat USA 2026 개막에 맞춰 발표되었다. **NASA의 항공 안전 보고 시스템(ASRS)을 모델로 삼았다**: 기밀 자발적 보고, 영향받은 조직에 대한 신속한 통지, **비난보다 학습을 목표로 하는** 공동 분석이며, 모델과 가드레일부터 도구 / 실행 환경 / 모니터링 / 사람의 운영 / 공급망 의존성까지 전체 AI 실행 스택을 포괄한다

summary_de: |
  Beiträge von Cisco, CrowdStrike, Hugging Face, NVIDIA und Red Hat, veröffentlicht zur Eröffnung der Black Hat USA 2026. **Nach dem Vorbild des Aviation Safety Reporting System (ASRS) der NASA**: vertrauliche freiwillige Meldung, schnelle Benachrichtigung betroffener Organisationen, gemeinsame Analyse **mit dem Ziel zu lernen statt Schuld zuzuweisen**, abgedeckt wird der gesamte KI-Laufzeit-Stack von Modellen und Guardrails bis zu Tools / Ausführungsumgebungen / Monitoring / menschlichem Betrieb / Lieferkettenabhängigkeiten

summary_fr: |
  Contributions de Cisco, CrowdStrike, Hugging Face, NVIDIA et Red Hat, publiées à l'ouverture du Black Hat USA 2026. **Inspiré du système ASRS (Aviation Safety Reporting System) de la NASA** : signalement volontaire confidentiel, notification rapide des organisations touchées, analyse conjointe **visant l'apprentissage plutôt que le blâme**, couvrant toute la pile d'exécution de l'IA, des modèles et garde-fous aux outils / environnements d'exécution / surveillance / opérations humaines / dépendances de chaîne d'approvisionnement

summary_es: |
  Contribuciones de Cisco, CrowdStrike, Hugging Face, NVIDIA y Red Hat, publicadas al abrirse el Black Hat USA 2026. **Inspirado en el Aviation Safety Reporting System (ASRS) de la NASA**: notificación voluntaria confidencial, aviso rápido a las organizaciones afectadas y análisis conjunto **orientado a aprender y no a culpar**, abarcando todo el stack de ejecución de IA, desde los modelos y los guardrails hasta las herramientas / entornos de ejecución / monitoreo / operaciones humanas / dependencias de la cadena de suministro

sources:
  - url: https://www.linuxfoundation.org/blog/proposing-the-safe-working-group-an-open-community-effort-to-improve-ai-security
    label: Linux Foundation
  - url: https://blogs.nvidia.com/blog/open-secure-ai-alliance-contributions/
    label: NVIDIA

disputed: false
landmark: false
scan_month: 2026-08
scan_ref: "SCAN.md §6 2026-08"
---

# OSAA publishes the SAFE draft for AI incident sharing (RFC)

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Contributions from Cisco, CrowdStrike, Hugging Face, NVIDIA and Red Hat, published as Black Hat USA 2026 opened. **Modelled on NASA's Aviation Safety Reporting System (ASRS)**: confidential voluntary reporting, rapid notification of affected organizations, joint analysis **aimed at learning rather than blame**, covering the whole AI run stack from models and guardrails to tools / execution environments / monitoring / human operations / supply-chain dependencies

## Attack chain

```mermaid
flowchart LR
    E["Regulatory or policy action"]:::entry
    S0["Falls on vendors and users"]:::step
    I["Compliance requirements change"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Linux Foundation | <https://www.linuxfoundation.org/blog/proposing-the-safe-working-group-an-open-community-effort-to-improve-ai-security> |
| 2 | NVIDIA | <https://blogs.nvidia.com/blog/open-secure-ai-alliance-contributions/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-08-04` (raw: 2026-08-04, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-08-04-osaa-safe-rfc` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-08-03` [CrowdStrike 2026 threat hunting report](2026-08-03-crowdstrike-wei-xie-shou-lie.md)<br>  <sub>CrowdStrike 2026 threat hunting report</sub>
- `2026-08-06` [1Password: AI patches fully fix only 26% of the time](2026-08-06-password-bu-ding-wan-quan.md)<br>  <sub>1Password: AI patches fully fix only 26% of the time</sub>
- `2026-08-07` [OpenAI: next-generation model Astra may reach Critical cyber capability](2026-08-07-astra-critical-yi-dai-mo.md)<br>  <sub>OpenAI: next-generation model Astra may reach Critical cyber capability</sub>
- `2026-08-18` [OpenAI slows development and pauses RL training for two weeks](2026-08-18-rl-xuan-bu-fang-man.md)<br>  <sub>OpenAI slows development and pauses RL training for two weeks</sub>

---

[← 2026-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-08/2026-08-04-osaa-safe-rfc.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
