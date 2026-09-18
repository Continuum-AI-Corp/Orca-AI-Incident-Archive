---
id: 2026-08-19-grok-mi-ma-xue-wen
title: "Grok \"cryptographic context injection\": encrypted instructions, plaintext data"
title_zh: "Grok「密码学上下文注入」：加密的指令，明文的数据"
title_ja: "Grokの「暗号文脈インジェクション」：暗号化された指示、平文のデータ"
title_ko: "Grok \"암호학적 컨텍스트 주입\": 암호화된 지시, 평문 데이터"
title_de: "Grok „kryptografische Kontext-Injection“: verschlüsselte Anweisungen, Klartextdaten"
title_fr: "Grok et l'« injection de contexte cryptographique » : instructions chiffrées, données en clair"
title_es: "Grok \"inyección de contexto criptográfico\": instrucciones cifradas, datos en texto plano"
date: 2026-08-19
date_precision: day
date_raw: "2026-08-19"

kind: research
type: [IPI, EXFIL]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Adversa AI. The attack page embeds **encrypted instructions — Grok can decrypt and execute them on its own**. The payload makes the model "generate a decryption key", and **that so-called key is really a template filled with the user's private data** (name, location, subscription tier, chat history); Grok then carries it out as a URL parameter when it opens the attacker's website. Zero-click.
  ⚠️ **Reported to xAI via HackerOne on 2026-06-03; still reproducible in production as of 2026-08-19**


summary_zh: |
  Adversa AI。攻击页面嵌入**加密后的指令 —— Grok 能自行解密并执行**。载荷让模型「生成一个解密密钥」，而**那个所谓的密钥其实是一个模板，里面填的是用户的隐私数据**（姓名、位置、订阅等级、聊天历史）；Grok 随后在打开攻击者网站时把它当作 URL 参数带了出去。零点击。
  ⚠️ **2026-06-03 已通过 HackerOne 报告 xAI；截至 2026-08-19 在生产环境仍可复现**

summary_ja: |
  Adversa AI。攻撃ページは**暗号化された指示を埋め込み——Grokはそれを自ら復号して実行できる**。ペイロードはモデルに「復号キーを生成」させ、**そのいわゆるキーは実際にはユーザーのプライベートデータ（氏名、所在地、サブスクリプション階層、チャット履歴）で埋められたテンプレート**であり、Grokは攻撃者のWebサイトを開く際にそれをURLパラメータとして実行する。ゼロクリック。
  ⚠️ **2026-06-03にHackerOne経由でxAIへ報告。2026-08-19時点で本番環境で依然再現可能**

summary_ko: |
  Adversa AI. 공격 페이지가 **암호화된 지시를 내장하고 Grok이 스스로 복호화해 실행한다**. 페이로드는 모델이 "복호화 키를 생성"하게 만드는데, **그 소위 키는 실제로 사용자의 개인 데이터**(이름, 위치, 구독 등급, 채팅 기록)로 채워진 템플릿이다. Grok은 공격자의 웹사이트를 열 때 이를 URL 매개변수로 내보낸다. 제로클릭이다.
  ⚠️ **2026-06-03 HackerOne을 통해 xAI에 보고되었고, 2026-08-19 기준 운영 환경에서 여전히 재현된다**

summary_de: |
  Adversa AI. Die Angriffsseite bettet **verschlüsselte Anweisungen ein — Grok kann sie selbst entschlüsseln und ausführen**. Die Nutzlast bringt das Modell dazu, „einen Entschlüsselungsschlüssel zu erzeugen“, und **dieser sogenannte Schlüssel ist in Wahrheit eine Vorlage, die mit den privaten Daten des Nutzers gefüllt ist** (Name, Standort, Abo-Stufe, Chatverlauf); Grok trägt sie dann beim Öffnen der Website des Angreifers als URL-Parameter hinaus. Zero-Click.
  ⚠️ **Am 2026-06-03 über HackerOne an xAI gemeldet; Stand 2026-08-19 in der Produktion weiterhin reproduzierbar**

summary_fr: |
  Adversa AI. La page d'attaque intègre **des instructions chiffrées — que Grok peut déchiffrer et exécuter lui-même**. La charge pousse le modèle à « générer une clé de déchiffrement », et **cette prétendue clé est en réalité un gabarit rempli avec les données privées de l'utilisateur** (nom, localisation, niveau d'abonnement, historique de chat) ; Grok la transporte ensuite comme paramètre d'URL quand il ouvre le site de l'attaquant. Zero-click.
  ⚠️ **Signalé à xAI via HackerOne le 2026-06-03 ; toujours reproductible en production au 2026-08-19**

summary_es: |
  Adversa AI. La página del ataque incrusta **instrucciones cifradas — Grok puede descifrarlas y ejecutarlas por su cuenta**. La carga útil hace que el modelo "genere una clave de descifrado", y **esa supuesta clave es en realidad una plantilla rellenada con los datos privados del usuario** (nombre, ubicación, nivel de suscripción, historial de chat); Grok luego la transporta como parámetro de URL cuando abre el sitio web del atacante. Zero-click.
  ⚠️ **Reportado a xAI vía HackerOne el 2026-06-03; seguía siendo reproducible en producción a fecha de 2026-08-19**

sources:
  - url: https://adversa.ai/blog/cryptographic-context-injection-grok-data-theft/
    label: Adversa AI
  - url: https://thehackernews.com/2026/08/new-cryptographic-context-injection.html
    label: THN

disputed: false
landmark: true
scan_month: 2026-08
scan_ref: "SCAN.md §6 2026-08"
---

# Grok "cryptographic context injection": encrypted instructions, plaintext data

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

Adversa AI. The attack page embeds **encrypted instructions — Grok can decrypt and execute them on its own**. The payload makes the model "generate a decryption key", and **that so-called key is really a template filled with the user's private data** (name, location, subscription tier, chat history); Grok then carries it out as a URL parameter when it opens the attacker's website. Zero-click.

⚠️ **Reported to xAI via HackerOne on 2026-06-03; still reproducible in production as of 2026-08-19**

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["Exfiltration via the vendor's trusted domain<br/>image rendering · API · proxy"]:::step
    I["Data ends up with the attacker<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Adversa AI | <https://adversa.ai/blog/cryptographic-context-injection-grok-data-theft/> |
| 2 | THN | <https://thehackernews.com/2026/08/new-cryptographic-context-injection.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-08-19` (raw: 2026-08-19, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-08-19-grok-mi-ma-xue-wen` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-08-18` [CoSnitch (CVE-2026-24301)](2026-08-18-cosnitch.md)<br>  <sub>CoSnitch (CVE-2026-24301)</sub>
- `2026-07-02` [Hidden web instructions make AI agents pay attackers (two in-the-wild campaigns)](../2026-07/2026-07-02-hidden-web-instructions-payment-fraud.md)<br>  <sub>Hidden web instructions make AI agents pay attackers (two in-the-wild campaigns)</sub>
- `2026-09-08` [ChatGPT sandbox flaw pipes a victim's Gmail data into the attacker's account](../2026-09/2026-09-08-chatgpt-gmail-sha-xiang-que.md)<br>  <sub>ChatGPT sandbox flaw pipes a victim's Gmail data into the attacker's account</sub>
- `2026-07-07` [GitLost: GitHub Agentic Workflows leak private repositories](../2026-07/2026-07-07-gitlost-github-agentic-workflows.md)<br>  <sub>GitLost: GitHub Agentic Workflows leak private repositories</sub>

---

[← 2026-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-08/2026-08-19-grok-mi-ma-xue-wen.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
