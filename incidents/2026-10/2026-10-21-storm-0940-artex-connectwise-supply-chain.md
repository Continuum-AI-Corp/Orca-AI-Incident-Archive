---
id: 2026-10-21-storm-0940-artex-connectwise-supply-chain
title: "Microsoft ties the ConnectWise supply-chain compromise to Storm-0940 driving attacks with the ARTEX agentic AI framework"
title_zh: "微软将 ConnectWise 供应链入侵归因于用 ARTEX agentic AI 框架驱动攻击的 Storm-0940"
title_ja: "MicrosoftがConnectWiseサプライチェーン侵害を、ARTEX agentic AIフレームワークで攻撃を駆動したStorm-0940に帰属"
title_ko: "마이크로소프트, ConnectWise 공급망 침해를 ARTEX agentic AI 프레임워크로 공격을 구동한 Storm-0940에 귀속"
title_de: "Microsoft führt die ConnectWise-Lieferketten-Kompromittierung auf Storm-0940 zurück, das Angriffe mit dem agentischen KI-Framework ARTEX steuert"
title_fr: "Microsoft attribue la compromission de la chaîne d'approvisionnement ConnectWise à Storm-0940, qui pilote ses attaques avec le cadre d'IA agentique ARTEX"
title_es: "Microsoft atribuye la brecha en la cadena de suministro de ConnectWise a Storm-0940, que impulsa sus ataques con el marco de IA agéntica ARTEX"
date: 2026-10-21
date_raw: "2026-10-21 (Microsoft Threat Intelligence); related password-spray campaign 2026-10-10 to 2026-10-14"
date_precision: day

kind: incident
type: [WEAPON, SUPPLY]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **On 21 October 2026 Microsoft Threat Intelligence attributed the **ConnectWise supply-chain compromise** to **Storm-0940** (a China state-aligned actor) and said the group used the **ARTEX agentic AI penetration-testing framework** to automate attacks against hundreds of organizations worldwide.** Abusing a compromised ConnectWise multi-tenant application already granted access, Storm-0940 authenticated into Microsoft 365 environments **without interactive sign-in (so MFA did not apply)** — ARTEX-driven activity reached **2,250+ tenants at up to 2,900 sign-in attempts per minute**. Microsoft says most targeting failed, **but the group gained privileged cloud access at several organizations, in some cases within three hours**: in affected tenants the agents moved beyond authentication into **Microsoft Graph and directory operations** — reconnaissance, **changing application credentials for persistence, altering identities, groups and privileged roles, bulk-reading secrets across multiple Azure Key Vaults**, and one ConnectWise application **self-assigned the Global Administrator role**. Microsoft did not confirm data exfiltration in this campaign. A related, largely-unsuccessful password-spray run (10–14 Oct) hit 327 accounts across 8 orgs with 151,000+ failed logons. Recorded `incident` / `WEAPON` + `SUPPLY` / `critical` / `real_harm: true`, `landmark` — the first Microsoft-attributed nation-state campaign driving a supply-chain compromise at scale with an agentic-AI framework.

summary_zh: |
  **2026 年 10 月 21 日，微软威胁情报将 **ConnectWise 供应链入侵**归因于 **Storm-0940**（中国国家关联行为体），并称该组织用 **ARTEX agentic AI 渗透测试框架**自动化攻击全球数百家组织。** Storm-0940 滥用一个已获授权的 ConnectWise 多租户应用的受损凭证，**无需交互式登录（故 MFA 不适用）**即认证进入 Microsoft 365 环境——ARTEX 驱动的活动触达 **2,250+ 个租户、最高 2,900 次/分钟登录尝试**。微软称多数攻击未得手，**但在若干组织中拿到了特权云访问，有的在三小时内**：在受影响租户里，agent 越过认证进入 **Microsoft Graph 与目录操作**——侦察、**改应用凭证做持久化、改身份/组/特权角色、批量读取多个 Azure Key Vault 的密钥**，且有一个 ConnectWise 应用**自赋全局管理员角色**。微软未确认此役中发生数据外带。相关的一次（基本失败的）密码喷洒（10-10 至 10-14）打了 8 家组织的 327 个账户、15.1 万+ 次失败登录。记为 `incident` / `WEAPON` + `SUPPLY` / `critical` / `real_harm: true`、`landmark`——首个微软归因的、用 agentic-AI 框架规模化驱动供应链入侵的国家级行动。

summary_ja: |
  **2026年10月21日、Microsoft Threat Intelligenceは**ConnectWiseサプライチェーン侵害**を**Storm-0940**（中国国家連携のアクター）に帰属させ、同グループが**ARTEX agentic AIペネトレーションテストフレームワーク**を用いて世界中の数百の組織への攻撃を自動化したと述べた。** 既にアクセスを付与されていたConnectWiseのマルチテナントアプリの侵害済み資格情報を悪用し、Storm-0940は**対話的サインインなし（したがってMFAは適用されず）**でMicrosoft 365環境に認証した——ARTEX駆動の活動は**2,250以上のテナント、最大で毎分2,900回のサインイン試行**に達した。Microsoftは大半は失敗したとしつつ、**複数の組織で特権的なクラウドアクセスを取得、場合によっては3時間以内**とした：影響を受けたテナントでは、エージェントが認証を越えて**Microsoft Graphとディレクトリ操作**に進み——偵察、**永続化のためのアプリ資格情報変更、ID・グループ・特権ロールの改変、複数のAzure Key Vaultからの秘密の一括読み取り**を行い、あるConnectWiseアプリは**グローバル管理者ロールを自己付与**した。本キャンペーンでのデータ持ち出しは未確認。関連する（ほぼ失敗した）パスワードスプレー（10/10–14）は8組織327アカウントに15.1万回超の失敗ログオン。`incident` / `WEAPON` + `SUPPLY` / `critical` / `real_harm: true`、`landmark`

summary_ko: |
  **2026년 10월 21일, 마이크로소프트 위협 인텔리전스는 **ConnectWise 공급망 침해**를 **Storm-0940**(중국 국가 연계 행위자)에 귀속시키고, 이 그룹이 **ARTEX agentic AI 침투 테스트 프레임워크**로 전 세계 수백 개 조직 공격을 자동화했다고 밝혔다.** 이미 접근 권한이 부여된 ConnectWise 멀티테넌트 앱의 침해된 자격 증명을 악용해 Storm-0940은 **대화형 로그인 없이(따라서 MFA 미적용)** Microsoft 365 환경에 인증했다——ARTEX 구동 활동은 **2,250개 이상 테넌트, 분당 최대 2,900회 로그인 시도**에 달했다. 마이크로소프트는 대부분 실패했다면서도 **여러 조직에서 특권 클라우드 접근을 획득, 일부는 3시간 이내**라고 했다: 영향받은 테넌트에서 에이전트는 인증을 넘어 **Microsoft Graph와 디렉터리 작업**으로 나아가——정찰, **지속성을 위한 앱 자격 증명 변경, 신원·그룹·특권 역할 변경, 여러 Azure Key Vault의 비밀 대량 읽기**를 했고, 한 ConnectWise 앱은 **전역 관리자 역할을 자가 부여**했다. 이번 캠페인에서 데이터 유출은 미확인. 관련된 (대체로 실패한) 패스워드 스프레이(10/10–14)는 8개 조직 327개 계정에 15.1만여 회 실패 로그온. `incident` / `WEAPON` + `SUPPLY` / `critical` / `real_harm: true`, `landmark`

summary_de: |
  **Am 21. Oktober 2026 führte Microsoft Threat Intelligence die **ConnectWise-Lieferketten-Kompromittierung** auf **Storm-0940** (ein China-staatlich ausgerichteter Akteur) zurück und erklärte, die Gruppe habe das **agentische KI-Penetrationstest-Framework ARTEX** genutzt, um Angriffe auf Hunderte Organisationen weltweit zu automatisieren.** Unter Missbrauch der kompromittierten Zugangsdaten einer bereits berechtigten ConnectWise-Mandantenanwendung authentifizierte sich Storm-0940 **ohne interaktive Anmeldung (MFA griff daher nicht)** in Microsoft-365-Umgebungen — die ARTEX-gesteuerte Aktivität erreichte **2.250+ Mandanten bei bis zu 2.900 Anmeldeversuchen pro Minute**. Microsoft sagt, das meiste Targeting scheiterte, **doch die Gruppe erlangte in mehreren Organisationen privilegierten Cloud-Zugriff, teils binnen drei Stunden**: in betroffenen Mandanten gingen die Agenten über die Authentifizierung hinaus in **Microsoft Graph und Verzeichnisoperationen** — Aufklärung, **Ändern von Anwendungs-Anmeldedaten zur Persistenz, Ändern von Identitäten, Gruppen und privilegierten Rollen, Massenauslesen von Secrets aus mehreren Azure Key Vaults**, und eine ConnectWise-Anwendung **wies sich selbst die Rolle Globaler Administrator zu**. Eine Datenexfiltration in dieser Kampagne bestätigte Microsoft nicht. Ein verwandter (weitgehend erfolgloser) Password-Spray-Lauf (10.–14. Okt.) traf 327 Konten in 8 Orgs mit 151.000+ fehlgeschlagenen Anmeldungen. `incident` / `WEAPON` + `SUPPLY` / `critical` / `real_harm: true`, `landmark`

summary_fr: |
  **Le 21 octobre 2026, Microsoft Threat Intelligence a attribué la **compromission de la chaîne d'approvisionnement ConnectWise** à **Storm-0940** (acteur aligné sur l'État chinois) et a indiqué que le groupe avait utilisé le **cadre d'IA agentique de test d'intrusion ARTEX** pour automatiser des attaques contre des centaines d'organisations dans le monde.** En abusant des identifiants compromis d'une application multi-tenant ConnectWise déjà autorisée, Storm-0940 s'est authentifié dans des environnements Microsoft 365 **sans connexion interactive (la MFA ne s'appliquait donc pas)** — l'activité pilotée par ARTEX a atteint **plus de 2 250 tenants à jusqu'à 2 900 tentatives de connexion par minute**. Microsoft indique que la plupart des ciblages ont échoué, **mais le groupe a obtenu un accès cloud privilégié dans plusieurs organisations, parfois en moins de trois heures** : dans les tenants touchés, les agents sont allés au-delà de l'authentification vers **Microsoft Graph et des opérations d'annuaire** — reconnaissance, **modification d'identifiants d'application pour la persistance, modification d'identités, de groupes et de rôles privilégiés, lecture en masse de secrets dans plusieurs Azure Key Vaults**, et une application ConnectWise **s'est auto-attribué le rôle d'administrateur général**. Microsoft n'a pas confirmé d'exfiltration de données dans cette campagne. Une campagne de password-spray connexe (10–14 oct.), largement infructueuse, a visé 327 comptes dans 8 organisations avec plus de 151 000 échecs de connexion. `incident` / `WEAPON` + `SUPPLY` / `critical` / `real_harm: true`, `landmark`

summary_es: |
  **El 21 de octubre de 2026, Microsoft Threat Intelligence atribuyó la **brecha en la cadena de suministro de ConnectWise** a **Storm-0940** (actor alineado con el Estado chino) y dijo que el grupo usó el **marco de IA agéntica de pruebas de penetración ARTEX** para automatizar ataques contra cientos de organizaciones en el mundo.** Abusando de las credenciales comprometidas de una aplicación multiinquilino de ConnectWise ya autorizada, Storm-0940 se autenticó en entornos de Microsoft 365 **sin inicio de sesión interactivo (por lo que la MFA no aplicaba)** — la actividad impulsada por ARTEX alcanzó **más de 2.250 inquilinos con hasta 2.900 intentos de inicio de sesión por minuto**. Microsoft dice que la mayoría de los ataques fracasó, **pero el grupo obtuvo acceso privilegiado a la nube en varias organizaciones, en algunos casos en menos de tres horas**: en los inquilinos afectados, los agentes fueron más allá de la autenticación hacia **Microsoft Graph y operaciones de directorio** — reconocimiento, **cambio de credenciales de aplicación para persistencia, alteración de identidades, grupos y roles privilegiados, lectura masiva de secretos en varios Azure Key Vaults**, y una aplicación de ConnectWise **se autoasignó el rol de Administrador Global**. Microsoft no confirmó exfiltración de datos en esta campaña. Una campaña de password-spray relacionada (10–14 oct.), en gran parte fallida, afectó a 327 cuentas en 8 organizaciones con más de 151.000 inicios de sesión fallidos. `incident` / `WEAPON` + `SUPPLY` / `critical` / `real_harm: true`, `landmark`

sources:
  - url: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/
    label: Microsoft Threat Intelligence
  - url: https://cyberscoop.com/microsoft-attributes-connectwise-supply-chain-attack-china-storm-0940/
    label: CyberScoop
  - url: https://brandefense.io/security-news/storm-0940-artex-connectwise-supply-chain-attack/
    label: Brandefense
disputed: false
landmark: true
scan_month: 2026-10
scan_ref: "SCAN.md §13.32"
---

# Microsoft ties the ConnectWise supply-chain compromise to Storm-0940 driving attacks with the ARTEX agentic AI framework

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-8F6A3C?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-3C6E8F?style=flat-square)

## Summary

**On 21 October 2026 Microsoft Threat Intelligence attributed the ConnectWise supply-chain compromise to Storm-0940 (a China state-aligned actor) and said the group used the ARTEX agentic AI penetration-testing framework to automate attacks against hundreds of organizations worldwide.** Abusing a compromised ConnectWise multi-tenant application already granted access, Storm-0940 authenticated into Microsoft 365 environments without interactive sign-in (so MFA did not apply) — ARTEX-driven activity reached 2,250+ tenants at up to 2,900 sign-in attempts per minute. Microsoft says most targeting failed, but the group gained privileged cloud access at several organizations, in some cases within three hours: in affected tenants the agents moved beyond authentication into Microsoft Graph and directory operations — reconnaissance, changing application credentials for persistence, altering identities, groups and privileged roles, bulk-reading secrets across multiple Azure Key Vaults, and one ConnectWise application self-assigned the Global Administrator role. Microsoft did not confirm data exfiltration in this campaign. A related, largely-unsuccessful password-spray run (10–14 Oct) hit 327 accounts across 8 orgs with 151,000+ failed logons. Recorded `incident` / `WEAPON` + `SUPPLY` / `critical` / `real_harm: true`, `landmark` — the first Microsoft-attributed nation-state campaign driving a supply-chain compromise at scale with an agentic-AI framework.

## Attack chain

```mermaid
flowchart LR
    E["Storm-0940 abuses a compromised ConnectWise<br/>multi-tenant app (already granted access)"]:::entry
    S1["ARTEX agentic framework automates sign-ins:<br/>2,250+ tenants, ~2,900/min, no interactive login (MFA N/A)"]:::step
    S2["In some tenants: Microsoft Graph + directory ops —<br/>persistence, privileged roles, Key Vault secret reads"]:::step
    I["Privileged cloud access at several orgs (some <3h);<br/>one app self-assigned Global Administrator"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The attribution.** On **21 October 2026**, Microsoft Threat Intelligence published a blog assessing that **Storm-0940** — a **China state-aligned** actor active since 2021 — was responsible for the recently-disclosed **ConnectWise supply-chain compromise** of a multi-tenant application, and that the group used the **ARTEX agentic AI penetration-testing framework** to automate the campaign against hundreds of organizations globally. (Microsoft frames the attribution as an assessment, and says the activity did not stem from any compromise of Microsoft's own systems, products or services.)

**How it worked.** Storm-0940 used compromised application credentials from the ConnectWise app — which customers had **already granted access** — to authenticate into Microsoft 365 environments **through that application, without an interactive user sign-in, so MFA did not apply**. ARTEX automated scanning, **OAuth-application abuse** and password spraying. The ConnectWise-linked activity involved attempted sign-ins to **more than 2,250 tenants at up to 2,900 attempts per minute**.

**What was actually achieved.** Microsoft says most targeting was unsuccessful, **but Storm-0940 gained privileged cloud access at several organizations, in some cases within three hours of initial targeting**. In affected tenants the AI-driven activity went **beyond authentication into Microsoft Graph and directory operations**: reconnaissance, **modifying application credentials to establish persistence**, and **changing identities, groups and privileged roles**. Microsoft's detection guidance also lists **bulk reads of secrets across multiple Azure Key Vaults** (with key enumeration and an unwrap operation), and notes that one ConnectWise application **self-assigned the Global Administrator role**. Microsoft did **not** confirm whether data was accessed or exfiltrated in this campaign. Separately, a largely-unsuccessful **password-spray** campaign (**10–14 October**) targeted 327 accounts across 8 organizations with 151,000+ failed logons and no observed successful authentication.

**How it is graded.** `incident` — a real, in-the-wild campaign. `WEAPON` (an agentic AI framework, ARTEX, drives the intrusion) + `SUPPLY` (the entry is a compromised ConnectWise multi-tenant application, a supply-chain vector). `real_harm: true`: beyond "attempts," Microsoft confirms **privileged cloud access, persistence changes, privileged-role changes, a self-assigned Global Administrator, and bulk Key Vault secret reads at real victim organizations** — even though data exfiltration is not confirmed. Severity `critical`: nation-state actor, agentic-AI automation at machine speed, confirmed privileged access/persistence/secret-reads across real tenants via a supply-chain vector that bypassed MFA. `landmark: true`: the first Microsoft-attributed nation-state campaign using an **agentic-AI framework** to drive a supply-chain compromise at this scale. Confidence `A`: Microsoft Threat Intelligence's own report, with independent reporting (CyberScoop, Brandefense). Dated to the 21 October Microsoft disclosure.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Microsoft Threat Intelligence | <https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/> |
| 2 | CyberScoop | <https://cyberscoop.com/microsoft-attributes-connectwise-supply-chain-attack-china-storm-0940/> |
| 3 | Brandefense | <https://brandefense.io/security-news/storm-0940-artex-connectwise-supply-chain-attack/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-10-21` (raw: 2026-10-21 Microsoft Threat Intelligence; related password-spray 2026-10-10 to 2026-10-14, precision `day`) |
| Kind | Real incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) [`SUPPLY`](../../taxonomy/types.md#supply) |
| Severity | **Critical** `critical` |
| Confidence | **A** — Microsoft Threat Intelligence report + independent reporting |
| Real harm | Yes — privileged cloud access, persistence, privileged-role changes, Global Admin self-assignment and Key Vault secret reads at several real organizations |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-10-21-storm-0940-artex-connectwise-supply-chain` |

<sub>**Why this classification:** A nation-state campaign (Storm-0940) driving a ConnectWise supply-chain compromise with the ARTEX agentic AI framework (`WEAPON` — AI as the attack driver; `SUPPLY` — compromised multi-tenant app vector). `incident` with `real_harm: true` because Microsoft confirms privileged cloud access, persistence, privileged-role changes and Key Vault secret reads at real orgs (data exfiltration not confirmed). `critical` for the scale, machine-speed automation and confirmed privileged access via an MFA-bypassing supply-chain vector. `landmark` as the first Microsoft-attributed nation-state agentic-AI-driven supply-chain compromise at scale. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI](../../topics/offensive-ai.md)

**Related records:**

- `2026-10-06` [ARTEX AI used against South Korean banks](2026-10-06-artex-ai-south-korea-banks.md)<br>  <sub>The same ARTEX agentic framework in a different campaign</sub>
- `2026-07-30` [Unit 42: Chinese-speaking autonomous offensive campaigns](../2026-07/2026-07-30-unit42-chinese-speaking-autonomous-campaigns.md)<br>  <sub>Earlier nation-state-adjacent agentic offensive operations</sub>
- `2026-10-21` [LiteLLM 1.107.0 supply-chain compromise](2026-10-21-litellm-1-107-supply-chain-compromise.md)<br>  <sub>Another agent-ecosystem supply-chain compromise the same day</sub>

---

[← 2026-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-10/2026-10-21-storm-0940-artex-connectwise-supply-chain.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
