---
id: 2025-04-01-deepseek-han-guo-jia
title: "DeepSeek pulled from app stores in South Korea"
title_zh: "DeepSeek 韩国下架"
title_ja: "韓国でDeepSeekがアプリストアから削除"
title_ko: "한국, DeepSeek를 앱스토어에서 삭제"
title_de: "DeepSeek aus den App-Stores in Südkorea entfernt"
title_fr: "DeepSeek retiré des magasins d'applications en Corée du Sud"
title_es: "DeepSeek retirado de las tiendas de aplicaciones en Corea del Sur"
date: 2025-04-01
date_precision: month
date_raw: "2025-04"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [KR]

summary: |
  PIPC: user data and prompts were sent back to servers in Beijing without authorization


summary_zh: |
  PIPC：未授权把用户数据与 prompt 传回北京服务器

summary_ja: |
  PIPC：ユーザーデータとプロンプトが無断で北京のサーバーに送信されていた

summary_ko: |
  개인정보보호위원회: 사용자 데이터와 프롬프트가 승인 없이 베이징 서버로 전송되었다

summary_de: |
  PIPC: Nutzerdaten und Prompts wurden ohne Autorisierung zurück an Server in Peking gesendet

summary_fr: |
  PIPC : les données et prompts des utilisateurs étaient renvoyés vers des serveurs à Pékin sans autorisation

summary_es: |
  PIPC: los datos y prompts de los usuarios se enviaban a servidores en Pekín sin autorización

sources:
  - url: https://genai.owasp.org/2025/07/14/owasp-gen-ai-incident-exploit-round-up-q225/
    label: "OWASP Q2'25"

disputed: false
landmark: false
scan_month: 2025-04
scan_ref: "SCAN.md §5 2025-04"
---

# DeepSeek pulled from app stores in South Korea

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

PIPC: user data and prompts were sent back to servers in Beijing without authorization

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
| 1 | OWASP Q2'25 | <https://genai.owasp.org/2025/07/14/owasp-gen-ai-incident-exploit-round-up-q225/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-04-01` (raw: 2025-04, precision `month`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [South Korea](../../regions/kr.md) |
| Archive ID | `2025-04-01-deepseek-han-guo-jia` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2025-03-01` [Sony pulls 75,000+ AI deepfake tracks](../2025-03/2025-03-01-sony-jia-wan-shen-wei.md)<br>  <sub>Sony pulls 75,000+ AI deepfake tracks</sub>
- `2025-02-21` [OpenAI bans accounts behind the "Peer Review" surveillance tool](../2025-02/2025-02-21-peer-review-feng-jin-jian.md)<br>  <sub>OpenAI bans accounts behind the "Peer Review" surveillance tool</sub>
- `2025-02-27` [Microsoft sues Storm-2139 and names the defendants](../2025-02/2025-02-27-storm-wei-ruan-qi-su.md)<br>  <sub>Microsoft sues Storm-2139 and names the defendants</sub>
- `2025-06-16` [Simon Willison names the "lethal trifecta"](../2025-06/2025-06-16-simon-willison-ti-chu-zhi.md)<br>  <sub>Simon Willison names the "lethal trifecta"</sub>

---

[← 2025-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-04/2025-04-01-deepseek-han-guo-jia.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
