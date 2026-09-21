---
id: 2026-09-02-litellm-mcp-auth-bypass-kev
title: "Any bearer token opens LiteLLM's MCP endpoint: CVE-2026-59822 enters CISA KEV"
title_zh: "任意 Bearer 令牌即可打开 LiteLLM 的 MCP 端点：CVE-2026-59822 进入 CISA KEV"
title_ja: "任意のBearerトークンでLiteLLMのMCPエンドポイントが開く：CVE-2026-59822がCISA KEVに追加"
title_ko: "아무 Bearer 토큰이나 LiteLLM의 MCP 엔드포인트를 연다: CVE-2026-59822, CISA KEV 등재"
title_de: "Jedes beliebige Bearer-Token öffnet den MCP-Endpunkt von LiteLLM: CVE-2026-59822 im CISA-KEV"
title_fr: "N'importe quel jeton Bearer ouvre le point de terminaison MCP de LiteLLM : CVE-2026-59822 entre au KEV de la CISA"
title_es: "Cualquier token Bearer abre el endpoint MCP de LiteLLM: CVE-2026-59822 entra en el KEV de CISA"
date: 2026-09-02
date_raw: "2026-09-02"
date_precision: day

kind: vulnerability
type: [INFRA, MCP]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **CISA adds CVE-2026-59822 to the Known Exploited Vulnerabilities catalog** on 2 September, listing it as "BerriAI LiteLLM Improper Authentication Vulnerability" — one of seven flaws in that day's batch. The bug is in **LiteLLM's MCP Streamable HTTP endpoint**: when validation of a LiteLLM key fails, the OAuth2 passthrough fallback substitutes an **empty `UserAPIKeyAuth()` object instead of rejecting the request**, so any fabricated `Authorization: Bearer` header establishes an authenticated MCP session. From there an unauthenticated attacker can **list and call every configured MCP tool and reach the services behind them** — and LiteLLM is the component that holds the master keys and cloud credentials. All versions before **1.84.0** are affected; **CVSS 4.0 8.8** (CVSS 3.1 scores it 8.2), CWE-287. Federal remediation was due **16 September**. This is the second LiteLLM MCP flaw to reach KEV in 2026, after CVE-2026-42271 in June

summary_zh: |
  **CISA 于 9 月 2 日把 CVE-2026-59822 加入已知被利用漏洞（KEV）目录**，条目名为「BerriAI LiteLLM Improper Authentication Vulnerability」，是当天七个漏洞中的一个。缺陷位于 **LiteLLM 的 MCP Streamable HTTP 端点**：当 LiteLLM 密钥校验失败时，OAuth2 passthrough 回退逻辑**不是拒绝请求，而是塞进一个空的 `UserAPIKeyAuth()` 对象**，于是任意伪造的 `Authorization: Bearer` 头都能建立一个已认证的 MCP 会话。由此，未认证攻击者可以**列出并调用全部已配置的 MCP 工具，并触达其背后的服务**——而 LiteLLM 恰恰是持有主密钥与云凭据的那个组件。**1.84.0** 之前的所有版本受影响；**CVSS 4.0 为 8.8**（CVSS 3.1 记 8.2），CWE-287。联邦机构的修复截止日为 **9 月 16 日**。这是 2026 年第二个进入 KEV 的 LiteLLM MCP 漏洞，前一个是 6 月的 CVE-2026-42271

summary_ja: |
  **CISAは9月2日、CVE-2026-59822を既知の悪用された脆弱性（KEV）カタログに追加**した。登録名は「BerriAI LiteLLM Improper Authentication Vulnerability」で、同日に追加された7件のうちの1件である。欠陥は **LiteLLMのMCP Streamable HTTPエンドポイント**にある。LiteLLMキーの検証に失敗した際、OAuth2パススルーのフォールバックがリクエストを拒否せず、**空の`UserAPIKeyAuth()`オブジェクトで置き換えてしまう**ため、偽造した`Authorization: Bearer`ヘッダーでも認証済みMCPセッションが成立する。これにより未認証の攻撃者は**設定済みのMCPツールをすべて列挙・呼び出し、その背後のサービスにも到達できる**——LiteLLMはまさにマスターキーとクラウド認証情報を保持するコンポーネントである。**1.84.0**より前の全バージョンが影響を受け、**CVSS 4.0で8.8**（CVSS 3.1では8.2）、CWE-287。連邦機関の修正期限は**9月16日**だった。2026年にKEV入りしたLiteLLMのMCP脆弱性としては、6月のCVE-2026-42271に次ぐ2件目である

summary_ko: |
  **CISA가 9월 2일 CVE-2026-59822를 알려진 악용 취약점(KEV) 목록에 추가**했다. 등재명은 "BerriAI LiteLLM Improper Authentication Vulnerability"이며, 그날 추가된 7건 중 하나다. 결함은 **LiteLLM의 MCP Streamable HTTP 엔드포인트**에 있다. LiteLLM 키 검증이 실패하면 OAuth2 패스스루 폴백이 요청을 거부하는 대신 **빈 `UserAPIKeyAuth()` 객체로 대체**해 버려, 위조한 `Authorization: Bearer` 헤더만으로도 인증된 MCP 세션이 성립한다. 이를 통해 비인증 공격자는 **설정된 모든 MCP 도구를 나열·호출하고 그 뒤의 서비스까지 도달**할 수 있다 — LiteLLM은 바로 마스터 키와 클라우드 자격 증명을 보관하는 구성 요소다. **1.84.0** 이전 모든 버전이 영향을 받으며 **CVSS 4.0 기준 8.8**(CVSS 3.1은 8.2), CWE-287. 연방기관 조치 기한은 **9월 16일**이었다. 2026년 KEV에 오른 두 번째 LiteLLM MCP 취약점으로, 앞서 6월에 CVE-2026-42271이 있었다

summary_de: |
  **Die CISA nimmt CVE-2026-59822 am 2. September in den Katalog bekannter ausgenutzter Schwachstellen (KEV) auf**, gelistet als "BerriAI LiteLLM Improper Authentication Vulnerability" — eine von sieben Schwachstellen dieses Tages. Der Fehler steckt im **MCP-Streamable-HTTP-Endpunkt von LiteLLM**: Schlägt die Prüfung eines LiteLLM-Schlüssels fehl, setzt der OAuth2-Passthrough-Fallback **ein leeres `UserAPIKeyAuth()`-Objekt ein, statt die Anfrage abzulehnen**, sodass jeder gefälschte `Authorization: Bearer`-Header eine authentifizierte MCP-Sitzung eröffnet. Ein nicht authentifizierter Angreifer kann damit **sämtliche konfigurierten MCP-Werkzeuge auflisten und aufrufen und die dahinterliegenden Dienste erreichen** — und LiteLLM ist ausgerechnet die Komponente, die Master-Schlüssel und Cloud-Zugangsdaten verwahrt. Betroffen sind alle Versionen vor **1.84.0**; **CVSS 4.0 8.8** (CVSS 3.1: 8.2), CWE-287. Die Frist für Bundesbehörden lief am **16. September** ab. Es ist die zweite LiteLLM-MCP-Schwachstelle im KEV des Jahres 2026 nach CVE-2026-42271 im Juni

summary_fr: |
  **La CISA ajoute CVE-2026-59822 au catalogue des vulnérabilités activement exploitées (KEV) le 2 septembre**, sous l'intitulé « BerriAI LiteLLM Improper Authentication Vulnerability » — l'une des sept failles du lot du jour. Le défaut se situe dans le **point de terminaison MCP Streamable HTTP de LiteLLM** : lorsque la validation d'une clé LiteLLM échoue, le repli OAuth2 passthrough **substitue un objet `UserAPIKeyAuth()` vide au lieu de rejeter la requête**, si bien que n'importe quel en-tête `Authorization: Bearer` fabriqué ouvre une session MCP authentifiée. Un attaquant non authentifié peut alors **énumérer et appeler tous les outils MCP configurés et atteindre les services situés derrière** — or LiteLLM est précisément le composant qui détient les clés maîtresses et les identifiants cloud. Toutes les versions antérieures à **1.84.0** sont concernées ; **CVSS 4.0 8.8** (8.2 en CVSS 3.1), CWE-287. L'échéance de remédiation fédérale était fixée au **16 septembre**. C'est la deuxième faille MCP de LiteLLM à entrer au KEV en 2026, après CVE-2026-42271 en juin

summary_es: |
  **La CISA añade CVE-2026-59822 al catálogo de vulnerabilidades explotadas conocidas (KEV) el 2 de septiembre**, con el título "BerriAI LiteLLM Improper Authentication Vulnerability", una de las siete fallas del lote de ese día. El defecto está en el **endpoint MCP Streamable HTTP de LiteLLM**: cuando falla la validación de una clave de LiteLLM, el mecanismo de reserva de OAuth2 passthrough **sustituye un objeto `UserAPIKeyAuth()` vacío en lugar de rechazar la petición**, de modo que cualquier cabecera `Authorization: Bearer` falsificada abre una sesión MCP autenticada. Desde ahí, un atacante no autenticado puede **enumerar y llamar a todas las herramientas MCP configuradas y alcanzar los servicios que hay detrás**, y LiteLLM es justamente el componente que custodia las claves maestras y las credenciales de nube. Afecta a todas las versiones anteriores a **1.84.0**; **CVSS 4.0 8.8** (8.2 en CVSS 3.1), CWE-287. El plazo federal de remediación venció el **16 de septiembre**. Es la segunda falla MCP de LiteLLM que entra en el KEV en 2026, tras CVE-2026-42271 en junio

sources:
  - url: https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog
    label: CISA
  - url: https://osv.dev/vulnerability/PYSEC-2026-3479
    label: OSV
  - url: https://github.com/BerriAI/litellm/security/advisories/GHSA-7488-6r32-c95q
    label: GitHub Security Advisory
  - url: https://advisories.gitlab.com/pypi/litellm/CVE-2026-59822/
    label: GitLab Advisory Database
  - url: https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html
    label: The Hacker News

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# Any bearer token opens LiteLLM's MCP endpoint: CVE-2026-59822 enters CISA KEV

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square)

## Summary

**CISA adds CVE-2026-59822 to the Known Exploited Vulnerabilities catalog** on 2 September, listing it as "BerriAI LiteLLM Improper Authentication Vulnerability" — one of seven flaws in that day's batch. The bug is in **LiteLLM's MCP Streamable HTTP endpoint**: when validation of a LiteLLM key fails, the OAuth2 passthrough fallback substitutes an **empty `UserAPIKeyAuth()` object instead of rejecting the request**, so any fabricated `Authorization: Bearer` header establishes an authenticated MCP session. From there an unauthenticated attacker can **list and call every configured MCP tool and reach the services behind them** — and LiteLLM is the component that holds the master keys and cloud credentials. All versions before **1.84.0** are affected; **CVSS 4.0 8.8** (CVSS 3.1 scores it 8.2), CWE-287. Federal remediation was due **16 September**. This is the second LiteLLM MCP flaw to reach KEV in 2026, after CVE-2026-42271 in June

## Attack chain

```mermaid
flowchart LR
    E["An internet-reachable LiteLLM proxy"]:::entry
    S0["A fabricated Authorization: Bearer header on the MCP Streamable HTTP endpoint"]:::step
    S1["Failed key validation falls back to an empty UserAPIKeyAuth instead of a rejection"]:::step
    I["Authenticated MCP session: list and call every configured tool, reach the services behind them"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**A fallback that fails open.** LiteLLM is an AI gateway: one endpoint in front of many model providers, which is why it ends up holding the master key and the cloud credentials for everything behind it. Its MCP support exposes a Streamable HTTP endpoint so that agents can discover and call the MCP tools an operator has configured. That endpoint is supposed to require a LiteLLM key. It also supports OAuth2 passthrough, and the handler for that path had the classic fail-open shape: when key validation returned a rejection, the fallback did not stop the request, it replaced the rejected authentication context with **an empty `UserAPIKeyAuth()` object** and carried on. An empty auth object is, for everything downstream, an authenticated one. The practical exploit is a single fabricated header — any string after `Bearer` will do.

**What the session is worth.** MCP is a tool-calling protocol, so an authenticated MCP session is not read access to one API, it is the operator's whole configured tool surface: `tools/list` enumerates what has been wired up, and `tools/call` invokes it with the gateway's own privileges. Whatever an operator connected — repositories, ticketing systems, databases, internal HTTP services — is reachable through the same hole. This is the reason the archive treats gateway CVEs as agent-infrastructure incidents rather than ordinary web bugs: the component compromised is the one deliberately given credentials to everything else.

**Scale and exposure.** BerriAI fixed the fallback gating in **1.84.0** ([PR #26463](https://github.com/BerriAI/litellm/pull/26463), commit `73869f0`); every earlier release is affected. CISA's addition on 2 September set a federal remediation deadline of **16 September**. The scanning service FOFA reported more than 80,000 internet-facing LiteLLM surfaces at the time of the KEV listing — a secondary figure, and one that counts reachable interfaces rather than vulnerable ones, but an indication of the population.

**Not the first, and that is the point.** Some coverage framed this as the first MCP flaw to reach CISA KEV. It is not: **CVE-2026-42271**, a command injection in LiteLLM's *MCP test endpoints*, entered the catalog on [8 June 2026](../2026-06/2026-06-08-litellm-mcp-duan-dian-jie.md) and was chained with BadHost ([CVE-2026-48710](../2026-05/2026-05-28-badhost.md)) into unauthenticated RCE. The same 2 September KEV batch in fact carried CVE-2026-48710 as well. Two separately exploited authentication failures in one gateway's MCP surface inside four months is the finding worth recording, not a first.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | CISA | <https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog> |
| 2 | OSV | <https://osv.dev/vulnerability/PYSEC-2026-3479> |
| 3 | GitHub Security Advisory | <https://github.com/BerriAI/litellm/security/advisories/GHSA-7488-6r32-c95q> |
| 4 | GitLab Advisory Database | <https://advisories.gitlab.com/pypi/litellm/CVE-2026-59822/> |
| 5 | The Hacker News | <https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-02` (raw: 2026-09-02, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure · [`MCP`](../../taxonomy/types.md#mcp) MCP and tool-chain |
| Severity | **High** `high` |
| Confidence | **A** — primary source: CISA, the upstream GitHub Security Advisory and OSV |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-02-litellm-mcp-auth-bypass-kev` |

<sub>**Why this classification:** A vulnerability disclosure, but `real_harm: true` — inclusion in CISA KEV means the agency has confirmed active exploitation in the wild, which is the archive's threshold for a disclosure to count as real damage. Rated `high` rather than `critical`: the flaw is severe and confirmed exploited, but no victim organisation has been named and no campaign has been attributed to it. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-06-08` [LiteLLM CVE-2026-42271 MCP endpoint takeover](../2026-06/2026-06-08-litellm-mcp-duan-dian-jie.md)<br>  <sub>The first LiteLLM MCP flaw to reach CISA KEV, three months earlier</sub>
- `2026-05-28` [BadHost (CVE-2026-48710)](../2026-05/2026-05-28-badhost.md)<br>  <sub>The Starlette header bypass chained with LiteLLM, added to KEV in the same 2 September batch</sub>
- `2026-08-06` [Unauthenticated Langflow RCE added to CISA KEV](../2026-08/2026-08-06-langflow-rce-cisa-kev.md)<br>  <sub>The same pattern in a neighbouring agent platform</sub>
- `2026-09-02` [Langflow CVE-2026-0768: the 12th Langflow flaw exploited in the wild this year](2026-09-02-langflow-jin-di-ye-li.md)<br>  <sub>Disclosed the same day</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-02-litellm-mcp-auth-bypass-kev.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
