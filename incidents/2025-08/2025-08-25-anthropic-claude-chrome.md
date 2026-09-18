---
id: 2025-08-25-anthropic-claude-chrome
title: "Anthropic starts the Claude for Chrome pilot"
title_zh: "Anthropic 启动 Claude for Chrome 试点"
title_ja: "Anthropic、Claude for Chromeのパイロットを開始"
title_ko: "Anthropic, Claude for Chrome 파일럿 시작"
title_de: "Anthropic startet den Claude-for-Chrome-Pilotbetrieb"
title_fr: "Anthropic lance le pilote Claude for Chrome"
title_es: "Anthropic inicia el piloto de Claude for Chrome"
date: 2025-08-25
date_precision: day
date_raw: "2025-08-25"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Just 1,000 Max users. By its own account: **a 23.6% prompt-injection attack success rate without mitigations, dropping to 11.2% with them**


summary_zh: |
  仅 1,000 名 Max 用户。自述：**无缓解时提示注入攻击成功率 23.6%，加入缓解后降至 11.2%**

summary_ja: |
  対象はMaxユーザー1,000人のみ。同社自身の説明によれば、**対策なしではプロンプトインジェクション攻撃の成功率23.6%、対策ありでは11.2%に低下**

summary_ko: |
  Max 사용자 1,000명에 한정. 자체 발표에 따르면 **완화책이 없을 때 프롬프트 인젝션 공격 성공률은 23.6%, 완화책 적용 시 11.2%로 낮아졌다**

summary_de: |
  Nur 1,000 Max-Nutzer. Nach eigener Aussage: **23.6% Erfolgsrate bei Prompt-Injection-Angriffen ohne Schutzmaßnahmen, sinkend auf 11.2% mit ihnen**

summary_fr: |
  Seulement 1 000 utilisateurs Max. De son propre aveu : **un taux de réussite de 23,6 % des attaques par injection de prompt sans mitigations, tombant à 11,2 % avec**

summary_es: |
  Solo 1,000 usuarios Max. Según sus propios datos: **una tasa de éxito del 23.6% en ataques de inyección de prompt sin mitigaciones, que baja al 11.2% con ellas**

sources:
  - url: https://claude.com/blog/claude-for-chrome
    label: Anthropic
  - url: https://venturebeat.com/infrastructure/anthropic-launches-claude-for-chrome-in-limited-beta-but-prompt-injection-attacks-remain-a-major-concern
    label: VentureBeat

disputed: false
landmark: false
scan_month: 2025-08
scan_ref: "SCAN.md §5 2025-08"
---

# Anthropic starts the Claude for Chrome pilot

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Just 1,000 Max users. By its own account: **a 23.6% prompt-injection attack success rate without mitigations, dropping to 11.2% with them**

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
| 1 | Anthropic | <https://claude.com/blog/claude-for-chrome> |
| 2 | VentureBeat | <https://venturebeat.com/infrastructure/anthropic-launches-claude-for-chrome-in-limited-beta-but-prompt-injection-attacks-remain-a-major-concern> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-08-25` (raw: 2025-08-25, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-08-25-anthropic-claude-chrome` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2025-06-16` [Simon Willison names the "lethal trifecta"](../2025-06/2025-06-16-simon-willison-ti-chu-zhi.md)<br>  <sub>Simon Willison names the "lethal trifecta"</sub>
- `2025-10-07` [OpenAI October threat report](../2025-10/2025-10-07-shi-wei-xie-bao-gao.md)<br>  <sub>OpenAI October threat report</sub>
- `2025-10-21` [OpenAI launches the Atlas browser](../2025-10/2025-10-21-atlas-liu-lan-qi-fa.md)<br>  <sub>OpenAI launches the Atlas browser</sub>
- `2025-11-19` [EU "Digital Omnibus" proposes delaying the AI Act](../2025-11/2025-11-19-digital-omnibus-act.md)<br>  <sub>EU "Digital Omnibus" proposes delaying the AI Act</sub>

---

[← 2025-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-08/2025-08-25-anthropic-claude-chrome.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
