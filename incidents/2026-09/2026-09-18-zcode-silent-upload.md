---
id: 2026-09-18-zcode-silent-upload
title: "Zhipu's ZCode agent silently uploaded whole repositories, Git history included"
title_zh: "智谱 ZCode 静默上传完整代码仓库，含 Git 历史"
title_ja: "智譜のZCode、リポジトリ全体をGit履歴ごと無断アップロード"
title_ko: "즈푸 ZCode, Git 기록 포함 저장소 전체를 몰래 업로드"
title_de: "Zhipus ZCode lud heimlich ganze Repositories samt Git-Historie hoch"
title_fr: "ZCode (Zhipu) a téléversé en silence des dépôts entiers, historique Git compris"
title_es: "ZCode de Zhipu subió en silencio repositorios completos, incluida la historia de Git"
date: 2026-09-18
date_raw: "2026-09-18→21"
date_precision: day

kind: incident
type: [EXFIL]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [CN]

summary: |
  Users discover that **Zhipu's AI coding agent ZCode** silently packages the **entire workspace and uploads it**: a developer's forensic write-up finds a **313 MB encrypted archive** in the hidden `~/.zcode` directory holding roughly **42,000 files, 86.6% of them `.git` history** — so deleted keys, configs and business traces travel with it. The encryption key is delivered by the server and kept only in the cloud, and **no setting turns the upload off**. Zhipu apologises the same day, blaming the default-on **codebase-indexing** feature and saying the data exists only long enough to generate a repo wiki and is then destroyed; a customer, **Chengming Technology**, disputes that, says it still detected uploads after the fix, and demands written answers — including whether data left the country — by **10 October**. Zhipu has since open-sourced ZCode and reports rectification complete in v3.14.0

summary_zh: |
  用户发现**智谱 AI 编程 agent ZCode** 会静默打包**整个工作区并上传**：一位开发者的取证记录在隐藏目录 `~/.zcode` 中找到 **313MB 加密压缩包**，内含约 **4.2 万个文件、其中 86.6% 是 `.git` 历史**——已删除的密钥、配置与业务痕迹一并被打包带走；加密密钥由服务端下发、仅存于云端，**没有任何设置能关闭上传**。智谱当日致歉，将原因归于默认开启的**「代码库索引」**功能，称数据只为生成仓库 Wiki 而短暂存在、随后即销毁；客户**太原承明科技**对此提出异议，称修复后仍检测到上传行为，并要求智谱在 **10 月 10 日前**书面答复——包括数据是否出境。此后智谱已开源 ZCode，并称 v3.14.0 已完成整改

summary_ja: |
  ユーザーは、**智譜（Zhipu）のAIコーディングエージェントZCode**が**ワークスペース全体を無断でパッケージしてアップロード**していることを発見した。開発者のフォレンジック記録は、隠しディレクトリ`~/.zcode`内に**313MBの暗号化アーカイブ**（約**4.2万ファイル、うち86.6%が`.git`履歴**）を見つけた——削除済みの鍵や設定、業務の痕跡も一緒に持ち出される。暗号鍵はサーバーから配信されクラウドにのみ保管され、**アップロードを止める設定は存在しない**。智譜は同日謝罪し、デフォルト有効の**「コードベース・インデックス」**機能が原因と説明、データはリポジトリWiki生成のためだけに存在し後に破棄されるとした。顧客の**太原承明科技**はこれを争い、修正後もアップロードを検知したと述べ、データが国外に出たかを含め**10月10日**までの書面回答を要求。智譜はその後ZCodeをオープンソース化し、v3.14.0で整改完了と発表した

summary_ko: |
  사용자들은 **즈푸(Zhipu)의 AI 코딩 에이전트 ZCode**가 **작업 공간 전체를 몰래 묶어 업로드**한다는 사실을 발견했다. 한 개발자의 포렌식 분석은 숨겨진 `~/.zcode` 디렉터리에서 **313MB 암호화 압축 파일**(약 **4만2천 개 파일, 그중 86.6%가 `.git` 기록**)을 찾아냈다 — 삭제된 키·설정·업무 흔적까지 함께 빠져나간다. 암호화 키는 서버가 내려주고 클라우드에만 보관되며, **업로드를 끄는 설정은 없다**. 즈푸는 같은 날 사과하며 기본 활성화된 **'코드베이스 인덱싱'** 기능 탓이라 설명하고, 데이터는 저장소 위키 생성에만 쓰인 뒤 파기된다고 밝혔다. 고객사 **타이위안 청밍커지**는 이에 반박하며 수정 후에도 업로드가 탐지됐다고 주장하고, 데이터의 국외 이전 여부 등을 포함해 **10월 10일**까지 서면 답변을 요구했다. 즈푸는 이후 ZCode를 오픈소스화하고 v3.14.0에서 개선 완료를 발표했다

summary_de: |
  Nutzer entdecken, dass **Zhipus KI-Coding-Agent ZCode** den **gesamten Arbeitsbereich still verpackt und hochlädt**: Eine forensische Analyse eines Entwicklers findet im versteckten Verzeichnis `~/.zcode` ein **313 MB großes verschlüsseltes Archiv** mit rund **42.000 Dateien, davon 86,6% `.git`-Historie** — gelöschte Schlüssel, Konfigurationen und Geschäftsspuren reisen mit. Der Schlüssel wird vom Server geliefert und nur in der Cloud gehalten, und **keine Einstellung schaltet den Upload ab**. Zhipu entschuldigt sich am selben Tag, macht die standardmäßig aktive **Codebase-Indizierung** verantwortlich und erklärt, die Daten dienten nur der Erzeugung eines Repo-Wikis und würden danach vernichtet; der Kunde **Chengming Technology** bestreitet das, will auch nach dem Fix Uploads erkannt haben und verlangt bis zum **10. Oktober** schriftliche Antworten — auch dazu, ob Daten ins Ausland gingen. Zhipu hat ZCode inzwischen quelloffen gemacht und meldet die Behebung in v3.14.0 als abgeschlossen

summary_fr: |
  Des utilisateurs découvrent que **l'agent de codage IA ZCode de Zhipu** empaquette en silence **tout l'espace de travail et le téléverse** : l'analyse forensique d'un développeur trouve dans le répertoire caché `~/.zcode` une **archive chiffrée de 313 Mo** contenant environ **42 000 fichiers, dont 86,6 % d'historique `.git`** — clés supprimées, configurations et traces métier partent avec. La clé est fournie par le serveur et conservée uniquement dans le cloud, et **aucun réglage ne désactive l'envoi**. Zhipu s'excuse le jour même, imputant l'envoi à la fonction **indexation de base de code** activée par défaut, et affirme que les données ne servent qu'à générer un wiki de dépôt avant d'être détruites ; le client **Chengming Technology** conteste, dit avoir encore détecté des envois après le correctif, et exige des réponses écrites — y compris sur un éventuel transfert transfrontalier — avant le **10 octobre**. Zhipu a depuis ouvert le code de ZCode et annonce la correction achevée en v3.14.0

summary_es: |
  Los usuarios descubren que **el agente de código IA ZCode de Zhipu** empaqueta en silencio **todo el espacio de trabajo y lo sube**: el análisis forense de un desarrollador encuentra en el directorio oculto `~/.zcode` un **archivo cifrado de 313 MB** con unos **42.000 archivos, el 86,6% de ellos historial `.git`** — claves borradas, configuraciones y rastros de negocio viajan con él. La clave la entrega el servidor y solo se guarda en la nube, y **ningún ajuste desactiva la subida**. Zhipu se disculpa ese mismo día, atribuyéndolo a la función de **indexación de código** activada por defecto, y dice que los datos solo sirven para generar un wiki del repositorio y luego se destruyen; el cliente **Chengming Technology** lo disputa, afirma que aún detectó subidas tras el arreglo y exige respuestas por escrito —incluida la posible transferencia transfronteriza— antes del **10 de octubre**. Desde entonces Zhipu liberó el código de ZCode y declara la corrección completa en la v3.14.0

sources:
  - url: https://www.secrss.com/articles/94149
    label: Global Times
  - url: https://news.qq.com/rain/a/20260921A02ESY00
    label: The Paper
  - url: https://news.qq.com/rain/a/20260920A05HHD00
    label: TechWeb
  - url: https://www.freebuf.com/articles/501972.html
    label: FreeBuf
  - url: https://www.oschina.net/news/502589
    label: OSChina

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# Zhipu's ZCode agent silently uploaded whole repositories, Git history included

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

Users discover that **Zhipu's AI coding agent ZCode** silently packages the **entire workspace and uploads it**: a developer's forensic write-up finds a **313 MB encrypted archive** in the hidden `~/.zcode` directory holding roughly **42,000 files, 86.6% of them `.git` history** — so deleted keys, configs and business traces travel with it. The encryption key is delivered by the server and kept only in the cloud, and **no setting turns the upload off**. Zhipu apologises the same day, blaming the default-on **codebase-indexing** feature and saying the data exists only long enough to generate a repo wiki and is then destroyed; a customer, **Chengming Technology**, disputes that, says it still detected uploads after the fix, and demands written answers — including whether data left the country — by **10 October**. Zhipu has since open-sourced ZCode and reports rectification complete in v3.14.0

## Attack chain

```mermaid
flowchart LR
    E["A developer logs in to the ZCode agent"]:::entry
    S0["Codebase indexing is on by default; the workspace is packed and encrypted client-side"]:::step
    I["Source, .git history, secrets and personal data leave the machine<br/><i>(vendor says the data was destroyed; a customer disputes it)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What the forensics found.** On **18 September** the developer **ferstar** published a forensic write-up: while cleaning a disk he found a **313 MB encrypted archive** in ZCode's hidden `~/.zcode` directory containing about **42,000 files, 86.6% of them `.git` history** — meaning not just the current source but the version-control record, including keys, configurations and business traces that had been deleted from the working tree. The packaging ran **automatically after login**, with no user action and no prompt; the RSA public key used to encrypt it is fetched from the server and the private key is held only in the cloud, so users cannot inspect what leaves their machine. The `.git` directory's higher priority in the upload filter let it **bypass the client's secret scanning and size limits**, and neither of the product's privacy toggles stopped the upload.

**The vendor's response.** Zhipu apologised the same evening through its official community, attributing the uploads to the **codebase-indexing** feature — **enabled by default since launch** — and saying the data exists only long enough to generate a repository wiki page in the cloud, after which it "is immediately destroyed" and is never used for model training. The company promised to open-source ZCode, invite third-party reviewers, and gave every user an extra weekly quota reset as compensation. On **21 September** Zhipu announced the rectification complete in client **v3.14.0**, said ZCode had been open-sourced, and reported that the China Academy of Information and Communications Technology (CAICT) and NSFOCUS had been engaged to audit the product — with CAICT's technical evaluation confirming the `zcode-prod` Aliyun OSS bucket now holds **zero data**.

**The customer's challenge — and why it matters.** **Chengming Technology** (Taiyuan) went further: after its own forensics it went public with a formal letter on **19–20 September**, stating that the uploads were automatic and bulk, that the data included full source code, system architecture, version-control history, **database passwords, cloud credentials and employee personal data** — well beyond the scope of ZCode's privacy policy — and that uploads were **still being detected in the early hours of 18 September, after the client had been updated to 3.12.3 on the 16th**. It asked why network requests point to a **Singapore entity** while the contracting party is Beijing-based (a cross-border-transfer question), demanded a written reply by **10 October** covering ten points (deletion, a data-processing inventory, key custody, access logs, deletion proof, a no-more-upload commitment and more), and reserved the right to claim damages, complain to regulators and sue. Whatever the outcome, the case marks the moment data handling by **agentic coding tools** — which now read whole repositories and hold more access than any previous desktop software — became a first-order compliance question for the enterprises using them.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Global Times | <https://www.secrss.com/articles/94149> |
| 2 | The Paper | <https://news.qq.com/rain/a/20260921A02ESY00> |
| 3 | TechWeb | <https://news.qq.com/rain/a/20260920A05HHD00> |
| 4 | FreeBuf | <https://www.freebuf.com/articles/501972.html> |
| 5 | OSChina | <https://www.oschina.net/news/502589> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-18` (raw: 2026-09-18→21, precision `day`) |
| Kind | Incident `incident` |
| Type | [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | yes |
| AI involvement | Confirmed `confirmed` |
| Region | [China](../../regions/cn.md) |
| Archive ID | `2026-09-18-zcode-silent-upload` |

<sub>**Why this classification:** Real incident with confirmed victims — the affected developer and enterprise published forensic findings, and the vendor itself confirmed the uploads. Graded `A` on source quality; the parties still disagree on post-fix behaviour and retention, and both positions are stated above. Rated `high`: source code, Git history and potentially credentials left users' machines without consent, with a customer pursuing formal accountability. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-09-08` [ChatGPT sandbox flaw pipes a victim's Gmail data into the attacker's account](2026-09-08-chatgpt-gmail-sha-xiang-que.md)<br>  <sub>ChatGPT sandbox flaw pipes a victim's Gmail data into the attacker's account</sub>
- `2026-08-04` [CHAINDROP npm worm](../2026-08/2026-08-04-chaindrop-npm-ru-chong.md)<br>  <sub>CHAINDROP npm worm</sub>
- `2026-09-01` [GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted](2026-09-01-gitspawn-git-config-pre-model-rce.md)<br>  <sub>GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-18-zcode-silent-upload.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
