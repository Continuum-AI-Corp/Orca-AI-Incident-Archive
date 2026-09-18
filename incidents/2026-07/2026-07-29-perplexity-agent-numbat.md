---
id: 2026-07-29-perplexity-agent-numbat
title: "Perplexity open-sources Numbat for agent behaviour monitoring"
title_zh: "Perplexity 开源 agent 行为监控 Numbat"
title_ja: "Perplexityがエージェント行動監視のNumbatをオープンソース化"
title_ko: "Perplexity, 에이전트 행동 모니터링 도구 Numbat 오픈소스화"
title_de: "Perplexity veröffentlicht Numbat zur Überwachung des Agentenverhaltens als Open Source"
title_fr: "Perplexity ouvre Numbat pour la surveillance du comportement des agents"
title_es: "Perplexity publica como código abierto Numbat para monitorear el comportamiento de agentes"
date: 2026-07-29
date_precision: day
date_raw: "2026-07-29"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  The focus is not prompt injection but **agents taking actions the user did not expect in pursuit of a goal** (deleting files, escalating privileges, exfiltrating keys). Lightweight Go hooks intercept before execution, session records are normalised to NDJSON, telemetry is OpenTelemetry local-first, with **52 built-in CEL detection rules**. Already deployed on thousands of its own machines, but **no detection or false-positive rates published**


summary_zh: |
  主眼不在提示注入，而在**agent 为达成目标而做出用户未预期的行为**（删文件、提权、外发密钥）。Go 语言轻量钩子在执行前拦截、会话记录规范化为 NDJSON、OpenTelemetry 本地优先遥测，内置 **52 条 CEL 检测规则**。已在自家数千台部署，但**未公布检出率/误报率**

summary_ja: |
  焦点はプロンプトインジェクションではなく、**エージェントが目標の追求中にユーザーが予期しない行動を取ること**（ファイル削除、権限昇格、鍵の持ち出し）である。軽量なGoフックが実行前に傍受し、セッション記録はNDJSONに正規化、テレメトリはOpenTelemetryローカルファースト、**52の組み込みCEL検出ルール**を備える。すでに自社の数千台で稼働しているが、**検出率や誤検知率は公表されていない**

summary_ko: |
  초점은 프롬프트 인젝션이 아니라 **에이전트가 목표를 추구하다 사용자가 예상하지 못한 행동을 하는 것**(파일 삭제, 권한 상승, 키 유출)이다. 경량 Go 훅이 실행 전에 가로채고, 세션 기록은 NDJSON으로 정규화되며, 텔레메트리는 OpenTelemetry 로컬 우선 방식이고 **내장 CEL 탐지 규칙 52개**를 갖췄다. 자사 머신 수천 대에 이미 배포했지만 **탐지율이나 오탐률은 공개하지 않았다**

summary_de: |
  Der Fokus liegt nicht auf Prompt-Injection, sondern auf **Agenten, die zur Zielerreichung Aktionen ausführen, die der Nutzer nicht erwartet hat** (Dateien löschen, Rechte erweitern, Schlüssel exfiltrieren). Leichtgewichtige Go-Hooks greifen vor der Ausführung ein, Sitzungsaufzeichnungen werden auf NDJSON normalisiert, Telemetrie ist OpenTelemetry local-first, mit **52 eingebauten CEL-Erkennungsregeln**. Bereits auf Tausenden eigener Rechner im Einsatz, doch **es wurden keine Erkennungs- oder Falsch-Positiv-Raten veröffentlicht**

summary_fr: |
  L'accent n'est pas mis sur l'injection de prompt mais sur **les agents qui prennent des actions inattendues pour l'utilisateur dans la poursuite d'un objectif** (supprimer des fichiers, élever des privilèges, exfiltrer des clés). Des hooks Go légers interceptent avant l'exécution, les enregistrements de session sont normalisés en NDJSON, la télémétrie est OpenTelemetry en local d'abord, avec **52 règles de détection CEL intégrées**. Déjà déployé sur des milliers de ses propres machines, mais **aucun taux de détection ni de faux positifs publié**

summary_es: |
  El foco no es la inyección de prompt sino **los agentes que toman acciones que el usuario no esperaba en pos de un objetivo** (borrar archivos, escalar privilegios, exfiltrar claves). Hooks ligeros en Go interceptan antes de la ejecución, los registros de sesión se normalizan a NDJSON, la telemetría es OpenTelemetry con enfoque local primero, con **52 reglas de detección CEL integradas**. Ya desplegado en miles de sus propias máquinas, pero **sin tasas de detección ni de falsos positivos publicadas**

sources:
  - url: https://research.perplexity.ai/articles/securing-agents-across-perplexity%E2%80%99s-client-endpoints-with-numbat
    label: Perplexity

disputed: false
landmark: false
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# Perplexity open-sources Numbat for agent behaviour monitoring

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

The focus is not prompt injection but **agents taking actions the user did not expect in pursuit of a goal** (deleting files, escalating privileges, exfiltrating keys). Lightweight Go hooks intercept before execution, session records are normalised to NDJSON, telemetry is OpenTelemetry local-first, with **52 built-in CEL detection rules**. Already deployed on thousands of its own machines, but **no detection or false-positive rates published**

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
| 1 | Perplexity | <https://research.perplexity.ai/articles/securing-agents-across-perplexity%E2%80%99s-client-endpoints-with-numbat> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-29` (raw: 2026-07-29, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-07-29-perplexity-agent-numbat` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-07-17` [Anthropic, "A CISO's guide to agentic AI"](2026-07-17-anthropic-ciso-guide-agentic.md)<br>  <sub>Anthropic, "A CISO's guide to agentic AI"</sub>
- `2026-07-23` [US representatives introduce the AI Kill Switch Act](2026-07-23-kill-switch-act.md)<br>  <sub>US representatives introduce the AI Kill Switch Act</sub>
- `2026-07-27` [NVIDIA convenes the Open Secure AI Alliance](2026-07-27-nvidia-open-secure-alliance.md)<br>  <sub>NVIDIA convenes the Open Secure AI Alliance</sub>
- `2026-07-28` ["Pacing the Frontier" open letter](2026-07-28-pacing-frontier-gong-kai-xin.md)<br>  <sub>"Pacing the Frontier" open letter</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-29-perplexity-agent-numbat.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
