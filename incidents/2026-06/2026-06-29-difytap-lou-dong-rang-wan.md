---
id: 2026-06-29-difytap-lou-dong-rang-wan
title: "DifyTap: four flaws leave 1M+ AI apps open to cross-tenant eavesdropping"
title_zh: "DifyTap：4 个漏洞让 100 万+ AI 应用被跨租户窃听"
title_ja: "DifyTap：4つの欠陥で100万以上のAIアプリがテナント間盗聴にさらされる"
title_ko: "DifyTap: 결함 4건으로 100만 개 이상의 AI 앱이 교차 테넌트 도청에 노출"
title_de: "DifyTap: vier Schwachstellen öffnen 1M+ KI-Apps für mandantenübergreifendes Mithören"
title_fr: "DifyTap : quatre failles exposent plus d'un million d'applications IA à l'écoute entre locataires"
title_es: "DifyTap: cuatro fallos dejan más de 1M de aplicaciones de IA expuestas a escuchas entre inquilinos"
date: 2026-06-29
date_precision: day
date_raw: "2026-06-29"

kind: vulnerability
type: [INFRA]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Found by Zafran. **CVE-2026-41947 (CVSS 9.1)**: the **tracing system in Dify < 1.14.2 lacks tenant-ownership validation** — an authenticated editor user can set and enable a tracing configuration for **any application**, **redirecting all of the victim app's messages and responses to an attacker-controlled LLM tracing provider** and creating a persistent exfiltration channel. Along with **CVE-2026-41948 (CVSS 9.4)** and others, four in total.
  Amplifying factor: **Dify Cloud allows unauthenticated free self-registration**, so creating an attacker account has no barrier at all. Fixed in 1.14.2


summary_zh: |
  Zafran 发现。**CVE-2026-41947（CVSS 9.1）**：Dify < 1.14.2 的 **tracing 系统缺少租户归属校验** —— 已认证的 editor 用户可以给**任意应用**设置并启用追踪配置，**把受害应用的全部消息与响应重定向到攻击者控制的 LLM 追踪提供方**，形成一条持久的外带通道。配套 **CVE-2026-41948（CVSS 9.4）** 等共 4 个。
  放大因素：**Dify Cloud 允许未认证免费自助注册**，攻击者建号毫无门槛。1.14.2 修复

summary_ja: |
  Zafranが発見。**CVE-2026-41947（CVSS 9.1）**：**Dify < 1.14.2のトレーシングシステムにテナント所有権の検証がない**——認証済みのエディタユーザーが**任意のアプリケーション**にトレーシング設定を行って有効化でき、**被害アプリのメッセージと応答のすべてを攻撃者制御のLLMトレーシングプロバイダーへ転送**し、永続的な外部送信チャネルを築ける。**CVE-2026-41948（CVSS 9.4）**などと合わせて計4件。
  増幅要因：**Dify Cloudは認証不要の無料セルフ登録を許可している**ため、攻撃者アカウントの作成に障壁がまったくない。1.14.2で修正

summary_ko: |
  Zafran이 발견했다. **CVE-2026-41947(CVSS 9.1)**: **Dify < 1.14.2의 트레이싱 시스템이 테넌트 소유권 검증을 하지 않아**, 인증된 편집자 사용자가 **어떤 애플리케이션에든** 트레이싱 설정을 지정·활성화할 수 있고, **피해 앱의 모든 메시지와 응답을 공격자가 제어하는 LLM 트레이싱 제공자로 돌려** 지속적인 유출 채널을 만든다. **CVE-2026-41948(CVSS 9.4)** 등과 함께 총 4건이다.
  증폭 요인: **Dify Cloud가 무인증 무료 셀프 가입을 허용**하므로 공격자 계정 생성에 아무 장벽이 없다. 1.14.2에서 수정

summary_de: |
  Gefunden von Zafran. **CVE-2026-41947 (CVSS 9.1)**: Das **Tracing-System in Dify < 1.14.2 entbehrt der Validierung der Mandantenzugehörigkeit** — ein authentifizierter Editor-Nutzer kann eine Tracing-Konfiguration für **jede beliebige Anwendung** setzen und aktivieren und damit **alle Nachrichten und Antworten der Opfer-App an einen vom Angreifer kontrollierten LLM-Tracing-Anbieter umleiten** und einen persistenten Exfiltrationskanal schaffen. Zusammen mit **CVE-2026-41948 (CVSS 9.4)** und weiteren sind es insgesamt vier.
  Verstärkender Faktor: **Dify Cloud erlaubt die unauthentifizierte kostenlose Selbstregistrierung**, das Anlegen eines Angreiferkontos hat also keinerlei Hürde. Behoben in 1.14.2

summary_fr: |
  Trouvé par Zafran. **CVE-2026-41947 (CVSS 9.1)** : le **système de traçage de Dify < 1.14.2 ne valide pas la propriété du locataire** — un utilisateur éditeur authentifié peut définir et activer une configuration de traçage pour **n'importe quelle application**, **redirigeant tous les messages et réponses de l'application victime vers un fournisseur de traçage LLM contrôlé par l'attaquant** et créant un canal d'exfiltration persistant. Avec **CVE-2026-41948 (CVSS 9.4)** et d'autres, quatre au total.
  Facteur amplificateur : **Dify Cloud permet l'auto-inscription gratuite non authentifiée**, si bien que créer un compte attaquant n'a aucune barrière. Corrigé en 1.14.2

summary_es: |
  Encontrado por Zafran. **CVE-2026-41947 (CVSS 9.1)**: el **sistema de tracing de Dify < 1.14.2 carece de validación de propiedad del inquilino** — un usuario editor autenticado puede configurar y habilitar una configuración de tracing para **cualquier aplicación**, **redirigiendo todos los mensajes y respuestas de la app víctima a un proveedor de tracing LLM controlado por el atacante** y creando un canal de exfiltración persistente. Junto con **CVE-2026-41948 (CVSS 9.4)** y otros, cuatro en total.
  Factor que amplifica: **Dify Cloud permite el autorregistro gratuito sin autenticación**, así que crear una cuenta de atacante no tiene ninguna barrera. Corregido en 1.14.2

sources:
  - url: https://www.securityweek.com/data-exposure-flaws-threaten-dify-ai-platform-powering-over-1-million-apps/
    label: SecurityWeek
  - url: https://securityaffairs.com/194081/hacking/difytap-four-bugs-put-over-1-million-ai-apps-at-risk.html
    label: Security Affairs

disputed: false
landmark: true
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# DifyTap: four flaws leave 1M+ AI apps open to cross-tenant eavesdropping

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

Found by Zafran. **CVE-2026-41947 (CVSS 9.1)**: the **tracing system in Dify < 1.14.2 lacks tenant-ownership validation** — an authenticated editor user can set and enable a tracing configuration for **any application**, **redirecting all of the victim app's messages and responses to an attacker-controlled LLM tracing provider** and creating a persistent exfiltration channel. Along with **CVE-2026-41948 (CVSS 9.4)** and others, four in total.

Amplifying factor: **Dify Cloud allows unauthenticated free self-registration**, so creating an attacker account has no barrier at all. Fixed in 1.14.2

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
| 1 | SecurityWeek | <https://www.securityweek.com/data-exposure-flaws-threaten-dify-ai-platform-powering-over-1-million-apps/> |
| 2 | Security Affairs | <https://securityaffairs.com/194081/hacking/difytap-four-bugs-put-over-1-million-ai-apps-at-risk.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-29` (raw: 2026-06-29, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-29-difytap-lou-dong-rang-wan` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-06-08` [LiteLLM CVE-2026-42271 MCP endpoint takeover](2026-06-08-litellm-mcp-duan-dian-jie.md)<br>  <sub>LiteLLM CVE-2026-42271 MCP endpoint takeover</sub>
- `2026-06-28` [Langflow CVE-2026-33017 used for Monero mining](2026-06-28-langflow-yong-yu-men-luo.md)<br>  <sub>Langflow CVE-2026-33017 used for Monero mining</sub>
- `2026-06-17` [Vertex AI SDK bucket takeover leads to cross-tenant RCE](2026-06-17-vertex-sdk-rce.md)<br>  <sub>Vertex AI SDK bucket takeover leads to cross-tenant RCE</sub>
- `2026-06-18` [AutoJack: one web page from AutoGen Studio to the host](2026-06-18-autojack-autogen-studio.md)<br>  <sub>AutoJack: one web page from AutoGen Studio to the host</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-29-difytap-lou-dong-rang-wan.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
