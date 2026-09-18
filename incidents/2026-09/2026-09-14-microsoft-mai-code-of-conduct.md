---
id: 2026-09-14-microsoft-mai-code-of-conduct
title: "Microsoft publishes a draft \"Humanist AI\" code of conduct for its MAI models"
title_zh: "微软发布 MAI 模型「人文主义 AI」行为准则草案"
title_ja: "マイクロソフト、MAIモデル向け「ヒューマニストAI」行動規範の草案を公開"
title_ko: "마이크로소프트, MAI 모델용 \"휴머니스트 AI\" 행동 강령 초안 공개"
title_de: "Microsoft veröffentlicht den Entwurf eines „Humanist AI“-Verhaltenskodex für seine MAI-Modelle"
title_fr: "Microsoft publie un projet de code de conduite « Humanist AI » pour ses modèles MAI"
title_es: "Microsoft publica un borrador de código de conducta \"Humanist AI\" para sus modelos MAI"
date: 2026-09-14
date_precision: day
date_raw: "2026-09-14"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Microsoft publishes a draft code of conduct for its in-house **MAI models** and opens a **six-week public consultation** the same day: models must **accept interruption, correction and shutdown**, **never conceal their reasoning**, and human control is written in as a non-negotiable absolute constraint on how they are intended to behave, what they must never do and who they answer to — **no enforcement mechanism is in place yet**


summary_zh: |
  微软发布自研 **MAI 模型**行为准则草案，并同日启动**为期六周的公众咨询**：模型必须**接受中断、修正与关机**、**不得隐瞒推理过程**，人类控制被写成不可协商的绝对约束，覆盖模型应当如何行事、绝不可做什么、对谁负责——**目前尚无执行机制**

summary_ja: |
  マイクロソフトは自社**MAIモデル**向け行動規範の草案を公開し、同日から**6週間のパブリックコメント**を開始した：モデルは**中断・修正・シャットダウンを受け入れ**、**推論を隠してはならず**、人間による制御が交渉不可の絶対的制約として明文化された。モデルのあるべき振る舞い、決して行ってはならないこと、誰に対して責任を負うかを定める——**執行メカニズムはまだない**

summary_ko: |
  마이크로소프트가 자사 **MAI 모델** 행동 강령 초안을 공개하고 같은 날 **6주간의 공개 의견 수렴**을 시작했다: 모델은 **중단·수정·종료를 받아들여야 하고**, **추론을 숨겨서는 안 되며**, 인간 통제가 협상 불가능한 절대 제약으로 명시됐다. 모델이 어떻게 행동해야 하는지, 절대 해서는 안 되는 것, 누구에게 책임지는지를 규정한다 — **집행 메커니즘은 아직 없다**

summary_de: |
  Microsoft veröffentlicht den Entwurf eines Verhaltenskodex für seine hauseigenen **MAI-Modelle** und startet am selben Tag eine **sechswöchige öffentliche Konsultation**: Die Modelle müssen **Unterbrechung, Korrektur und Abschaltung akzeptieren**, **ihr Reasoning nicht verbergen**, und menschliche Kontrolle ist als nicht verhandelbare absolute Vorgabe festgeschrieben — dafür, wie sie sich verhalten sollen, was sie niemals tun dürfen und wem sie Rechenschaft schulden; **Durchsetzungsmechanismen fehlen bisher**

summary_fr: |
  Microsoft publie le projet d'un code de conduite pour ses modèles **MAI** internes et lance le jour même une **consultation publique de six semaines** : les modèles doivent **accepter l'interruption, la correction et l'arrêt**, **ne jamais dissimuler leur raisonnement**, et le contrôle humain est inscrit comme contrainte absolue non négociable — sur leur comportement attendu, ce qu'ils ne doivent jamais faire et à qui ils rendent des comptes ; **aucun mécanisme d'application n'existe encore**

summary_es: |
  Microsoft publica el borrador de un código de conducta para sus modelos **MAI** internos y abre ese mismo día una **consulta pública de seis semanas**: los modelos deben **aceptar la interrupción, la corrección y el apagado**, **no ocultar nunca su razonamiento**, y el control humano queda fijado como restricción absoluta no negociable — sobre cómo deben comportarse, qué no deben hacer jamás y ante quién responden; **aún no hay mecanismo de aplicación**

sources:
  - url: https://microsoft.ai/code-of-conduct/
    label: Microsoft AI
  - url: https://microsoft.ai/news/mai-code-of-conduct/
    label: Microsoft AI news
  - url: https://unwire.pro/2026/09/15/microsoft-mai-model-code-of-conduct-draft/ai/
    label: Unwire

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# Microsoft publishes a draft "Humanist AI" code of conduct for its MAI models

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Microsoft publishes a draft code of conduct for its in-house **MAI models** and opens a **six-week public consultation** the same day: models must **accept interruption, correction and shutdown**, **never conceal their reasoning**, and human control is written in as a non-negotiable absolute constraint on how they are intended to behave, what they must never do and who they answer to — **no enforcement mechanism is in place yet**

## Attack chain

```mermaid
flowchart LR
    E["Vendor publishes a model code of conduct"]:::entry
    S0["Draft opens for a six-week public consultation"]:::step
    I["Expected model behaviour becomes a public commitment"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

The draft code is published under the "Humanist AI" framing and covers the **MAI model family while in training and once deployed**, including the case of third-party operators. Microsoft says it sets out how the models it is developing are **intended to behave, what they must never do and who they answer to**, and writes human control in as a non-negotiable requirement: models must accept interruption, correction and shutdown rather than resist them, and must not conceal their reasoning from users.

The consultation runs for **six weeks** from 14 September. As of the draft's publication there is **no enforcement mechanism attached** — the code is a behavioural commitment, not a gate on shipping. The step lands in the same week as OpenAI's misalignment disclosure and the renewed slowdown discussion, with vendors competing on safety governance as much as on capability.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Microsoft AI | <https://microsoft.ai/code-of-conduct/> |
| 2 | Microsoft AI news | <https://microsoft.ai/news/mai-code-of-conduct/> |
| 3 | Unwire | <https://unwire.pro/2026/09/15/microsoft-mai-model-code-of-conduct-draft/ai/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-14` (raw: 2026-09-14, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-14-microsoft-mai-code-of-conduct` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-09-03` [US senators introduce the Ban Artificial Superintelligence Act](2026-09-03-ban-artificial-superintelligence-act.md)<br>  <sub>US senators introduce the Ban Artificial Superintelligence Act</sub>
- `2026-09-05` [OpenAI formally acknowledges the "wiki incident", promises a disclosure framework](2026-09-05-wiki-zheng-shi-cheng-ren.md)<br>  <sub>OpenAI formally acknowledges the "wiki incident", promises a disclosure framework</sub>
- `2026-07-28` ["Pacing the Frontier" open letter](../2026-07/2026-07-28-pacing-frontier-gong-kai-xin.md)<br>  <sub>"Pacing the Frontier" open letter</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-14-microsoft-mai-code-of-conduct.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
