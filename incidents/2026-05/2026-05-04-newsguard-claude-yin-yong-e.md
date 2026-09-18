---
id: 2026-05-04-newsguard-claude-yin-yong-e
title: "NewsGuard: Claude cites Russian and Iranian state propaganda more often"
title_zh: "NewsGuard：Claude 更多引用俄伊国家宣传"
title_ja: "NewsGuard：Claudeがロシア・イランの国家プロパガンダをより多く引用"
title_ko: "NewsGuard: Claude, 러시아·이란 국영 선전 인용 증가"
title_de: "NewsGuard: Claude zitiert russische und iranische Staatspropaganda häufiger"
title_fr: "NewsGuard : Claude cite plus souvent la propagande d'État russe et iranienne"
title_es: "NewsGuard: Claude cita con más frecuencia propaganda estatal rusa e iraní"
date: 2026-05-04
date_precision: day
date_raw: "2026-05-04"

kind: policy
type: [OTHER]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Citations of the "Pravda" network rose markedly; leaked documents from the same period show Russia's **Social Design Agency (SDA)** plans to deploy a German Wikipedia clone with **200,000+ articles** — **data poisoning is now a state-level strategy**


summary_zh: |
  引用 "Pravda" 网络频率显著上升；同期泄露文件显示俄 **社会设计局(SDA)** 计划部署含 **20 万+ 文章**的德语维基百科克隆 —— **数据投毒已是国家级战略**

summary_ja: |
  「Pravda」ネットワークの引用が顕著に増加。同時期の流出文書は、ロシアの**Social Design Agency（SDA）**が**20万記事以上**のドイツ語Wikipediaクローンを展開する計画を示している——**データポイズニングは今や国家レベルの戦略である**

summary_ko: |
  "Pravda" 네트워크 인용이 눈에 띄게 늘었다. 같은 시기 유출 문서에 따르면 러시아의 **Social Design Agency (SDA)**가 **20만 문서 이상**의 독일어 위키백과 복제판을 배치할 계획이다 — **데이터 오염이 이제 국가 수준 전략이다**

summary_de: |
  Die Zitate des „Pravda“-Netzwerks nahmen deutlich zu; geleakte Dokumente aus demselben Zeitraum zeigen, dass Russlands **Social Design Agency (SDA)** den Aufbau eines deutschen Wikipedia-Klons mit **200,000+ Artikeln** plant — **Datenvergiftung ist nun eine Strategie auf Staatsebene**

summary_fr: |
  Les citations du réseau « Pravda » ont nettement augmenté ; des documents fuités de la même période montrent que l'agence russe **Social Design Agency (SDA)** prévoit de déployer un clone de Wikipédia allemand avec **plus de 200 000 articles** — **l'empoisonnement de données est désormais une stratégie étatique**

summary_es: |
  Las citas de la red "Pravda" aumentaron notablemente; documentos filtrados del mismo período muestran que la **Agencia de Diseño Social (SDA)** de Rusia planea desplegar un clon de Wikipedia en alemán con **más de 200,000 artículos** — **el envenenamiento de datos es ahora una estrategia a nivel estatal**

sources:
  - url: https://www.newsguardtech.com/special-reports/anthropic-ai-chatbot-claude-russia-iran-propaganda/
    label: NewsGuard
  - url: https://www.t-online.de/nachrichten/deutschland/innenpolitik/id_101262296/propaganda-offensive-gegen-deutschland-leak-enthuellt-russlands-vorgehen.html
    label: "t-online (SDA leak)"

disputed: false
landmark: false
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# NewsGuard: Claude cites Russian and Iranian state propaganda more often

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

Citations of the "Pravda" network rose markedly; leaked documents from the same period show Russia's **Social Design Agency (SDA)** plans to deploy a German Wikipedia clone with **200,000+ articles** — **data poisoning is now a state-level strategy**

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
| 1 | NewsGuard | <https://www.newsguardtech.com/special-reports/anthropic-ai-chatbot-claude-russia-iran-propaganda/> |
| 2 | t-online (SDA leak) | <https://www.t-online.de/nachrichten/deutschland/innenpolitik/id_101262296/propaganda-offensive-gegen-deutschland-leak-enthuellt-russlands-vorgehen.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-04` (raw: 2026-05-04, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-04-newsguard-claude-yin-yong-e` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-04-newsguard-claude-yin-yong-e.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
