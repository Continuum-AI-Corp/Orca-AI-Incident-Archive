---
id: 2024-12-01-storm-azure-llmjacking
title: "Storm-2139 Azure OpenAI LLMjacking"
title_zh: "Storm-2139 Azure OpenAI LLMjacking"
title_ja: "Storm-2139によるAzure OpenAIのLLMjacking"
title_ko: "Storm-2139의 Azure OpenAI LLMjacking"
title_de: "Storm-2139 Azure OpenAI LLMjacking"
title_fr: "Storm-2139 : LLMjacking d'Azure OpenAI"
title_es: "LLMjacking de Azure OpenAI por Storm-2139"
date: 2024-12-01
date_end: 2025-02-01
date_precision: month
date_raw: "2024-12→2025-02"

kind: incident
type: [CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Microsoft's DCU filed suit in the Eastern District of Virginia in 2024-12 against 10 "John Doe" defendants; stolen credentials were used to take over Azure OpenAI, jailbreak techniques bypassed safeguards and the **service was resold**. The defendants were named publicly on 2025-02-27


summary_zh: |
  微软 DCU 2024-12 在弗吉尼亚东区起诉 10 名「John Doe」；盗取凭据接管 Azure OpenAI，用越狱技术绕过安全防护并**转售服务**。2025-02-27 公开被告身份

summary_ja: |
  MicrosoftのDCUは2024-12にバージニア東部地区連邦地裁で10名の「John Doe」被告に対して訴訟を提起した。盗まれた認証情報がAzure OpenAIの乗っ取りに使われ、ジェイルブレイク手法がセーフガードを回避し、**サービスは転売された**。被告の氏名は2025-02-27に公開された

summary_ko: |
  마이크로소프트 DCU는 2024-12 버지니아 동부지방법원에 "John Doe" 피고 10명을 상대로 소송을 제기했다. 도난당한 자격 증명으로 Azure OpenAI를 장악했고, 탈옥 기법으로 안전장치를 우회해 **서비스를 재판매**했다. 피고들의 실명은 2025-02-27에 공개되었다

summary_de: |
  Microsofts DCU reichte 2024-12 beim Eastern District of Virginia Klage gegen 10 Beklagte ein, die als „John Doe“ geführt wurden; mit gestohlenen Zugangsdaten wurde Azure OpenAI übernommen, Jailbreak-Techniken umgingen die Schutzmechanismen, und **der Dienst wurde weiterverkauft**. Die Beklagten wurden am 2025-02-27 öffentlich benannt

summary_fr: |
  La DCU de Microsoft a déposé plainte en 2024-12 devant le tribunal du district est de la Virginie contre 10 défendeurs « John Doe » ; des identifiants volés ont servi à détourner Azure OpenAI, des techniques de jailbreak ont contourné les garde-fous et **le service a été revendu**. Les défendeurs ont été nommés publiquement le 2025-02-27

summary_es: |
  La DCU de Microsoft presentó una demanda en el Distrito Este de Virginia en 2024-12 contra 10 acusados "John Doe"; se usaron credenciales robadas para tomar el control de Azure OpenAI, técnicas de jailbreak eludieron las protecciones y **el servicio se revendió**. Los acusados fueron identificados públicamente el 2025-02-27

sources:
  - url: https://blogs.microsoft.com/on-the-issues/2025/02/27/disrupting-cybercrime-abusing-gen-ai/
    label: Microsoft

disputed: false
landmark: false
scan_month: 2025-01
scan_ref: "SCAN.md §5 2025-01"
---

# Storm-2139 Azure OpenAI LLMjacking

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

Microsoft's DCU filed suit in the Eastern District of Virginia in 2024-12 against 10 "John Doe" defendants; stolen credentials were used to take over Azure OpenAI, jailbreak techniques bypassed safeguards and the **service was resold**. The defendants were named publicly on 2025-02-27

## Attack chain

```mermaid
flowchart LR
    E["Credentials within an agent's reach"]:::entry
    S0["The agent picks them up and calls out"]:::step
    I["Credentials are abused"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Microsoft | <https://blogs.microsoft.com/on-the-issues/2025/02/27/disrupting-cybercrime-abusing-gen-ai/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2024-12-01` → `2025-02-01` (raw: 2024-12→2025-02, precision `month`) |
| Kind | Incident `incident` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2024-12-01-storm-azure-llmjacking` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2025-06-30` [McDonald's McHire "Olivia" hiring bot](../2025-06/2025-06-30-mcdonald-mchire-olivia.md)<br>  <sub>McDonald's McHire "Olivia" hiring bot</sub>
- `2025-06-13` [Smithery.ai path traversal](../2025-06/2025-06-13-smithery-ai-lu-jing-chuan-yue.md)<br>  <sub>Smithery.ai path traversal</sub>
- `2025-07-01` [RoguePilot](../2025-07/2025-07-01-roguepilot.md)<br>  <sub>RoguePilot</sub>
- `2025-07-09` [McHire flaw goes public](../2025-07/2025-07-09-mchire-lou-dong-gong-kai.md)<br>  <sub>McHire flaw goes public</sub>

---

[← 2024-12 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2024-12/2024-12-01-storm-azure-llmjacking.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
