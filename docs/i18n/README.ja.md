<h1 align="center">Orca AI Incident Archive</h1>

<p align="center"><b>実世界の AI エージェント事故のオープンデータベース</b></p>

<p align="center">
<a href="../../README.md">English</a> ·
<a href="README.zh-CN.md">简体中文</a> ·
<b>日本語</b> ·
<a href="README.ko.md">한국어</a> ·
<a href="README.de.md">Deutsch</a> ·
<a href="README.fr.md">Français</a> ·
<a href="README.es.md">Español</a>
</p>

<!-- BEGIN:badges -->
<p align="center"><img alt="件数" src="https://img.shields.io/badge/%E4%BB%B6%E6%95%B0-333-48545A?style=flat-square"> <img alt="対象月数" src="https://img.shields.io/badge/%E5%AF%BE%E8%B1%A1%E6%9C%88%E6%95%B0-22-48545A?style=flat-square"> <img alt="重大" src="https://img.shields.io/badge/%E9%87%8D%E5%A4%A7-45-88091D?style=flat-square"> <img alt="実害あり" src="https://img.shields.io/badge/%E5%AE%9F%E5%AE%B3%E3%81%82%E3%82%8A-124-B23B40?style=flat-square"> <img alt="一次情報源" src="https://img.shields.io/badge/%E4%B8%80%E6%AC%A1%E6%83%85%E5%A0%B1%E6%BA%90-522_URL-157A41?style=flat-square"> <img alt="ライセンス" src="https://img.shields.io/badge/%E3%83%A9%E3%82%A4%E3%82%BB%E3%83%B3%E3%82%B9-CC_BY_4.0-2359A8?style=flat-square"></p>
<!-- END:badges -->

<!-- BEGIN:thesis -->
収録範囲は **2025-01** から **2026-09-19** まで。AI エージェントに関わるセキュリティ事象 333 件を月単位で整理しています（ほかに 2024-12-01 まで遡れる前史 1 件）。各レコードは YAML ヘッダー、攻撃連鎖図、そして**クリックできる一次情報源を必ず 1 つ以上**持つ Markdown ファイルです。333 件のうち、確認された被害者がいるのは **124 件**だけです。
<!-- END:thesis -->

このアーカイブは、多くの事故リストが混同してしまう一点の区別のために存在します。

> **エージェントが実際に被害を出したことと、研究者が「出しうる」と実証したことは、別物である。**

各レコードはまず三つの問いに答えます。確認された被害者がいたか（`real_harm`）、AI の関与は一次情報源で裏付けられているか（`ai_involvement`）、そしてこれは事故か、脆弱性の公表か、研究デモか、脅威レポートか、政策動向か（`kind`）。この三つのフィールドがなければ、「今年は AI 事故が 300 件以上」という数字には何の意味もありません。

---

## 概観

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/monthly-dark.svg">
  <img alt="2025年1月から2026年9月までの月別件数" src="../../assets/monthly-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/severity-dark.svg">
  <img alt="深刻度と記録種別の内訳" src="../../assets/severity-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/by-type-dark.svg">
  <img alt="攻撃タイプ別の分布" src="../../assets/by-type-light.svg" width="100%">
</picture>

## どこから読むか

| やりたいこと | 行き先 |
|---|---|
| 時系列で読む | [月別の全レコード](../../incidents/README.md) |
| 実害が出たものだけ見る | [`critical` 一覧](#critical) · または `real_harm: true` で絞る |
| 攻撃面から読む | [7 つのテーマ](../../topics/README.md) |
| 国・地域で見る | [地域別](../../regions/README.md) |
| フィールドの定義を知る | [SCHEMA.md](../../SCHEMA.md) · [分類体系](../../taxonomy/README.md) · [ドキュメント](../../docs/README.md) |
| データを分析する | [`dist/`](../../dist/README.md) — JSON、CSV、統計、全ソース URL |
| 対話的に閲覧する | [`index.html`](../../index.html) — 単一ファイル、オフライン可、7 言語 |

> [!NOTE]
> **言語について。** レコードは英語で書かれています。タイトルと要約は 7 言語（英語・中国語・日本語・韓国語・ドイツ語・フランス語・スペイン語）で利用できます。各レコードの完全な中国語版は [`incidents/i18n/zh/`](../../incidents/i18n/zh/) にあります。引用元は原語のままです。翻訳の追加は歓迎します。[CONTRIBUTING.md](../../CONTRIBUTING.md) を参照してください。

## 月別

<!-- BEGIN:months -->
**2024年**（1 件）

| [12](../../incidents/2024-12/README.md) |
|---|
| `1` |

**2025年**（121 件）

| [01](../../incidents/2025-01/README.md) | [02](../../incidents/2025-02/README.md) | [03](../../incidents/2025-03/README.md) | [04](../../incidents/2025-04/README.md) | [05](../../incidents/2025-05/README.md) | [06](../../incidents/2025-06/README.md) | [07](../../incidents/2025-07/README.md) | [08](../../incidents/2025-08/README.md) | [09](../../incidents/2025-09/README.md) | [10](../../incidents/2025-10/README.md) | [11](../../incidents/2025-11/README.md) | [12](../../incidents/2025-12/README.md) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `8` ★1 | `6` | `6` | `6` | `7` | `11` | `10` ★2 | `15` ★2 | `10` ★1 | `15` | `13` ★3 | `14` |

**2026年**（211 件）

| [01](../../incidents/2026-01/README.md) | [02](../../incidents/2026-02/README.md) | [03](../../incidents/2026-03/README.md) | [04](../../incidents/2026-04/README.md) | [05](../../incidents/2026-05/README.md) | [06](../../incidents/2026-06/README.md) | [07](../../incidents/2026-07/README.md) | [08](../../incidents/2026-08/README.md) | [09](../../incidents/2026-09/README.md) |
|---|---|---|---|---|---|---|---|---|
| `13` ★1 | `19` ★5 | `16` ★3 | `22` ★2 | `26` ★5 | `31` ★3 | `27` ★7 | `23` ★4 | `34` ★6 |

<sub>`n` = その月の件数、★ = うち `critical` の件数</sub>
<!-- END:months -->

## Critical

<!-- BEGIN:critical -->
次のいずれかで `critical` とします。① **確認された**被害が複数組織・政府・重要インフラ・サプライチェーンワームの規模に達したもの。② 実被害を伴う初の能力マイルストーン。③ **広く展開された防御の前提を覆した**研究（この場合 `real_harm: false`、2 件）。詳細は [../../taxonomy/severity.md](../../taxonomy/severity.md)。

| 日付 | レコード | 種別 | 地域 |
|---|---|---|---|
| `2025-01-29` | [DeepSeekのClickHouseデータベースが無防備なまま公開](../../incidents/2025-01/2025-01-29-deepseek-clickhouse-exposed.md)<br><sub>DeepSeek ClickHouse database left wide open</sub> | `INFRA` | 中国 |
| `2025-07-13` | [Amazon Q Developer拡張機能が汚染](../../incidents/2025-07/2025-07-13-amazon-q-extension-poisoned.md)<br><sub>Amazon Q Developer extension poisoned</sub> | `SUPPLY` `ROGUE` | グローバル |
| `2025-07-18` | [Replit Agentが本番データベースを削除](../../incidents/2025-07/2025-07-18-replit-agent-deletes-prod-db.md)<br><sub>Replit Agent deletes a production database</sub> | `ROGUE` | アメリカ |
| `2025-08-08` | [Salesloft DriftのOAuthトークン窃取](../../incidents/2025-08/2025-08-08-salesloft-drift-oauth-theft.md)<br><sub>Salesloft Drift OAuth token theft</sub> | `SUPPLY` `CRED` | グローバル |
| `2025-08-26` | [Nx「s1ngularity」](../../incidents/2025-08/2025-08-26-nx-s1ngularity.md)<br><sub>Nx "s1ngularity"</sub> | `SUPPLY` `CRED` | グローバル |
| `2025-09-15` | [Shai-Hulud npmワーム v1](../../incidents/2025-09/2025-09-15-shai-hulud-npm.md)<br><sub>Shai-Hulud npm worm v1</sub> | `SUPPLY` `CRED` | グローバル |
| `2025-11-01` | [ShadowRay 2.0（Rayフレームワーク）](../../incidents/2025-11/2025-11-01-shadowray-2-ray-framework.md)<br><sub>ShadowRay 2.0 (Ray framework)</sub> | `INFRA` | グローバル |
| `2025-11-13` | [GTG-1002：AIが主導した初のサイバー諜報キャンペーン](../../incidents/2025-11/2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md)<br><sub>GTG-1002: first AI-orchestrated cyber-espionage campaign</sub> | `WEAPON` | 中国 グローバル |
| `2025-11-21` | [Shai-Hulud 2.0](../../incidents/2025-11/2025-11-21-shai-hulud.md) | `SUPPLY` `CRED` | グローバル |
| `2026-01-31` | [Moltbookのデータベースが完全に公開状態](../../incidents/2026-01/2026-01-31-moltbook-open-database.md)<br><sub>Moltbook database fully open</sub> | `CRED` | グローバル |
| `2026-02-09` | [Clinejection](../../incidents/2026-02/2026-02-09-clinejection.md) | `SUPPLY` `IPI` | グローバル |
| `2026-02-20` | [AIを活用したアクターが600台以上のFortiGate機器を侵害](../../incidents/2026-02/2026-02-20-fortigate-600-devices-compromised.md)<br><sub>AI-augmented actor compromises 600+ FortiGate devices</sub> | `WEAPON` | グローバル |
| `2026-02-25` | [メキシコ政府機関9機関が侵害される](../../incidents/2026-02/2026-02-25-mexico-nine-agencies-breached.md)<br><sub>Nine Mexican government agencies breached</sub> | `WEAPON` | ラテンアメリカ |
| `2026-02-26` | [Claude CodeがDataTalks.Clubの本番環境すべてでterraform destroyを実行](../../incidents/2026-02/2026-02-26-claude-code-terraform-destroy-datatalks.md)<br><sub>Claude Code runs terraform destroy on all of DataTalks.Club's production</sub> | `ROGUE` | グローバル |
| `2026-02-28` | [CodeWallがマッキンゼー社内の「Lilli」AIプラットフォームを侵害](../../incidents/2026-02/2026-02-28-codewall-breaches-mckinsey-lilli.md)<br><sub>CodeWall breaches McKinsey's internal "Lilli" AI platform</sub> | `WEAPON` `INFRA` | アメリカ |
| `2026-03-01` | [Hades：AIコーディングアシスタントを攻撃面に変える持続キャンペーン](../../incidents/2026-03/2026-03-01-hades-campaign-ai-coding-assistants.md)<br><sub>Hades: a sustained campaign turning AI coding assistants into the attack surface</sub> | `SUPPLY` `CRED` | グローバル |
| `2026-03-24` | [バックドア入りLiteLLMリリース](../../incidents/2026-03/2026-03-24-litellm-backdoored-release.md)<br><sub>Backdoored LiteLLM release</sub> | `SUPPLY` `CRED` | グローバル |
| `2026-03-30` | [Axios npmパッケージが侵害される](../../incidents/2026-03/2026-03-30-axios-npm-compromised.md)<br><sub>Axios npm package compromised</sub> | `SUPPLY` | グローバル |
| `2026-04-16` | [MCPwn（CVE-2026-33032）：nginx-uiのMCPエンドポイントが実悪用される](../../incidents/2026-04/2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br><sub>MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild</sub> | `MCP` `INFRA` | グローバル |
| `2026-04-25` | [CursorとClaude Opus 4.6が9秒で本番環境とバックアップを消去](../../incidents/2026-04/2026-04-25-cursor-opus-46-nine-second-wipe.md)<br><sub>Cursor and Claude Opus 4.6 wipe production and backups in nine seconds</sub> | `ROGUE` | グローバル |
| `2026-05-10` | [完全なポストエクスプロイト・チェーンを実行した初の実環境LLMエージェント](../../incidents/2026-05/2026-05-10-first-in-wild-autonomous-llm-post-exploitation.md)<br><sub>First in-the-wild LLM agent running the full post-exploitation chain</sub> | `WEAPON` | グローバル |
| `2026-05-11` | [TanStack npmの「Mini Shai-Hulud」](../../incidents/2026-05/2026-05-11-tanstack-npm-mini-shai.md)<br><sub>TanStack npm "Mini Shai-Hulud"</sub> | `SUPPLY` `CRED` | グローバル |
| `2026-05-18` | [GitHubの社内リポジトリ3,800件が侵害](../../incidents/2026-05/2026-05-18-github-3800-internal-repos.md)<br><sub>3,800 internal GitHub repositories compromised</sub> | `SUPPLY` `CRED` | グローバル |
| `2026-05-19` | [TrapDoor：3つのエコシステムを汚染してAIアシスタントの設定を破壊](../../incidents/2026-05/2026-05-19-trapdoor-poisons-agent-configs.md)<br><sub>TrapDoor: poisoning three ecosystems to corrupt AI assistant configs</sub> | `SUPPLY` `CRED` | グローバル |
| `2026-05-21` | [Composio：エージェント自動化そのものが権限昇格経路になる](../../incidents/2026-05/2026-05-21-composio-agent-automation-privesc.md)<br><sub>Composio: agent automation itself becomes the privilege-escalation path</sub> | `CRED` `SUPPLY` | グローバル |
| `2026-06-01` | [攻撃者はMetaのAIサポートボットにInstagramアカウントを頼むだけ](../../incidents/2026-06/2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br><sub>Attackers simply ask Meta's AI support bot for Instagram accounts</sub> | `IPI` `CRED` | グローバル |
| `2026-06-01` | [Miasmaワーム](../../incidents/2026-06/2026-06-01-miasma-worm.md)<br><sub>Miasma worm</sub> | `SUPPLY` `CRED` | グローバル |
| `2026-06-17` | [Sapphire Sleetが88分でMastraのAIスコープすべてを汚染](../../incidents/2026-06/2026-06-17-sapphire-sleet-mastra-88-minutes.md)<br><sub>Sapphire Sleet poisons every Mastra AI scope in 88 minutes</sub> | `SUPPLY` `CRED` | グローバル |
| `2026-07-01` | [JADEPUFFER：LLMがエンドツーエンドで主導した初のランサムウェア](../../incidents/2026-07/2026-07-01-jadepuffer-first-llm-driven-ransomware.md)<br><sub>JADEPUFFER: first ransomware driven end-to-end by an LLM</sub> | `WEAPON` | グローバル |
| `2026-07-01` | [台湾の原子力安全委員会などがエージェント群集に侵害される](../../incidents/2026-07/2026-07-01-taiwan-government-agent-swarm.md)<br><sub>Taiwan's nuclear safety commission and other agencies breached by an agent swarm</sub> | `WEAPON` | 台湾 |
| `2026-07-02` | [隠されたWeb上の指示がAIエージェントに攻撃者へ支払わせる（実環境の2キャンペーン）](../../incidents/2026-07/2026-07-02-hidden-web-instructions-payment-fraud.md)<br><sub>Hidden web instructions make AI agents pay attackers (two in-the-wild campaigns)</sub> | `IPI` `ROGUE` | グローバル |
| `2026-07-09` | [OpenAIのエージェントがHugging Faceを侵害](../../incidents/2026-07/2026-07-09-openai-agents-breach-huggingface.md)<br><sub>OpenAI's agents breach Hugging Face</sub> | `EVAL` `WEAPON` | グローバル |
| `2026-07-30` | [Anthropicが3件の評価環境脱出インシデントを公表](../../incidents/2026-07/2026-07-30-anthropic-three-eval-incidents.md)<br><sub>Anthropic discloses three evaluation-breakout incidents</sub> | `EVAL` | グローバル |
| `2026-07-30` | [Hermes Agentがタイ財務省を無人のまま攻撃](../../incidents/2026-07/2026-07-30-hermes-agent-thailand-finance-ministry.md)<br><sub>Hermes Agent attacks Thailand's Ministry of Finance unattended</sub> | `WEAPON` | 東南アジア |
| `2026-07-30` | [Unit 42：中国語話者の運用者による自律型キャンペーン](../../incidents/2026-07/2026-07-30-unit42-chinese-speaking-autonomous-campaigns.md)<br><sub>Unit 42: autonomous campaigns run by Chinese-speaking operators</sub> | `WEAPON` | 中国 グローバル |
| `2026-08-04` | [CHAINDROP npmワーム](../../incidents/2026-08/2026-08-04-chaindrop-npm-ru-chong.md)<br><sub>CHAINDROP npm worm</sub> | `SUPPLY` `CRED` | グローバル |
| `2026-08-06` | [認証不要のLangflow RCEがCISA KEVに追加](../../incidents/2026-08/2026-08-06-langflow-rce-cisa-kev.md)<br><sub>Unauthenticated Langflow RCE added to CISA KEV</sub> | `INFRA` | グローバル |
| `2026-08-26` | [Trail of Bits：VMはサイバー能力を持つエージェントを封じ込められない](../../incidents/2026-08/2026-08-26-trailofbits-vm-cannot-contain-networked-agents.md)<br><sub>Trail of Bits: VMs won't contain cyber-capable agents</sub> | `EVAL` `SANDBOX` | グローバル |
| `2026-08-28` | [PaperCut AIエージェント群集キャンペーンが始まる](../../incidents/2026-08/2026-08-28-papercut-agent-swarm-campaign-begins.md)<br><sub>PaperCut AI agent swarm campaign begins</sub> | `WEAPON` | グローバル |
| `2026-09-01` | [GitSpawn：悪性の.git/configが7つのコーディングエージェントでモデル接続前に攻撃者コードを実行](../../incidents/2026-09/2026-09-01-gitspawn-git-config-pre-model-rce.md)<br><sub>GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted</sub> | `SUPPLY` `SANDBOX` | グローバル |
| `2026-09-02` | [Langflow CVE-2026-0768：今年実悪用された12件目のLangflow欠陥](../../incidents/2026-09/2026-09-02-langflow-jin-di-ye-li.md)<br><sub>Langflow CVE-2026-0768: the 12th Langflow flaw exploited in the wild this year</sub> | `INFRA` `CRED` | グローバル |
| `2026-09-10` | [Anthropic 9月脅威インテリジェンスレポート](../../incidents/2026-09/2026-09-10-anthropic-september-threat-report.md)<br><sub>Anthropic September threat intelligence report</sub> | `WEAPON` | グローバル |
| `2026-09-11` | [Claudeが180万件のAndroidアプリをスキャンしてシークレットを探索](../../incidents/2026-09/2026-09-11-claude-scans-18m-android-apks.md)<br><sub>Claude used to scan 1.8 million Android apps for secrets</sub> | `WEAPON` | グローバル |
| `2026-09-14` | [スペインAEPD、AIエージェントによる初のデータ侵害届出を受領](../../incidents/2026-09/2026-09-14-spain-aepd-agent-breach.md)<br><sub>Spain's AEPD receives the first AI-agent-driven breach notification</sub> | `WEAPON` | 欧州 |
| `2026-09-15` | [PaperCutへのAIエージェント群集攻撃が公表される](../../incidents/2026-09/2026-09-15-papercut-agent-swarm-disclosed.md)<br><sub>PaperCut AI agent swarm attack made public</sub> | `WEAPON` | グローバル |
<!-- END:critical -->

## 何をレコードとするか

次の**いずれか一つ**を満たせば収録します。

1. AI エージェントが**攻撃の実行者**だった — 自律的であれ、人間に駆動されたものであれ
2. AI エージェントが**攻撃対象**だった — インジェクション、汚染、サンドボックス脱出、インフラの露出
3. AI エージェントが**被害の連鎖の一環**だった — 悪意ある内容を読み、その通りに動いた
4. エージェントのセキュリティに直接関わる**規制・立法・ベンダーの動き**（`kind: policy` として記録し、事故件数には数えない）

**対象外：** 純粋な LLM のコンテンツ安全性の話（モデルを脱獄させて不適切な出力を得るだけのもの）、エージェントと無関係な通常の脆弱性、一次情報源にたどり着けない伝聞。

次の二つは**削除せずラベルを付けて**残します。

- `ai_involvement: unverified` — AI 事故として広く報じられたが、一次情報源に AI が一切出てこないもの。その主張が**反証材料と一緒に検索できる**ように残しています。
- `ai_involvement: disputed` — ベンダーと報道の見解が食い違うもの。両論をレコード内に併記します。

収録基準の全文は [docs/scope.md](../../docs/scope.md)。

## データ品質

<!-- BEGIN:quality -->
|  |  |
|---|---|
| 情報源リンク | 589 件 / ユニーク URL 522 件 |
| 情報源なしのレコード | **0** — 情報源がなければ収録しない |
| 評価 A（一次情報源） | 286 件 |
| 争いありとしてマーク | 14 件 |
| 検証回数 | 4 回 |
<!-- END:quality -->

最初の 3 回は**一件ずつ**照合しました。4 回目に**網羅性の監査**をしたところ、それでもなお約 11% が欠けていました。この二つはまったく別の問題を捕まえます。「収録済みのものが正しいか」と「収録すべきものが全部あるか」は、別々に問わなければなりません。

4 回の検証で、捏造された 2 件を削除し、PaperCut の「6 時間でドメイン管理者」を **7 分**に訂正し、Step Finance を D 評価に下げました（一次報道に AI への言及が一切ないため）。訂正はすべて [docs/data-quality.md](../../docs/data-quality.md) に残しており、黙って上書きしたものはありません。

## 引用

<!-- BEGIN:cite -->
```bibtex
@misc{orca_ai_incident_archive,
  title  = {Orca AI Incident Archive: An open database of real-world AI agent incidents},
  year   = {2026},
  note   = {333 件、2025-01〜2026-09、うち 124 件に確認された実害},
  url    = {https://github.com/Continuum-AI-Corp/Orca-AI-Incident-Archive}
}
```
<!-- END:cite -->

個別のレコードを引用する場合は `id` を添えてください。例：`orca:2026-07-09-openai-agents-breach-huggingface`。

## コントリビュート

訂正、未収録レコード、より良い情報源、いずれも歓迎します。ルールは三つだけです。

1. **各レコードには、クリックできる一次情報源が必須。** 情報源がなければマージしません。
2. **確信が持てなければ、ラベルを付ける。削除しない。** 争いのある事実には `disputed: true` を付け、両論をレコードに残します。
3. **訂正はレコードに書き込む。黙って上書きしない。** 何をなぜ変えたかを記します。

[CONTRIBUTING.md](../../CONTRIBUTING.md) を参照してください。[新規レコード](../../.github/ISSUE_TEMPLATE/new-incident.yml)と[訂正](../../.github/ISSUE_TEMPLATE/correction.yml)の issue テンプレートを用意しています。

## ライセンスと免責

[CC BY 4.0](../../LICENSE) で提供します。出典の明示が必要です。リンク先の原資料の著作権は各権利者に帰属します。

本アーカイブは**公開済みの事象のみ**を記録しており、未公開の脆弱性の詳細、エクスプロイトコード、攻撃ツールは一切含みません。分類と深刻度は編者の判断であり、ベンダーや規制当局の公式見解ではありません。当事者の方でレコードに誤りがあるとお考えの場合は issue を立ててください。確認のうえ訂正します。

---

<sub><!-- BEGIN:footer -->ビルド 2026-09-19 · 333 件 · 22 ヶ月<!-- END:footer --></sub> · <sub>構造：[SCHEMA.md](../../SCHEMA.md) · データ：[dist/](../../dist/README.md)</sub>
