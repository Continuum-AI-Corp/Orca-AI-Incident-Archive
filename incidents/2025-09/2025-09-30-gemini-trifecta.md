---
id: 2025-09-30-gemini-trifecta
title: "Gemini \"Trifecta\""
title_zh: "Gemini \"Trifecta\""
title_ja: "Geminiの「Trifecta」"
title_ko: "Gemini \"삼중주\""
title_de: "Gemini „Trifecta“"
title_fr: "La « Trifecta » de Gemini"
title_es: "La \"Trifecta\" de Gemini"
date: 2025-09-30
date_precision: day
date_raw: "2025-09-30"

kind: research
type: [IPI, EXFIL]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Tenable's three chains: ① search injection in the Search Personalization model ② **log-to-prompt injection** in Gemini Cloud Assist ③ the Browsing tool exfiltrating saved information and location. Google has fixed all of them (rolled back the vulnerable model, stopped rendering malicious hyperlinks, deployed layered prompt-injection defenses)


summary_zh: |
  Tenable 三条链：① Search Personalization 模型的搜索注入 ② Gemini Cloud Assist 的**日志转提示注入** ③ Browsing 工具外带已保存信息与位置。Google 已全部修复（回滚脆弱模型、停止恶意超链接渲染、部署分层提示注入防御）

summary_ja: |
  Tenableの3つのチェーン：① Search Personalizationモデルにおける検索インジェクション ② Gemini Cloud Assistにおける**log-to-promptインジェクション** ③ Browsingツールによる保存情報と位置情報の外部送信。Googleはすべて修正済み（脆弱なモデルのロールバック、悪意あるハイパーリンクの描画停止、プロンプトインジェクション対策の多層防御の導入）

summary_ko: |
  Tenable이 찾은 세 가지 체인: ① Search Personalization 모델의 검색 인젝션 ② Gemini Cloud Assist의 **로그→프롬프트 인젝션** ③ Browsing 도구가 저장된 정보와 위치를 유출. 구글은 모두 수정했다(취약 모델 롤백, 악성 하이퍼링크 렌더링 중단, 계층형 프롬프트 인젝션 방어 배포)

summary_de: |
  Tenables drei Ketten: ① Search-Injection im Search-Personalization-Modell ② **Log-to-Prompt-Injection** in Gemini Cloud Assist ③ das Browsing-Tool, das gespeicherte Informationen und den Standort exfiltriert. Google hat alle behoben (das verwundbare Modell zurückgerollt, das Rendern bösartiger Hyperlinks gestoppt, mehrschichtige Prompt-Injection-Abwehr eingeführt)

summary_fr: |
  Les trois chaînes de Tenable : ① injection via la recherche dans le modèle Search Personalization ② **injection log-to-prompt** dans Gemini Cloud Assist ③ l'outil Browsing qui exfiltre les informations enregistrées et la localisation. Google a tout corrigé (retrait du modèle vulnérable, arrêt du rendu des hyperliens malveillants, déploiement de défenses en couches contre l'injection de prompt)

summary_es: |
  Las tres cadenas de Tenable: ① inyección en la búsqueda del modelo Search Personalization ② **inyección de logs a prompt** en Gemini Cloud Assist ③ la herramienta Browsing exfiltraba información guardada y ubicación. Google las ha corregido todas (revirtió el modelo vulnerable, dejó de renderizar hipervínculos maliciosos, desplegó defensas de inyección de prompt por capas)

sources:
  - url: https://www.tenable.com/blog/the-trifecta-how-three-new-gemini-vulnerabilities-in-cloud-assist-search-model-and-browsing
    label: Tenable
  - url: https://thehackernews.com/2025/09/researchers-disclose-google-gemini-ai.html
    label: THN

disputed: false
landmark: true
scan_month: 2025-09
scan_ref: "SCAN.md §5 2025-09"
---

# Gemini "Trifecta"

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

Tenable's three chains: ① search injection in the Search Personalization model ② **log-to-prompt injection** in Gemini Cloud Assist ③ the Browsing tool exfiltrating saved information and location. Google has fixed all of them (rolled back the vulnerable model, stopped rendering malicious hyperlinks, deployed layered prompt-injection defenses)

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["Exfiltration via the vendor's trusted domain<br/>image rendering · API · proxy"]:::step
    I["Data ends up with the attacker<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Tenable | <https://www.tenable.com/blog/the-trifecta-how-three-new-gemini-vulnerabilities-in-cloud-assist-search-model-and-browsing> |
| 2 | THN | <https://thehackernews.com/2025/09/researchers-disclose-google-gemini-ai.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-09-30` (raw: 2025-09-30, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-09-30-gemini-trifecta` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2025-09-18` [ShadowLeak](2025-09-18-shadowleak.md)<br>  <sub>ShadowLeak</sub>
- `2025-09-19` [Notion 3.0 agent hits the lethal trifecta](2025-09-19-notion-agent-zhi-ming-san.md)<br>  <sub>Notion 3.0 agent hits the lethal trifecta</sub>
- `2025-09-25` [ForcedLeak (Salesforce Agentforce)](2025-09-25-forcedleak-salesforce-agentforce.md)<br>  <sub>ForcedLeak (Salesforce Agentforce)</sub>
- `2025-08-06` [AgentFlayer zero-click attack set (Black Hat USA)](../2025-08/2025-08-06-agentflayer-black-hat-usa.md)<br>  <sub>AgentFlayer zero-click attack set (Black Hat USA)</sub>

---

[← 2025-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-09/2025-09-30-gemini-trifecta.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
