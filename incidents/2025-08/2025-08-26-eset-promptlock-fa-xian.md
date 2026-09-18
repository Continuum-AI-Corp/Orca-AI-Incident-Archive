---
id: 2025-08-26-eset-promptlock-fa-xian
title: "ESET finds PromptLock"
title_zh: "ESET 发现 PromptLock"
title_ja: "ESETがPromptLockを発見"
title_ko: "ESET, PromptLock 발견"
title_de: "ESET entdeckt PromptLock"
title_fr: "ESET découvre PromptLock"
title_es: "ESET encuentra PromptLock"
date: 2025-08-26
date_precision: day
date_raw: "2025-08-26"

kind: incident
type: [WEAPON]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  "The first AI-driven ransomware": written in Golang, it calls **gpt-oss:20b** locally through the Ollama API to generate cross-platform Lua scripts in real time, deciding on its own whether to exfiltrate or encrypt, using SPECK 128-bit. ⚠️ **Later, after the academic paper's authors contacted ESET, it was confirmed that the sample came from the NYU research prototype "Ransomware 3.0: Self-Composing and LLM-Orchestrated" — a PoC rather than an in-the-wild deployment**


summary_zh: |
  「首个 AI 驱动勒索软件」：Golang 编写，经 Ollama API 本地调用 **gpt-oss:20b** 实时生成跨平台 Lua 脚本，自主判断外带还是加密，用 SPECK 128-bit。⚠️ **后经学术论文作者联系 ESET 确认，样本来自 NYU 研究原型《Ransomware 3.0: Self-Composing and LLM-Orchestrated》，是 PoC 而非在野部署**

summary_ja: |
  「初のAI駆動ランサムウェア」：Golangで書かれ、Ollama API経由でローカルに**gpt-oss:20b**を呼び出してクロスプラットフォームのLuaスクリプトをリアルタイム生成し、外部送信か暗号化かを自ら判断、SPECK 128ビットを使用。⚠️ **その後、学術論文の著者がESETに連絡したことで、サンプルはNYUの研究プロトタイプ「Ransomware 3.0: Self-Composing and LLM-Orchestrated」由来、つまり実環境の配備ではなくPoCであることが確認された**

summary_ko: |
  "최초의 AI 기반 랜섬웨어": Golang으로 작성되었고, Ollama API를 통해 로컬의 **gpt-oss:20b**를 호출해 크로스 플랫폼 Lua 스크립트를 실시간으로 생성하며, 유출할지 암호화할지 스스로 판단하고 SPECK 128비트를 사용한다. ⚠️ **이후 학술 논문 저자들이 ESET에 연락하면서, 이 샘플이 NYU 연구 프로토타입 "Ransomware 3.0: Self-Composing and LLM-Orchestrated"에서 나온 것으로 확인되었다 — 실제 배포가 아닌 PoC다**

summary_de: |
  „Die erste KI-gesteuerte Ransomware“: in Golang geschrieben, ruft sie lokal über die Ollama-API **gpt-oss:20b** auf, um in Echtzeit plattformübergreifende Lua-Skripte zu erzeugen, und entscheidet selbst, ob exfiltriert oder verschlüsselt wird, mit SPECK 128-Bit. ⚠️ **Später, nachdem die Autoren der wissenschaftlichen Arbeit ESET kontaktiert hatten, wurde bestätigt, dass das Sample aus dem NYU-Forschungprototyp „Ransomware 3.0: Self-Composing and LLM-Orchestrated“ stammte — ein PoC und kein Einsatz in freier Wildbahn**

summary_fr: |
  « Le premier ransomware piloté par IA » : écrit en Golang, il appelle **gpt-oss:20b** en local via l'API Ollama pour générer en temps réel des scripts Lua multiplateformes, décidant seul d'exfiltrer ou de chiffrer, avec SPECK 128 bits. ⚠️ **Plus tard, après que les auteurs de l'article académique ont contacté ESET, il a été confirmé que l'échantillon venait du prototype de recherche de la NYU « Ransomware 3.0: Self-Composing and LLM-Orchestrated » — un PoC, pas un déploiement en conditions réelles**

summary_es: |
  "El primer ransomware impulsado por IA": escrito en Golang, llama localmente a **gpt-oss:20b** mediante la API de Ollama para generar scripts Lua multiplataforma en tiempo real, decidiendo por sí mismo si exfiltrar o cifrar, usando SPECK de 128 bits. ⚠️ **Después, tras contactar los autores del artículo académico con ESET, se confirmó que la muestra provenía del prototipo de investigación de la NYU "Ransomware 3.0: Self-Composing and LLM-Orchestrated" — un PoC y no un despliegue en entornos reales**

sources:
  - url: https://www.welivesecurity.com/en/ransomware/first-known-ai-powered-ransomware-uncovered-eset-research/
    label: ESET

disputed: false
landmark: false
scan_month: 2025-08
scan_ref: "SCAN.md §5 2025-08"
---

# ESET finds PromptLock

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

"The first AI-driven ransomware": written in Golang, it calls **gpt-oss:20b** locally through the Ollama API to generate cross-platform Lua scripts in real time, deciding on its own whether to exfiltrate or encrypt, using SPECK 128-bit. ⚠️ **Later, after the academic paper's authors contacted ESET, it was confirmed that the sample came from the NYU research prototype "Ransomware 3.0: Self-Composing and LLM-Orchestrated" — a PoC rather than an in-the-wild deployment**

## Attack chain

```mermaid
flowchart LR
    E["Attacker + jailbreak prompts"]:::entry
    S0["An LLM orchestrator drives a cluster of sub-agents"]:::step
    I["The target system is compromised"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | ESET | <https://www.welivesecurity.com/en/ransomware/first-known-ai-powered-ransomware-uncovered-eset-research/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-08-26` (raw: 2025-08-26, precision `day`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-08-26-eset-promptlock-fa-xian` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2025-08-27` [Anthropic August threat report](2025-08-27-anthropic-ba-wei-xie-bao.md)<br>  <sub>Anthropic August threat report</sub>
- `2025-09-02` [HexStrike-AI turned on a Citrix zero-day](../2025-09/2025-09-02-hexstrike-citrix-day.md)<br>  <sub>HexStrike-AI turned on a Citrix zero-day</sub>
- `2025-09-01` [Villager (Cyberspike) AI pentest tool](../2025-09/2025-09-01-villager-cyberspike-shen-tou-gong.md)<br>  <sub>Villager (Cyberspike) AI pentest tool</sub>
- `2025-09-15` [Anthropic detects GTG-1002](../2025-09/2025-09-15-anthropic-gtg-jian-ce-dao.md)<br>  <sub>Anthropic detects GTG-1002</sub>

---

[← 2025-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-08/2025-08-26-eset-promptlock-fa-xian.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
