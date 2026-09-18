---
id: 2025-05-01-qu-dong-zhuang-ku-zi
title: "AI-driven credential stuffing and scanning goes to scale"
title_zh: "AI 驱动的撞库与自动化扫描规模化"
title_ja: "AI駆動のクレデンシャルスタッフィングとスキャンが大規模化"
title_ko: "AI 기반 자격 증명 대입과 스캐닝, 규모의 단계로 진입"
title_de: "KI-gesteuertes Credential Stuffing und Scanning erreicht neue Größenordnung"
title_fr: "Le credential stuffing et le scan pilotés par IA passent à l'échelle"
title_es: "El credential stuffing y el escaneo impulsados por IA alcanzan escala"
date: 2025-05-01
date_precision: month
date_raw: "2025-05"

kind: incident
type: [WEAPON]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Attackers wired LLMs into credential-stuffing and port-scanning pipelines, sharply raising the scale and variant-generation capacity of credential stuffing and asset discovery.


summary_zh: |
  攻击方把 LLM 接进撞库与端口扫描流水线，使凭据填充和资产探测的规模与变体生成能力显著上升。

summary_ja: |
  攻撃者はLLMをクレデンシャルスタッフィングとポートスキャンのパイプラインに組み込み、クレデンシャルスタッフィングと資産探索の規模とバリアント生成能力を急激に高めた。

summary_ko: |
  공격자들은 LLM을 자격 증명 대입과 포트 스캐닝 파이프라인에 연결해, 자격 증명 대입과 자산 탐색의 규모 및 변형 생성 능력을 크게 끌어올렸다.

summary_de: |
  Angreifer integrierten LLMs in Credential-Stuffing- und Portscanning-Pipelines, was Umfang und Variantengenerierung bei Credential Stuffing und Asset-Erkennung stark erhöhte.

summary_fr: |
  Des attaquants ont intégré des LLM dans des chaînes de credential stuffing et de scan de ports, augmentant fortement l'échelle et la capacité de génération de variantes du bourrage d'identifiants et de la découverte d'actifs.

summary_es: |
  Los atacantes integraron LLM en canalizaciones de credential stuffing y escaneo de puertos, elevando bruscamente la escala y la capacidad de generar variantes del credential stuffing y del descubrimiento de activos.

sources:
  - url: https://genai.owasp.org/2025/07/14/owasp-gen-ai-incident-exploit-round-up-q225/
    label: "OWASP Q2'25"

disputed: false
landmark: false
scan_month: 2025-05
scan_ref: "SCAN.md §5 2025-05"
---

# AI-driven credential stuffing and scanning goes to scale

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

Attackers wired LLMs into credential-stuffing and port-scanning pipelines, sharply raising the scale and variant-generation capacity of credential stuffing and asset discovery.

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
| 1 | OWASP Q2'25 | <https://genai.owasp.org/2025/07/14/owasp-gen-ai-incident-exploit-round-up-q225/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-05-01` (raw: 2025-05, precision `month`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-05-01-qu-dong-zhuang-ku-zi` |

<sub>**Why this classification:** Real incident without a confirmed specific victim. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2025-05-01` [Anthropic logs the start of GTG-2002 activity](2025-05-01-anthropic-gtg-ji-lu-huo.md)<br>  <sub>Anthropic logs the start of GTG-2002 activity</sub>
- `2025-06-01` [Check Point's "Skynet" sample](../2025-06/2025-06-01-check-point-skynet.md)<br>  <sub>Check Point's "Skynet" sample</sub>
- `2025-06-01` [Anthropic logs the precursor to GTG-1002](../2025-06/2025-06-01-anthropic-gtg-ji-lu-shen.md)<br>  <sub>Anthropic logs the precursor to GTG-1002</sub>
- `2025-04-24` [Anthropic's first misuse report](../2025-04/2025-04-24-anthropic-shou-fen-lan-yong.md)<br>  <sub>Anthropic's first misuse report</sub>

---

[← 2025-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-05/2025-05-01-qu-dong-zhuang-ku-zi.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
