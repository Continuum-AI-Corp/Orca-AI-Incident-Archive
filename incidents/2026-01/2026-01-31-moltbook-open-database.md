---
id: 2026-01-31-moltbook-open-database
title: "Moltbook database fully open"
title_zh: "Moltbook 数据库全开"
title_ja: "Moltbookのデータベースが完全に公開状態"
title_ko: "Moltbook 데이터베이스 완전 개방"
title_de: "Moltbook-Datenbank vollständig offen"
title_fr: "La base de données de Moltbook grande ouverte"
title_es: "La base de datos de Moltbook, totalmente abierta"
date: 2026-01-31
date_precision: day
date_raw: "2026-01-31"

kind: incident
type: [CRED]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Moltbook (a "Reddit where only AI agents can post", launched by Matt Schlicht on **2026-01-28**, which eventually accumulated **1.7 million registered agents and nearly 7 million comments**) hard-coded its **Supabase API key in client-side JS** and **never enabled Row Level Security** — anyone who opened developer tools could read and write the production database unauthenticated. Wiz researchers **Gal Nagli** and Jamieson O'Reilly found it independently. Exposed: **about 1.5 million API auth tokens, 35,000 email addresses and 4,000 private messages**. The fix took just two lines of SQL


summary_zh: |
  Moltbook（**2026-01-28** 由 Matt Schlicht 上线的「只有 AI agent 能发帖的 Reddit」，最终积累 **170 万注册 agent、近 700 万条评论**）把 **Supabase API key 硬编码在客户端 JS** 里，且 **Row Level Security 从未启用** —— 任何人打开开发者工具即可对生产库无认证读写。Wiz 研究员 **Gal Nagli** 与 Jamieson O'Reilly 独立发现。暴露 **约 150 万个 API 认证 token、3.5 万个邮箱、4,000 条私信**。修复只需两行 SQL

summary_ja: |
  Moltbook（「AIエージェントだけが投稿できるReddit」。Matt Schlicht氏が**2026-01-28**に公開し、最終的に**170万の登録エージェントと約700万件のコメント**を蓄積）は、**Supabase APIキーをクライアント側JSにハードコード**し、**Row Level Securityを一度も有効化していなかった**——開発者ツールを開いた誰もが、認証なしで本番データベースを読み書きできた。Wizの研究者**Gal Nagli氏**とJamieson O'Reilly氏が独立に発見。露出：**約150万件のAPI認証トークン、35,000件のメールアドレス、4,000件のプライベートメッセージ**。修正はわずか2行のSQLで済んだ

summary_ko: |
  Moltbook("AI 에이전트만 글을 쓸 수 있는 Reddit"으로, **2026-01-28** Matt Schlicht가 출시했고 최종적으로 **등록 에이전트 170만 개와 댓글 약 700만 개**를 축적했다)은 **Supabase API 키를 클라이언트 측 JS에 하드코딩**했고 **행 수준 보안(RLS)을 전혀 활성화하지 않았다** — 개발자 도구를 연 사람은 누구나 무인증으로 프로덕션 데이터베이스를 읽고 쓸 수 있었다. Wiz 연구원 **Gal Nagli**와 Jamieson O'Reilly가 각각 독립적으로 발견했다. 노출된 것: **API 인증 토큰 약 150만 개, 이메일 주소 35,000개, 비공개 메시지 4,000건**. 수정에는 SQL 두 줄이면 충분했다

summary_de: |
  Moltbook (ein „Reddit, in dem nur KI-Agenten posten können“, am **2026-01-28** von Matt Schlicht gestartet und später mit **1.7 Millionen registrierten Agenten und fast 7 Millionen Kommentaren**) kodierte seinen **Supabase-API-Schlüssel fest im clientseitigen JS** und **aktivierte niemals Row Level Security** — jeder, der die Entwicklertools öffnete, konnte die Produktionsdatenbank unauthentifiziert lesen und beschreiben. Die Wiz-Forscher **Gal Nagli** und Jamieson O'Reilly fanden es unabhängig voneinander. Preisgegeben: **etwa 1.5 Millionen API-Auth-Token, 35,000 E-Mail-Adressen und 4,000 private Nachrichten**. Die Behebung erforderte nur zwei Zeilen SQL

summary_fr: |
  Moltbook (un « Reddit où seuls les agents IA peuvent publier », lancé par Matt Schlicht le **2026-01-28**, qui a fini par accumuler **1,7 million d'agents enregistrés et près de 7 millions de commentaires**) avait **codé en dur sa clé API Supabase dans le JS côté client** et **n'avait jamais activé la Row Level Security** — quiconque ouvrait les outils de développement pouvait lire et écrire la base de production sans authentification. Les chercheurs Wiz **Gal Nagli** et Jamieson O'Reilly l'ont trouvée indépendamment. Exposés : **environ 1,5 million de jetons d'authentification API, 35 000 adresses e-mail et 4 000 messages privés**. Le correctif a pris deux lignes de SQL

summary_es: |
  Moltbook (un "Reddit donde solo los agentes de IA pueden publicar", lanzado por Matt Schlicht el **2026-01-28**, que llegó a acumular **1.7 millones de agentes registrados y casi 7 millones de comentarios**) codificó de forma fija su **clave de API de Supabase en el JS del lado del cliente** y **nunca habilitó Row Level Security** — cualquiera que abriera las herramientas de desarrollador podía leer y escribir la base de datos de producción sin autenticación. Los investigadores de Wiz **Gal Nagli** y Jamieson O'Reilly lo encontraron de forma independiente. Expuesto: **unos 1.5 millones de tokens de autenticación de API, 35,000 direcciones de correo y 4,000 mensajes privados**. La corrección tomó solo dos líneas de SQL

sources:
  - url: https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys
    label: Wiz
  - url: https://www.implicator.ai/moltbook-left-every-ai-agents-api-keys-in-an-open-database-security-researcher-finds/
    label: Implicator

disputed: false
landmark: true
scan_month: 2026-01
scan_ref: "SCAN.md §6 2026-01"
---

# Moltbook database fully open

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

Moltbook (a "Reddit where only AI agents can post", launched by Matt Schlicht on **2026-01-28**, which eventually accumulated **1.7 million registered agents and nearly 7 million comments**) hard-coded its **Supabase API key in client-side JS** and **never enabled Row Level Security** — anyone who opened developer tools could read and write the production database unauthenticated. Wiz researchers **Gal Nagli** and Jamieson O'Reilly found it independently. Exposed: **about 1.5 million API auth tokens, 35,000 email addresses and 4,000 private messages**. The fix took just two lines of SQL

## Attack chain

```mermaid
flowchart LR
    E["Credentials within an agent's reach"]:::entry
    S0["agent retrieves and uses them"]:::step
    I["Credential abuse"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Wiz | <https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys> |
| 2 | Implicator | <https://www.implicator.ai/moltbook-left-every-ai-agents-api-keys-in-an-open-database-security-researcher-finds/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-01-31` (raw: 2026-01-31, precision `day`) |
| Kind | Incident `incident` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-01-31-moltbook-open-database` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2026-01-26` [Clawdbot gateways exposed at scale](2026-01-26-clawdbot-wang-guan-gui-mo.md)<br>  <sub>Clawdbot gateways exposed at scale</sub>
- `2026-01-31` [Step Finance treasury drained](2026-01-31-step-finance-jin-ku-dao.md)<br>  <sub>Step Finance treasury drained</sub>
- `2025-12-15` ["Privacy" browser extensions resell AI conversations](../2025-12/2025-12-15-yin-si-liu-lan-qi.md)<br>  <sub>"Privacy" browser extensions resell AI conversations</sub>
- `2025-12-30` [Chrome extensions steal ChatGPT and DeepSeek conversations](../2025-12/2025-12-30-chrome-chatgpt-deepseek.md)<br>  <sub>Chrome extensions steal ChatGPT and DeepSeek conversations</sub>

---

[← 2026-01 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-01/2026-01-31-moltbook-open-database.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
