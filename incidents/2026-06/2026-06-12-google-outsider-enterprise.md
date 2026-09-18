---
id: 2026-06-12-google-outsider-enterprise
title: "Google sues the China-linked \"Outsider Enterprise\" smishing network"
title_zh: "Google 起诉中国背景的 \"Outsider Enterprise\" 短信钓鱼网络"
title_ja: "Google、中国関連の「Outsider Enterprise」スミッシング・ネットワークを提訴"
title_ko: "구글, 중국 연계 \"Outsider Enterprise\" 스미싱 네트워크 제소"
title_de: "Google verklagt das mit China verbundene Smishing-Netzwerk „Outsider Enterprise“"
title_fr: "Google poursuit le réseau de smishing « Outsider Enterprise » lié à la Chine"
title_es: "Google demanda a la red de smishing \"Outsider Enterprise\", vinculada a China"
date: 2026-06-12
date_precision: day
date_raw: "2026-06-12"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [CN, US]

summary: |
  9,000 domains, 1.59M+ malicious URLs, 100,000+ victims and millions of dollars in losses; 2.55 million SMS messages sent between 2026-05-18 → 06-01. **The defendants disguised "generate gift-redemption-page HTML" as an ordinary programming request to have Gemini generate scam-site code**


summary_zh: |
  9,000 个域名、159 万+ 恶意 URL、10 万+ 受害者、数百万美元损失；2026-05-18→06-01 发出 255 万条短信。**被告把「生成礼品兑换页 HTML」伪装成正常编程请求让 Gemini 生成诈骗站代码**

summary_ja: |
  ドメイン9,000件、悪性URL159万件以上、被害者10万人以上、損失は数百万ドル。2026-05-18 → 06-01の間に255万通のSMSを送信。**被告らは「景品引き換えページのHTMLを生成」を通常のプログラミング依頼と偽り、Geminiに詐欺サイトのコードを生成させていた**

summary_ko: |
  도메인 9,000개, 악성 URL 159만 개 이상, 피해자 10만 명 이상, 수백만 달러의 손실. 2026-05-18 → 06-01 사이에 SMS 255만 통이 발송되었다. **피고들은 "기프트 교환 페이지 HTML을 생성해 달라"를 평범한 프로그래밍 요청으로 위장해 Gemini가 사기 사이트 코드를 만들게 했다**

summary_de: |
  9,000 Domains, 1.59M+ bösartige URLs, 100,000+ Opfer und Schäden in Millionenhöhe; 2.55 Millionen versandte SMS zwischen 2026-05-18 → 06-01. **Die Beklagten tarnten „generiere HTML für eine Geschenk-Einlöseseite“ als gewöhnliche Programmieranfrage, um Gemini Code für Betrugsseiten erzeugen zu lassen**

summary_fr: |
  9 000 domaines, plus de 1,59 million d'URL malveillantes, plus de 100 000 victimes et des millions de dollars de pertes ; 2,55 millions de SMS envoyés entre le 2026-05-18 → 06-01. **Les défendeurs ont déguisé « générer le HTML d'une page de rédemption de cadeau » en requête de programmation ordinaire pour faire produire par Gemini du code de site d'arnaque**

summary_es: |
  9,000 dominios, más de 1.59M de URL maliciosas, más de 100,000 víctimas y millones de dólares en pérdidas; 2.55 millones de mensajes SMS enviados entre el 2026-05-18 y el 06-01. **Los demandados disfrazaron "genera el HTML de una página de canje de regalos" como una solicitud de programación normal para que Gemini generara código de sitios de estafa**

sources:
  - url: https://blog.google/innovation-and-ai/technology/safety-security/combatting-ai-scams/
    label: Google
  - url: https://thehackernews.com/2026/06/google-sues-chinese-smishing-network.html
    label: THN

disputed: false
landmark: false
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# Google sues the China-linked "Outsider Enterprise" smishing network

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

9,000 domains, 1.59M+ malicious URLs, 100,000+ victims and millions of dollars in losses; 2.55 million SMS messages sent between 2026-05-18 → 06-01. **The defendants disguised "generate gift-redemption-page HTML" as an ordinary programming request to have Gemini generate scam-site code**

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
| 1 | Google | <https://blog.google/innovation-and-ai/technology/safety-security/combatting-ai-scams/> |
| 2 | THN | <https://thehackernews.com/2026/06/google-sues-chinese-smishing-network.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-12` (raw: 2026-06-12, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [China](../../regions/cn.md) · [United States](../../regions/us.md) |
| Archive ID | `2026-06-12-google-outsider-enterprise` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-06-09` [Anthropic Claude Fable 5 GA, Mythos 5 limited release](2026-06-09-anthropic-claude-fable-ga.md)<br>  <sub>Anthropic Claude Fable 5 GA, Mythos 5 limited release</sub>
- `2026-06-11` [CISA BOD 26-04](2026-06-11-cisa-bod.md)<br>  <sub>CISA BOD 26-04</sub>
- `2026-06-12` [US government issues export controls to Anthropic](2026-06-12-anthropic-mei-guo-zheng-fu.md)<br>  <sub>US government issues export controls to Anthropic</sub>
- `2026-06-23` [Five Eyes joint statement to boards and executives](2026-06-23-five-eyes-zhi-qi-ye.md)<br>  <sub>Five Eyes joint statement to boards and executives</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-12-google-outsider-enterprise.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
