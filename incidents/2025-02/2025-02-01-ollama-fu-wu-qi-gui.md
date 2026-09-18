---
id: 2025-02-01-ollama-fu-wu-qi-gui
title: "Thousands of Ollama servers exposed without auth"
title_zh: "Ollama 服务器大规模裸奔"
title_ja: "数千台のOllamaサーバーが認証なしで公開"
title_ko: "수천 대의 Ollama 서버, 인증 없이 노출"
title_de: "Tausende Ollama-Server ohne Authentifizierung exponiert"
title_fr: "Des milliers de serveurs Ollama exposés sans authentification"
title_es: "Miles de servidores Ollama expuestos sin autenticación"
date: 2025-02-01
date_precision: month
date_raw: "2025-02"

kind: incident
type: [INFRA]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [CN, GLOBAL]

summary: |
  QiAnXin Hunter: of **8,971** Ollama servers worldwide, **6,449 are active**, and **88.9% have no effective security protection**; **5,669 of the 8,971 are in China**. There is no authentication by default (port 11434), so models can be stolen, false information fed in, inference capacity hijacked or deployed DeepSeek/Qwen model files even deleted. CNVD-2025-04094


summary_zh: |
  奇安信鹰图：全球 **8,971** 台 Ollama 服务器中 **6,449 台活跃**，其中 **88.9% 无有效安全防护**；8,971 台中 **5,669 台在中国**。默认无身份验证（11434 端口），可窃取模型、投喂虚假信息、盗用推理资源，甚至删除已部署的 DeepSeek/Qwen 模型文件。CNVD-2025-04094

summary_ja: |
  QiAnXin Hunter：世界の**8,971**台のOllamaサーバーのうち**6,449**台が稼働中で、**88.9%に有効なセキュリティ保護がない**。**8,971台のうち5,669台が中国にある**。デフォルトでは認証がなく（ポート11434）、モデルの窃取、虚偽情報の投入、推論能力の乗っ取り、デプロイ済みのDeepSeek/Qwenモデルファイルの削除まで可能だ。CNVD-2025-04094

summary_ko: |
  QiAnXin Hunter: 전 세계 **8,971대**의 Ollama 서버 가운데 **6,449대가 활성 상태**이며 **88.9%가 실효성 있는 보안 보호가 없다**. **8,971대 중 5,669대는 중국에 있다**. 기본적으로 인증이 없어(포트 11434) 모델 탈취, 허위 정보 주입, 추론 용량 탈취는 물론 배포된 DeepSeek/Qwen 모델 파일 삭제까지 가능하다. CNVD-2025-04094

summary_de: |
  QiAnXin Hunter: Von **8,971** Ollama-Servern weltweit sind **6,449 aktiv**, und **88.9% haben keinen wirksamen Schutz**; **5,669 der 8,971 stehen in China**. Standardmäßig gibt es keine Authentifizierung (Port 11434), sodass Modelle gestohlen, Falschinformationen eingespeist, Inferenzkapazität gekapert oder eingesetzte DeepSeek/Qwen-Modelldateien sogar gelöscht werden können. CNVD-2025-04094

summary_fr: |
  QiAnXin Hunter : sur **8 971** serveurs Ollama dans le monde, **6 449 sont actifs** et **88,9 % n'ont aucune protection de sécurité efficace** ; **5 669 des 8 971 se trouvent en Chine**. L'authentification n'est pas activée par défaut (port 11434), ce qui permet de voler les modèles, d'y injecter de fausses informations, de détourner la capacité d'inférence ou même de supprimer les fichiers de modèles DeepSeek/Qwen déployés. CNVD-2025-04094

summary_es: |
  QiAnXin Hunter: de **8,971** servidores Ollama en todo el mundo, **6,449 están activos** y **el 88.9% no tiene protección de seguridad efectiva**; **5,669 de los 8,971 están en China**. No hay autenticación por defecto (puerto 11434), por lo que los modelos pueden robarse, se puede introducir información falsa, secuestrar la capacidad de inferencia o incluso borrar los archivos de modelos DeepSeek/Qwen desplegados. CNVD-2025-04094

sources:
  - url: https://www.qianxin.com/news/detail?news_id=13062
    label: QiAnXin
  - url: https://www.secrss.com/articles/76168
    label: CNCERT advisory
  - url: https://blog.nsfocus.net/cnvd-2025-04094/
    label: NSFOCUS

disputed: true
landmark: false
scan_month: 2025-02
scan_ref: "SCAN.md §5 2025-02"
---

# Thousands of Ollama servers exposed without auth

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

> [!WARNING]
> **This record contains disputed or not fully confirmed facts**; the claims of each party are kept side by side in the body, so do not cite any single one of them in isolation.

## Summary

QiAnXin Hunter: of **8,971** Ollama servers worldwide, **6,449 are active**, and **88.9% have no effective security protection**; **5,669 of the 8,971 are in China**. There is no authentication by default (port 11434), so models can be stolen, false information fed in, inference capacity hijacked or deployed DeepSeek/Qwen model files even deleted. CNVD-2025-04094

## Attack chain

```mermaid
flowchart LR
    E["Agent infrastructure exposed to the internet"]:::entry
    S0["Unauthenticated access"]:::step
    I["RCE / data leak"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | QiAnXin | <https://www.qianxin.com/news/detail?news_id=13062> |
| 2 | CNCERT advisory | <https://www.secrss.com/articles/76168> |
| 3 | NSFOCUS | <https://blog.nsfocus.net/cnvd-2025-04094/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-02-01` (raw: 2025-02, precision `month`) |
| Kind | Incident `incident` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [China](../../regions/cn.md) · [Global](../../regions/global.md) |
| Archive ID | `2025-02-01-ollama-fu-wu-qi-gui` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2025-01-29` [DeepSeek ClickHouse database left wide open](../2025-01/2025-01-29-deepseek-clickhouse-exposed.md)<br>  <sub>DeepSeek ClickHouse database left wide open</sub>
- `2025-03-01` [ChatGPT SSRF CVE-2024-27564 exploited in the wild](../2025-03/2025-03-01-chatgpt-ssrf-ye-li-yong.md)<br>  <sub>ChatGPT SSRF CVE-2024-27564 exploited in the wild</sub>
- `2025-03-03` [DeepSeek exposure window closes](../2025-03/2025-03-03-deepseek-bao-lu-chuang-kou.md)<br>  <sub>DeepSeek exposure window closes</sub>
- `2025-04-29` [NVIDIA TensorRT-LLM deserialization RCE](../2025-04/2025-04-29-nvidia-tensorrt-llm-rce.md)<br>  <sub>NVIDIA TensorRT-LLM deserialization RCE</sub>

---

[← 2025-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-02/2025-02-01-ollama-fu-wu-qi-gui.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
