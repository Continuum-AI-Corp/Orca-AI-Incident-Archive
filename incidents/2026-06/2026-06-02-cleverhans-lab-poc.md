---
id: 2026-06-02-cleverhans-lab-poc
title: "CleverHans Lab adaptive AI worm PoC"
title_zh: "CleverHans Lab 自适应 AI 蠕虫 PoC"
title_ja: "CleverHans Labの適応型AIワームPoC"
title_ko: "CleverHans Lab 적응형 AI 웜 PoC"
title_de: "CleverHans Lab: PoC eines adaptiven KI-Wurms"
title_fr: "PoC de ver IA adaptatif du CleverHans Lab"
title_es: "PoC de gusano de IA adaptativo de CleverHans Lab"
date: 2026-06-02
date_precision: day
date_raw: "2026-06-02"

kind: research
type: [WEAPON]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Uses **locally hosted open-weight models** to adjust attack strategy in real time, parasitizing the victim's compute so the attack cost approaches zero, and bypassing centralized vendor safety filters entirely


summary_zh: |
  用**本地开源权重模型**实时调整攻击策略，寄生受害者算力使攻击成本趋近于零，且完全绕开中心化厂商的安全过滤

summary_ja: |
  **ローカルでホストされるオープンウェイトモデル**を使い、攻撃戦略をリアルタイムに調整。被害者の計算資源に寄生することで攻撃コストをほぼゼロに近づけ、中央集権的なベンダーの安全フィルターを完全に回避する

summary_ko: |
  **로컬에서 호스팅되는 오픈 웨이트 모델**을 사용해 공격 전략을 실시간으로 조정하고, 피해자의 연산을 기생해 공격 비용을 거의 0에 가깝게 만들며, 중앙집중식 벤더 안전 필터를 완전히 우회한다

summary_de: |
  Nutzt **lokal gehostete Open-Weight-Modelle**, um die Angriffsstrategie in Echtzeit anzupassen, parasitiert die Rechenleistung des Opfers, sodass die Angriffskosten gegen null gehen, und umgeht zentrale Sicherheitsfilter der Anbieter vollständig

summary_fr: |
  Utilise **des modèles open-weight hébergés localement** pour ajuster en temps réel la stratégie d'attaque, parasite le calcul de la victime pour que le coût de l'attaque tende vers zéro, et contourne entièrement les filtres de sécurité centralisés des fournisseurs

summary_es: |
  Usa **modelos de pesos abiertos alojados localmente** para ajustar la estrategia de ataque en tiempo real, parasitando la capacidad de cómputo de la víctima para que el costo del ataque se acerque a cero, y eludiendo por completo los filtros de seguridad centralizados de los proveedores

sources:
  - url: https://cleverhans.io/worm.html
    label: CleverHans Lab

disputed: false
landmark: false
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# CleverHans Lab adaptive AI worm PoC

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

Uses **locally hosted open-weight models** to adjust attack strategy in real time, parasitizing the victim's compute so the attack cost approaches zero, and bypassing centralized vendor safety filters entirely

## Attack chain

```mermaid
flowchart LR
    E["Attacker + jailbreak script"]:::entry
    S0["LLM orchestrator drives a cluster of sub-agents"]:::step
    I["Target systems compromised<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | CleverHans Lab | <https://cleverhans.io/worm.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-02` (raw: 2026-06-02, precision `day`) |
| Kind | Research demo `research` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-02-cleverhans-lab-poc` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-06-15` [UNC6508 breaches North American research institutions via REDCap](2026-06-15-unc6508-redcap-jing-ru-qin.md)<br>  <sub>UNC6508 breaches North American research institutions via REDCap</sub>
- `2026-06-24` [macOS.Gaslight: malware prompt-injects the AI analyst](2026-06-24-macos-gaslight-e-yi-ruan-jian.md)<br>  <sub>macOS.Gaslight: malware prompt-injects the AI analyst</sub>
- `2026-06-03` [Anthropic, "LLM ATT&CK Navigator"](2026-06-03-anthropic-llm-att-ck.md)<br>  <sub>Anthropic, "LLM ATT&CK Navigator"</sub>
- `2026-06-09` [Anthropic: N-day is really "N-hour"](2026-06-09-anthropic-day-hour.md)<br>  <sub>Anthropic: N-day is really "N-hour"</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-02-cleverhans-lab-poc.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
