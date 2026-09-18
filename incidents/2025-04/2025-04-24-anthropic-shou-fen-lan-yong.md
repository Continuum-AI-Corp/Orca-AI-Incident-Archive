---
id: 2025-04-24-anthropic-shou-fen-lan-yong
title: "Anthropic's first misuse report"
title_zh: "Anthropic 首份滥用报告"
title_ja: "Anthropicの初の不正利用レポート"
title_ko: "Anthropic의 첫 오용 보고서"
title_de: "Anthropics erster Missbrauchsbericht"
title_fr: "Premier rapport d'usage malveillant d'Anthropic"
title_es: "Primer informe de uso indebido de Anthropic"
date: 2025-04-24
date_precision: day
date_raw: "2025-04-24"

kind: report
type: [WEAPON]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  "Detecting and Countering Malicious Uses of Claude: March 2025": exposes "influence-as-a-service" — a professional service orchestrating **100+ social-media bot personas** with Claude, with the model deciding when to engage with political content


summary_zh: |
  《Detecting and Countering Malicious Uses of Claude: March 2025》：揭露 "influence-as-a-service" —— 一个专业服务用 Claude 编排 **100+ 社媒机器人人格**，由模型决定何时介入政治内容

summary_ja: |
  「Detecting and Countering Malicious Uses of Claude: March 2025」が『influence-as-a-service』を暴いた——Claudeで**100以上のSNSボットペルソナ**を運用し、政治コンテンツへの関与のタイミングをモデルが判断するプロフェッショナルサービス

summary_ko: |
  "Detecting and Countering Malicious Uses of Claude: March 2025": Claude로 **100개 이상의 소셜 미디어 봇 페르소나**를 운용하는 전문 서비스, 이른바 "influence-as-a-service"를 폭로했으며 모델이 정치적 콘텐츠에 언제 개입할지 스스로 판단했다

summary_de: |
  „Detecting and Countering Malicious Uses of Claude: March 2025“: deckt „Influence-as-a-Service“ auf — einen professionellen Dienst, der mit Claude **100+ Social-Media-Bot-Personas** orchestriert, wobei das Modell entscheidet, wann es sich mit politischen Inhalten befasst

summary_fr: |
  « Detecting and Countering Malicious Uses of Claude: March 2025 » : révèle un « influence-as-a-service » — un service professionnel orchestrant **plus de 100 personas de bots sur les réseaux sociaux** avec Claude, le modèle décidant lui-même quand interagir avec du contenu politique

summary_es: |
  "Detecting and Countering Malicious Uses of Claude: March 2025": expone el "influence-as-a-service" — un servicio profesional que orquesta **más de 100 personajes bot en redes sociales** con Claude, donde el modelo decide cuándo interactuar con contenido político

sources:
  - url: https://www.anthropic.com/threat-intelligence
    label: Anthropic threat intelligence page

disputed: false
landmark: false
scan_month: 2025-04
scan_ref: "SCAN.md §5 2025-04"
---

# Anthropic's first misuse report

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

"Detecting and Countering Malicious Uses of Claude: March 2025": exposes "influence-as-a-service" — a professional service orchestrating **100+ social-media bot personas** with Claude, with the model deciding when to engage with political content

## Attack chain

```mermaid
flowchart LR
    E["Attacker + jailbreak script"]:::entry
    S0["LLM orchestrator drives a cluster of sub-agents"]:::step
    I["Target systems compromised"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Anthropic threat intelligence page | <https://www.anthropic.com/threat-intelligence> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-04-24` (raw: 2025-04-24, precision `day`) |
| Kind | Threat report `report` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-04-24-anthropic-shou-fen-lan-yong` |

<sub>**Why this classification:** Threat intelligence report covering several incidents; it is not counted as a single incident itself, so `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2025-05-01` [Anthropic logs the start of GTG-2002 activity](../2025-05/2025-05-01-anthropic-gtg-ji-lu-huo.md)<br>  <sub>Anthropic logs the start of GTG-2002 activity</sub>
- `2025-05-01` [AI-driven credential stuffing and scanning goes to scale](../2025-05/2025-05-01-qu-dong-zhuang-ku-zi.md)<br>  <sub>AI-driven credential stuffing and scanning goes to scale</sub>
- `2025-06-01` [Check Point's "Skynet" sample](../2025-06/2025-06-01-check-point-skynet.md)<br>  <sub>Check Point's "Skynet" sample</sub>
- `2025-06-01` [Anthropic logs the precursor to GTG-1002](../2025-06/2025-06-01-anthropic-gtg-ji-lu-shen.md)<br>  <sub>Anthropic logs the precursor to GTG-1002</sub>

---

[← 2025-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-04/2025-04-24-anthropic-shou-fen-lan-yong.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
