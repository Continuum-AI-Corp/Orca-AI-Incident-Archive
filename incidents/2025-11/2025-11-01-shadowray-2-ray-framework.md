---
id: 2025-11-01-shadowray-2-ray-framework
title: "ShadowRay 2.0 (Ray framework)"
title_zh: "ShadowRay 2.0（Ray 框架）"
title_ja: "ShadowRay 2.0（Rayフレームワーク）"
title_ko: "ShadowRay 2.0(Ray 프레임워크)"
title_de: "ShadowRay 2.0 (Ray-Framework)"
title_fr: "ShadowRay 2.0 (framework Ray)"
title_es: "ShadowRay 2.0 (framework Ray)"
date: 2025-11-01
date_precision: month
date_raw: "2025-11"

kind: incident
type: [INFRA]
severity: critical
confidence: B
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Oligo Security: exploits **CVE-2023-48022** (left unfixed because Ray's maintainers consider it "consistent with the designed trust model") to build a self-propagating botnet that compromised **230,000+** internet-facing Ray servers (many with NVIDIA A100s), used for cryptomining, data and credential theft, and DDoS. **Much of the attack payload is AI-generated** — marked by redundant docstrings, pointless echo statements, repeated comments and boilerplate error handling


summary_zh: |
  Oligo Security：利用 **CVE-2023-48022**（Ray 维护者视为「符合设计信任模型」而长期未修）构建自我传播僵尸网络，攻陷 **23 万+** 联网 Ray 服务器（大量搭载 NVIDIA A100），用于挖矿、数据与凭据窃取、DDoS。**攻击载荷大量由 AI 生成**——特征是冗余 docstring、无用 echo、重复注释与模板化错误处理

summary_ja: |
  Oligo Security：**CVE-2023-48022**（Rayのメンテナーが「設計上の信頼モデルと整合する」として未修正のまま）を悪用し、自己増殖型ボットネットを構築、**23万台以上**のインターネット公開Rayサーバー（多くはNVIDIA A100搭載）を侵害。暗号資産マイニング、データと認証情報の窃取、DDoSに利用された。**攻撃ペイロードの多くはAI生成**——冗長なdocstring、無意味なecho文、繰り返されるコメント、定型のエラーハンドリングが特徴

summary_ko: |
  Oligo Security: **CVE-2023-48022**(Ray 유지관리자들이 "설계된 신뢰 모델에 부합한다"며 수정하지 않은 결함)를 악용해 자기 전파 봇넷을 구축하고 인터넷에 노출된 Ray 서버 **23만 대 이상**(다수가 NVIDIA A100 탑재)을 장악했으며, 암호화폐 채굴, 데이터·자격 증명 탈취, DDoS에 사용했다. **공격 페이로드 상당 부분이 AI 생성물**이며, 불필요한 독스트링, 의미 없는 echo 문, 반복되는 주석, 상용구 오류 처리 등이 그 특징이다

summary_de: |
  Oligo Security: Nutzt **CVE-2023-48022** aus (unbehoben gelassen, weil Rays Maintainer sie als „konsistent mit dem entworfenen Vertrauensmodell“ betrachten), um ein selbstverbreitendes Botnetz aufzubauen, das **230,000+** internetzugewandte Ray-Server kompromittierte (viele mit NVIDIA A100), genutzt für Kryptomining, Daten- und Zugangsdatendiebstahl sowie DDoS. **Ein großer Teil der Angriffsnutzlast ist KI-generiert** — erkennbar an redundanten Docstrings, sinnlosen echo-Anweisungen, wiederholten Kommentaren und Boilerplate-Fehlerbehandlung

summary_fr: |
  Oligo Security : exploite **CVE-2023-48022** (laissée non corrigée car les mainteneurs de Ray la jugent « conforme au modèle de confiance conçu ») pour bâtir un botnet auto-propagateur qui a compromis **plus de 230 000** serveurs Ray exposés sur Internet (beaucoup avec des NVIDIA A100), utilisé pour du cryptominage, du vol de données et d'identifiants et du DDoS. **Une grande partie de la charge d'attaque est générée par IA** — marquée par des docstrings redondantes, des instructions echo inutiles, des commentaires répétés et une gestion d'erreurs stéréotypée

summary_es: |
  Oligo Security: explota **CVE-2023-48022** (que quedó sin corregir porque los mantenedores de Ray lo consideran "coherente con el modelo de confianza diseñado") para construir una botnet autorreplicante que comprometió **más de 230,000** servidores Ray expuestos a internet (muchos con NVIDIA A100), usada para criptominería, robo de datos y credenciales, y DDoS. **Gran parte de la carga útil del ataque está generada por IA** — se nota por docstrings redundantes, sentencias echo inútiles, comentarios repetidos y manejo de errores de plantilla

sources:
  - url: https://www.oligo.security/blog/shadowray-attack-ai-workloads-actively-exploited-in-the-wild
    label: Oligo

disputed: true
landmark: true
scan_month: 2025-11
scan_ref: "SCAN.md §5 2025-11"
---

# ShadowRay 2.0 (Ray framework)

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

> [!WARNING]
> **This record contains disputed or not fully confirmed facts**; the claims of each party are kept side by side in the body, so do not cite any single one of them in isolation.

## Summary

Oligo Security: exploits **CVE-2023-48022** (left unfixed because Ray's maintainers consider it "consistent with the designed trust model") to build a self-propagating botnet that compromised **230,000+** internet-facing Ray servers (many with NVIDIA A100s), used for cryptomining, data and credential theft, and DDoS. **Much of the attack payload is AI-generated** — marked by redundant docstrings, pointless echo statements, repeated comments and boilerplate error handling

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
| 1 | Oligo | <https://www.oligo.security/blog/shadowray-attack-ai-workloads-actively-exploited-in-the-wild> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-11-01` (raw: 2025-11, precision `month`) |
| Kind | Incident `incident` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **Critical** `critical` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-11-01-shadowray-2-ray-framework` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2025-10-30` [ServiceNow BodySnatcher](../2025-10/2025-10-30-servicenow-bodysnatcher.md)<br>  <sub>ServiceNow BodySnatcher</sub>
- `2026-01-26` [Clawdbot gateways exposed at scale](../2026-01/2026-01-26-clawdbot-wang-guan-gui-mo.md)<br>  <sub>Clawdbot gateways exposed at scale</sub>
- `2026-01-29` [OpenClaw Control UI WebSocket hijack RCE](../2026-01/2026-01-29-openclaw-control-ui-websocket.md)<br>  <sub>OpenClaw Control UI WebSocket hijack RCE</sub>
- `2026-02-28` [CodeWall breaches McKinsey's internal "Lilli" AI platform](../2026-02/2026-02-28-codewall-breaches-mckinsey-lilli.md)<br>  <sub>CodeWall breaches McKinsey's internal "Lilli" AI platform</sub>

---

[← 2025-11 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-11/2025-11-01-shadowray-2-ray-framework.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
