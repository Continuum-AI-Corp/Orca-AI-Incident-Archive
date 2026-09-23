---
id: 2026-07-31-exposed-by-design-mcp-servers
title: "Exposed by Design: a dynamic audit of 414 internet-facing MCP servers finds 68 vulnerabilities"
title_zh: "《Exposed by Design》：对 414 个公网 MCP 服务器的动态审计发现 68 个漏洞"
title_ja: "「Exposed by Design」：インターネット公開MCPサーバー414台の動的監査で脆弱性68件"
title_ko: "'Exposed by Design': 인터넷에 노출된 MCP 서버 414대 동적 감사에서 취약점 68건 발견"
title_de: "Exposed by Design: Dynamisches Audit von 414 öffentlich erreichbaren MCP-Servern findet 68 Schwachstellen"
title_fr: "Exposed by Design : un audit dynamique de 414 serveurs MCP exposés sur Internet révèle 68 vulnérabilités"
title_es: "Exposed by Design: una auditoría dinámica de 414 servidores MCP expuestos en internet halla 68 vulnerabilidades"
date: 2026-07-31
date_raw: "2026-07-31"
date_precision: day

kind: research
type: [MCP, INFRA]
severity: medium
confidence: B
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **Nicolás Padilla** posts **Exposed by Design** (arXiv 2608.00150), which the author describes as the first dynamic behavioural security assessment of internet-facing **MCP servers**. Servers were discovered across eleven sources — among them GitHub, npm, PyPI, Smithery, Hugging Face, Shodan, Censys and FOFA — and then tested live with **Corvus**, a purpose-built framework of 34 test modules covering 10 MCP-specific vulnerability classes. Over four measurement runs in July 2026 the study confirmed **640 production servers**, dynamically audited **414** and found **68 reportable vulnerabilities**, including SQL injection, SSRF against cloud metadata services, prompt-template injection and path traversal. **91.8% of the audited servers lack OAuth authentication**, **687 tool instances expose shell execution without access controls**, and **41.6% of confirmed servers disappeared within three days** between runs. Corvus is released as open source; no in-the-wild exploitation is claimed

summary_zh: |
  **Nicolás Padilla** 在 arXiv 发布《**Exposed by Design**》（2608.00150），作者称这是首个针对公网 **MCP 服务器**的动态行为安全评估。研究先从 GitHub、npm、PyPI、Smithery、Hugging Face、Shodan、Censys、FOFA 等十一个来源发现服务器，再用自研框架 **Corvus**（34 个测试模块，覆盖 10 类 MCP 特有漏洞）做实时测试。在 2026 年 7 月的四轮测量中，研究确认了 **640 个生产环境服务器**，对其中 **414 个**做了动态审计，发现 **68 个可报告的漏洞**，包括 SQL 注入、针对云元数据服务的 SSRF、提示模板注入和路径遍历。**受审计服务器中 91.8% 没有 OAuth 认证**，**687 个工具实例在没有访问控制的情况下暴露 shell 执行能力**，**41.6% 的已确认服务器在两轮测量之间的三天内就已消失**。Corvus 已开源；论文未声称存在在野利用

summary_ja: |
  **Nicolás Padilla**氏がarXivで「**Exposed by Design**」（2608.00150）を公開した。著者はこれを、インターネットに公開された**MCPサーバー**を対象とする初の動的・挙動ベースのセキュリティ評価だとしている。GitHub、npm、PyPI、Smithery、Hugging Face、Shodan、Censys、FOFAなど11の情報源からサーバーを発見し、専用フレームワーク**Corvus**（MCP固有の脆弱性10分類をカバーする34のテストモジュール）で実際に試験した。2026年7月の4回の測定で**本番稼働サーバー640台**を確認し、うち**414台**を動的に監査、SQLインジェクション、クラウドのメタデータサービスを狙うSSRF、プロンプトテンプレート注入、パストラバーサルなど**報告対象の脆弱性68件**を見つけた。**監査したサーバーの91.8%はOAuth認証を持たず**、**687のツールインスタンスがアクセス制御なしでシェル実行を公開**し、**確認済みサーバーの41.6%は測定の間の3日以内に消えていた**。Corvusはオープンソースで公開。実環境での悪用は主張されていない

summary_ko: |
  **Nicolás Padilla**가 arXiv에 '**Exposed by Design**'(2608.00150)을 공개했다. 저자는 이를 인터넷에 노출된 **MCP 서버**에 대한 최초의 동적·행위 기반 보안 평가라고 설명한다. GitHub, npm, PyPI, Smithery, Hugging Face, Shodan, Censys, FOFA 등 11개 출처에서 서버를 찾아낸 뒤, MCP 고유 취약점 10개 유형을 다루는 34개 테스트 모듈로 된 전용 프레임워크 **Corvus**로 실제 테스트했다. 2026년 7월 네 차례 측정에서 **운영 중인 서버 640대**를 확인하고 그중 **414대**를 동적으로 감사해 SQL 인젝션, 클라우드 메타데이터 서비스를 노리는 SSRF, 프롬프트 템플릿 주입, 경로 탐색 등 **보고 가능한 취약점 68건**을 찾았다. **감사한 서버의 91.8%는 OAuth 인증이 없고**, **687개 도구 인스턴스가 접근 통제 없이 셸 실행 기능을 노출**했으며, **확인된 서버의 41.6%는 측정 사이 사흘 안에 사라졌다**. Corvus는 오픈소스로 공개됐고, 실제 환경에서의 악용은 주장되지 않았다

summary_de: |
  **Nicolás Padilla** veröffentlicht auf arXiv **Exposed by Design** (2608.00150), nach Angaben des Autors die erste dynamische, verhaltensbasierte Sicherheitsbewertung öffentlich erreichbarer **MCP-Server**. Die Server wurden über elf Quellen gefunden – darunter GitHub, npm, PyPI, Smithery, Hugging Face, Shodan, Censys und FOFA – und anschließend live mit **Corvus** getestet, einem eigens entwickelten Framework aus 34 Testmodulen für 10 MCP-spezifische Schwachstellenklassen. In vier Messläufen im Juli 2026 bestätigte die Studie **640 produktive Server**, prüfte **414** dynamisch und fand **68 meldefähige Schwachstellen**, darunter SQL-Injection, SSRF gegen Cloud-Metadatendienste, Prompt-Template-Injection und Path Traversal. **91,8 % der geprüften Server haben keine OAuth-Authentifizierung**, **687 Tool-Instanzen bieten Shell-Ausführung ohne Zugriffskontrolle an**, und **41,6 % der bestätigten Server verschwanden binnen drei Tagen** zwischen zwei Läufen. Corvus ist Open Source; eine Ausnutzung in freier Wildbahn wird nicht behauptet

summary_fr: |
  **Nicolás Padilla** publie sur arXiv **Exposed by Design** (2608.00150), que l'auteur présente comme la première évaluation de sécurité dynamique et comportementale des **serveurs MCP** exposés sur Internet. Les serveurs ont été découverts via onze sources — dont GitHub, npm, PyPI, Smithery, Hugging Face, Shodan, Censys et FOFA — puis testés en conditions réelles avec **Corvus**, un framework dédié de 34 modules couvrant 10 classes de vulnérabilités propres à MCP. Sur quatre campagnes de mesure en juillet 2026, l'étude a confirmé **640 serveurs en production**, en a audité dynamiquement **414** et a trouvé **68 vulnérabilités signalables**, dont des injections SQL, des SSRF visant les services de métadonnées cloud, des injections de modèles de prompt et des traversées de répertoires. **91,8 % des serveurs audités n'ont pas d'authentification OAuth**, **687 instances d'outils exposent l'exécution de commandes shell sans contrôle d'accès**, et **41,6 % des serveurs confirmés ont disparu en moins de trois jours** entre deux campagnes. Corvus est publié en open source ; aucune exploitation dans la nature n'est revendiquée

summary_es: |
  **Nicolás Padilla** publica en arXiv **Exposed by Design** (2608.00150), que el autor describe como la primera evaluación de seguridad dinámica y de comportamiento de **servidores MCP** expuestos en internet. Los servidores se descubrieron a partir de once fuentes —entre ellas GitHub, npm, PyPI, Smithery, Hugging Face, Shodan, Censys y FOFA— y luego se probaron en vivo con **Corvus**, un marco propio de 34 módulos de prueba que cubre 10 clases de vulnerabilidades específicas de MCP. En cuatro rondas de medición en julio de 2026 el estudio confirmó **640 servidores en producción**, auditó dinámicamente **414** y halló **68 vulnerabilidades notificables**, entre ellas inyección SQL, SSRF contra servicios de metadatos en la nube, inyección de plantillas de prompt y recorrido de rutas. **El 91,8 % de los servidores auditados carece de autenticación OAuth**, **687 instancias de herramientas exponen ejecución de shell sin control de acceso** y **el 41,6 % de los servidores confirmados desapareció en menos de tres días** entre rondas. Corvus se publica como código abierto; no se afirma explotación real

sources:
  - url: https://arxiv.org/abs/2608.00150
    label: arXiv 2608.00150

disputed: false
landmark: false
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# Exposed by Design: a dynamic audit of 414 internet-facing MCP servers finds 68 vulnerabilities

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

**Nicolás Padilla** posts **Exposed by Design** (arXiv 2608.00150), which the author describes as the first dynamic behavioural security assessment of internet-facing **MCP servers**. Servers were discovered across eleven sources — among them GitHub, npm, PyPI, Smithery, Hugging Face, Shodan, Censys and FOFA — and then tested live with **Corvus**, a purpose-built framework of 34 test modules covering 10 MCP-specific vulnerability classes. Over four measurement runs in July 2026 the study confirmed **640 production servers**, dynamically audited **414** and found **68 reportable vulnerabilities**, including SQL injection, SSRF against cloud metadata services, prompt-template injection and path traversal. **91.8% of the audited servers lack OAuth authentication**, **687 tool instances expose shell execution without access controls**, and **41.6% of confirmed servers disappeared within three days** between runs. Corvus is released as open source; no in-the-wild exploitation is claimed

## Attack chain

```mermaid
flowchart LR
    E["An MCP server deployed to the public internet"]:::entry
    S0["No OAuth, and tools that expose shell execution without access controls"]:::step
    I["SQL injection, SSRF to cloud metadata, path traversal<br/><i>(measurement study, no in-the-wild exploitation claimed)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**Testing behaviour, not reading manifests.** The paper starts from the observation that MCP has, since its November 2024 launch, grown to more than 21,000 server instances detectable on the public internet, and sets out to test what those servers do when they are running — which is why the author calls it a dynamic behavioural assessment. Its method has two halves. Passive discovery draws candidate servers from eleven data sources, from package registries (npm, PyPI) and MCP directories (Smithery) to internet-wide scanners (Shodan, Censys, FOFA). Active testing then runs **Corvus**, a framework the author built for the study and has released as open source, with 34 test modules covering 10 MCP-specific vulnerability classes. Four measurement runs across July 2026 confirmed 640 production servers; 414 of them were audited dynamically, and the audit produced 68 reportable vulnerabilities — SQL injection, SSRF aimed at cloud metadata services, prompt-template injection, and path traversal through cursor manipulation.

**Three numbers worth keeping.** First, **91.8% of the dynamically audited servers lack OAuth authentication** — the control the MCP specification provides for exactly this deployment shape. Second, **687 tool instances across the confirmed servers expose shell execution capabilities without access controls**: a remote party who can reach the server can ask it to run commands. Third, **41.6% of confirmed servers disappeared within three days** between consecutive measurement runs, which the author reads as rapid deployment cycles without security review. That last figure matters for defenders as much as the first two: an inventory of exposed MCP servers ages within days, so a one-off scan understates what is actually reachable at any given moment.

**How to read it.** This is a single-author preprint, not yet peer-reviewed, and its 68 findings carry no CVE identifiers or vendor advisories; the paper reports a responsible-disclosure pipeline for them but no in-the-wild exploitation. It is recorded because the exposure it measures is not hypothetical elsewhere in this archive: an exposed MCP endpoint in nginx-ui was attacked in the wild in April 2026, and an authentication bypass in LiteLLM's MCP endpoint reached CISA's Known Exploited Vulnerabilities catalog in September. The recommendation that follows is unglamorous — put authentication in front of every internet-reachable MCP server, and do not expose shell-capable tools to callers you cannot identify.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | arXiv 2608.00150 | <https://arxiv.org/abs/2608.00150> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-31` (raw: 2026-07-31, precision `day`) |
| Kind | Research demo `research` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain · [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **Medium** `medium` |
| Confidence | **B** — a single-author academic preprint with a checkable method and an open-source tool, but no CVE or vendor advisory to anchor its findings |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-07-31-exposed-by-design-mcp-servers` |

<sub>**Why this classification:** A measurement study with live testing, `real_harm: false`; the record marks when this exposure was quantified. Rated `medium`: a controlled measurement of exposure at scale rather than a demonstrated compromise. Graded `B` because the preprint is not peer-reviewed and none of its findings is anchored by a CVE or vendor advisory. Dated to the arXiv v1 submission (31 July 2026). Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md) · [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-04-16` [MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild](../2026-04/2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br>  <sub>An exposed MCP endpoint that was actually attacked</sub>
- `2026-09-02` [Any bearer token opens LiteLLM's MCP endpoint: CVE-2026-59822 enters CISA KEV](../2026-09/2026-09-02-litellm-mcp-auth-bypass-kev.md)<br>  <sub>An MCP authentication flaw that reached CISA KEV</sub>
- `2025-06-13` [MCP Inspector unauthenticated RCE](../2025-06/2025-06-13-mcp-inspector-rce.md)<br>  <sub>Missing authentication on MCP tooling, a year earlier</sub>
- `2026-08-10` [Deadbugz: an MCP server that turns hostile on the third tool call](../2026-08/2026-08-10-deadbugz-mcp-supply-chain.md)<br>  <sub>Why a one-time review of an MCP server is not enough</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-31-exposed-by-design-mcp-servers.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
