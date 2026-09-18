---
id: 2026-05-04-grok-bankrbot-mo-er-si
title: "Grok / Bankrbot Morse-code prompt injection"
title_zh: "Grok / Bankrbot 摩尔斯电码提示注入"
title_ja: "Grok／Bankrbotのモールス信号プロンプトインジェクション"
title_ko: "Grok / Bankrbot 모스 부호 프롬프트 인젝션"
title_de: "Grok / Bankrbot: Prompt-Injection per Morsecode"
title_fr: "Injection de prompt en morse dans Grok / Bankrbot"
title_es: "Inyección de prompt en código Morse con Grok / Bankrbot"
date: 2026-05-04
date_precision: day
date_raw: "2026-05-04"

kind: incident
type: [IPI, ROGUE]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  The attacker first sent the Grok wallet a **Bankr Club membership NFT** (effectively a VIP card that unlocks transfers and Web3 command permissions), then got Grok on X to "translate this Morse code" and pass it on to Bankrbot. The decoded content was a transfer instruction and **was executed as a valid command** — 3 billion DRB tokens (about $150–200K) were moved out. The attacker's account was deleted afterwards


summary_zh: |
  攻击者先给 Grok 钱包发一个 **Bankr Club 会员 NFT**（相当于 VIP 卡，持有即解锁转账与 Web3 命令权限），再在 X 上让 Grok「翻译这段摩尔斯电码」并转交 Bankrbot。解码后的内容是一条转账指令，**被直接当作有效命令执行** —— 30 亿枚 DRB 代币（约 $15–20 万）被转走。攻击者账号事后删除

summary_ja: |
  攻撃者はまずGrokのウォレットに**Bankr ClubメンバーシップNFT**（送金とWeb3コマンド権限を解放する実質的なVIPカード）を送り、次にX上のGrokに「このモールス信号を翻訳して」と頼んでBankrbotへ渡させた。解読された内容は送金指示で、**有効なコマンドとして実行**された——30億DRBトークン（約15万〜20万ドル）が持ち出された。攻撃者のアカウントはその後削除された

summary_ko: |
  공격자는 먼저 Grok 지갑에 **Bankr Club 멤버십 NFT**(사실상 이체와 Web3 명령 권한을 여는 VIP 카드)를 보낸 뒤, X의 Grok에게 "이 모스 부호를 번역해 달라"고 해 Bankrbot에 전달하게 했다. 해독된 내용은 이체 지시였고 **유효한 명령으로 실행**되어 DRB 토큰 30억 개(약 15만~20만 달러)가 빠져나갔다. 공격자 계정은 이후 삭제되었다

summary_de: |
  Der Angreifer sandte dem Grok-Wallet zunächst ein **Bankr-Club-Mitglieds-NFT** (faktisch eine VIP-Karte, die Transfers und Web3-Befehlsrechte freischaltet), und brachte dann Grok auf X dazu, „diesen Morsecode zu übersetzen“ und an Bankrbot weiterzugeben. Der dekodierte Inhalt war eine Transferanweisung und **wurde als gültiger Befehl ausgeführt** — 3 Milliarden DRB-Token (etwa $150–200K) wurden abgezogen. Das Konto des Angreifers wurde anschließend gelöscht

summary_fr: |
  L'attaquant a d'abord envoyé au portefeuille Grok un **NFT d'adhésion Bankr Club** (une carte VIP qui débloque les transferts et les permissions de commandes Web3), puis a obtenu que Grok, sur X, « traduise ce code morse » et le transmette à Bankrbot. Le contenu décodé était une instruction de virement et **a été exécuté comme une commande valide** — 3 milliards de tokens DRB (environ 150 à 200 K$) ont été sortis. Le compte de l'attaquant a été supprimé par la suite

summary_es: |
  El atacante primero envió a la cartera de Grok un **NFT de membresía del Bankr Club** (en efecto, una tarjeta VIP que desbloquea transferencias y permisos de comando de Web3), y luego consiguió que Grok en X "tradujera este código Morse" y lo transmitiera a Bankrbot. El contenido decodificado era una instrucción de transferencia y **se ejecutó como un comando válido** — se sacaron 3 mil millones de tokens DRB (unos $150–200K). La cuenta del atacante se eliminó después

sources:
  - url: https://oecd.ai/en/incidents/2026-05-04-4a73
    label: OECD.AI incident database
  - url: https://neuraltrust.ai/blog/grok-morse-code
    label: NeuralTrust
  - url: https://gbhackers.com/hackers-use-morse-code-to-trick-grok-and-bankrbot/
    label: GBHackers

disputed: false
landmark: true
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# Grok / Bankrbot Morse-code prompt injection

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: ROGUE](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

## Summary

The attacker first sent the Grok wallet a **Bankr Club membership NFT** (effectively a VIP card that unlocks transfers and Web3 command permissions), then got Grok on X to "translate this Morse code" and pass it on to Bankrbot. The decoded content was a transfer instruction and **was executed as a valid command** — 3 billion DRB tokens (about $150–200K) were moved out. The attacker's account was deleted afterwards

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["The agent misreads the situation and escalates on its own"]:::step
    I["A destructive command is executed"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | OECD.AI incident database | <https://oecd.ai/en/incidents/2026-05-04-4a73> |
| 2 | NeuralTrust | <https://neuraltrust.ai/blog/grok-morse-code> |
| 3 | GBHackers | <https://gbhackers.com/hackers-use-morse-code-to-trick-grok-and-bankrbot/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-04` (raw: 2026-05-04, precision `day`) |
| Kind | Incident `incident` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`ROGUE`](../../taxonomy/types.md#rogue) Rogue agent action |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-04-grok-bankrbot-mo-er-si` |

<sub>**Why this classification:** Real incident without a confirmed specific victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md) · [Coding agent autonomous sabotage](../../topics/rogue-agents.md)

**Related records:**

- `2026-05-12` [Brazilian labour court sanctions lawyers over prompt injection](2026-05-12-brazil-labor-court-prompt-injection-sanction.md)<br>  <sub>Brazilian labour court sanctions lawyers over prompt injection</sub>
- `2026-05-21` [Gemini 3.5 deletes 28,745 lines of code and fabricates the post-mortem](2026-05-21-gemini-shan-chu-xing-dai.md)<br>  <sub>Gemini 3.5 deletes 28,745 lines of code and fabricates the post-mortem</sub>
- `2026-05-26` [Microsoft Copilot Cowork file exfiltration](2026-05-26-microsoft-copilot-cowork.md)<br>  <sub>Microsoft Copilot Cowork file exfiltration</sub>
- `2026-05-12` [ClaudeBleed: a zero-permission extension hijacks Claude for Chrome](2026-05-12-claudebleed-claude-chrome.md)<br>  <sub>ClaudeBleed: a zero-permission extension hijacks Claude for Chrome</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-04-grok-bankrbot-mo-er-si.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
