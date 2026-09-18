---
id: 2026-08-17-snowflake-jira-zhao-dao-can
title: "AI finds a flaw AI helped write: Snowflake's Jira token"
title_zh: "AI 找到了 AI 参与写的漏洞：Snowflake 的 Jira 令牌"
title_ja: "AIがAIの書いた欠陥を発見：SnowflakeのJiraトークン"
title_ko: "AI가 AI가 작성에 기여한 결함을 찾다: Snowflake의 Jira 토큰"
title_de: "KI findet einen Fehler, den KI mitschreiben half: Snowflakes Jira-Token"
title_fr: "L'IA trouve une faille que l'IA a aidé à écrire : le jeton Jira de Snowflake"
title_es: "La IA encuentra un fallo que la IA ayudó a escribir: el token de Jira de Snowflake"
date: 2026-08-17
date_precision: day
date_raw: "2026-08-17"

kind: research
type: [CRED, SUPPLY]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  In a GitHub Actions workflow of `snowflakedb/snowflake-connector-net` (which automatically files a Jira ticket when an issue is opened), **a change co-authored under the label "Copilot Autofix powered by AI" on 2026-06-18** introduced a script injection flaw — the issue title was expanded straight into a shell command instead of being passed through an environment variable, which could be used to exfiltrate Jira credentials.
  It was found by **Wiz's autonomous "Red Agent"** (reported 2026-06-23); Snowflake fixed it and rotated the token the same day, confirming that no third party other than Wiz accessed it during the 5-day exposure window. Wiz published the full analysis on 2026-08-17.
  ⚠️ **GitHub disputes the characterisation**: the flawed workflow logic can be traced back to **a commit by a human Snowflake engineer in 2025-08**, and the Autofix "co-author" tag was only attached during the 2026-06-18 squash merge. **The record must keep both accounts side by side**


summary_zh: |
  `snowflakedb/snowflake-connector-net` 的一个 GitHub Actions 工作流（开 issue 时自动建 Jira 工单）中，**2026-06-18 一次标注为「Copilot Autofix powered by AI」共同署名的变更**引入了脚本注入缺陷 —— issue 标题被直接展开进 shell 命令而非经环境变量传递，可用于外带 Jira 凭据。
  发现方是 **Wiz 的自主「Red Agent」**（2026-06-23 报告），Snowflake 当天修复并轮换令牌，确认 5 天暴露窗口内除 Wiz 外无第三方访问。Wiz 2026-08-17 发布完整分析。
  ⚠️ **GitHub 对定性提出异议**：有问题的工作流逻辑可追溯到 **2025 年 8 月一名 Snowflake 人类工程师的提交**，Autofix 的「共同作者」标签是在 2026-06-18 的 squash 合并中才被附上的。**入库须并列两种说法**

summary_ja: |
  `snowflakedb/snowflake-connector-net`のGitHub Actionsワークフロー（イシューが開かれると自動でJiraチケットを作成する）で、**2026-06-18に「Copilot Autofix powered by AI」のラベルで共同作成された変更**がスクリプトインジェクションの欠陥を持ち込んだ——イシューのタイトルが環境変数を経由せずシェルコマンドに直接展開され、Jiraの認証情報の外部送信に利用できた。
  発見したのは**Wizの自律型「Red Agent」**（2026-06-23に報告）。Snowflakeは同日中に修正してトークンをローテーションし、5日間の露出期間中にWiz以外の第三者がアクセスしていないことを確認した。Wizは2026-08-17に完全な分析を公開した。
  ⚠️ **GitHubはこの位置づけに異議を唱えている**：欠陥のあるワークフローロジックは**2025-08のSnowflakeの人間のエンジニアによるコミット**に遡り、Autofixの「共同作成」タグは2026-06-18のsquashマージ時に付いただけだとしている。**記録は両方の主張を併記する必要がある**

summary_ko: |
  `snowflakedb/snowflake-connector-net`의 GitHub Actions 워크플로(이슈가 열리면 자동으로 Jira 티켓을 생성한다)에서 **2026-06-18에 "Copilot Autofix powered by AI" 레이블로 공동 작성된 변경**이 스크립트 인젝션 결함을 도입했다 — 이슈 제목이 환경 변수를 거치지 않고 셸 명령으로 곧바로 확장되어 Jira 자격 증명을 유출하는 데 쓰일 수 있었다.
  이는 **Wiz의 자율 "Red Agent"**가 발견했고(2026-06-23 보고), Snowflake는 같은 날 수정하고 토큰을 교체했으며 5일의 노출 기간에 Wiz 외 제3자가 접근하지 않았음을 확인했다. Wiz는 2026-08-17에 전체 분석을 공개했다.
  ⚠️ **GitHub은 이 규정에 이견을 제기한다**: 결함 있는 워크플로 로직은 **2025-08 Snowflake 사람 엔지니어의 커밋**으로 거슬러 올라가며, Autofix "공동 작성" 태그는 2026-06-18 스쿼시 병합 때에야 붙었다. **기록은 두 설명을 나란히 유지해야 한다**

summary_de: |
  In einem GitHub-Actions-Workflow von `snowflakedb/snowflake-connector-net` (der beim Öffnen eines Issues automatisch ein Jira-Ticket anlegt) **führte eine Änderung, die am 2026-06-18 unter dem Label „Copilot Autofix powered by AI“ als Mitautor geführt wurde**, einen Script-Injection-Fehler ein — der Issue-Titel wurde direkt in einen Shell-Befehl expandiert, statt über eine Umgebungsvariable übergeben zu werden, was zur Exfiltration von Jira-Zugangsdaten genutzt werden konnte.
  Gefunden wurde es von **Wizs autonomem „Red Agent“** (gemeldet am 2026-06-23); Snowflake behob es und rotierte das Token am selben Tag und bestätigte, dass während des 5-tägigen Expositionsfensters kein Dritter außer Wiz darauf zugegriffen hat. Wiz veröffentlichte die vollständige Analyse am 2026-08-17.
  ⚠️ **GitHub bestreitet die Darstellung**: Die fehlerhafte Workflow-Logik lässt sich auf **einen Commit eines menschlichen Snowflake-Ingenieurs im 2025-08** zurückverfolgen, und das „Co-Autor“-Tag von Autofix wurde erst beim Squash-Merge am 2026-06-18 angehängt. **Der Eintrag muss beide Darstellungen nebeneinander festhalten**

summary_fr: |
  Dans un workflow GitHub Actions de `snowflakedb/snowflake-connector-net` (qui ouvre automatiquement un ticket Jira quand une issue est créée), **une modification co-signée sous l'étiquette « Copilot Autofix powered by AI » le 2026-06-18** a introduit une faille d'injection de script — le titre de l'issue était développé directement dans une commande shell au lieu de passer par une variable d'environnement, ce qui pouvait servir à exfiltrer les identifiants Jira.
  Elle a été trouvée par **le « Red Agent » autonome de Wiz** (signalé le 2026-06-23) ; Snowflake l'a corrigée et a renouvelé le jeton le jour même, confirmant qu'aucun tiers autre que Wiz n'y a accédé pendant la fenêtre d'exposition de 5 jours. Wiz a publié l'analyse complète le 2026-08-17.
  ⚠️ **GitHub conteste cette caractérisation** : la logique de workflow défectueuse remonte à **un commit d'un ingénieur Snowflake humain en 2025-08**, et l'étiquette de « co-auteur » Autofix n'a été attachée que lors du squash merge du 2026-06-18. **L'enregistrement doit conserver les deux versions côte à côte**

summary_es: |
  En un flujo de trabajo de GitHub Actions de `snowflakedb/snowflake-connector-net` (que abre automáticamente un ticket de Jira cuando se crea un issue), **un cambio coautorado bajo la etiqueta "Copilot Autofix powered by AI" el 2026-06-18** introdujo un fallo de inyección de script — el título del issue se expandía directamente dentro de un comando de shell en lugar de pasarse por una variable de entorno, lo que podía usarse para exfiltrar credenciales de Jira.
  Lo encontró el **"Red Agent" autónomo de Wiz** (reportado el 2026-06-23); Snowflake lo corrigió y rotó el token ese mismo día, confirmando que ningún tercero aparte de Wiz accedió a él durante la ventana de exposición de 5 días. Wiz publicó el análisis completo el 2026-08-17.
  ⚠️ **GitHub discute esta caracterización**: la lógica defectuosa del flujo de trabajo se remonta a **un commit de un ingeniero humano de Snowflake en 2025-08**, y la etiqueta de "coautoría" de Autofix solo se añadió durante el squash merge del 2026-06-18. **El registro debe mantener ambas versiones una junto a la otra**

sources:
  - url: https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug
    label: Wiz
  - url: https://thehackernews.com/2026/08/snowflake-github-actions-flaw-lets_0330881554.html
    label: THN

disputed: false
landmark: true
scan_month: 2026-08
scan_ref: "SCAN.md §6 2026-08"
---

# AI finds a flaw AI helped write: Snowflake's Jira token

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## Summary

In a GitHub Actions workflow of `snowflakedb/snowflake-connector-net` (which automatically files a Jira ticket when an issue is opened), **a change co-authored under the label "Copilot Autofix powered by AI" on 2026-06-18** introduced a script injection flaw — the issue title was expanded straight into a shell command instead of being passed through an environment variable, which could be used to exfiltrate Jira credentials.

It was found by **Wiz's autonomous "Red Agent"** (reported 2026-06-23); Snowflake fixed it and rotated the token the same day, confirming that no third party other than Wiz accessed it during the 5-day exposure window. Wiz published the full analysis on 2026-08-17.

⚠️ **GitHub disputes the characterisation**: the flawed workflow logic can be traced back to **a commit by a human Snowflake engineer in 2025-08**, and the Autofix "co-author" tag was only attached during the 2026-06-18 squash merge. **The record must keep both accounts side by side**

## Attack chain

```mermaid
flowchart LR
    E["Credentials within an agent's reach"]:::entry
    S0["The agent picks them up and calls out"]:::step
    S1["Developer or agent installs it automatically"]:::step
    I["Credential theft and self-propagation<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Wiz | <https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug> |
| 2 | THN | <https://thehackernews.com/2026/08/snowflake-github-actions-flaw-lets_0330881554.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-08-17` (raw: 2026-08-17, precision `day`) |
| Kind | Research demo `research` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse · [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-08-17-snowflake-jira-zhao-dao-can` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-08-04` [CHAINDROP npm worm](2026-08-04-chaindrop-npm-ru-chong.md)<br>  <sub>CHAINDROP npm worm</sub>
- `2026-08-01` [Azure SRE Agent privilege escalation (CVE-2026-62830)](2026-08-01-azure-sre-agent.md)<br>  <sub>Azure SRE Agent privilege escalation (CVE-2026-62830)</sub>
- `2026-08-18` [Context7 MCP prompt injection (CVE-2026-75130)](2026-08-18-context7-mcp-ti-shi-zhu.md)<br>  <sub>Context7 MCP prompt injection (CVE-2026-75130)</sub>
- `2026-09-01` [GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted](../2026-09/2026-09-01-gitspawn-git-config-pre-model-rce.md)<br>  <sub>GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted</sub>

---

[← 2026-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-08/2026-08-17-snowflake-jira-zhao-dao-can.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
