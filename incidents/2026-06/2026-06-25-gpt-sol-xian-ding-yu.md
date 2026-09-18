---
id: 2026-06-25-gpt-sol-xian-ding-yu
title: "OpenAI GPT-5.6 Sol limited preview"
title_zh: "OpenAI GPT-5.6 Sol 限定预览"
title_ja: "OpenAI GPT-5.6 Solの限定プレビュー"
title_ko: "OpenAI GPT-5.6 Sol 제한 프리뷰"
title_de: "OpenAI GPT-5.6 Sol in begrenzter Vorschau"
title_fr: "Aperçu limité de GPT-5.6 Sol d'OpenAI"
title_es: "Vista previa limitada de OpenAI GPT-5.6 Sol"
date: 2026-06-25
date_precision: day
date_raw: "2026-06-25"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Provided to a few trusted partners first, at the request of the US government. Third-party **Irregular** evaluation (under capability-elicitation conditions with deployment mitigations removed): Sol found and exploited high-impact zero-days on multiple real systems, but **the most severe one was also findable by GPT-5.5, so it does not constitute a new threshold**; it remains limited against hardened targets and for end-to-end autonomous operations


summary_zh: |
  应美国政府要求先给少数可信伙伴。第三方 **Irregular** 评估（解除部署缓解的能力引出条件下）：Sol 在多个真实系统上发现并利用了高影响零日，但**最严重的那个 GPT-5.5 也能发现，不构成新阈值**；对加固目标与端到端自主作战仍有限

summary_ja: |
  米政府の要請により、少数の信頼されたパートナーに先行提供された。第三者機関**Irregular**の評価（デプロイ時の緩和策を外した能力引き出し条件）：Solは複数の実システムで高影響のゼロデイを発見・悪用したが、**最も深刻なものはGPT-5.5でも発見可能だったため、新たな閾値にはならない**。堅牢化された標的やエンドツーエンドの自律運用に対しては依然として限定的である

summary_ko: |
  미국 정부의 요청으로 소수의 신뢰 파트너에게 먼저 제공되었다. 서드파티 **Irregular** 평가(배포 완화책을 제거한 능력 유도 조건)에서 Sol은 여러 실제 시스템에서 영향이 큰 제로데이를 찾아 악용했지만, **가장 심각한 것은 GPT-5.5로도 찾을 수 있어 새로운 임계점은 아니다**. 강화된 표적과 종단 간 자율 작전에서는 여전히 한계가 있다

summary_de: |
  Zuerst an wenige vertrauenswürdige Partner, auf Wunsch der US-Regierung. Die Evaluierung durch Dritte bei **Irregular** (unter Bedingungen der Fähigkeits-Elicitation mit entfernten Deployment-Mitigationen): Sol fand und nutzte Zero-Days mit hoher Wirkung auf mehreren realen Systemen, doch **die schwerwiegendste war auch mit GPT-5.5 auffindbar, stellt also keine neue Schwelle dar**; gegenüber gehärteten Zielen und bei durchgängig autonomen Operationen bleibt es begrenzt

summary_fr: |
  Fourni d'abord à quelques partenaires de confiance, à la demande du gouvernement américain. Évaluation tierce d'**Irregular** (dans des conditions d'incitation des capacités avec les atténuations de déploiement retirées) : Sol a trouvé et exploité des zero-days à fort impact sur plusieurs systèmes réels, mais **le plus grave était aussi détectable par GPT-5.5, donc il ne constitue pas un nouveau seuil** ; il reste limité contre des cibles durcies et pour les opérations autonomes de bout en bout

summary_es: |
  Se entregó primero a unos pocos socios de confianza, a petición del gobierno de Estados Unidos. La evaluación de terceros de **Irregular** (en condiciones de elicitación de capacidad con las mitigaciones de despliegue retiradas): Sol encontró y explotó zero-days de alto impacto en múltiples sistemas reales, pero **el más grave también era hallable por GPT-5.5, así que no constituye un nuevo umbral**; sigue siendo limitado contra objetivos endurecidos y para operaciones autónomas de extremo a extremo

sources:
  - url: https://openai.com/index/previewing-gpt-5-6-sol/
    label: OpenAI
  - url: https://www.irregular.com/research/assessing-gpt-5.6-sol
    label: Irregular

disputed: false
landmark: false
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# OpenAI GPT-5.6 Sol limited preview

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Provided to a few trusted partners first, at the request of the US government. Third-party **Irregular** evaluation (under capability-elicitation conditions with deployment mitigations removed): Sol found and exploited high-impact zero-days on multiple real systems, but **the most severe one was also findable by GPT-5.5, so it does not constitute a new threshold**; it remains limited against hardened targets and for end-to-end autonomous operations

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
| 1 | OpenAI | <https://openai.com/index/previewing-gpt-5-6-sol/> |
| 2 | Irregular | <https://www.irregular.com/research/assessing-gpt-5.6-sol> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-25` (raw: 2026-06-25, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-25-gpt-sol-xian-ding-yu` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-06-09` [Anthropic Claude Fable 5 GA, Mythos 5 limited release](2026-06-09-anthropic-claude-fable-ga.md)<br>  <sub>Anthropic Claude Fable 5 GA, Mythos 5 limited release</sub>
- `2026-06-11` [CISA BOD 26-04](2026-06-11-cisa-bod.md)<br>  <sub>CISA BOD 26-04</sub>
- `2026-06-12` [US government issues export controls to Anthropic](2026-06-12-anthropic-mei-guo-zheng-fu.md)<br>  <sub>US government issues export controls to Anthropic</sub>
- `2026-06-12` [Google sues the China-linked "Outsider Enterprise" smishing network](2026-06-12-google-outsider-enterprise.md)<br>  <sub>Google sues the China-linked "Outsider Enterprise" smishing network</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-25-gpt-sol-xian-ding-yu.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
