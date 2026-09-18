---
id: 2026-02-01-naver-kakao-karrot-openclaw
title: "Naver, Kakao and Karrot ban OpenClaw company-wide"
title_zh: "韩国 Naver / Kakao / 당근(Karrot) 全面禁用 OpenClaw"
title_ja: "Naver、Kakao、Karrotが全社でOpenClawを禁止"
title_ko: "네이버·카카오·당근, OpenClaw 전사 금지"
title_de: "Naver, Kakao und Karrot verbieten OpenClaw unternehmensweit"
title_fr: "Naver, Kakao et Karrot bannissent OpenClaw à l'échelle de l'entreprise"
title_es: "Naver, Kakao y Karrot prohíben OpenClaw en toda la empresa"
date: 2026-02-01
date_precision: month
date_raw: "2026-02"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [KR]

summary: |
  Reason: OpenClaw directly controls employees' computers, so corporate secrets and personal data could leak


summary_zh: |
  理由：OpenClaw 直接控制员工电脑，企业机密与个人信息可能外泄

summary_ja: |
  理由：OpenClawが従業員のコンピュータを直接操作するため、企業秘密や個人データが漏えいする可能性があるから

summary_ko: |
  이유: OpenClaw가 직원 컴퓨터를 직접 제어하므로 기업 기밀과 개인정보가 유출될 수 있다

summary_de: |
  Grund: OpenClaw steuert die Rechner der Beschäftigten direkt, sodass Firmengeheimnisse und personenbezogene Daten abfließen könnten

summary_fr: |
  Raison : OpenClaw contrôle directement les ordinateurs des employés, si bien que des secrets d'entreprise et des données personnelles pourraient fuiter

summary_es: |
  Motivo: OpenClaw controla directamente las computadoras de los empleados, por lo que podrían filtrarse secretos corporativos y datos personales

sources:
  - url: https://en.sedaily.com/finance/2026/02/09/naver-kakao-karrot-ban-ai-agent-openclaw-over-security
    label: Seoul Economic Daily

disputed: false
landmark: false
scan_month: 2026-02
scan_ref: "SCAN.md §6 2026-02"
---

# Naver, Kakao and Karrot ban OpenClaw company-wide

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Reason: OpenClaw directly controls employees' computers, so corporate secrets and personal data could leak

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
| 1 | Seoul Economic Daily | <https://en.sedaily.com/finance/2026/02/09/naver-kakao-karrot-ban-ai-agent-openclaw-over-security> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-02-01` (raw: 2026-02, precision `month`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [South Korea](../../regions/kr.md) |
| Archive ID | `2026-02-01-naver-kakao-karrot-openclaw` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-02-05` [GPT-5.3-Codex rated "High" for cyber capability](2026-02-05-gpt-codex-high.md)<br>  <sub>GPT-5.3-Codex rated "High" for cyber capability</sub>
- `2026-02-05` [Claude Opus 4.6 finds 500+ zero-days in open-source projects](2026-02-05-claude-opus-kai-yuan-xiang.md)<br>  <sub>Claude Opus 4.6 finds 500+ zero-days in open-source projects</sub>
- `2026-02-13` [ChatGPT introduces Lockdown Mode](2026-02-13-chatgpt-lockdown-mode.md)<br>  <sub>ChatGPT introduces Lockdown Mode</sub>
- `2026-02-18` [Anthropic, "Measuring AI agent autonomy in practice"](2026-02-18-anthropic-measuring-agent-autonomy.md)<br>  <sub>Anthropic, "Measuring AI agent autonomy in practice"</sub>

---

[← 2026-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-02/2026-02-01-naver-kakao-karrot-openclaw.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
