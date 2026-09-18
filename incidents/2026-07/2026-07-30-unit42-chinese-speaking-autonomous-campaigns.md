---
id: 2026-07-30-unit42-chinese-speaking-autonomous-campaigns
title: "Unit 42: autonomous campaigns run by Chinese-speaking operators"
title_zh: "Unit 42：中文使用者的自主攻击战役"
title_ja: "Unit 42：中国語話者の運用者による自律型キャンペーン"
title_ko: "Unit 42: 중국어권 운영자의 자율 작전"
title_de: "Unit 42: autonome Kampagnen chinesischsprachiger Betreiber"
title_fr: "Unit 42 : campagnes autonomes menées par des opérateurs sinophones"
title_es: "Unit 42: campañas autónomas dirigidas por operadores de habla china"
date: 2026-07-30
date_precision: day
date_raw: "2026-07-30"

kind: incident
type: [WEAPON]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [CN, GLOBAL]

summary: |
  The actor is based in **Zhuhai**, uses the handles knaithe / KnYuan, and runs an automated vulnerability-intelligence pipeline called 1DayNews. The main executor is **Hermes Agent + DeepSeek** (Claude Code was used only for connectivity tests and proxy validation, Codex only in a few tests). It tried **460+ targets** and 7 CVEs. **The autonomous part mostly failed on unmet preconditions** (the Langflow target had auto_login disabled, n8n had no unauthenticated public forms); **the manual part did succeed**: Citrix NetScaler CVE-2026-3055 exfiltrated data from **3 organizations**, Marimo command execution on **11 instances**, and Tomcat CVE-2026-34486 reverse-shell attempts against 9 servers. Malaysian government agencies were targeted over several consecutive days. Unit 42's judgement: **the margin between success and failure is small, and the autonomous attack loop is already operationally viable**


summary_zh: |
  行为者位于**珠海**，化名 knaithe / KnYuan，运营自动化漏洞情报流水线 1DayNews。主执行器是 **Hermes Agent + DeepSeek**（Claude Code 仅用于连通性测试与代理验证，Codex 仅少量测试）。尝试 **460+ 个目标**、7 个 CVE。**自主部分多因前提条件不满足而失败**（Langflow 目标没开 auto_login、n8n 没有未认证公开表单）；**手动部分确实得手**：Citrix NetScaler CVE-2026-3055 从 **3 个组织**外带数据、Marimo **11 个实例**命令执行、Tomcat CVE-2026-34486 对 9 台服务器尝试反弹 shell。马来西亚政府机构被连续多日针对。Unit 42 判断：**成败之差很小，自主攻击循环在运营上已经成立**

summary_ja: |
  アクターは**珠海（Zhuhai）**に拠点を置き、ハンドルはknaithe／KnYuan、1DayNewsという自動脆弱性インテリジェンスパイプラインを運用していた。主な実行者は**Hermes Agent＋DeepSeek**（Claude Codeは接続テストとプロキシ検証のみ、Codexは少数のテストのみ）。**460以上の標的**と7件のCVEを試行した。**自律部分は満たされない前提条件により大半が失敗**（Langflowの標的はauto_loginが無効、n8nには認証不要の公開フォームがなかった）。**手動部分は実際に成功した**：Citrix NetScaler CVE-2026-3055が**3組織**からデータを外部送信し、Marimoのコマンド実行が**11インスタンス**、Tomcat CVE-2026-34486のリバースシェル試行が9サーバーに対して行われた。マレーシアの政府機関が数日連続で標的とされた。Unit 42の判断：**成功と失敗の差は小さく、自律型攻撃ループはすでに運用上実行可能である**

summary_ko: |
  행위자는 **주하이**에 기반을 두고 핸들 knaithe / KnYuan을 사용하며 1DayNews라는 자동 취약점 인텔리전스 파이프라인을 운영한다. 주 실행자는 **Hermes Agent + DeepSeek**였다(Claude Code는 연결 테스트와 프록시 검증에만, Codex는 몇몇 테스트에만 사용되었다). **표적 460개 이상**과 CVE 7건을 시도했다. **자율 부분은 대부분 전제 조건이 충족되지 않아 실패했지만**(Langflow 표적은 auto_login이 꺼져 있었고, n8n은 무인증 공개 폼이 없었다) **수동 부분은 성공했다**: Citrix NetScaler CVE-2026-3055로 **3개 조직**의 데이터를 유출했고, **11개 인스턴스**에서 Marimo 명령 실행, 9개 서버에 Tomcat CVE-2026-34486 리버스 셸 시도를 했다. 말레이시아 정부 기관이 여러 날 연속으로 표적이 되었다. Unit 42의 판단: **성공과 실패의 차이는 작으며 자율 공격 루프는 이미 운영 가능한 수준이다**

summary_de: |
  Der Akteur sitzt in **Zhuhai**, nutzt die Handles knaithe / KnYuan und betreibt eine automatisierte Pipeline für Schwachstelleninformationen namens 1DayNews. Der Hauptausführer ist **Hermes Agent + DeepSeek** (Claude Code wurde nur für Konnektivitätstests und Proxy-Validierung genutzt, Codex nur in wenigen Tests). Er versuchte sich an **460+ Zielen** und 7 CVEs. **Der autonome Teil scheiterte überwiegend an unerfüllten Vorbedingungen** (beim Langflow-Ziel war auto_login deaktiviert, n8n hatte keine nicht authentifizierten öffentlichen Formulare); **der manuelle Teil gelang**: Citrix NetScaler CVE-2026-3055 exfiltrierte Daten aus **3 Organisationen**, Marimo-Befehlsausführung auf **11 Instanzen** und Reverse-Shell-Versuche über Tomcat CVE-2026-34486 gegen 9 Server. Malaysische Regierungsstellen wurden über mehrere aufeinanderfolgende Tage ins Visier genommen. Unit 42s Einschätzung: **Der Abstand zwischen Erfolg und Misserfolg ist klein, und die autonome Angriffsschleife ist operativ bereits tragfähig**

summary_fr: |
  L'acteur est basé à **Zhuhai**, utilise les pseudonymes knaithe / KnYuan, et exploite un pipeline automatisé de renseignement sur les vulnérabilités appelé 1DayNews. L'exécuteur principal est **Hermes Agent + DeepSeek** (Claude Code n'a servi qu'à des tests de connectivité et de validation de proxy, Codex qu'à quelques tests). Il a essayé **plus de 460 cibles** et 7 CVE. **La partie autonome a surtout échoué faute de préconditions remplies** (la cible Langflow avait auto_login désactivé, n8n n'avait pas de formulaires publics non authentifiés) ; **la partie manuelle a réussi** : CVE-2026-3055 de Citrix NetScaler a exfiltré des données de **3 organisations**, l'exécution de commandes Marimo sur **11 instances**, et des tentatives de reverse shell Tomcat CVE-2026-34486 contre 9 serveurs. Des agences gouvernementales malaisiennes ont été ciblées plusieurs jours consécutifs. Jugement d'Unit 42 : **la marge entre succès et échec est mince, et la boucle d'attaque autonome est déjà opérationnellement viable**

summary_es: |
  El actor tiene base en **Zhuhai**, usa los alias knaithe / KnYuan y gestiona una canalización automatizada de inteligencia de vulnerabilidades llamada 1DayNews. El ejecutor principal es **Hermes Agent + DeepSeek** (Claude Code solo se usó para pruebas de conectividad y validación de proxy, Codex solo en unas pocas pruebas). Probó **más de 460 objetivos** y 7 CVE. **La parte autónoma falló en su mayoría por precondiciones no cumplidas** (el objetivo Langflow tenía auto_login desactivado, n8n no tenía formularios públicos sin autenticación); **la parte manual sí tuvo éxito**: Citrix NetScaler CVE-2026-3055 exfiltró datos de **3 organizaciones**, ejecución de comandos en Marimo en **11 instancias**, e intentos de reverse shell contra Tomcat CVE-2026-34486 en 9 servidores. Se atacó a agencias del gobierno de Malasia durante varios días consecutivos. El juicio de Unit 42: **el margen entre éxito y fracaso es pequeño, y el bucle de ataque autónomo ya es operativamente viable**

sources:
  - url: https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/
    label: Unit 42
  - url: https://hunt.io/blog/chinese-operators-claude-deepseek-government-intrusion
    label: Hunt.io four-country report

disputed: false
landmark: true
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# Unit 42: autonomous campaigns run by Chinese-speaking operators

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

The actor is based in **Zhuhai**, uses the handles knaithe / KnYuan, and runs an automated vulnerability-intelligence pipeline called 1DayNews. The main executor is **Hermes Agent + DeepSeek** (Claude Code was used only for connectivity tests and proxy validation, Codex only in a few tests). It tried **460+ targets** and 7 CVEs. **The autonomous part mostly failed on unmet preconditions** (the Langflow target had auto_login disabled, n8n had no unauthenticated public forms); **the manual part did succeed**: Citrix NetScaler CVE-2026-3055 exfiltrated data from **3 organizations**, Marimo command execution on **11 instances**, and Tomcat CVE-2026-34486 reverse-shell attempts against 9 servers. Malaysian government agencies were targeted over several consecutive days. Unit 42's judgement: **the margin between success and failure is small, and the autonomous attack loop is already operationally viable**

## Attack chain

```mermaid
flowchart LR
    E["Attacker + jailbreak script"]:::entry
    S0["LLM orchestrator drives a cluster of sub-agents"]:::step
    I["Target systems compromised"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Unit 42 | <https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/> |
| 2 | Hunt.io four-country report | <https://hunt.io/blog/chinese-operators-claude-deepseek-government-intrusion> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-30` (raw: 2026-07-30, precision `day`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [China](../../regions/cn.md) · [Global](../../regions/global.md) |
| Archive ID | `2026-07-30-unit42-chinese-speaking-autonomous-campaigns` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-07-01` [Taiwan's nuclear safety commission and other agencies breached by an agent swarm](2026-07-01-taiwan-government-agent-swarm.md)<br>  <sub>Taiwan's nuclear safety commission and other agencies breached by an agent swarm</sub>
- `2026-07-01` [JADEPUFFER: first ransomware driven end-to-end by an LLM](2026-07-01-jadepuffer-first-llm-driven-ransomware.md)<br>  <sub>JADEPUFFER: first ransomware driven end-to-end by an LLM</sub>
- `2026-07-09` [OpenAI's agents breach Hugging Face](2026-07-09-openai-agents-breach-huggingface.md)<br>  <sub>OpenAI's agents breach Hugging Face</sub>
- `2026-07-30` [Hermes Agent attacks Thailand's Ministry of Finance unattended](2026-07-30-hermes-agent-thailand-finance-ministry.md)<br>  <sub>Hermes Agent attacks Thailand's Ministry of Finance unattended</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-30-unit42-chinese-speaking-autonomous-campaigns.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
