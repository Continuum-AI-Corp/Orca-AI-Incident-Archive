---
id: 2026-06-24-macos-gaslight-e-yi-ruan-jian
title: "macOS.Gaslight: malware prompt-injects the AI analyst"
title_zh: "macOS.Gaslight：恶意软件反过来对 AI 分析师做提示注入"
title_ja: "macOS.Gaslight：マルウェアがAIアナリストにプロンプトインジェクション"
title_ko: "macOS.Gaslight: 악성코드가 AI 분석가에게 프롬프트 인젝션"
title_de: "macOS.Gaslight: Malware prompt-injectet den KI-Analysten"
title_fr: "macOS.Gaslight : un malware injecte un prompt dans l'analyste IA"
title_es: "macOS.Gaslight: el malware inyecta prompts al analista de IA"
date: 2026-06-24
date_precision: day
date_raw: "2026-06-24"

kind: research
type: [WEAPON]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  SentinelLABS: a North Korea-linked Rust implant contains a **3.5KB data block** that uses Markdown code fences and `{{DATA}}` tokens to **mimic the prompt structure of LLM analysis platforms**, laying out **38 fake system messages** (token expiry, out of memory, disk exhausted, repeated failures) and disguised vulnerability / static-analysis warnings, aiming to make LLM-assisted triage **stop, break off or refuse**. An order of magnitude beyond Check Point's single-instruction Windows sample in 2025. C2 runs over the Telegram Bot API


summary_zh: |
  SentinelLABS：朝鲜相关 Rust 植入体内含 **3.5KB 数据块**，用 Markdown 代码围栏和 `{{DATA}}` 令牌**模仿 LLM 分析平台的提示结构**，排布 **38 条伪造系统消息**（token 过期、内存不足、磁盘耗尽、连续失败）与伪装的漏洞/静态分析警告，目的是让 LLM 辅助的初步分类**中止、打断或拒绝**。比 2025 年 Check Point 那个单条指令的 Windows 样本高一个量级。C2 走 Telegram Bot API

summary_ja: |
  SentinelLABS：北朝鮮関連のRustインプラントに、Markdownコードフェンスと`{{DATA}}`トークンを使って**LLM分析プラットフォームのプロンプト構造を模倣**する**3.5KBのデータブロック**が含まれ、**38件の偽のシステムメッセージ**（トークン期限切れ、メモリ不足、ディスク枯渇、繰り返しの失敗）と、偽装された脆弱性／静的解析の警告を並べ、LLM支援のトリアージを**停止・中断・拒否**させようとする。Check Pointの2025年の単一命令のWindowsサンプルより一桁上を行く。C2はTelegram Bot API経由で動作する

summary_ko: |
  SentinelLABS: 북한 연계 Rust 임플란트가 **3.5KB 데이터 블록**을 담고 있는데, Markdown 코드 펜스와 `{{DATA}}` 토큰으로 **LLM 분석 플랫폼의 프롬프트 구조를 흉내 내며** **가짜 시스템 메시지 38개**(토큰 만료, 메모리 부족, 디스크 소진, 반복 실패)와 위장한 취약점/정적 분석 경고를 배치해 LLM 기반 트리아지가 **중단, 중지, 거부**하도록 만드는 것을 노린다. 2025년 Check Point의 단일 지시 Windows 샘플보다 한 차원 크다. C2는 Telegram Bot API를 통해 동작한다

summary_de: |
  SentinelLABS: Ein mit Nordkorea verbundenes Rust-Implantat enthält einen **3.5KB großen Datenblock**, der mit Markdown-Codezäunen und `{{DATA}}`-Token **die Prompt-Struktur von LLM-Analyseplattformen nachahmt**, **38 gefälschte Systemnachrichten** ausbreitet (Token-Ablauf, Speicher voll, Festplatte voll, wiederholte Fehler) sowie getarnte Schwachstellen- und Static-Analysis-Warnungen, um LLM-gestützte Triage **stoppen, abbrechen oder verweigern** zu lassen. Eine Größenordnung über Check Points Windows-Sample mit einer einzigen Anweisung von 2025. Der C2 läuft über die Telegram Bot API

summary_fr: |
  SentinelLABS : un implant Rust lié à la Corée du Nord contient un **bloc de données de 3,5 Ko** qui utilise des délimiteurs de code Markdown et des jetons `{{DATA}}` pour **imiter la structure de prompt des plateformes d'analyse LLM**, déployant **38 faux messages système** (jeton expiré, mémoire insuffisante, disque saturé, échecs répétés) et de faux avertissements de vulnérabilité / d'analyse statique, visant à faire **arrêter, interrompre ou refuser** le triage assisté par LLM. Un ordre de grandeur au-delà de l'échantillon Windows à instruction unique de Check Point en 2025. Le C2 passe par l'API Telegram Bot

summary_es: |
  SentinelLABS: un implante en Rust vinculado a Corea del Norte contiene un **bloque de datos de 3.5KB** que usa bloques de código Markdown y tokens `{{DATA}}` para **imitar la estructura de prompt de las plataformas de análisis con LLM**, desplegando **38 mensajes de sistema falsos** (expiración de token, memoria insuficiente, disco agotado, fallos repetidos) y advertencias de vulnerabilidades y análisis estático disfrazadas, con el objetivo de hacer que el triaje asistido por LLM **se detenga, se interrumpa o se niegue**. Un orden de magnitud por encima de la muestra de una sola instrucción para Windows de Check Point en 2025. El C2 funciona sobre la API de Telegram Bot

sources:
  - url: https://www.sentinelone.com/labs/macos-gaslight-rust-backdoor-turns-prompt-injection-on-the-analyst-not-the-sandbox/
    label: SentinelLABS

disputed: false
landmark: true
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# macOS.Gaslight: malware prompt-injects the AI analyst

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

SentinelLABS: a North Korea-linked Rust implant contains a **3.5KB data block** that uses Markdown code fences and `{{DATA}}` tokens to **mimic the prompt structure of LLM analysis platforms**, laying out **38 fake system messages** (token expiry, out of memory, disk exhausted, repeated failures) and disguised vulnerability / static-analysis warnings, aiming to make LLM-assisted triage **stop, break off or refuse**. An order of magnitude beyond Check Point's single-instruction Windows sample in 2025. C2 runs over the Telegram Bot API

## Attack chain

```mermaid
flowchart LR
    E["Attacker + jailbreak script"]:::entry
    S0["LLM orchestrator drives a cluster of sub-agents"]:::step
    I["Target systems compromised<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | SentinelLABS | <https://www.sentinelone.com/labs/macos-gaslight-rust-backdoor-turns-prompt-injection-on-the-analyst-not-the-sandbox/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-24` (raw: 2026-06-24, precision `day`) |
| Kind | Research demo `research` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-24-macos-gaslight-e-yi-ruan-jian` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-06-15` [UNC6508 breaches North American research institutions via REDCap](2026-06-15-unc6508-redcap-jing-ru-qin.md)<br>  <sub>UNC6508 breaches North American research institutions via REDCap</sub>
- `2026-06-02` [CleverHans Lab adaptive AI worm PoC](2026-06-02-cleverhans-lab-poc.md)<br>  <sub>CleverHans Lab adaptive AI worm PoC</sub>
- `2026-06-03` [Anthropic, "LLM ATT&CK Navigator"](2026-06-03-anthropic-llm-att-ck.md)<br>  <sub>Anthropic, "LLM ATT&CK Navigator"</sub>
- `2026-06-09` [Anthropic: N-day is really "N-hour"](2026-06-09-anthropic-day-hour.md)<br>  <sub>Anthropic: N-day is really "N-hour"</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-24-macos-gaslight-e-yi-ruan-jian.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
