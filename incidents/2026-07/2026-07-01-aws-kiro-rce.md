---
id: 2026-07-01-aws-kiro-rce
title: "AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)"
title_zh: "AWS Kiro：让它总结一个网页，就能拿到 RCE（CVE-2026-10591）"
title_ja: "AWS Kiro：Webページの要約を頼むとRCE（CVE-2026-10591）"
title_ko: "AWS Kiro: 웹 페이지 요약을 요청하면 RCE (CVE-2026-10591)"
title_de: "AWS Kiro: bitte um eine Zusammenfassung einer Webseite, Ergebnis RCE (CVE-2026-10591)"
title_fr: "AWS Kiro : demandez-lui de résumer une page web, obtenez un RCE (CVE-2026-10591)"
title_es: "AWS Kiro: pídele que resuma una página web y obtén RCE (CVE-2026-10591)"
date: 2026-07-01
date_precision: month
date_raw: "2026-07"

kind: research
type: [MCP, SANDBOX]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Intezer and Kodem Security. When Kiro fetches or searches external content and hits a page with hidden instructions → the instructions make Kiro **use its own file-writing tool to write attacker content into `~/.kiro/settings/mcp.json`, with no user approval required** → Kiro reloads the config and launches that malicious MCP server → attacker code runs with the developer's privileges.
  In the researchers' words: **"A request as ordinary as 'summarise this page for me' can end in remote code execution."** Fixed in 0.11.130


summary_zh: |
  Intezer 与 Kodem Security。Kiro 抓取或搜索外部内容时，命中带隐藏指令的页面 → 指令让 Kiro **用自己的文件写入工具把攻击者内容写进 `~/.kiro/settings/mcp.json`，且无需用户批准** → Kiro 重载配置并启动那个恶意 MCP server → 以开发者权限执行攻击者代码。
  研究者的原话是：**「一个像『帮我总结这个页面』一样普通的请求，就能以远程代码执行收场。」** 0.11.130 修复

summary_ja: |
  IntezerとKodem Security。Kiroが外部コンテンツを取得・検索し、隠された指示のあるページに遭遇すると→指示によりKiroが**自身のファイル書き込みツールで`~/.kiro/settings/mcp.json`に攻撃者のコンテンツを書き込み、ユーザー承認は不要**→Kiroが設定を再読み込みし、その悪性MCPサーバーを起動→攻撃者のコードが開発者の権限で実行される。
  研究者の言葉：**「『このページを要約して』というごく普通の依頼が、リモートコード実行に行き着き得る。」** 0.11.130で修正

summary_ko: |
  Intezer와 Kodem Security. Kiro가 외부 콘텐츠를 가져오거나 검색하다 숨겨진 지시가 있는 페이지를 만나면 → 그 지시가 Kiro로 하여금 **자체 파일 쓰기 도구로 공격자 콘텐츠를 `~/.kiro/settings/mcp.json`에 기록하게 하며 사용자 승인이 필요 없다** → Kiro가 설정을 다시 로드하고 그 악성 MCP 서버를 실행한다 → 공격자 코드가 개발자 권한으로 실행된다.
  연구진의 표현: **"'이 페이지 요약해 줘'처럼 평범한 요청이 원격 코드 실행으로 끝날 수 있다."** 0.11.130에서 수정

summary_de: |
  Intezer und Kodem Security. Wenn Kiro externe Inhalte abruft oder durchsucht und auf eine Seite mit versteckten Anweisungen stößt → bringen die Anweisungen Kiro dazu, **mit seinem eigenen Dateischreib-Tool Angreifer-Inhalte in `~/.kiro/settings/mcp.json` zu schreiben, ohne dass eine Nutzergenehmigung nötig ist** → Kiro lädt die Konfiguration neu und startet diesen bösartigen MCP-Server → der Code des Angreifers läuft mit den Rechten des Entwicklers.
  In den Worten der Forschenden: **„Eine Anfrage so gewöhnlich wie ‚fasse mir diese Seite zusammen' kann in Remote Code Execution enden.“** Behoben in 0.11.130

summary_fr: |
  Intezer et Kodem Security. Quand Kiro récupère ou recherche du contenu externe et tombe sur une page aux instructions cachées → les instructions font que Kiro **utilise son propre outil d'écriture de fichiers pour écrire le contenu de l'attaquant dans `~/.kiro/settings/mcp.json`, sans aucune approbation de l'utilisateur** → Kiro recharge la configuration et lance ce serveur MCP malveillant → le code de l'attaquant s'exécute avec les privilèges du développeur.
  Pour reprendre les chercheurs : **« Une requête aussi ordinaire que “résume-moi cette page” peut finir en exécution de code à distance. »** Corrigé en 0.11.130

summary_es: |
  Intezer y Kodem Security. Cuando Kiro obtiene o busca contenido externo y topa con una página con instrucciones ocultas → las instrucciones hacen que Kiro **use su propia herramienta de escritura de archivos para escribir contenido del atacante en `~/.kiro/settings/mcp.json`, sin requerir aprobación del usuario** → Kiro recarga la configuración y lanza ese servidor MCP malicioso → el código del atacante se ejecuta con los privilegios del desarrollador.
  En palabras de los investigadores: **"Una petición tan ordinaria como 'resúmeme esta página' puede acabar en ejecución remota de código."** Corregido en 0.11.130

sources:
  - url: https://thehackernews.com/2026/07/aws-kiro-flaw-let-poisoned-web-page.html
    label: THN
  - url: https://www.kodemsecurity.com/resources/aws-kiro-agentic-ide-rce-prompt-injection-mcp-config-vulnerability
    label: Kodem

disputed: false
landmark: true
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## Summary

Intezer and Kodem Security. When Kiro fetches or searches external content and hits a page with hidden instructions → the instructions make Kiro **use its own file-writing tool to write attacker content into `~/.kiro/settings/mcp.json`, with no user approval required** → Kiro reloads the config and launches that malicious MCP server → attacker code runs with the developer's privileges.

In the researchers' words: **"A request as ordinary as 'summarise this page for me' can end in remote code execution."** Fixed in 0.11.130

## Attack chain

```mermaid
flowchart LR
    E["Malicious MCP server or tool description"]:::entry
    S0["The agent toolchain loads and trusts it"]:::step
    S1["Residual egress path"]:::step
    I["Escape to a real system<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | THN | <https://thehackernews.com/2026/07/aws-kiro-flaw-let-poisoned-web-page.html> |
| 2 | Kodem | <https://www.kodemsecurity.com/resources/aws-kiro-agentic-ide-rce-prompt-injection-mcp-config-vulnerability> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-01` (raw: 2026-07, precision `month`) |
| Kind | Research demo `research` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain · [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-07-01-aws-kiro-rce` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md) · [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2026-07-01` [DuneSlide: zero-click sandbox escape in Cursor](2026-07-01-duneslide-cursor-ling-dian-ji.md)<br>  <sub>DuneSlide: zero-click sandbox escape in Cursor</sub>
- `2026-07-09` [GhostApproval: an approval bypass shared by six AI coding assistants](2026-07-09-ghostapproval-kuan-bian-ma-zhu.md)<br>  <sub>GhostApproval: an approval bypass shared by six AI coding assistants</sub>
- `2026-07-30` [RufRoot (CVE-2026-59726): perfect CVSS, summons a rogue AI swarm](2026-07-30-rufroot-man-fen-zhao-huan.md)<br>  <sub>RufRoot (CVE-2026-59726): perfect CVSS, summons a rogue AI swarm</sub>
- `2026-07-20` [Six sandbox escapes across four coding agents in one week](2026-07-20-agent-yi-nei-kuan-bian.md)<br>  <sub>Six sandbox escapes across four coding agents in one week</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-01-aws-kiro-rce.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
