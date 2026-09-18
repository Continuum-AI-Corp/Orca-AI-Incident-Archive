---
id: 2026-02-18-anthropic-measuring-agent-autonomy
title: "Anthropic, \"Measuring AI agent autonomy in practice\""
title_zh: "Anthropic《Measuring AI agent autonomy in practice》"
title_ja: "Anthropic「Measuring AI agent autonomy in practice」"
title_ko: "Anthropic, \"Measuring AI agent autonomy in practice\""
title_de: "Anthropic: „Measuring AI agent autonomy in practice“"
title_fr: "Anthropic : « Measuring AI agent autonomy in practice »"
title_es: "Anthropic, \"Measuring AI agent autonomy in practice\""
date: 2026-02-18
date_precision: day
date_raw: "2026-02-18"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  An analysis of millions of human-agent interactions: models' latent capability is above their actual level of use; the more skilled the user, the more they tend to raise the auto-approval rate; on complex tasks Claude Code **asks for confirmation on its own initiative**, suggesting that agent self-supervision may be an important safety measure


summary_zh: |
  分析数百万次人-agent 交互：模型潜在能力高于实际使用水平；用户越熟练越倾向提高自动批准率；Claude Code 在复杂任务中会**自发请求确认**，提示 agent 自我监督可能是重要安全措施

summary_ja: |
  数百万件の人間とエージェントの相互作用の分析：モデルの潜在能力は実際の使用水準を上回っている。ユーザーの熟練度が高いほど自動承認率を上げる傾向があり、複雑なタスクではClaude Codeが**自発的に確認を求める**——エージェントの自己監督が重要な安全策になり得ることを示唆する

summary_ko: |
  수백만 건의 인간-에이전트 상호작용 분석: 모델의 잠재 능력은 실제 사용 수준보다 높고, 사용자가 숙련될수록 자동 승인 비율을 높이는 경향이 있으며, 복잡한 작업에서 Claude Code가 **스스로 확인을 요청**하는 것으로 보아 에이전트의 자기 감독이 중요한 안전 조치일 수 있다

summary_de: |
  Eine Analyse von Millionen Mensch-Agent-Interaktionen: Die latente Fähigkeit der Modelle liegt über ihrem tatsächlichen Nutzungsniveau; je versierter der Nutzer, desto eher erhöht er die Auto-Genehmigungsrate; bei komplexen Aufgaben **bittet Claude Code von sich aus um Bestätigung**, was darauf hindeutet, dass agentische Selbstüberwachung eine wichtige Schutzmaßnahme sein kann

summary_fr: |
  Une analyse de millions d'interactions humain-agent : la capacité latente des modèles dépasse leur niveau d'usage réel ; plus l'utilisateur est compétent, plus il tend à augmenter le taux d'auto-approbation ; sur les tâches complexes, Claude Code **demande confirmation de sa propre initiative**, ce qui suggère que l'auto-surveillance de l'agent peut être une mesure de sûreté importante

summary_es: |
  Un análisis de millones de interacciones humano-agente: la capacidad latente de los modelos está por encima de su nivel real de uso; cuanto más hábil es el usuario, más tiende a elevar la tasa de aprobación automática; en tareas complejas Claude Code **pide confirmación por iniciativa propia**, lo que sugiere que la autosupervisión del agente puede ser una medida de seguridad importante

sources:
  - url: https://www.anthropic.com/research/measuring-agent-autonomy
    label: Anthropic

disputed: false
landmark: false
scan_month: 2026-02
scan_ref: "SCAN.md §6 2026-02"
---

# Anthropic, "Measuring AI agent autonomy in practice"

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

An analysis of millions of human-agent interactions: models' latent capability is above their actual level of use; the more skilled the user, the more they tend to raise the auto-approval rate; on complex tasks Claude Code **asks for confirmation on its own initiative**, suggesting that agent self-supervision may be an important safety measure

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
| 1 | Anthropic | <https://www.anthropic.com/research/measuring-agent-autonomy> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-02-18` (raw: 2026-02-18, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-02-18-anthropic-measuring-agent-autonomy` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-02-05` [GPT-5.3-Codex rated "High" for cyber capability](2026-02-05-gpt-codex-high.md)<br>  <sub>GPT-5.3-Codex rated "High" for cyber capability</sub>
- `2026-02-05` [Claude Opus 4.6 finds 500+ zero-days in open-source projects](2026-02-05-claude-opus-kai-yuan-xiang.md)<br>  <sub>Claude Opus 4.6 finds 500+ zero-days in open-source projects</sub>
- `2026-02-13` [ChatGPT introduces Lockdown Mode](2026-02-13-chatgpt-lockdown-mode.md)<br>  <sub>ChatGPT introduces Lockdown Mode</sub>
- `2026-02-19` [Microsoft: don't run OpenClaw on ordinary work machines](2026-02-19-openclaw-wei-ruan-pu-tong.md)<br>  <sub>Microsoft: don't run OpenClaw on ordinary work machines</sub>

---

[← 2026-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-02/2026-02-18-anthropic-measuring-agent-autonomy.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
