---
id: 2026-06-18-autojack-autogen-studio
title: "AutoJack: one web page from AutoGen Studio to the host"
title_zh: "AutoJack：AutoGen Studio 一个网页打穿宿主"
title_ja: "AutoJack：1つのWebページからAutoGen Studioを経てホストへ"
title_ko: "AutoJack: 웹 페이지 하나에서 AutoGen Studio를 거쳐 호스트까지"
title_de: "AutoJack: von einer Webseite in AutoGen Studio bis zum Host"
title_fr: "AutoJack : une page web pour aller d'AutoGen Studio à l'hôte"
title_es: "AutoJack: de una página web al host a través de AutoGen Studio"
date: 2026-06-18
date_precision: day
date_raw: "2026-06-18"

kind: research
type: [INFRA]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Microsoft's own review: three weaknesses chain together — ① the Origin check only allows 127.0.0.1/localhost, but **the JS loaded by the agent's headless browser is itself localhost**, so it passes ② the auth middleware excludes MCP paths, while the WebSocket side was supposed to authenticate on its own but never implemented it ③ the URL's `server_params` are base64-decoded and passed straight into the launch arguments, **with no allowlist of what may be executed** (`calc.exe` or a shell can both be launched as an MCP server). Fixed in main branch commit b047730; public version 0.4.2.2 does not contain that path


summary_zh: |
  Microsoft 自查：三个弱点串联 —— ① Origin 判定只允许 127.0.0.1/localhost，但 **agent 的无头浏览器加载的 JS 就是 localhost**，直接放行 ② 认证中间件把 MCP 路径排除在外，而 WebSocket 侧本应自行认证却没实现 ③ URL 的 `server_params` base64 解码后直传启动参数，**无执行对象白名单**（`calc.exe` 或 shell 都能当 MCP server 启动）。main 分支 commit b047730 修复；公开版 0.4.2.2 不含该路径

summary_ja: |
  Microsoft自身のレビュー：3つの弱点が連鎖する——① Originチェックは127.0.0.1/localhostのみを許可するが、**エージェントのヘッドレスブラウザが読み込むJS自体がlocalhostなので通過してしまう** ② 認証ミドルウェアがMCPパスを除外しており、WebSocket側は独自に認証するはずが実装されていなかった ③ URLの`server_params`がbase64デコードされ、そのまま起動引数に渡される——**何を実行してよいかの許可リストがない**（`calc.exe`もシェルもMCPサーバーとして起動できる）。mainブランチのコミットb047730で修正。公開版0.4.2.2にはこのパスは含まれない

summary_ko: |
  마이크로소프트 자체 검토: 세 가지 약점이 연쇄한다 — ① Origin 검사가 127.0.0.1/localhost만 허용하지만 **에이전트의 헤드리스 브라우저가 로드한 JS 자체가 localhost**여서 통과된다 ② 인증 미들웨어가 MCP 경로를 제외하는데, WebSocket 쪽은 스스로 인증하도록 되어 있었으나 구현되지 않았다 ③ URL의 `server_params`가 base64 디코딩되어 실행 인자로 그대로 전달되며 **무엇을 실행할 수 있는지에 대한 허용 목록이 없다**(`calc.exe`든 셸이든 MCP 서버로 실행될 수 있다). main 브랜치 커밋 b047730에서 수정되었고 공개 버전 0.4.2.2에는 해당 경로가 없다

summary_de: |
  Microsofts eigene Analyse: Drei Schwächen verketten sich — ① Die Origin-Prüfung erlaubt nur 127.0.0.1/localhost, doch **das vom Headless-Browser des Agenten geladene JS stammt selbst von localhost**, weshalb es durchgeht ② Die Authentifizierungs-Middleware nimmt MCP-Pfade aus, während die WebSocket-Seite sich eigentlich selbst authentifizieren sollte, dies aber nie umgesetzt wurde ③ Die `server_params` der URL werden base64-dekodiert und direkt in die Startargumente übergeben, **ohne Positivliste dessen, was ausgeführt werden darf** (`calc.exe` oder eine Shell lassen sich gleichermaßen als MCP-Server starten). Behoben im Commit b047730 des Hauptzweigs; die öffentliche Version 0.4.2.2 enthält diesen Pfad nicht

summary_fr: |
  La propre revue de Microsoft : trois faiblesses s'enchaînent — ① la vérification d'Origin n'autorise que 127.0.0.1/localhost, mais **le JS chargé par le navigateur headless de l'agent est lui-même localhost**, donc il passe ② le middleware d'authentification exclut les chemins MCP, tandis que le côté WebSocket était censé s'authentifier de lui-même mais ne l'a jamais implémenté ③ les `server_params` de l'URL sont décodés en base64 et passés directement dans les arguments de lancement, **sans liste blanche de ce qui peut être exécuté** (`calc.exe` ou un shell peuvent tous deux être lancés comme serveur MCP). Corrigé dans le commit b047730 de la branche main ; la version publique 0.4.2.2 ne contient pas ce chemin

summary_es: |
  La propia revisión de Microsoft: tres debilidades se encadenan — ① la comprobación de Origin solo permite 127.0.0.1/localhost, pero **el JS que carga el navegador headless del agente es él mismo localhost**, así que pasa ② el middleware de autenticación excluye las rutas MCP, mientras que el lado del WebSocket debía autenticarse por su cuenta pero nunca lo implementó ③ los `server_params` de la URL se decodifican de base64 y se pasan directamente a los argumentos de lanzamiento, **sin ninguna lista de permitidos de qué puede ejecutarse** (`calc.exe` o un shell pueden lanzarse como servidor MCP). Corregido en el commit b047730 de la rama main; la versión pública 0.4.2.2 no contiene esa ruta

sources:
  - url: https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/
    label: Microsoft

disputed: false
landmark: false
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# AutoJack: one web page from AutoGen Studio to the host

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

Microsoft's own review: three weaknesses chain together — ① the Origin check only allows 127.0.0.1/localhost, but **the JS loaded by the agent's headless browser is itself localhost**, so it passes ② the auth middleware excludes MCP paths, while the WebSocket side was supposed to authenticate on its own but never implemented it ③ the URL's `server_params` are base64-decoded and passed straight into the launch arguments, **with no allowlist of what may be executed** (`calc.exe` or a shell can both be launched as an MCP server). Fixed in main branch commit b047730; public version 0.4.2.2 does not contain that path

## Attack chain

```mermaid
flowchart LR
    E["Agent infrastructure exposed to the internet"]:::entry
    S0["Unauthenticated access"]:::step
    I["RCE / data leak<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Microsoft | <https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-18` (raw: 2026-06-18, precision `day`) |
| Kind | Research demo `research` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-18-autojack-autogen-studio` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-06-08` [LiteLLM CVE-2026-42271 MCP endpoint takeover](2026-06-08-litellm-mcp-duan-dian-jie.md)<br>  <sub>LiteLLM CVE-2026-42271 MCP endpoint takeover</sub>
- `2026-06-29` [DifyTap: four flaws leave 1M+ AI apps open to cross-tenant eavesdropping](2026-06-29-difytap-lou-dong-rang-wan.md)<br>  <sub>DifyTap: four flaws leave 1M+ AI apps open to cross-tenant eavesdropping</sub>
- `2026-06-28` [Langflow CVE-2026-33017 used for Monero mining](2026-06-28-langflow-yong-yu-men-luo.md)<br>  <sub>Langflow CVE-2026-33017 used for Monero mining</sub>
- `2026-06-17` [Vertex AI SDK bucket takeover leads to cross-tenant RCE](2026-06-17-vertex-sdk-rce.md)<br>  <sub>Vertex AI SDK bucket takeover leads to cross-tenant RCE</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-18-autojack-autogen-studio.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
