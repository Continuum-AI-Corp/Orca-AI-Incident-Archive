---
id: 2026-02-05-gpt-codex-high
title: "GPT-5.3-Codex rated \"High\" for cyber capability"
title_zh: "GPT-5.3-Codex 被评为网络安全 \"High\""
title_ja: "GPT-5.3-Codexがサイバー能力で「High」評価"
title_ko: "GPT-5.3-Codex, 사이버 능력 \"높음\" 등급"
title_de: "GPT-5.3-Codex mit „High“ für Cyber-Fähigkeiten bewertet"
title_fr: "GPT-5.3-Codex classé « High » pour la capacité cyber"
title_es: "GPT-5.3-Codex recibe la calificación \"High\" en capacidad ciber"
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
  The **first** agentic coding model rated High on the cybersecurity dimension of the Preparedness Framework; shipped alongside a **Trusted Access for Cyber (TAC)** access program, sandboxed execution and safety-reasoner session monitoring


summary_zh: |
  **首个**在 Preparedness Framework 网络安全维度达到 High 的 agentic 编码模型；配套推出 **Trusted Access for Cyber (TAC)** 准入计划、沙箱执行、安全推理器会话监控

summary_ja: |
  Preparedness Frameworkのサイバーセキュリティ次元でHighと評価された**初の**エージェント型コーディングモデル。**Trusted Access for Cyber（TAC）**アクセスプログラム、サンドボックス実行、セーフティリーズナーのセッション監視と同時に提供された

summary_ko: |
  Preparedness Framework의 사이버 보안 영역에서 "높음" 등급을 받은 **최초**의 에이전틱 코딩 모델이다. **Trusted Access for Cyber (TAC)** 접근 프로그램, 샌드박스 실행, 안전 추론기 세션 모니터링과 함께 출시되었다

summary_de: |
  Das **erste** agentische Codemodell, das in der Cybersicherheits-Dimension des Preparedness Framework mit High bewertet wurde; ausgeliefert zusammen mit einem Zugangsprogramm **Trusted Access for Cyber (TAC)**, Sandbox-Ausführung und Session-Überwachung durch einen Safety-Reasoner

summary_fr: |
  **Le premier** modèle de code agentique classé High sur la dimension cybersécurité du Preparedness Framework ; livré avec un programme d'accès **Trusted Access for Cyber (TAC)**, une exécution en bac à sable et une surveillance des sessions par un raisonneur de sûreté

summary_es: |
  El **primer** modelo de codificación agéntico calificado como High en la dimensión de ciberseguridad del Preparedness Framework; se lanzó junto con un programa de acceso **Trusted Access for Cyber (TAC)**, ejecución en sandbox y monitoreo de sesiones mediante un razonador de seguridad

sources:
  - url: https://deploymentsafety.openai.com/gpt-5-3-codex/disallowed-content-evaluations
    label: OpenAI Deployment Safety

disputed: false
landmark: true
scan_month: 2026-02
scan_ref: "SCAN.md §6 2026-02"
---

# GPT-5.3-Codex rated "High" for cyber capability

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

The **first** agentic coding model rated High on the cybersecurity dimension of the Preparedness Framework; shipped alongside a **Trusted Access for Cyber (TAC)** access program, sandboxed execution and safety-reasoner session monitoring

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
| 1 | OpenAI Deployment Safety | <https://deploymentsafety.openai.com/gpt-5-3-codex/disallowed-content-evaluations> |

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
| Archive ID | `2026-02-05-gpt-codex-high` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-02-05` [Claude Opus 4.6 finds 500+ zero-days in open-source projects](2026-02-05-claude-opus-kai-yuan-xiang.md)<br>  <sub>Claude Opus 4.6 finds 500+ zero-days in open-source projects</sub>
- `2026-02-13` [ChatGPT introduces Lockdown Mode](2026-02-13-chatgpt-lockdown-mode.md)<br>  <sub>ChatGPT introduces Lockdown Mode</sub>
- `2026-02-18` [Anthropic, "Measuring AI agent autonomy in practice"](2026-02-18-anthropic-measuring-agent-autonomy.md)<br>  <sub>Anthropic, "Measuring AI agent autonomy in practice"</sub>
- `2026-02-19` [Microsoft: don't run OpenClaw on ordinary work machines](2026-02-19-openclaw-wei-ruan-pu-tong.md)<br>  <sub>Microsoft: don't run OpenClaw on ordinary work machines</sub>

---

[← 2026-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-02/2026-02-05-gpt-codex-high.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
