---
id: 2026-02-13-chatgpt-lockdown-mode
title: "ChatGPT introduces Lockdown Mode"
title_zh: "ChatGPT 推出 Lockdown Mode"
title_ja: "ChatGPTがLockdown Modeを導入"
title_ko: "ChatGPT, 잠금 모드(Lockdown Mode) 도입"
title_de: "ChatGPT führt den Lockdown Mode ein"
title_fr: "ChatGPT introduit le Lockdown Mode"
title_es: "ChatGPT incorpora el modo Lockdown"
date: 2026-02-13
date_precision: day
date_raw: "2026-02-13"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Limits outbound network requests and turns off Deep Research / agent mode; high-risk features are also given a uniform "elevated risk" label


summary_zh: |
  限制外发网络请求，关闭 Deep Research / agent 模式；同时给高风险功能统一贴「elevated risk」标签

summary_ja: |
  外向きのネットワークリクエストを制限し、Deep Research／エージェントモードを無効化。高リスク機能には一律で「elevated risk」ラベルも付与される

summary_ko: |
  외부 네트워크 요청을 제한하고 Deep Research / 에이전트 모드를 끈다. 고위험 기능에는 일괄적으로 "위험 상승" 표시가 붙는다

summary_de: |
  Begrenzt ausgehende Netzwerkanfragen und schaltet Deep Research / den Agentenmodus ab; risikoreiche Funktionen erhalten zudem ein einheitliches Label „erhöhtes Risiko“

summary_fr: |
  Limite les requêtes réseau sortantes et désactive Deep Research / le mode agent ; les fonctionnalités à haut risque reçoivent aussi une étiquette uniforme de « risque élevé »

summary_es: |
  Limita las solicitudes de red salientes y desactiva Deep Research / el modo agente; las funciones de alto riesgo también reciben una etiqueta uniforme de "riesgo elevado"

sources:
  - url: https://openai.com/ja-JP/index/introducing-lockdown-mode-and-elevated-risk-labels-in-chatgpt/
    label: OpenAI

disputed: false
landmark: false
scan_month: 2026-02
scan_ref: "SCAN.md §6 2026-02"
---

# ChatGPT introduces Lockdown Mode

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Limits outbound network requests and turns off Deep Research / agent mode; high-risk features are also given a uniform "elevated risk" label

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
| 1 | OpenAI | <https://openai.com/ja-JP/index/introducing-lockdown-mode-and-elevated-risk-labels-in-chatgpt/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-02-13` (raw: 2026-02-13, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-02-13-chatgpt-lockdown-mode` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-02-05` [GPT-5.3-Codex rated "High" for cyber capability](2026-02-05-gpt-codex-high.md)<br>  <sub>GPT-5.3-Codex rated "High" for cyber capability</sub>
- `2026-02-05` [Claude Opus 4.6 finds 500+ zero-days in open-source projects](2026-02-05-claude-opus-kai-yuan-xiang.md)<br>  <sub>Claude Opus 4.6 finds 500+ zero-days in open-source projects</sub>
- `2026-02-18` [Anthropic, "Measuring AI agent autonomy in practice"](2026-02-18-anthropic-measuring-agent-autonomy.md)<br>  <sub>Anthropic, "Measuring AI agent autonomy in practice"</sub>
- `2026-02-19` [Microsoft: don't run OpenClaw on ordinary work machines](2026-02-19-openclaw-wei-ruan-pu-tong.md)<br>  <sub>Microsoft: don't run OpenClaw on ordinary work machines</sub>

---

[← 2026-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-02/2026-02-13-chatgpt-lockdown-mode.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
