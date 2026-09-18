---
id: 2025-12-22-liu-lan-qi-ti-shi
title: "OpenAI: browser prompt injection \"may never be fully solved\""
title_zh: "OpenAI：浏览器提示注入「可能永远无法彻底解决」"
title_ja: "OpenAI：ブラウザのプロンプトインジェクションは「完全に解決できない可能性がある」"
title_ko: "OpenAI: 브라우저 프롬프트 인젝션은 \"완전히 해결되지 않을 수도\""
title_de: "OpenAI: Prompt-Injection im Browser „lässt sich vielleicht nie vollständig lösen“"
title_fr: "OpenAI : l'injection de prompt dans le navigateur « ne sera peut-être jamais entièrement résolue »"
title_es: "OpenAI: la inyección de prompt en el navegador \"puede que nunca se resuelva del todo\""
date: 2025-12-22
date_precision: day
date_raw: "2025-12-22"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Also announces an RL-driven automated LLM red-team system that continuously hardens Atlas — using **privileged access to the defensive model's reasoning process** for more precise attack simulation


summary_zh: |
  同时公布用 RL 驱动的 LLM 自动红队系统持续加固 Atlas —— 利用**对防御模型推理过程的特权访问**做更精确的攻击模拟

summary_ja: |
  RL駆動の自動LLMレッドチームシステムも発表し、Atlasを継続的に強化する——**防御モデルの推論プロセスへの特権アクセス**を用いて、より精密な攻撃シミュレーションを行う

summary_ko: |
  또한 Atlas를 지속적으로 강화하는 RL 기반 자동 LLM 레드팀 시스템을 발표했다 — **방어 모델의 추론 과정에 대한 특권 접근**을 이용해 더 정밀하게 공격을 시뮬레이션한다

summary_de: |
  Kündigt außerdem ein RL-getriebenes automatisiertes LLM-Red-Team-System an, das Atlas kontinuierlich härter macht — mit **privilegiertem Zugriff auf den Argumentationsprozess des defensiven Modells** für präzisere Angriffssimulation

summary_fr: |
  Annonce aussi un système de red-team LLM automatisé piloté par RL qui durcit en continu Atlas — en utilisant **un accès privilégié au processus de raisonnement du modèle défensif** pour une simulation d'attaque plus précise

summary_es: |
  También anuncia un sistema automatizado de red-team de LLM impulsado por RL que endurece Atlas continuamente — usando **acceso privilegiado al proceso de razonamiento del modelo defensivo** para simular ataques con más precisión

sources:
  - url: https://openai.com/ja-JP/index/hardening-atlas-against-prompt-injection/
    label: OpenAI
  - url: https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/
    label: TechCrunch

disputed: false
landmark: true
scan_month: 2025-12
scan_ref: "SCAN.md §5 2025-12"
---

# OpenAI: browser prompt injection "may never be fully solved"

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Also announces an RL-driven automated LLM red-team system that continuously hardens Atlas — using **privileged access to the defensive model's reasoning process** for more precise attack simulation

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
| 1 | OpenAI | <https://openai.com/ja-JP/index/hardening-atlas-against-prompt-injection/> |
| 2 | TechCrunch | <https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-12-22` (raw: 2025-12-22, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-12-22-liu-lan-qi-ti-shi` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2025-12-09` [OWASP Top 10 for Agentic Applications 2026](2025-12-09-owasp-top-agentic-applications.md)<br>  <sub>OWASP Top 10 for Agentic Applications 2026</sub>
- `2025-12-11` [GPT-5.2 system card updates cyber capability](2025-12-11-gpt-xi-tong-ka-wang.md)<br>  <sub>GPT-5.2 system card updates cyber capability</sub>
- `2025-11-19` [EU "Digital Omnibus" proposes delaying the AI Act](../2025-11/2025-11-19-digital-omnibus-act.md)<br>  <sub>EU "Digital Omnibus" proposes delaying the AI Act</sub>
- `2026-01-30` [Anthropic ships Constitutional Classifiers++](../2026-01/2026-01-30-anthropic-constitutional-classifiers.md)<br>  <sub>Anthropic ships Constitutional Classifiers++</sub>

---

[← 2025-12 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-12/2025-12-22-liu-lan-qi-ti-shi.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
