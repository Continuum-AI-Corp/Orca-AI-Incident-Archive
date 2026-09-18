---
id: 2025-09-01-villager-cyberspike-shen-tou-gong
title: "Villager (Cyberspike) AI pentest tool"
title_zh: "Villager（Cyberspike）AI 渗透工具"
title_ja: "Villager（Cyberspike）AIペンテストツール"
title_ko: "Villager (Cyberspike) AI 침투 테스트 도구"
title_de: "Villager (Cyberspike): KI-Pentest-Tool"
title_fr: "Villager (Cyberspike), un outil de pentest IA"
title_es: "Villager (Cyberspike), herramienta de pentest con IA"
date: 2025-09-01
date_precision: month
date_raw: "2025-09"

kind: research
type: [WEAPON]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [CN, GLOBAL]

summary: |
  Uploaded to PyPI in late 2025-07 by user `stupidfish001` (a former CTF player from China's HSCSEC team). Kali toolchain + **DeepSeek** + **MCP client**, with a built-in database of **4,201 AI system prompts**, automatically creating isolated Kali containers on demand. **11,000 downloads** in two months; described as "Cobalt Strike's AI-native successor"


summary_zh: |
  2025-07 下旬由用户 `stupidfish001`（前中国 HSCSEC 战队 CTF 选手）上传 PyPI。Kali 工具链 + **DeepSeek** + **MCP 客户端**，内置 **4,201 条 AI 系统提示**数据库，按需自动创建隔离的 Kali 容器。两个月 **11,000 次下载**，被评为「Cobalt Strike 的 AI 原生继任者」

summary_ja: |
  2025-07後半にユーザー`stupidfish001`（中国HSCSECチーム出身の元CTFプレイヤー）がPyPIにアップロード。Kaliツールチェーン＋**DeepSeek**＋**MCPクライアント**で、**4,201件のAIシステムプロンプト**のデータベースを内蔵し、必要に応じて分離されたKaliコンテナを自動生成する。2か月で**11,000ダウンロード**。「Cobalt StrikeのAIネイティブな後継」と評された

summary_ko: |
  2025-07 말 사용자 `stupidfish001`(중국 HSCSEC 팀 출신의 전직 CTF 플레이어)이 PyPI에 업로드했다. Kali 툴체인 + **DeepSeek** + **MCP 클라이언트** 조합이며 **AI 시스템 프롬프트 4,201개** 데이터베이스를 내장하고 요청 시 격리된 Kali 컨테이너를 자동 생성한다. 두 달 만에 **1만 1천 회 다운로드**되었고 "Cobalt Strike의 AI 네이티브 후속"으로 묘사되었다

summary_de: |
  Ende 2025-07 von dem Nutzer `stupidfish001` (einem ehemaligen CTF-Spieler aus dem chinesischen HSCSEC-Team) auf PyPI hochgeladen. Kali-Toolchain + **DeepSeek** + **MCP-Client**, mit einer eingebauten Datenbank von **4,201 KI-System-Prompts**, die bei Bedarf automatisch isolierte Kali-Container erstellt. **11,000 Downloads** in zwei Monaten; beschrieben als „die KI-native Nachfolgerin von Cobalt Strike“

summary_fr: |
  Téléchargé sur PyPI fin 2025-07 par l'utilisateur `stupidfish001` (un ancien joueur de CTF de l'équipe chinoise HSCSEC). Chaîne d'outils Kali + **DeepSeek** + **client MCP**, avec une base intégrée de **4 201 prompts système d'IA**, créant automatiquement des conteneurs Kali isolés à la demande. **11 000 téléchargements** en deux mois ; décrit comme « le successeur natif IA de Cobalt Strike »

summary_es: |
  Subida a PyPI a finales de 2025-07 por el usuario `stupidfish001` (un exjugador de CTF del equipo HSCSEC de China). Cadena de herramientas de Kali + **DeepSeek** + **cliente MCP**, con una base de datos integrada de **4,201 system prompts de IA**, creando contenedores Kali aislados automáticamente bajo demanda. **11,000 descargas** en dos meses; descrita como "el sucesor nativo de IA de Cobalt Strike"

sources:
  - url: https://www.straiker.ai/blog/cyberspike-villager-cobalt-strike-ai-native-successor
    label: Straiker
  - url: https://thehackernews.com/2025/09/ai-powered-villager-pen-testing-tool.html
    label: THN

disputed: false
landmark: false
scan_month: 2025-09
scan_ref: "SCAN.md §5 2025-09"
---

# Villager (Cyberspike) AI pentest tool

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

Uploaded to PyPI in late 2025-07 by user `stupidfish001` (a former CTF player from China's HSCSEC team). Kali toolchain + **DeepSeek** + **MCP client**, with a built-in database of **4,201 AI system prompts**, automatically creating isolated Kali containers on demand. **11,000 downloads** in two months; described as "Cobalt Strike's AI-native successor"

## Attack chain

```mermaid
flowchart LR
    E["Attacker + jailbreak prompts"]:::entry
    S0["An LLM orchestrator drives a cluster of sub-agents"]:::step
    I["The target system is compromised<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Straiker | <https://www.straiker.ai/blog/cyberspike-villager-cobalt-strike-ai-native-successor> |
| 2 | THN | <https://thehackernews.com/2025/09/ai-powered-villager-pen-testing-tool.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-09-01` (raw: 2025-09, precision `month`) |
| Kind | Research demo `research` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [China](../../regions/cn.md) · [Global](../../regions/global.md) |
| Archive ID | `2025-09-01-villager-cyberspike-shen-tou-gong` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2025-09-02` [HexStrike-AI turned on a Citrix zero-day](2025-09-02-hexstrike-citrix-day.md)<br>  <sub>HexStrike-AI turned on a Citrix zero-day</sub>
- `2025-09-15` [Anthropic detects GTG-1002](2025-09-15-anthropic-gtg-jian-ce-dao.md)<br>  <sub>Anthropic detects GTG-1002</sub>
- `2025-08-26` [ESET finds PromptLock](../2025-08/2025-08-26-eset-promptlock-fa-xian.md)<br>  <sub>ESET finds PromptLock</sub>
- `2025-08-27` [Anthropic August threat report](../2025-08/2025-08-27-anthropic-ba-wei-xie-bao.md)<br>  <sub>Anthropic August threat report</sub>

---

[← 2025-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-09/2025-09-01-villager-cyberspike-shen-tou-gong.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
