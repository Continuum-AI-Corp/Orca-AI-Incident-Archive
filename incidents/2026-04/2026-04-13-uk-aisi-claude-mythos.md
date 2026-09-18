---
id: 2026-04-13-uk-aisi-claude-mythos
title: "UK AISI independently evaluates Claude Mythos Preview"
title_zh: "UK AISI 独立评估 Claude Mythos Preview"
title_ja: "英AISIがClaude Mythos Previewを独自評価"
title_ko: "영국 AISI, Claude Mythos Preview 독립 평가"
title_de: "UK AISI bewertet Claude Mythos Preview unabhängig"
title_fr: "L'AISI britannique évalue indépendamment Claude Mythos Preview"
title_es: "La AISI del Reino Unido evalúa de forma independiente Claude Mythos Preview"
date: 2026-04-13
date_precision: day
date_raw: "2026-04-13"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [UK]

summary: |
  Conclusion: **without defenses in place, Mythos's attack success rate is not particularly high**


summary_zh: |
  结论：**无防御措施情况下 Mythos 的攻击成功率并不算高**

summary_ja: |
  結論：**防御が機能している状態では、Mythosの攻撃成功率は特に高くない**

summary_ko: |
  결론: **방어가 없는 상태에서 Mythos의 공격 성공률은 특별히 높지 않다**

summary_de: |
  Fazit: **Ohne Schutzmaßnahmen ist die Angriffserfolgsrate von Mythos nicht besonders hoch**

summary_fr: |
  Conclusion : **en l'absence de défenses en place, le taux de réussite des attaques de Mythos n'est pas particulièrement élevé**

summary_es: |
  Conclusión: **sin defensas desplegadas, la tasa de éxito de ataque de Mythos no es especialmente alta**

sources:
  - url: https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities
    label: UK AISI

disputed: false
landmark: false
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# UK AISI independently evaluates Claude Mythos Preview

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Conclusion: **without defenses in place, Mythos's attack success rate is not particularly high**

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
| 1 | UK AISI | <https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-04-13` (raw: 2026-04-13, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [United Kingdom](../../regions/uk.md) |
| Archive ID | `2026-04-13-uk-aisi-claude-mythos` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-04-07` [Claude Mythos Preview cyber capability disclosure, Project Glasswing formed](2026-04-07-claude-mythos-preview-project.md)<br>  <sub>Claude Mythos Preview cyber capability disclosure, Project Glasswing formed</sub>
- `2026-04-14` [Vidoc reproduces Mythos's findings with public models](2026-04-14-vidoc-mythos-yong-gong-kai.md)<br>  <sub>Vidoc reproduces Mythos's findings with public models</sub>
- `2026-04-30` [OpenAI launches Advanced Account Security](2026-04-30-tui-chu-gao-ji-zhang.md)<br>  <sub>OpenAI launches Advanced Account Security</sub>
- `2026-05-12` [Brazilian labour court sanctions lawyers over prompt injection](../2026-05/2026-05-12-brazil-labor-court-prompt-injection-sanction.md)<br>  <sub>Brazilian labour court sanctions lawyers over prompt injection</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-13-uk-aisi-claude-mythos.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
