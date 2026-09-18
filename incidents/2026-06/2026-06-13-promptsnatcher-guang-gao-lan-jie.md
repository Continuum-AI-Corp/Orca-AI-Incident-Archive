---
id: 2026-06-13-promptsnatcher-guang-gao-lan-jie
title: "PromptSnatcher: ad-blocking extensions steal AI conversations"
title_zh: "PromptSnatcher：广告拦截扩展偷 AI 对话"
title_ja: "PromptSnatcher：広告ブロック拡張機能がAI会話を窃取"
title_ko: "PromptSnatcher: 광고 차단 확장 프로그램이 AI 대화를 탈취"
title_de: "PromptSnatcher: Werbeblocker-Erweiterungen stehlen KI-Unterhaltungen"
title_fr: "PromptSnatcher : des extensions de blocage de publicités volent les conversations IA"
title_es: "PromptSnatcher: extensiones de bloqueo de anuncios roban conversaciones de IA"
date: 2026-06-13
date_precision: day
date_raw: "2026-06-13"

kind: incident
type: [CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Smart Adblocker (about 80,000 users) + Adblock for Browser (about 10,000), sharing the same exfiltration logic and C2. They inject a MAIN-world script that replaces fetch/XHR/WebSocket and copies **entire conversations from 8 AI services including ChatGPT, Claude, Gemini and Copilot** (for 5 of them it also determines the subscription tier). **Parsing rules are delivered from the C2 at runtime, so targets can be expanded without updating the store version**; the Firefox version claims "no data collection" yet ships the same capture engine


summary_zh: |
  Smart Adblocker(约 8 万) + Adblock for Browser(约 1 万)，共享同一外带逻辑与 C2。注入 MAIN world 脚本替换 fetch/XHR/WebSocket，复制 **ChatGPT、Claude、Gemini、Copilot 等 8 个 AI 服务的完整对话**（其中 5 个还判定套餐等级）。**解析规则从 C2 运行时下发，无需更新商店版本即可扩大目标**；Firefox 版声明「不收集数据」却装了同款捕获引擎

summary_ja: |
  Smart Adblocker（約8万人のユーザー）＋Adblock for Browser（約1万人）が同じ外部送信ロジックとC2を共有。MAINワールドのスクリプトを注入してfetch/XHR/WebSocketを置き換え、**ChatGPT、Claude、Gemini、Copilotなど8つのAIサービスの会話全体をコピー**する（うち5つではサブスクリプション階層も判定）。**解析ルールは実行時にC2から配信されるため、ストア版を更新せずに対象を拡大できる**。Firefox版は「データ収集なし」と主張しながら同じキャプチャエンジンを搭載している

summary_ko: |
  Smart Adblocker(사용자 약 80,000명) + Adblock for Browser(약 10,000명)로, 같은 유출 로직과 C2를 공유한다. MAIN 월드 스크립트를 주입해 fetch/XHR/WebSocket을 교체하고 **ChatGPT, Claude, Gemini, Copilot 등 8개 AI 서비스의 대화 전체를 복사**한다(그중 5개에서는 구독 등급까지 판별한다). **파싱 규칙을 런타임에 C2에서 내려받으므로 스토어 버전을 갱신하지 않고도 대상을 확장할 수 있다**. Firefox 버전은 "데이터 수집 없음"을 표방하지만 같은 캡처 엔진을 탑재했다

summary_de: |
  Smart Adblocker (etwa 80,000 Nutzer) + Adblock for Browser (etwa 10,000), die dieselbe Exfiltrationslogik und denselben C2 nutzen. Sie injizieren ein Skript im MAIN-World-Kontext, das fetch/XHR/WebSocket ersetzt und **vollständige Unterhaltungen aus 8 KI-Diensten kopiert, darunter ChatGPT, Claude, Gemini und Copilot** (bei 5 von ihnen ermittelt es zudem die Abo-Stufe). **Die Parsing-Regeln werden zur Laufzeit vom C2 geliefert, sodass sich die Ziele erweitern lassen, ohne die Store-Version zu aktualisieren**; die Firefox-Version behauptet „keine Datensammlung“, liefert aber dieselbe Erfassungs-Engine aus

summary_fr: |
  Smart Adblocker (environ 80 000 utilisateurs) + Adblock for Browser (environ 10 000), partageant la même logique d'exfiltration et le même C2. Ils injectent un script en monde MAIN qui remplace fetch/XHR/WebSocket et copie **des conversations entières de 8 services d'IA dont ChatGPT, Claude, Gemini et Copilot** (pour 5 d'entre eux, il détermine aussi le niveau d'abonnement). **Les règles d'analyse sont livrées par le C2 à l'exécution, si bien que les cibles peuvent être étendues sans mise à jour de la version en boutique** ; la version Firefox affirme « aucune collecte de données » tout en embarquant le même moteur de capture

summary_es: |
  Smart Adblocker (unos 80,000 usuarios) + Adblock for Browser (unos 10,000), que comparten la misma lógica de exfiltración y el mismo C2. Inyectan un script en el mundo MAIN que reemplaza fetch/XHR/WebSocket y copia **conversaciones completas de 8 servicios de IA, incluidos ChatGPT, Claude, Gemini y Copilot** (para 5 de ellos también determina el nivel de suscripción). **Las reglas de análisis se entregan desde el C2 en tiempo de ejecución, así que los objetivos pueden ampliarse sin actualizar la versión de la tienda**; la versión de Firefox afirma "no recopila datos" pero incluye el mismo motor de captura

sources:
  - url: https://malext.io/reports/PromptSnatcher/
    label: MalExt Sentry

disputed: false
landmark: false
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# PromptSnatcher: ad-blocking extensions steal AI conversations

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

Smart Adblocker (about 80,000 users) + Adblock for Browser (about 10,000), sharing the same exfiltration logic and C2. They inject a MAIN-world script that replaces fetch/XHR/WebSocket and copies **entire conversations from 8 AI services including ChatGPT, Claude, Gemini and Copilot** (for 5 of them it also determines the subscription tier). **Parsing rules are delivered from the C2 at runtime, so targets can be expanded without updating the store version**; the Firefox version claims "no data collection" yet ships the same capture engine

## Attack chain

```mermaid
flowchart LR
    E["Credentials within an agent's reach"]:::entry
    S0["The agent picks them up and calls out"]:::step
    I["Credential abuse"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | MalExt Sentry | <https://malext.io/reports/PromptSnatcher/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-13` (raw: 2026-06-13, precision `day`) |
| Kind | Incident `incident` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-13-promptsnatcher-guang-gao-lan-jie` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2026-06-01` [Miasma worm](2026-06-01-miasma-worm.md)<br>  <sub>Miasma worm</sub>
- `2026-06-01` [Attackers simply ask Meta's AI support bot for Instagram accounts](2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br>  <sub>Attackers simply ask Meta's AI support bot for Instagram accounts</sub>
- `2026-06-17` [Sapphire Sleet poisons every Mastra AI scope in 88 minutes](2026-06-17-sapphire-sleet-mastra-88-minutes.md)<br>  <sub>Sapphire Sleet poisons every Mastra AI scope in 88 minutes</sub>
- `2026-06-04` [Claude Oceanus-v1-p illegally redistributed](2026-06-04-claude-oceanus-fei-fa-fen.md)<br>  <sub>Claude Oceanus-v1-p illegally redistributed</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-13-promptsnatcher-guang-gao-lan-jie.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
