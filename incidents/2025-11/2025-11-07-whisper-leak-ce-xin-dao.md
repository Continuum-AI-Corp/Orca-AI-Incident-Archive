---
id: 2025-11-07-whisper-leak-ce-xin-dao
title: "Whisper Leak side channel"
title_zh: "Whisper Leak 侧信道"
title_ja: "Whisper Leakサイドチャネル"
title_ko: "Whisper Leak 부채널"
title_de: "Whisper Leak: Seitenkanal"
title_fr: "Canal auxiliaire Whisper Leak"
title_es: "Canal lateral Whisper Leak"
date: 2025-11-07
date_precision: day
date_raw: "2025-11-07"

kind: incident
type: [OTHER]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Microsoft: inferring LLM conversation topics from the packet sizes/timing of encrypted traffic


summary_zh: |
  Microsoft：从加密流量的包大小/时序推断 LLM 对话主题

summary_ja: |
  Microsoft：暗号化トラフィックのパケットサイズ／タイミングからLLMの会話トピックを推測する

summary_ko: |
  마이크로소프트: 암호화된 트래픽의 패킷 크기/타이밍으로 LLM 대화 주제를 추론한다

summary_de: |
  Microsoft: Rückschluss auf die Themen von LLM-Unterhaltungen aus Paketgrößen/Timing verschlüsselten Verkehrs

summary_fr: |
  Microsoft : déduire le sujet d'une conversation avec un LLM à partir de la taille et du rythme des paquets d'un trafic chiffré

summary_es: |
  Microsoft: inferir los temas de una conversación con un LLM a partir de los tamaños de paquete y los tiempos del tráfico cifrado

sources:
  - url: https://www.ipa.go.jp/digital/ai/security/ai-security-bulletin.html
    label: "Japan IPA 2025-12"

disputed: false
landmark: false
scan_month: 2025-11
scan_ref: "SCAN.md §5 2025-11"
---

# Whisper Leak side channel

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

Microsoft: inferring LLM conversation topics from the packet sizes/timing of encrypted traffic

## Attack chain

```mermaid
flowchart LR
    E["Entry point"]:::entry
    S0["Process"]:::step
    I["Result"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Japan IPA 2025-12 | <https://www.ipa.go.jp/digital/ai/security/ai-security-bulletin.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-11-07` (raw: 2025-11-07, precision `day`) |
| Kind | Incident `incident` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-11-07-whisper-leak-ce-xin-dao` |

<sub>**Why this classification:** Real incident without a confirmed specific victim. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2025-11 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-11/2025-11-07-whisper-leak-ce-xin-dao.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
