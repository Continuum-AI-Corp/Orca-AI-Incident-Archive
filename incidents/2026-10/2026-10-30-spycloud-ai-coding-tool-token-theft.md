---
id: 2026-10-30-spycloud-ai-coding-tool-token-theft
title: "SpyCloud: infostealers now harvest AI coding-tool tokens and API keys — WardenStealer and Aoki target Claude Code and Codex"
title_zh: "SpyCloud：窃密软件开始收割 AI 编码工具的令牌与 API 密钥——WardenStealer 与 Aoki 盯上 Claude Code 与 Codex"
title_ja: "SpyCloud：インフォスティーラーがAIコーディングツールのトークンとAPIキーを収集——WardenStealerとAokiがClaude CodeとCodexを標的に"
title_ko: "SpyCloud: 인포스틸러가 이제 AI 코딩 도구의 토큰과 API 키를 수집——WardenStealer와 Aoki가 Claude Code와 Codex를 노린다"
title_de: "SpyCloud: Infostealer sammeln jetzt Tokens und API-Schlüssel von KI-Coding-Tools — WardenStealer und Aoki zielen auf Claude Code und Codex"
title_fr: "SpyCloud : les infostealers récoltent désormais les jetons et clés d'API des outils de codage IA — WardenStealer et Aoki visent Claude Code et Codex"
title_es: "SpyCloud: los infostealers ahora recolectan tokens y claves de API de herramientas de codificación con IA — WardenStealer y Aoki apuntan a Claude Code y Codex"
date: 2026-10-30
date_raw: "2026-10-30 (SpyCloud report; WardenStealer first seen 2026-08-03, Aoki 2026-10-04)"
date_precision: day

kind: research
type: [CRED, EXFIL]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **On 30 October 2026, SpyCloud (Trevor Hilligoss) reported that infostealer malware now harvests credentials from AI coding tools, naming two families — WardenStealer and Aoki — that pull tokens and API keys from local Claude Code, Codex, Copilot, Cursor and desktop AI apps.** SpyCloud first saw **WardenStealer** on **3 August 2026** and has ingested **130,000+** unique infections; **Aoki** (a Go stealer) appeared in its recaptured data on **4 October 2026** (Symantec published on Aoki 15 October). What they take is **account access and context**: Claude Code's **OAuth access and refresh tokens**, tokens for connected **MCP servers**, the account config (user/machine IDs) and the `CLAUDE.md` instruction file; Codex's auth file with an **OpenAI API key** plus access/refresh tokens; Copilot and Cursor token files; and desktop-app cookies. A criminal market has adjusted in step — a **$100 Codex or Claude API credit advertised for $8.94**, AI subscriptions at 40–60% below list, a Telegram bot at up to 91% off, and a wholesaler paying suppliers 35% of billings for Anthropic/AWS-Bedrock Claude keys. **SpyCloud is explicit that it cannot confirm abuse of these specific credentials** (and that not all material being sold was necessarily taken by these stealers), so this is recorded `research` / `CRED` + `EXFIL` / `medium` / `real_harm: false` — the escalation of the trend first recorded for Gen Digital on 8 September 2026.

summary_zh: |
  **2026 年 10 月 30 日，SpyCloud（Trevor Hilligoss）报告称：窃密软件如今开始从 AI 编码工具收割凭据，并点名两个家族——WardenStealer 与 Aoki——它们从本地的 Claude Code、Codex、Copilot、Cursor 及桌面 AI 应用中抽取令牌与 API 密钥。** SpyCloud 首次见到 **WardenStealer** 是在 **2026 年 8 月 3 日**,已摄入 **13 万+** 个唯一感染；**Aoki**（一款 Go 窃密木马）于 **2026 年 10 月 4 日** 出现在其回捕数据中（Symantec 于 10 月 15 日发布对 Aoki 的分析）。它们拿走的是**账户访问权与上下文**：Claude Code 的 **OAuth 访问与刷新令牌**、所连 **MCP server** 的令牌、账户配置（用户/机器 ID）与 `CLAUDE.md` 指令文件；Codex 的认证文件（含一个 **OpenAI API 密钥** 及访问/刷新令牌）；Copilot 与 Cursor 的令牌文件；以及桌面应用的 cookie。地下市场随之调整——**标价 $100 的 Codex 或 Claude API 额度只卖 $8.94**、AI 订阅低至 4–6 折、某 Telegram 机器人低至 9.1 折，以及某批发商按 Anthropic/AWS-Bedrock Claude 密钥计费额的 35% 向供货方付费。**SpyCloud 明确表示无法确认这些具体凭据被滥用**（且在售材料未必全部由这些窃密木马取得），故记为 `research` / `CRED` + `EXFIL` / `medium` / `real_harm: false`——这是 2026 年 9 月 8 日 Gen Digital 首次记录的那条趋势的升级。

summary_ja: |
  **2026年10月30日、SpyCloud（Trevor Hilligoss）は、インフォスティーラーがAIコーディングツールから資格情報を収集するようになったと報告し、二つのファミリー——WardenStealerとAoki——を名指しした。これらはローカルのClaude Code、Codex、Copilot、Cursorおよびデスクトップ版AIアプリからトークンとAPIキーを抜き取る。** SpyCloudが **WardenStealer** を初めて確認したのは **2026年8月3日** で、**13万超**の固有感染を取り込んだ。**Aoki**（Go製スティーラー）は **2026年10月4日** に回収データに現れた（Symantecは10月15日にAokiを公表）。奪われるのは**アカウントアクセスと文脈**だ——Claude Codeの **OAuthアクセス/リフレッシュトークン**、接続された **MCPサーバー** のトークン、アカウント設定（ユーザー/マシンID）と `CLAUDE.md` 指示ファイル；Codexの認証ファイル（**OpenAI APIキー** とアクセス/リフレッシュトークン入り）；CopilotとCursorのトークンファイル；デスクトップアプリのクッキー。地下市場も歩調を合わせた——**$100分のCodexまたはClaude APIクレジットが$8.94** で出回り、AIサブスクが定価の4〜6割引、あるTelegramボットは最大91%引き、ある卸はAnthropic/AWS-Bedrock Claudeキーの請求額の35%を供給者に支払う。**SpyCloudはこれら特定の資格情報の悪用を確認できないと明言**している（売られている素材すべてがこれらのスティーラーで取得されたとは限らない）ため、`research` / `CRED` + `EXFIL` / `medium` / `real_harm: false` として記録する——2026年9月8日にGen Digitalで初めて記録された傾向の激化である。

summary_ko: |
  **2026년 10월 30일, SpyCloud(Trevor Hilligoss)는 인포스틸러 악성코드가 이제 AI 코딩 도구에서 자격 증명을 수집한다고 보고하며 두 계열——WardenStealer와 Aoki——을 지목했다. 이들은 로컬의 Claude Code, Codex, Copilot, Cursor 및 데스크톱 AI 앱에서 토큰과 API 키를 빼낸다.** SpyCloud가 **WardenStealer**를 처음 본 것은 **2026년 8월 3일**이며 **13만 개 이상**의 고유 감염을 수집했다. **Aoki**(Go 기반 스틸러)는 **2026년 10월 4일** 회수 데이터에 나타났다(Symantec은 10월 15일 Aoki를 공개). 이들이 가져가는 것은 **계정 접근권과 맥락**이다——Claude Code의 **OAuth 액세스·리프레시 토큰**, 연결된 **MCP 서버** 토큰, 계정 구성(사용자/머신 ID)과 `CLAUDE.md` 지시 파일; Codex의 인증 파일(**OpenAI API 키**와 액세스/리프레시 토큰 포함); Copilot과 Cursor의 토큰 파일; 데스크톱 앱 쿠키. 지하 시장도 발맞춰 조정됐다——**$100짜리 Codex 또는 Claude API 크레딧이 $8.94**에 광고되고, AI 구독이 정가 대비 40–60% 할인, 한 Telegram 봇은 최대 91% 할인, 한 도매상은 Anthropic/AWS-Bedrock Claude 키 청구액의 35%를 공급자에게 지급한다. **SpyCloud는 이 특정 자격 증명들의 악용을 확인할 수 없다고 명시**한다(판매 중인 자료가 모두 이 스틸러로 취득된 것은 아니다). 따라서 `research` / `CRED` + `EXFIL` / `medium` / `real_harm: false`로 기록한다——2026년 9월 8일 Gen Digital에서 처음 기록된 추세의 심화다.

summary_de: |
  **Am 30. Oktober 2026 berichtete SpyCloud (Trevor Hilligoss), dass Infostealer-Malware nun Anmeldedaten aus KI-Coding-Tools abgreift, und nannte zwei Familien — WardenStealer und Aoki —, die Tokens und API-Schlüssel aus lokalem Claude Code, Codex, Copilot, Cursor und Desktop-KI-Apps ziehen.** SpyCloud sah **WardenStealer** erstmals am **3. August 2026** und hat **über 130.000** eindeutige Infektionen erfasst; **Aoki** (ein Go-Stealer) tauchte am **4. Oktober 2026** in den wiedererlangten Daten auf (Symantec veröffentlichte am 15. Oktober zu Aoki). Entwendet werden **Kontozugang und Kontext**: Claude Codes **OAuth-Access- und Refresh-Tokens**, Tokens verbundener **MCP-Server**, die Kontokonfiguration (Nutzer-/Maschinen-IDs) und die `CLAUDE.md`-Anweisungsdatei; Codex' Auth-Datei mit einem **OpenAI-API-Schlüssel** samt Access-/Refresh-Tokens; Copilot- und Cursor-Token-Dateien; sowie Desktop-App-Cookies. Ein krimineller Markt hat nachgezogen — ein **für 8,94 $ beworbenes 100-$-Codex- oder -Claude-API-Guthaben**, KI-Abos 40–60 % unter Listenpreis, ein Telegram-Bot mit bis zu 91 % Rabatt und ein Großhändler, der Lieferanten 35 % der Abrechnung für Anthropic/AWS-Bedrock-Claude-Schlüssel zahlt. **SpyCloud stellt ausdrücklich klar, dass es den Missbrauch dieser konkreten Anmeldedaten nicht bestätigen kann** (und dass nicht alles verkaufte Material zwangsläufig von diesen Stealern stammt), daher `research` / `CRED` + `EXFIL` / `medium` / `real_harm: false` — die Eskalation des Trends, der am 8. September 2026 für Gen Digital erstmals erfasst wurde.

summary_fr: |
  **Le 30 octobre 2026, SpyCloud (Trevor Hilligoss) a signalé que les infostealers récoltent désormais des identifiants dans les outils de codage IA, nommant deux familles — WardenStealer et Aoki — qui extraient jetons et clés d'API de Claude Code, Codex, Copilot, Cursor et des applis IA de bureau en local.** SpyCloud a vu **WardenStealer** pour la première fois le **3 août 2026** et a ingéré **plus de 130 000** infections uniques ; **Aoki** (un stealer en Go) est apparu dans ses données récupérées le **4 octobre 2026** (Symantec a publié sur Aoki le 15 octobre). Ce qui est pris, c'est l'**accès au compte et le contexte** : les **jetons OAuth d'accès et de rafraîchissement** de Claude Code, les jetons des **serveurs MCP** connectés, la config du compte (ID utilisateur/machine) et le fichier d'instructions `CLAUDE.md` ; le fichier d'auth de Codex avec une **clé d'API OpenAI** et des jetons d'accès/rafraîchissement ; les fichiers de jetons de Copilot et Cursor ; et les cookies des applis de bureau. Un marché criminel s'est ajusté — un **crédit d'API Codex ou Claude de 100 $ annoncé à 8,94 $**, des abonnements IA 40–60 % sous le prix courant, un bot Telegram jusqu'à 91 % de remise, et un grossiste payant aux fournisseurs 35 % de la facturation pour des clés Claude Anthropic/AWS-Bedrock. **SpyCloud précise explicitement qu'il ne peut confirmer l'abus de ces identifiants précis** (et que tout le matériel vendu n'a pas nécessairement été pris par ces stealers), d'où un enregistrement `research` / `CRED` + `EXFIL` / `medium` / `real_harm: false` — l'escalade de la tendance enregistrée pour la première fois chez Gen Digital le 8 septembre 2026.

summary_es: |
  **El 30 de octubre de 2026, SpyCloud (Trevor Hilligoss) informó que el malware infostealer ahora recolecta credenciales de herramientas de codificación con IA, nombrando dos familias — WardenStealer y Aoki — que extraen tokens y claves de API de Claude Code, Codex, Copilot, Cursor y apps de IA de escritorio en local.** SpyCloud vio **WardenStealer** por primera vez el **3 de agosto de 2026** y ha ingerido **más de 130.000** infecciones únicas; **Aoki** (un stealer en Go) apareció en sus datos recuperados el **4 de octubre de 2026** (Symantec publicó sobre Aoki el 15 de octubre). Lo que se llevan es el **acceso a la cuenta y el contexto**: los **tokens OAuth de acceso y de actualización** de Claude Code, los tokens de los **servidores MCP** conectados, la configuración de la cuenta (ID de usuario/máquina) y el archivo de instrucciones `CLAUDE.md`; el archivo de autenticación de Codex con una **clave de API de OpenAI** más tokens de acceso/actualización; los archivos de tokens de Copilot y Cursor; y las cookies de apps de escritorio. Un mercado criminal se ha ajustado — un **crédito de API de Codex o Claude de 100 $ anunciado por 8,94 $**, suscripciones de IA un 40–60 % por debajo del precio de lista, un bot de Telegram con hasta un 91 % de descuento, y un mayorista que paga a los proveedores el 35 % de la facturación por claves de Claude de Anthropic/AWS-Bedrock. **SpyCloud es explícito en que no puede confirmar el abuso de estas credenciales concretas** (y que no todo el material en venta fue necesariamente tomado por estos stealers), por lo que se registra como `research` / `CRED` + `EXFIL` / `medium` / `real_harm: false` — la escalada de la tendencia registrada por primera vez para Gen Digital el 8 de septiembre de 2026.

sources:
  - url: https://spycloud.com/blog/infostealers-now-target-ai-tokens-and-api-keys/
    label: SpyCloud ("Infostealers now target AI tokens and API keys")
  - url: https://www.infosecurity-magazine.com/news/aoki-infostealer-ai-coding/
    label: Infosecurity Magazine (Aoki / Symantec)
  - url: https://cybersecuritynews.com/hackers-use-new-infostealer-malware/
    label: Cyber Security News
disputed: false
landmark: false
scan_month: 2026-11
scan_ref: "SCAN.md §13.37"
---

# SpyCloud: infostealers now harvest AI coding-tool tokens and API keys — WardenStealer and Aoki target Claude Code and Codex

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-8F6A3C?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-3C6E8F?style=flat-square)

## Summary

**On 30 October 2026, SpyCloud (Trevor Hilligoss) reported that infostealer malware now harvests credentials from AI coding tools, naming two families — WardenStealer and Aoki — that pull tokens and API keys from local Claude Code, Codex, Copilot, Cursor and desktop AI apps.** SpyCloud first saw WardenStealer on 3 August 2026 and has ingested 130,000+ unique infections; Aoki (a Go stealer) appeared in its recaptured data on 4 October 2026 (Symantec published on Aoki 15 October). What they take is account access and context: Claude Code's OAuth access and refresh tokens, tokens for connected MCP servers, the account config (user/machine IDs) and the `CLAUDE.md` instruction file; Codex's auth file with an OpenAI API key plus access/refresh tokens; Copilot and Cursor token files; and desktop-app cookies. A criminal market has adjusted in step — a $100 Codex or Claude API credit advertised for $8.94, AI subscriptions at 40–60% below list, a Telegram bot at up to 91% off, and a wholesaler paying suppliers 35% of billings for Anthropic/AWS-Bedrock Claude keys. SpyCloud is explicit that it cannot confirm abuse of these specific credentials (and that not all material being sold was necessarily taken by these stealers), so this is recorded `research` / `CRED` + `EXFIL` / `medium` / `real_harm: false` — the escalation of the trend first recorded for Gen Digital on 8 September 2026.

## Attack chain

```mermaid
flowchart LR
    E["An infostealer (WardenStealer / Aoki)<br/>runs on a developer's machine"]:::entry
    S0["Collection rules target AI-tool local paths:<br/>Claude Code OAuth + MCP tokens, CLAUDE.md,<br/>Codex OpenAI API key, Copilot/Cursor tokens"]:::step
    I["Reusable AI account access leaves in the logs;<br/>sold cheap ($100 API credit for $8.94)<br/><i>— downstream abuse not confirmed by SpyCloud</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What SpyCloud reported.** On **30 October 2026**, SpyCloud's Trevor Hilligoss published *"Infostealers now target AI tokens and API keys,"* documenting — from SpyCloud's recaptured-malware-log telemetry — that infostealer families have added AI coding tools to their collection scope. Two families anchor the report: **WardenStealer**, first seen by SpyCloud on **3 August 2026** (Gen Digital places its earliest builds in early May), with **more than 130,000** unique infections ingested; and **Aoki**, a **Go**-based Windows stealer first seen in SpyCloud's recaptured data on **4 October 2026**, which sorts stolen AI material into a dedicated `AISessions` folder with per-tool subfolders (Symantec published its own Aoki analysis on **15 October 2026**).

**What is taken — access and context.** The stolen files are the agents' local credentials and state, not preferences:

- **Claude Code** — the OAuth **access and refresh tokens**, tokens for connected **MCP servers**, the account configuration file (user and machine identifiers), and the **`CLAUDE.md`** standing-instruction file.
- **Codex** — the authentication file holding an **OpenAI API key** plus access and refresh tokens (referred to as "Codex CLI" in WardenStealer logs).
- **GitHub Copilot and Cursor** — token files (seen in Aoki logs).
- **Claude Desktop / ChatGPT desktop** — configuration, plan/usage history and Netscape-format session cookies.

As SpyCloud notes, resetting a password does not revoke these tokens, which is what makes them valuable.

**The market adjusted in step.** SpyCloud shows the buyer's side: a **$100 Codex API credit advertised for $8.94** (and a $100 Claude API token for the same), a Russian-language shop selling Claude/ChatGPT/Grok subscriptions **40–60% below list**, a Telegram bot offering OpenAI/Anthropic access **up to 91% off** with $1 deposits, and a wholesale service paying suppliers **35% of billings** for Anthropic and AWS-Bedrock Claude keys (20% for OpenAI).

**The limits, stated by SpyCloud.** This is a capability-and-market trend, not a named-victim breach. SpyCloud is explicit that it **cannot confirm that all of the material being sold was taken by infostealer malware**, and it does not document confirmed abuse of victim credentials from these two families (the oft-cited $46,000/day figure is a 2024 Sysdig estimate; the Storm-2139 case is from 2024 and involved stolen Azure OpenAI keys). This record keeps those limits.

**How it is graded.** `research` — a vendor analysis of its own telemetry and the criminal market, not an incident with a named victim. `CRED` (what is harvested is **reusable credentials** — OAuth tokens, MCP tokens, API keys) + `EXFIL` (those credentials leave the machine in stealer logs). `real_harm: false`: the harvesting is real and measured (130,000+ WardenStealer infections), but SpyCloud confirms **no specific downstream account takeover** tied to these families — the same basis as the archive's Gen Digital record. Severity `medium`: the underlying data (reusable tokens and MCP credentials) is genuinely sensitive and the trend is one-way. Confidence `A`: SpyCloud's own recaptured-data analysis, corroborated independently by Symantec's Aoki report (via Infosecurity Magazine) and Cyber Security News. `ai_involvement: confirmed`: the targeted artifacts are AI-agent credentials and instruction files. This is the **escalation** of the trend first recorded for Gen Digital (8 September 2026) — now specifically AI coding-tool OAuth/MCP tokens and a priced resale market.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | SpyCloud ("Infostealers now target AI tokens and API keys") | <https://spycloud.com/blog/infostealers-now-target-ai-tokens-and-api-keys/> |
| 2 | Infosecurity Magazine (Aoki infostealer / Symantec) | <https://www.infosecurity-magazine.com/news/aoki-infostealer-ai-coding/> |
| 3 | Cyber Security News | <https://cybersecuritynews.com/hackers-use-new-infostealer-malware/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-10-30` (raw: 2026-10-30 SpyCloud report; WardenStealer first seen 2026-08-03, Aoki 2026-10-04, precision `day`) |
| Kind | Research / vendor analysis `research` |
| Type | [`CRED`](../../taxonomy/types.md#cred) [`EXFIL`](../../taxonomy/types.md#exfil) |
| Severity | **Medium** `medium` |
| Confidence | **A** — SpyCloud's own recaptured-data analysis, with independent Symantec (Aoki) and Cyber Security News corroboration |
| Real harm | No — harvesting is real and measured, but SpyCloud confirms no specific downstream account takeover |
| AI involvement | Confirmed `confirmed` — the targeted artifacts are AI-agent credentials and instruction files |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-10-30-spycloud-ai-coding-tool-token-theft` |

<sub>**Why this classification:** A vendor analysis of SpyCloud's own recaptured malware logs and the criminal market (`research`), showing infostealers harvesting reusable AI coding-tool credentials — OAuth/MCP tokens, API keys (`CRED`) — that leave the machine in stealer logs (`EXFIL`). `real_harm: false`: the trend is real and measured but SpyCloud confirms no specific downstream account takeover tied to these families (same basis as the Gen Digital record). `medium` severity because the data is genuinely sensitive. Confidence `A` — SpyCloud's own data plus independent Symantec and Cyber Security News reporting. Dated to SpyCloud's post (30 October 2026). Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-09-08` [Infostealers turn to AI-agent data: collection rules now target Claude, Cursor and Codex](../2026-09/2026-09-08-gen-digital-infostealers-ai-agent-data.md)<br>  <sub>The same trend, first recorded — this SpyCloud report is its escalation (named families, OAuth/MCP tokens, priced market)</sub>
- `2026-10-17` [OpenCode Console breach leaks stored AI API keys](2026-10-17-opencode-console-breach-api-keys.md)<br>  <sub>Where stolen AI credentials turned into named, billed abuse</sub>
- `2026-06-24` [Operation Endgame (Europol) takes down StealC and Amadey](../2026-06/2026-06-24-operation-endgame-europol-stealc.md)<br>  <sub>The commodity-stealer market this behaviour rides on</sub>

---

[← 2026-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-10/2026-10-30-spycloud-ai-coding-tool-token-theft.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
