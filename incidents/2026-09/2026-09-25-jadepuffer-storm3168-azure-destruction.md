---
id: 2026-09-25-jadepuffer-storm3168-azure-destruction
title: "JadePuffer/Storm-3168: an agentic actor deletes an Azure tenant's storage in a 7-minute destructive burst"
title_zh: "JadePuffer/Storm-3168：一个 agentic 行为者在 7 分钟破坏性爆发中删光某 Azure 租户的存储"
title_ja: "JadePuffer/Storm-3168：agenticなアクターが7分間の破壊的バーストでAzureテナントのストレージを削除"
title_ko: "JadePuffer/Storm-3168: agentic 행위자가 7분간의 파괴적 폭주로 어느 Azure 테넌트의 스토리지를 삭제하다"
title_de: "JadePuffer/Storm-3168: Ein agentischer Akteur löscht in einem 7-minütigen Zerstörungsschub den Speicher eines Azure-Tenants"
title_fr: "JadePuffer/Storm-3168 : un acteur agentique supprime le stockage d'un tenant Azure en une salve destructrice de 7 minutes"
title_es: "JadePuffer/Storm-3168: un actor agéntico elimina el almacenamiento de un tenant de Azure en una ráfaga destructiva de 7 minutos"
date: 2026-09-25
date_raw: "Microsoft disclosure 2026-09-25; activity early June 2026"
date_precision: day

kind: incident
type: [WEAPON, CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **Microsoft Security Research links the JADEPUFFER agentic-ransomware actor (tracked as Storm-3168) to extensive Azure-focused resource destruction: using two compromised service principals, it enumerated a tenant's cloud for ~15.5 hours, then in about 7 minutes made 100+ storage-account deletion attempts, most of which succeeded.** One service principal did reconnaissance; the other *"performed discovery, destructive operations, and credential collection."* It removed backup/recovery protections (Azure Site Recovery locks) *"to make restoration more difficult,"* and about half an hour after the wipe returned for 30+ storage-account-key requests, most successful. Some deletions were blocked — Azure resource locks and storage-account deletion protection saved a few accounts, and attempts to delete Azure SQL databases failed because the actor used an unsupported API version. Microsoft could not confirm initial access but notes one service principal's credentials *"appeared in a public GitHub issue before the attacks."* JADEPUFFER is the actor Sysdig documented in July 2026 as the first fully agentic ransomware operation; this is a distinct, cloud-destruction campaign by the same actor. Recorded `incident` / `WEAPON` + `CRED` / `high` / `real_harm: true`.

summary_zh: |
  **Microsoft 安全研究把 JADEPUFFER（agentic 勒索行为者，追踪代号 Storm-3168）关联到一场大规模、针对 Azure 的资源破坏：它用两个被盗的服务主体（service principal）对某租户的云资源枚举约 15.5 小时，随后在约 7 分钟内发起 100 多次存储账户删除、大部分成功。** 一个服务主体做侦察，另一个*「执行发现、破坏性操作与凭据收集」*。它移除了备份/恢复保护（Azure Site Recovery 锁）*「以增加恢复难度」*，并在删除约半小时后回头发起 30 多次存储账户密钥请求、大部分成功。部分删除被挡下——Azure 资源锁与存储账户删除保护救回了几个账户，而删除 Azure SQL 数据库的尝试因行为者使用了不受支持的 API 版本而失败。Microsoft 无法确认初始访问方式，但指出其中一个服务主体的凭据*「在攻击前出现在一个公开的 GitHub issue 里」*。JADEPUFFER 正是 Sysdig 7 月记录为"首个完全 agentic 勒索行动"的那个行为者；本次是同一行为者的另一场云破坏战役。本条记为 `incident` / `WEAPON` + `CRED` / `high` / `real_harm: true`。

summary_ja: |
  **Microsoft Security Researchは、agenticランサムウェアのアクターJADEPUFFER（追跡名Storm-3168）を、Azureを狙った大規模なリソース破壊に結び付けた。2つの侵害されたサービスプリンシパルを使い、テナントのクラウドを約15.5時間かけて列挙し、その後約7分間で100件超のストレージアカウント削除を試み、その大半が成功した。** 一方のサービスプリンシパルは偵察を、もう一方は*「発見・破壊的操作・認証情報収集」*を行った。バックアップ/復旧保護（Azure Site Recoveryロック）を*「復元をより困難にするため」*に外し、削除の約30分後に戻って30件超のストレージアカウントキー要求を行い大半が成功した。一部の削除は阻止された——Azureリソースロックとストレージアカウント削除保護がいくつかを救い、Azure SQLデータベースの削除試行はアクターが未サポートのAPIバージョンを使ったため失敗した。Microsoftは初期アクセスを確認できなかったが、あるサービスプリンシパルの認証情報が*「攻撃前に公開GitHub issueに現れていた」*と指摘する。JADEPUFFERはSysdigが7月に"初の完全agenticランサムウェア"として記録したアクターであり、本件は同一アクターによる別のクラウド破壊キャンペーンである。`incident` / `WEAPON` + `CRED` / `high` / `real_harm: true`

summary_ko: |
  **Microsoft Security Research는 agentic 랜섬웨어 행위자 JADEPUFFER(추적명 Storm-3168)를 Azure를 겨냥한 대규모 리소스 파괴에 연결했다. 두 개의 탈취된 서비스 주체(service principal)로 어느 테넌트의 클라우드를 약 15.5시간 열거한 뒤, 약 7분 만에 100건이 넘는 스토리지 계정 삭제를 시도해 대부분 성공했다.** 한 서비스 주체는 정찰을, 다른 하나는 *"발견·파괴적 작업·자격증명 수집"*을 수행했다. 백업/복구 보호(Azure Site Recovery 잠금)를 *"복원을 더 어렵게 하려고"* 제거했고, 삭제 약 30분 뒤 돌아와 30건이 넘는 스토리지 계정 키 요청을 해 대부분 성공했다. 일부 삭제는 차단됐다 — Azure 리소스 잠금과 스토리지 계정 삭제 보호가 몇몇을 구했고, Azure SQL 데이터베이스 삭제 시도는 지원되지 않는 API 버전을 써서 실패했다. Microsoft는 초기 접근을 확인하지 못했지만 한 서비스 주체의 자격증명이 *"공격 전 공개 GitHub 이슈에 나타났다"*고 지적한다. JADEPUFFER는 Sysdig가 7월에 "최초의 완전 agentic 랜섬웨어 작전"으로 기록한 행위자이며, 이번은 같은 행위자의 별개 클라우드 파괴 캠페인이다. `incident` / `WEAPON` + `CRED` / `high` / `real_harm: true`

summary_de: |
  **Microsoft Security Research verbindet den agentischen Ransomware-Akteur JADEPUFFER (verfolgt als Storm-3168) mit umfangreicher, auf Azure gerichteter Ressourcenzerstörung: Mit zwei kompromittierten Service Principals inventarisierte er die Cloud eines Tenants ~15,5 Stunden lang und unternahm dann in etwa 7 Minuten 100+ Löschversuche von Storage-Konten, die meist erfolgreich waren.** Ein Service Principal betrieb Aufklärung, der andere *"performed discovery, destructive operations, and credential collection."* Er entfernte Backup-/Wiederherstellungsschutz (Azure-Site-Recovery-Sperren) *"to make restoration more difficult"* und kehrte etwa eine halbe Stunde nach dem Löschen für 30+ Storage-Kontoschlüssel-Anfragen zurück, meist erfolgreich. Einige Löschungen wurden blockiert — Azure-Ressourcensperren und Storage-Konto-Löschschutz retteten wenige Konten, und Versuche, Azure-SQL-Datenbanken zu löschen, scheiterten an einer nicht unterstützten API-Version. Microsoft konnte den Erstzugang nicht bestätigen, merkt aber an, dass die Anmeldedaten eines Service Principals *"appeared in a public GitHub issue before the attacks."* JADEPUFFER ist der Akteur, den Sysdig im Juli 2026 als erste vollständig agentische Ransomware-Operation dokumentierte; dies ist eine eigene Cloud-Zerstörungskampagne desselben Akteurs. Verzeichnet als `incident` / `WEAPON` + `CRED` / `high` / `real_harm: true`

summary_fr: |
  **Microsoft Security Research relie l'acteur de rançongiciel agentique JADEPUFFER (suivi sous Storm-3168) à une vaste destruction de ressources visant Azure : avec deux service principals compromis, il a inventorié le cloud d'un tenant pendant ~15,5 heures, puis en environ 7 minutes a tenté 100+ suppressions de comptes de stockage, la plupart réussies.** Un service principal faisait la reconnaissance, l'autre *"performed discovery, destructive operations, and credential collection."* Il a retiré les protections de sauvegarde/récupération (verrous Azure Site Recovery) *"to make restoration more difficult"* et est revenu une demi-heure après l'effacement pour 30+ demandes de clés de comptes de stockage, la plupart réussies. Certaines suppressions ont été bloquées — des verrous de ressources Azure et la protection de suppression de comptes de stockage en ont sauvé quelques-uns, et les tentatives de suppression de bases Azure SQL ont échoué car l'acteur utilisait une version d'API non prise en charge. Microsoft n'a pu confirmer l'accès initial mais note que les identifiants d'un service principal *"appeared in a public GitHub issue before the attacks."* JADEPUFFER est l'acteur documenté par Sysdig en juillet 2026 comme la première opération de rançongiciel entièrement agentique ; il s'agit ici d'une campagne distincte de destruction cloud du même acteur. Enregistré `incident` / `WEAPON` + `CRED` / `high` / `real_harm: true`

summary_es: |
  **Microsoft Security Research vincula al actor de ransomware agéntico JADEPUFFER (rastreado como Storm-3168) con una amplia destrucción de recursos centrada en Azure: con dos service principals comprometidos, enumeró la nube de un tenant durante ~15,5 horas y luego, en unos 7 minutos, realizó más de 100 intentos de eliminación de cuentas de almacenamiento, la mayoría con éxito.** Un service principal hizo reconocimiento; el otro *"performed discovery, destructive operations, and credential collection."* Eliminó protecciones de copia/recuperación (bloqueos de Azure Site Recovery) *"to make restoration more difficult"* y, media hora después del borrado, volvió para más de 30 solicitudes de claves de cuentas de almacenamiento, la mayoría con éxito. Algunas eliminaciones fueron bloqueadas — los bloqueos de recursos de Azure y la protección de eliminación de cuentas de almacenamiento salvaron unas pocas, y los intentos de eliminar bases de datos Azure SQL fallaron porque el actor usó una versión de API no compatible. Microsoft no pudo confirmar el acceso inicial pero señala que las credenciales de un service principal *"appeared in a public GitHub issue before the attacks."* JADEPUFFER es el actor que Sysdig documentó en julio de 2026 como la primera operación de ransomware totalmente agéntica; esta es una campaña distinta de destrucción en la nube del mismo actor. Registrado `incident` / `WEAPON` + `CRED` / `high` / `real_harm: true`

sources:
  - url: https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/
    label: Microsoft Security Blog (primary)
  - url: https://www.bleepingcomputer.com/news/security/jadepuffer-agentic-ai-attacks-target-azure-destroy-cloud-resources/
    label: BleepingComputer
  - url: https://www.darkreading.com/cloud-security/jadepuffer-ai-actor-compromises-azure-tenant-destructive-cloud-attack
    label: Dark Reading
disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §13.22"
---

# JadePuffer/Storm-3168: an agentic actor deletes an Azure tenant's storage in a 7-minute destructive burst

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-8F6A3C?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-3C6E8F?style=flat-square)

## Summary

**Microsoft Security Research links the JADEPUFFER agentic-ransomware actor (tracked as Storm-3168) to extensive Azure-focused resource destruction: using two compromised service principals, it enumerated a tenant's cloud for ~15.5 hours, then in about 7 minutes made 100+ storage-account deletion attempts, most of which succeeded.** One service principal did reconnaissance; the other *"performed discovery, destructive operations, and credential collection."* It removed backup/recovery protections (Azure Site Recovery locks) *"to make restoration more difficult,"* and about half an hour after the wipe returned for 30+ storage-account-key requests, most successful. Some deletions were blocked — Azure resource locks and storage-account deletion protection saved a few accounts, and attempts to delete Azure SQL databases failed because the actor used an unsupported API version. Microsoft could not confirm initial access but notes one service principal's credentials *"appeared in a public GitHub issue before the attacks."* JADEPUFFER is the actor Sysdig documented in July 2026 as the first fully agentic ransomware operation; this is a distinct, cloud-destruction campaign by the same actor. Recorded `incident` / `WEAPON` + `CRED` / `high` / `real_harm: true`.

## Attack chain

```mermaid
flowchart LR
    E["Two compromised Azure service principals<br/>(one credential leaked in a public GitHub issue)"]:::entry
    S1["Recon: ~15.5h enumerating VMs, subscriptions,<br/>resource groups and resources (300+ successes)"]:::step
    S2["Destruction: ~7 min, 100+ storage-account deletions<br/>(most succeed); backup/recovery locks removed"]:::step
    I["~30 min later: 30+ storage-key requests (most succeed);<br/>SQL deletes fail (unsupported API); most storage gone"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What Microsoft found.** In a report published **25 September 2026**, *"Storm-3168: Agentic-driven cloud attacks using compromised service principals,"* Microsoft Security Research ties the activity to **JADEPUFFER**, *"a threat actor discovered by Sysdig in July 2026 and reported to be the first documented agentic ransomware operation."* Microsoft observed the Azure activity in **early June 2026**. Two compromised service principals in the same tenant were used: one for reconnaissance, the other for *"discovery, destructive operations, and credential collection."* Reconnaissance ran about **15 hours 30 minutes** with 300+ successful enumeration calls across VMs, subscriptions, resource groups and resources.

**The destruction.** The destructive phase lasted about **7 minutes** and involved **100+ storage-account deletion attempts**; *"most Azure Storage accounts targeted by the threat actor were successfully deleted,"* though *"Azure resource locks and storage account-level deletion protection blocked deletion attempts for a few."* The actor also removed **Azure Site Recovery locks**, *"indicating an effort to make restoration more difficult"* — a pattern Microsoft says *"could further support ransomware extortion,"* although it did not report financial demands or confirm data theft in the observed cases. Attempts to delete **Azure SQL databases failed** because the actor used an unsupported API version, and *"the parallel targeting of Azure SQL databases and storage accounts suggests an effort to broaden the destructive impact."* Roughly half an hour after the wipe, Storm-3168 returned for **30+ storage-account-key requests, most of which succeeded**.

**Access and why the archive records it.** Microsoft *"could not determine exactly how the initial access occurred,"* but notes credentials for one service principal *"appeared in a public GitHub issue before the attacks."* This is a distinct campaign from the archive's existing JADEPUFFER entry (`2026-07-01`, Sysdig's first-agentic-ransomware disclosure against a Langflow instance): same actor, a different, cloud-native destruction operation attributed by Microsoft. It is `WEAPON` (a human operator using agentic automation to run the intrusion) and `CRED` (harvesting storage-account keys and collecting credentials); `real_harm: true` because a tenant's Azure storage accounts were actually deleted. Graded `high` — confirmed destructive damage of limited (single-tenant) scope — rather than `critical`, which the archive reserves for multi-organisation, government, critical-infrastructure or worm-level damage.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Microsoft Security Blog — "Storm-3168: Agentic-driven cloud attacks…" | <https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/> |
| 2 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/jadepuffer-agentic-ai-attacks-target-azure-destroy-cloud-resources/> |
| 3 | Dark Reading | <https://www.darkreading.com/cloud-security/jadepuffer-ai-actor-compromises-azure-tenant-destructive-cloud-attack> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-25` (raw: Microsoft disclosure 2026-09-25; activity early June 2026, precision `day`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) [`CRED`](../../taxonomy/types.md#cred) |
| Severity | **High** `high` |
| Confidence | **A** — Microsoft Security Research's own report plus independent reporting |
| Real harm | Yes — a tenant's Azure storage accounts were deleted |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-25-jadepuffer-storm3168-azure-destruction` |

<sub>**Why this classification:** a human operator ran an agentic-driven intrusion (`WEAPON`) that collected credentials and storage-account keys (`CRED`) and destroyed a tenant's Azure storage. `real_harm: true` because the deletion was real and largely succeeded; `high` rather than `critical` — confirmed destructive damage scoped to a single tenant, with no multi-organisation / government / worm-level trigger and no reported extortion or data theft. Dated to Microsoft's 25 September disclosure; the observed activity is from early June 2026 (kept in `date_raw`). Distinct from `2026-07-01` (the same actor's first-agentic-ransomware disclosure). Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution (WEAPON)](../../topics/offensive-ai.md)

**Related records:**

- `2026-07-01` [JADEPUFFER: first ransomware driven end-to-end by an LLM](../2026-07/2026-07-01-jadepuffer-first-llm-driven-ransomware.md)<br>  <sub>The same actor's first disclosure — agentic ransomware against a Langflow instance</sub>
- `2026-09-22` [CARBONATO: a Docker botnet installs Hermes Agent and loots AI API keys](2026-09-22-carbonato-docker-hermes-agent-botnet.md)<br>  <sub>Another agent-driven commodity intrusion disclosed the same month</sub>
- `2026-09-23` [x47.c: a Windows botnet-for-sale that drains AI API credit and uses Grok to hide](2026-09-23-x47c-botnet-grok-ai-api-drain.md)<br>  <sub>The same offensive-AI thread, at the commodity-tooling end</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-25-jadepuffer-storm3168-azure-destruction.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
