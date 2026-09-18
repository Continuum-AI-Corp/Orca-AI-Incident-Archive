---
id: 2026-06-08-litellm-mcp-duan-dian-jie
title: "LiteLLM CVE-2026-42271 MCP endpoint takeover"
title_zh: "LiteLLM CVE-2026-42271 MCP 端点接管"
title_ja: "LiteLLM CVE-2026-42271のMCPエンドポイント乗っ取り"
title_ko: "LiteLLM CVE-2026-42271 MCP 엔드포인트 장악"
title_de: "LiteLLM CVE-2026-42271: Übernahme des MCP-Endpunkts"
title_fr: "Prise de contrôle du point de terminaison MCP de LiteLLM (CVE-2026-42271)"
title_es: "Toma de control del endpoint MCP por CVE-2026-42271 en LiteLLM"
date: 2026-06-08
date_precision: day
date_raw: "2026-06-08"

kind: vulnerability
type: [INFRA]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Chains with CVE-2026-42208 (pre-auth SQLi) and CVE-2026-48710 (BadHost) into RCE; **the first exploitation appeared within 36 hours**, and it entered CISA KEV on 06-08. LiteLLM holds master keys and cloud credentials


summary_zh: |
  与 CVE-2026-42208(Pre-Auth SQLi)、CVE-2026-48710(BadHost) 组成 RCE 链；**首次利用出现在 36 小时内**，06-08 进 CISA KEV。LiteLLM 持有主密钥与云凭据

summary_ja: |
  CVE-2026-42208（認証前SQLi）とCVE-2026-48710（BadHost）と連鎖してRCEに至る。**最初の悪用は36時間以内に出現**し、06-08にCISA KEVに入った。LiteLLMはマスターキーとクラウド認証情報を保持している

summary_ko: |
  CVE-2026-42208(인증 전 SQLi) 및 CVE-2026-48710(BadHost)과 연쇄되어 RCE로 이어진다. **36시간 안에 첫 악용이 나타났고** 06-08 CISA KEV에 등재되었다. LiteLLM은 마스터 키와 클라우드 자격 증명을 보유한다

summary_de: |
  Verkettet sich mit CVE-2026-42208 (Pre-Auth-SQLi) und CVE-2026-48710 (BadHost) zu RCE; **die erste Ausnutzung erschien innerhalb von 36 Stunden**, und am 06-08 wurde es in die CISA KEV aufgenommen. LiteLLM hält Master-Schlüssel und Cloud-Zugangsdaten

summary_fr: |
  S'enchaîne avec CVE-2026-42208 (SQLi pré-auth) et CVE-2026-48710 (BadHost) pour aboutir à un RCE ; **la première exploitation est apparue en 36 heures**, et il est entré dans le KEV de la CISA le 06-08. LiteLLM détient des clés maîtresses et des identifiants cloud

summary_es: |
  Se encadena con CVE-2026-42208 (SQLi preautenticación) y CVE-2026-48710 (BadHost) hasta lograr RCE; **la primera explotación apareció en 36 horas**, y entró en el catálogo KEV de CISA el 06-08. LiteLLM guarda claves maestras y credenciales de nube

sources:
  - url: https://theori.io/ko/blog/2026-h1-hot-security-issue-case
    label: Theori

disputed: false
landmark: false
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# LiteLLM CVE-2026-42271 MCP endpoint takeover

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

Chains with CVE-2026-42208 (pre-auth SQLi) and CVE-2026-48710 (BadHost) into RCE; **the first exploitation appeared within 36 hours**, and it entered CISA KEV on 06-08. LiteLLM holds master keys and cloud credentials

## Attack chain

```mermaid
flowchart LR
    E["Agent infrastructure exposed to the internet"]:::entry
    S0["Unauthenticated access"]:::step
    I["RCE / data leak<br/><i>(flaw disclosed, no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Theori | <https://theori.io/ko/blog/2026-h1-hot-security-issue-case> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-08` (raw: 2026-06-08, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-08-litellm-mcp-duan-dian-jie` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-06-29` [DifyTap: four flaws leave 1M+ AI apps open to cross-tenant eavesdropping](2026-06-29-difytap-lou-dong-rang-wan.md)<br>  <sub>DifyTap: four flaws leave 1M+ AI apps open to cross-tenant eavesdropping</sub>
- `2026-06-28` [Langflow CVE-2026-33017 used for Monero mining](2026-06-28-langflow-yong-yu-men-luo.md)<br>  <sub>Langflow CVE-2026-33017 used for Monero mining</sub>
- `2026-06-17` [Vertex AI SDK bucket takeover leads to cross-tenant RCE](2026-06-17-vertex-sdk-rce.md)<br>  <sub>Vertex AI SDK bucket takeover leads to cross-tenant RCE</sub>
- `2026-06-18` [AutoJack: one web page from AutoGen Studio to the host](2026-06-18-autojack-autogen-studio.md)<br>  <sub>AutoJack: one web page from AutoGen Studio to the host</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-08-litellm-mcp-duan-dian-jie.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
