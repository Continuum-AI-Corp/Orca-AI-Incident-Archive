---
id: 2026-09-18-crowdsec-tanstack-offboarding-breach
title: "CrowdSec: a nine-minute repository dump, enabled by an offboarding gap"
title_zh: "CrowdSec：一次九分钟的仓库转储——缺口出在离职流程"
title_ja: "CrowdSec：9分間のリポジトリ流出——隙はオフボーディング手続きに"
title_ko: "CrowdSec: 오프보딩 공백이 낳은 9분간의 저장소 탈취"
title_de: "CrowdSec: Ein neunminütiger Repository-Abzug – ermöglicht durch eine Offboarding-Lücke"
title_fr: "CrowdSec : une exfiltration de dépôts en neuf minutes, permise par une faille d'offboarding"
title_es: "CrowdSec: un volcado de repositorios de nueve minutos, habilitado por un hueco en la desvinculación"
date: 2026-09-18
date_raw: "2026-09-18"
date_precision: day

kind: incident
type: [SUPPLY, CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **About 170 private GitHub repositories were copied from the French security firm CrowdSec in a nine-minute burst — because a just-departed developer's account, infected by the TanStack/Shai-Hulud supply-chain attack, still carried a token with read access to private repositories.** CrowdSec traced the exfiltration to **22 May, 05:52–06:01 UTC**, from a Toronto IP; the copy was tied to the BreachForum founder and a member using the handle "diencracked". The company **only discovered it on 16 September**, when an archive of its source code appeared on the crime marketplace pwnforum (the Fuites Info team alerted it); it removed the account on 25 May — three days after the intrusion, but only after the fact. CEO Philippe Humeau's account: the leak is *"limited to CrowdSecurity's source code, including 130+ public repositories and many private ones"*; no infrastructure or databases were accessed and no code was altered — but **the company's first statement that no user data was affected was later corrected: 83 users' email addresses and information on 51 investors appeared in the leaked data**. This is the archive's second downstream victim of the May TanStack npm compromise (after OpenAI staff devices) — the failure was not exotic: an offboarding process that did not revoke read access. Recorded `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: true`

summary_zh: |
  **约 170 个私有 GitHub 仓库从法国安全公司 CrowdSec 被拷走——整个过程只持续九分钟，缺口是一名刚离职开发者的账号：该账号被 TanStack/Shai-Hulud 供应链攻击感染，而其凭据仍保留私有仓库读取权限。** CrowdSec 把外泄追踪至 **5 月 22 日 05:52–06:01 UTC**、来自多伦多 IP；拷贝行为关联到 BreachForum 创始人与化名 "diencracked" 的成员。公司**直到 9 月 16 日才发现**——其源代码档案出现在犯罪市场 pwnforum 上（Fuites Info 团队通知了公司）；账号在 5 月 25 日被移除——即入侵发生三天后，但为时已晚。CEO Philippe Humeau 的说法：泄漏*「限于 CrowdSecurity 的源代码，包括 130+ 个公共仓库和许多私有仓库」*；基础设施与数据库未被访问、代码未被篡改——但**公司最初「无用户数据受影响」的声明随后被更正：泄漏数据中出现 83 名用户的邮箱与 51 名投资人的信息**。这是本档案中 5 月 TanStack npm 事件（继 OpenAI 员工设备之后）的第二个下游受害方——失效点并不复杂：一套没有及时回收读取权限的离职流程。本条记为 `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: true`

summary_ja: |
  **フランスのセキュリティ企業CrowdSecから約170の非公開GitHubリポジトリが流出——わずか9分間の出来事で、隙は直前に退職した開発者のアカウントだった：TanStack/Shai-Huludサプライチェーン攻撃に感染したそのアカウントのトークンが、非公開リポジトリの読み取り権限を保持していた。** 外泄は**5月22日05:52〜06:01 UTC**（トロントのIP）と特定され、BreachForum創設者と「diencracked」というハンドルの人物に結び付けられた。発見は**9月16日**——犯罪マーケットpwnforumにソースコードのアーカイブが出現してから（Fuites Infoが通報）。アカウントは5月25日に削除された。CEO Philippe Humeau曰く、漏洩は*「CrowdSecurityのソースコードに限定され、130以上の公開リポジトリと多数の非公開リポジトリを含む」*；インフラとデータベースは未アクセス、コード改変もなし——ただし**「ユーザーデータへの影響なし」という当初声明は後に訂正され、83名のユーザーメールと51名の投資家情報が漏洩データに現れた**

summary_ko: |
  **프랑스 보안 기업 CrowdSec에서 약 170개의 비공개 GitHub 저장소가 유출됐다 — 단 9분 만에 벌어진 일이며, 빈틈은 막 퇴사한 개발자의 계정이었다: TanStack/Shai-Hulud 공급망 공격에 감염된 그 계정의 토큰이 비공개 저장소 읽기 권한을 그대로 보유하고 있었다.** 유출은 **5월 22일 05:52~06:01 UTC** (토론토 IP)로 추적되었고, BreachForum 창립자와 "diencracked" 핸들 사용자에게 연결됐다. 발견은 **9월 16일** — 범죄 마켓플레이스 pwnforum에 소스 코드 아카이브가 나타난 뒤에야(Fuites Info가 통보). 계정은 5월 25일 제거됐다. CEO Philippe Humeau에 따르면 유출은 *"CrowdSecurity 소스 코드에 국한되며 130개 이상 공개 저장소와 다수 비공개 저장소를 포함"*; 인프라와 데이터베이스는 접근되지 않았고 코드 변조도 없었다 — 그러나 **"사용자 데이터 영향 없음"이라는 첫 성명은 이후 정정되어 83명 사용자 이메일과 51명 투자자 정보가 유출 데이터에 나타났다**

summary_de: |
  **Rund 170 private GitHub-Repositories wurden aus dem französischen Sicherheitsunternehmen CrowdSec kopiert – in einem neunminütigen Vorgang, ermöglicht durch das Konto eines gerade ausgeschiedenen Entwicklers: infiziert durch den TanStack/Shai-Hulud-Lieferkettenangriff, trug dessen Token weiterhin Lesezugriff auf private Repositories.** Die Exfiltration wurde auf den **22. Mai, 05:52–06:01 UTC**, von einer Toronto-IP zurückverfolgt und mit dem BreachForum-Gründer und einem Mitglied namens „diencracked" verbunden. Entdeckt wurde sie erst am **16. September**, als ein Quellcode-Archiv auf dem Marktplatz pwnforum erschien (das Fuites-Info-Team informierte). Das Konto wurde am 25. Mai entfernt. CEO Philippe Humeau: Der Leak sei *„auf den Quellcode von CrowdSecurity begrenzt, einschließlich 130+ öffentlicher und vieler privater Repositories"*; Infrastruktur und Datenbanken blieben unberührt – doch **die erste Aussage, keine Nutzerdaten seien betroffen, wurde später korrigiert: 83 Nutzer-E-Mails und Daten zu 51 Investoren erschienen in den geleakten Daten**

summary_fr: |
  **Environ 170 dépôts GitHub privés ont été copiés chez la société française CrowdSec en neuf minutes — la faille : le compte d'un développeur tout juste parti, infecté par l'attaque de supply chain TanStack/Shai-Hulud, dont le jeton conservait un accès en lecture aux dépôts privés.** L'exfiltration est datée du **22 mai, 05:52–06:01 UTC**, depuis une IP de Toronto, liée au fondateur de BreachForum et à un membre « diencracked ». La découverte n'a eu lieu que le **16 septembre**, quand une archive du code source est apparue sur la place de marché criminelle pwnforum (l'équipe Fuites Info a alerté). Le compte a été retiré le 25 mai. Selon le CEO Philippe Humeau, la fuite est *« limitée au code source de CrowdSecurity, incluant 130+ dépôts publics et de nombreux privés »* ; ni infrastructure ni bases de données touchées — mais **la première déclaration d'absence d'impact sur les données utilisateurs a été corrigée : 83 e-mails d'utilisateurs et des informations sur 51 investisseurs figurent dans les données divulguées**

summary_es: |
  **Unos 170 repositorios privados de GitHub fueron copiados de la firma francesa CrowdSec en nueve minutos — el fallo: la cuenta de un desarrollador recién salido, infectada por el ataque de cadena de suministro TanStack/Shai-Hulud, cuyo token conservaba acceso de lectura a los repositorios privados.** La exfiltración se fecha el **22 de mayo, 05:52–06:01 UTC**, desde una IP de Toronto, vinculada al fundador de BreachForum y a un miembro «diencracked». El descubrimiento solo ocurrió el **16 de septiembre**, cuando apareció un archivo del código fuente en el mercado criminal pwnforum (el equipo Fuites Info avisó). La cuenta se retiró el 25 de mayo. Según el CEO Philippe Humeau, la filtración se *«limita al código fuente de CrowdSecurity, incluidos 130+ repositorios públicos y muchos privados»*; ni infraestructura ni bases de datos fueron accedidas — pero **la primera declaración de que no había datos de usuarios afectados se corrigió después: 83 correos de usuarios e información de 51 inversores aparecieron en los datos filtrados**

sources:
  - url: https://www.darkreading.com/cyberattacks-data-breaches/shai-hulud-attack-cyber-firm-crowdsec-github-data
    label: Dark Reading
  - url: https://thehackernews.com/2026/09/crowdsec-says-tanstack-npm-attack-led.html
    label: The Hacker News
  - url: https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/09/CSA_research_note_crowdsec_tanstack_offboarding_breach_20260920-csa-styled.pdf
    label: Cloud Security Alliance
  - url: https://devops.com/teampcp-supply-chain-attack-leads-to-crowdsec-source-code-being-stolen/
    label: DevOps.com

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# CrowdSec: a nine-minute repository dump, enabled by an offboarding gap

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-B23B40?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-3C6E8F?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-6E4B8F?style=flat-square)

## Summary

**About 170 private GitHub repositories were copied from the French security firm CrowdSec in a nine-minute burst — because a just-departed developer's account, infected by the TanStack/Shai-Hulud supply-chain attack, still carried a token with read access to private repositories.** CrowdSec traced the exfiltration to **22 May, 05:52–06:01 UTC**, from a Toronto IP; the copy was tied to the BreachForum founder and a member using the handle "diencracked". The company **only discovered it on 16 September**, when an archive of its source code appeared on the crime marketplace pwnforum (the Fuites Info team alerted it); it removed the account on 25 May — three days after the intrusion, but only after the fact. CEO Philippe Humeau's account: the leak is *"limited to CrowdSecurity's source code, including 130+ public repositories and many private ones"*; no infrastructure or databases were accessed and no code was altered — but **the company's first statement that no user data was affected was later corrected: 83 users' email addresses and information on 51 investors appeared in the leaked data**. This is the archive's second downstream victim of the May TanStack npm compromise (after OpenAI staff devices) — the failure was not exotic: an offboarding process that did not revoke read access. Recorded `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: true`

## Timeline

```mermaid
flowchart LR
    E["May: a departing CrowdSec developer's machine<br/>is infected by the TanStack/Shai-Hulud attack"]:::step
    S1["22 May 05:52-06:01 UTC: ~170 private repos<br/>copied from a Toronto IP (9 minutes)"]:::impact
    S2["25 May: the account is removed -<br/>but the copy already happened"]:::step
    I["16 Sep: source archive surfaces on pwnforum;<br/>CrowdSec investigates and discloses"]:::impact
    E --> S1 --> S2 --> I
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**A nine-minute job.** Per CrowdSec's own post, the attacker used a **GitHub API token taken from a former employee's machine that retained permission to read the company's private repositories**, and downloaded the contents *"over the course of just several minutes."* The company's investigation put the operation at **22 May, 05:52–06:01 UTC**, from a Toronto IP address, and tied it to the BreachForum founder and a user known as "diencracked"; the token no longer appeared in GitHub's own audit records, so CrowdSec enlisted GitHub to trace the access back to the account — a former developer *"who had just left the company, but that was still part of the GitHub organization for legitimate reasons."* The ex-employee's machine, Humeau wrote, *"got compromised by the TanStack supply chain attack, matching the methodology."* The account was removed on 25 May.

**How it surfaced — and the correction.** CrowdSec discovered the breach only on **16 September**, when a user published an archive containing source code from the company's GitHub on **pwnforum**, an underground marketplace; the **Fuites Info** team then contacted the company directly. In the first public statement the company said the leak was limited to source code (130+ public repositories and many private ones) with no infrastructure or database access and no tampering; the disclosure was then **corrected to acknowledge that leaked data included the email addresses of 83 users and information on 51 investors** — a two-version sequence this record keeps side by side, per the archive's rule on self-correcting disclosures.

**Why it belongs in this archive.** The TanStack npm compromise (TeamPCP's "Mini Shai-Hulud") already appears twice in the archive — the worm itself and the OpenAI staff-device follow-on. CrowdSec is the second downstream victim, and its value as a record is precisely that **nothing here was sophisticated**: no zero-day, no novel tooling — a legitimate token with read access, kept alive by an offboarding process that revoked "membership" but not "capability", against infrastructure that kept no record of the token's use. The attacker's search for usable credentials in the stolen material apparently turned up little else; the copy itself, however, was already done.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Dark Reading | <https://www.darkreading.com/cyberattacks-data-breaches/shai-hulud-attack-cyber-firm-crowdsec-github-data> |
| 2 | The Hacker News | <https://thehackernews.com/2026/09/crowdsec-says-tanstack-npm-attack-led.html> |
| 3 | Cloud Security Alliance | <https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/09/CSA_research_note_crowdsec_tanstack_offboarding_breach_20260920-csa-styled.pdf> |
| 4 | DevOps.com | <https://devops.com/teampcp-supply-chain-attack-leads-to-crowdsec-source-code-being-stolen/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-18` (raw: 2026-09-18, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) [`CRED`](../../taxonomy/types.md#cred) |
| Severity | **High** `high` |
| Confidence | **A** — the victim company's own account (CEO statement) plus independent analyses and press |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-18-crowdsec-tanstack-offboarding-breach` |

<sub>**Why this classification:** A compromise whose entry point and payload both run through the AI-tooling supply chain — the TanStack npm attack's infected machine seeding a token that dumped private repositories: `SUPPLY` + `CRED`, matching the archive's treatment of the Mini Shai-Hulud records. Rated `high`: confirmed real damage of substantial scope (source code of 130+ public and many private repositories, plus limited personal data) at a security vendor itself; not `critical`, as infrastructure and customer systems were untouched and the company's own impact assessment stayed at the source-code level. Dated to the disclosure with the corrected impact statement (18 September 2026). Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-05-11` [TanStack npm: the "Mini Shai-Hulud" worm](../2026-05/2026-05-11-tanstack-npm-mini-shai.md)<br>  <sub>The upstream supply-chain attack this breach flows from</sub>
- `2026-05-13` [OpenAI staff devices compromised via the TanStack incident](../2026-05/2026-05-13-tanstack-yuan-gong-she-bei.md)<br>  <sub>The other downstream victim - same worm, same month</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-18-crowdsec-tanstack-offboarding-breach.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
