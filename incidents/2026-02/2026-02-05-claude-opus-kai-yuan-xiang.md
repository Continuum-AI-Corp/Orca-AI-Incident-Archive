---
id: 2026-02-05-claude-opus-kai-yuan-xiang
title: "Claude Opus 4.6 finds 500+ zero-days in open-source projects"
title_zh: "Claude Opus 4.6 在开源项目中发现 500+ 零日"
title_ja: "Claude Opus 4.6がオープンソースプロジェクトで500以上のゼロデイを発見"
title_ko: "Claude Opus 4.6, 오픈소스 프로젝트에서 제로데이 500건 이상 발견"
title_de: "Claude Opus 4.6 findet 500+ Zero-Days in Open-Source-Projekten"
title_fr: "Claude Opus 4.6 trouve plus de 500 zero-days dans des projets open source"
title_es: "Claude Opus 4.6 encuentra más de 500 zero-days en proyectos de código abierto"
date: 2026-02-05
date_precision: day
date_raw: "2026-02-05"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  No special scaffolding needed; it analysed git commit history, identified dangerous patterns and worked through complex logic such as GIF LZW compression. Anthropic also launched a model-based probe that detects misuse in real time


summary_zh: |
  无需特殊脚手架；分析 git 提交历史、识别危险模式、理解 GIF 的 LZW 压缩等复杂逻辑。Anthropic 同时上线基于模型的 probe 实时检测滥用

summary_ja: |
  特別な足場（scaffolding）は不要で、gitのコミット履歴を分析して危険なパターンを特定し、GIFのLZW圧縮のような複雑なロジックも処理した。Anthropicは悪用をリアルタイムに検知するモデルベースのプローブも開始した

summary_ko: |
  특별한 스캐폴딩 없이도 git 커밋 이력을 분석하고 위험한 패턴을 식별했으며 GIF LZW 압축 같은 복잡한 로직까지 파고들었다. Anthropic은 실시간으로 오용을 탐지하는 모델 기반 프로브도 출시했다

summary_de: |
  Kein spezielles Scaffolding nötig; es analysierte die git-Commit-Historie, erkannte gefährliche Muster und arbeitete komplexe Logik wie die GIF-LZW-Kompression durch. Anthropic startete außerdem eine modellbasierte Sonde, die Missbrauch in Echtzeit erkennt

summary_fr: |
  Sans échafaudage particulier ; il a analysé l'historique des commits git, identifié des schémas dangereux et traité une logique complexe comme la compression GIF LZW. Anthropic a aussi lancé une sonde basée sur le modèle qui détecte les usages abusifs en temps réel

summary_es: |
  No se necesitó ningún andamiaje especial; analizó el historial de commits de git, identificó patrones peligrosos y resolvió lógica compleja como la compresión LZW de GIF. Anthropic también lanzó una sonda basada en modelos que detecta el uso indebido en tiempo real

sources:
  - url: https://red.anthropic.com/2026/zero-days/
    label: red.anthropic.com

disputed: false
landmark: false
scan_month: 2026-02
scan_ref: "SCAN.md §6 2026-02"
---

# Claude Opus 4.6 finds 500+ zero-days in open-source projects

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

No special scaffolding needed; it analysed git commit history, identified dangerous patterns and worked through complex logic such as GIF LZW compression. Anthropic also launched a model-based probe that detects misuse in real time

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
| 1 | red.anthropic.com | <https://red.anthropic.com/2026/zero-days/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-02-05` (raw: 2026-02-05, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-02-05-claude-opus-kai-yuan-xiang` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-02-05` [GPT-5.3-Codex rated "High" for cyber capability](2026-02-05-gpt-codex-high.md)<br>  <sub>GPT-5.3-Codex rated "High" for cyber capability</sub>
- `2026-02-13` [ChatGPT introduces Lockdown Mode](2026-02-13-chatgpt-lockdown-mode.md)<br>  <sub>ChatGPT introduces Lockdown Mode</sub>
- `2026-02-18` [Anthropic, "Measuring AI agent autonomy in practice"](2026-02-18-anthropic-measuring-agent-autonomy.md)<br>  <sub>Anthropic, "Measuring AI agent autonomy in practice"</sub>
- `2026-02-19` [Microsoft: don't run OpenClaw on ordinary work machines](2026-02-19-openclaw-wei-ruan-pu-tong.md)<br>  <sub>Microsoft: don't run OpenClaw on ordinary work machines</sub>

---

[← 2026-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-02/2026-02-05-claude-opus-kai-yuan-xiang.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
