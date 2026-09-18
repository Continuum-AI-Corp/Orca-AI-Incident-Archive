---
id: 2026-05-27-anthropic-zero-trust-agents
title: "Anthropic publishes \"Zero Trust for AI agents\""
title_zh: "Anthropic 发布《Zero Trust for AI agents》"
title_ja: "Anthropicが「Zero Trust for AI agents」を公表"
title_ko: "Anthropic, \"Zero Trust for AI agents\" 발표"
title_de: "Anthropic veröffentlicht „Zero Trust for AI agents“"
title_fr: "Anthropic publie « Zero Trust for AI agents »"
title_es: "Anthropic publica \"Zero Trust for AI agents\""
date: 2026-05-27
date_precision: day
date_raw: "2026-05-27"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  A three-level maturity model (Foundation / Enterprise / Advanced); introduces OWASP's **least agency**; recommends encrypted ephemeral tokens, mutual TLS with certificate pinning, container sandboxes, spotlighting input validation and agentic SOAR


summary_zh: |
  三级成熟度模型（Foundation / Enterprise / Advanced）；引入 OWASP 的 **least agency（最小行动权）**；推荐加密临时令牌、带证书固定的双向 TLS、容器沙箱、spotlighting 输入校验、agentic SOAR

summary_ja: |
  3段階の成熟度モデル（Foundation／Enterprise／Advanced）。OWASPの**least agency**を紹介し、暗号化された一時トークン、証明書ピン留め付き相互TLS、コンテナサンドボックス、spotlightingによる入力検証、agentic SOARを推奨する

summary_ko: |
  3단계 성숙도 모델(Foundation / Enterprise / Advanced). OWASP의 **최소 에이전시(least agency)**를 소개하고, 암호화된 임시 토큰, 인증서 고정을 적용한 상호 TLS, 컨테이너 샌드박스, 스포트라이팅 입력 검증, 에이전틱 SOAR를 권장한다

summary_de: |
  Ein dreistufiges Reifegradmodell (Foundation / Enterprise / Advanced); führt OWASPs **Least Agency** ein; empfiehlt verschlüsselte ephemere Token, gegenseitiges TLS mit Zertifikats-Pinning, Container-Sandboxes, Spotlighting-Eingabevalidierung und agentisches SOAR

summary_fr: |
  Un modèle de maturité à trois niveaux (Foundation / Enterprise / Advanced) ; introduit le **least agency** de l'OWASP ; recommande des jetons éphémères chiffrés, du mTLS avec épinglage de certificats, des bacs à sable de conteneurs, la validation d'entrée par spotlighting et un SOAR agentique

summary_es: |
  Un modelo de madurez de tres niveles (Foundation / Enterprise / Advanced); introduce el **least agency** de OWASP; recomienda tokens efímeros cifrados, TLS mutuo con fijación de certificados, sandboxes de contenedores, validación de entradas con spotlighting y SOAR agéntico

sources:
  - url: https://claude.com/blog/zero-trust-for-ai-agents
    label: Anthropic

disputed: false
landmark: false
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# Anthropic publishes "Zero Trust for AI agents"

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

A three-level maturity model (Foundation / Enterprise / Advanced); introduces OWASP's **least agency**; recommends encrypted ephemeral tokens, mutual TLS with certificate pinning, container sandboxes, spotlighting input validation and agentic SOAR

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
| 1 | Anthropic | <https://claude.com/blog/zero-trust-for-ai-agents> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-27` (raw: 2026-05-27, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-27-anthropic-zero-trust-agents` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-05-12` [Brazilian labour court sanctions lawyers over prompt injection](2026-05-12-brazil-labor-court-prompt-injection-sanction.md)<br>  <sub>Brazilian labour court sanctions lawyers over prompt injection</sub>
- `2026-05-04` [Five Eyes: agentic AI is not ready for rapid rollout](2026-05-04-five-eyes-agentic.md)<br>  <sub>Five Eyes: agentic AI is not ready for rapid rollout</sub>
- `2026-05-01` [Pwn2Own Berlin 2026: 47 zero-days as AI floods the entry list](2026-05-01-pwn2own-berlin-ling-can-sai.md)<br>  <sub>Pwn2Own Berlin 2026: 47 zero-days as AI floods the entry list</sub>
- `2026-04-07` [Claude Mythos Preview cyber capability disclosure, Project Glasswing formed](../2026-04/2026-04-07-claude-mythos-preview-project.md)<br>  <sub>Claude Mythos Preview cyber capability disclosure, Project Glasswing formed</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-27-anthropic-zero-trust-agents.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
