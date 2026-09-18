---
id: 2026-06-12-anthropic-mei-guo-zheng-fu
title: "US government issues export controls to Anthropic"
title_zh: "美国政府对 Anthropic 发出出口管制指令"
title_ja: "米政府がAnthropicに輸出管理を発動"
title_ko: "미국 정부, Anthropic에 수출 통제 발동"
title_de: "US-Regierung erlässt Ausfuhrkontrollen gegenüber Anthropic"
title_fr: "Le gouvernement américain impose des contrôles à l'exportation à Anthropic"
title_es: "El gobierno de Estados Unidos emite controles de exportación a Anthropic"
date: 2026-06-12
date_precision: day
date_raw: "2026-06-12"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [US]

summary: |
  The US government issued an export-control directive to Anthropic, restricting access to models of certain capability tiers for some countries and entities — the first time frontier models' cyber capabilities have been treated as a controlled item.


summary_zh: |
  美国政府向 Anthropic 发出出口管制指令，限制特定能力等级的模型对部分国家与实体开放——首次把前沿模型的网络能力当作受控物项处理。

summary_ja: |
  米政府はAnthropicに輸出管理指令を発出し、一部の国とエンティティに対する特定能力層のモデルへのアクセスを制限した——フロンティアモデルのサイバー能力が管理対象品目として扱われたのは初めてである。

summary_ko: |
  미국 정부가 Anthropic에 수출 통제 지시를 내려 일부 국가와 기관의 특정 능력 등급 모델 접근을 제한했다. 프런티어 모델의 사이버 능력이 통제 품목으로 취급된 것은 이번이 처음이다.

summary_de: |
  Die US-Regierung erließ eine Ausfuhrkontrollanweisung an Anthropic, die den Zugang zu Modellen bestimmter Fähigkeitsstufen für einige Länder und Einrichtungen beschränkt — das erste Mal, dass die Cyber-Fähigkeiten von Frontier-Modellen als kontrolliertes Gut behandelt werden.

summary_fr: |
  Le gouvernement américain a émis une directive de contrôle des exportations à l'encontre d'Anthropic, restreignant l'accès à des modèles de certains niveaux de capacité pour certains pays et entités — c'est la première fois que les capacités cyber de modèles de frontière sont traitées comme un bien contrôlé.

summary_es: |
  El gobierno de Estados Unidos emitió una directiva de control de exportaciones a Anthropic, restringiendo el acceso a modelos de ciertos niveles de capacidad para algunos países y entidades — la primera vez que las capacidades ciber de modelos de frontera se tratan como un artículo controlado.

sources:
  - url: https://www.anthropic.com/news/fable-mythos-access
    label: Anthropic statement
  - url: https://freefable.org/
    label: freefable.org open letter
  - url: https://www.anthropic.com/news/redeploying-fable-5
    label: Anthropic restoration notice

disputed: false
landmark: true
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# US government issues export controls to Anthropic

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

The US government issued an export-control directive to Anthropic, restricting access to models of certain capability tiers for some countries and entities — the first time frontier models' cyber capabilities have been treated as a controlled item.

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

## Details

The archive's **only case of "regulation directly cutting off the supply of a commercial AI model"**:

1. Anthropic released Fable 5 (GA) on 06-09 together with Mythos 5 (limited to Glasswing partners)
2. **Amazon researchers reported a way to bypass Fable 5's safeguards**: they induced it to locate several software vulnerabilities, one of which produced exploitability-verification code
3. The US government issued a directive under national-security authority to **stop access for all foreign nationals**, including Anthropic's own foreign employees
4. Because it could not verify nationality in real time, Anthropic **took both models offline for everyone worldwide**
5. Anthropic pushed back publicly: **weaker models such as Opus 4.8, GPT-5.5 and Kimi K2.7 could also find the same vulnerabilities**, and every model tested could generate equivalent exploit code, so the technique **did not expose a capability unique to Mythos**; it also argued that applying the same standard industry-wide would effectively halt new model releases. Working with the government, it trained a classifier that blocks the technique **more than 99%** of the time
6. Operators and technical staff in the US and allied countries signed an open letter (to the Commerce Secretary and the National Cyber Director) saying the move **takes the best models away from defenders**
7. **06-26** limited supply of Mythos 5 approved for some US organizations → **06-30** export controls lifted → **07-01** Fable 5 restored globally

> **Why it matters**: it put "AI cyber capabilities are a dual-use controlled item" on the table for the first time, and the conclusion is — **the control is technically unenforceable (nationality cannot be verified in real time) and in effect harms defenders**.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Anthropic statement | <https://www.anthropic.com/news/fable-mythos-access> |
| 2 | freefable.org open letter | <https://freefable.org/> |
| 3 | Anthropic restoration notice | <https://www.anthropic.com/news/redeploying-fable-5> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-12` (raw: 2026-06-12, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [United States](../../regions/us.md) |
| Archive ID | `2026-06-12-anthropic-mei-guo-zheng-fu` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-06-09` [Anthropic Claude Fable 5 GA, Mythos 5 limited release](2026-06-09-anthropic-claude-fable-ga.md)<br>  <sub>Anthropic Claude Fable 5 GA, Mythos 5 limited release</sub>
- `2026-06-11` [CISA BOD 26-04](2026-06-11-cisa-bod.md)<br>  <sub>CISA BOD 26-04</sub>
- `2026-06-12` [Google sues the China-linked "Outsider Enterprise" smishing network](2026-06-12-google-outsider-enterprise.md)<br>  <sub>Google sues the China-linked "Outsider Enterprise" smishing network</sub>
- `2026-06-23` [Five Eyes joint statement to boards and executives](2026-06-23-five-eyes-zhi-qi-ye.md)<br>  <sub>Five Eyes joint statement to boards and executives</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-12-anthropic-mei-guo-zheng-fu.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
