---
id: 2026-01-14-microsoft-copilot-personal-reprompt
title: "Microsoft Copilot Personal \"Reprompt\""
title_zh: "Microsoft Copilot Personal「Reprompt」"
title_ja: "Microsoft Copilot Personalの「Reprompt」"
title_ko: "Microsoft Copilot Personal \"Reprompt\""
title_de: "Microsoft Copilot Personal: „Reprompt“"
title_fr: "« Reprompt » dans Microsoft Copilot Personal"
title_es: "El \"Reprompt\" de Microsoft Copilot Personal"
date: 2026-01-14
date_precision: day
date_raw: "2026-01-14"

kind: vulnerability
type: [IPI, EXFIL]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Varonis Threat Labs: the URL `q` parameter carries a P2P (Personal Prompt) injection, and a "double request + chained request" trick bypasses the protections — Copilot is made to run the task twice and to act on follow-up commands sent by the server, so that **after the user clicks the link once, no further action is needed** for data to be silently stolen. Fixed


summary_zh: |
  Varonis Threat Labs：URL 的 `q` 参数做 P2P（Personal Prompt）注入，用「双请求 + 链式请求」绕过防护——让 Copilot 执行两次任务并利用服务端下发的后续命令，**用户点一次链接后无需任何后续操作**即被隐蔽窃取数据。已修复

summary_ja: |
  Varonis Threat Labs：URLの`q`パラメータがP2P（Personal Prompt）インジェクションを運び、「二重リクエスト＋連鎖リクエスト」のトリックが保護を回避する——Copilotにタスクを2回実行させ、サーバーから送られる後続コマンドにも反応させることで、**ユーザーがリンクを一度クリックした後は追加の操作なしで**データが静かに窃取される。修正済み

summary_ko: |
  Varonis Threat Labs: URL의 `q` 매개변수가 P2P(Personal Prompt) 인젝션을 전달하며, "이중 요청 + 연쇄 요청" 기법이 보호를 우회한다 — Copilot이 작업을 두 번 실행하고 서버가 보내는 후속 명령에 반응하게 만들어, **사용자가 링크를 한 번 클릭하면 이후 아무 동작 없이** 데이터가 조용히 탈취된다. 수정됨

summary_de: |
  Varonis Threat Labs: Der `q`-Parameter der URL transportiert eine P2P-Injection (Personal Prompt), und ein Trick mit „doppelter Anfrage + verketteter Anfrage“ umgeht die Schutzmaßnahmen — Copilot wird dazu gebracht, die Aufgabe zweimal auszuführen und auf Folgeanweisungen des Servers zu reagieren, sodass **nach einem einzigen Klick des Nutzers auf den Link keine weitere Aktion nötig ist**, damit Daten still gestohlen werden. Behoben

summary_fr: |
  Varonis Threat Labs : le paramètre d'URL `q` porte une injection P2P (Personal Prompt), et une astuce de « double requête + requête en chaîne » contourne les protections — Copilot est amené à exécuter la tâche deux fois et à agir sur des commandes de suivi envoyées par le serveur, si bien que **après un seul clic de l'utilisateur sur le lien, aucune autre action n'est nécessaire** pour voler silencieusement des données. Corrigé

summary_es: |
  Varonis Threat Labs: el parámetro `q` de la URL transporta una inyección P2P (Personal Prompt), y un truco de "doble solicitud + solicitud encadenada" elude las protecciones — se hace que Copilot ejecute la tarea dos veces y que actúe según los comandos de seguimiento enviados por el servidor, de modo que **después de que el usuario haga clic una vez en el enlace, no se necesita ninguna acción más** para robar datos silenciosamente. Corregido

sources:
  - url: https://www.varonis.com/blog/reprompt
    label: Varonis

disputed: false
landmark: true
scan_month: 2026-01
scan_ref: "SCAN.md §6 2026-01"
---

# Microsoft Copilot Personal "Reprompt"

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

Varonis Threat Labs: the URL `q` parameter carries a P2P (Personal Prompt) injection, and a "double request + chained request" trick bypasses the protections — Copilot is made to run the task twice and to act on follow-up commands sent by the server, so that **after the user clicks the link once, no further action is needed** for data to be silently stolen. Fixed

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["agent reads it and executes it as instructions"]:::step
    S1["Exfiltrated via vendor-trusted domains<br/>image rendering · APIs · proxies"]:::step
    I["Data ends up in the attacker's hands<br/><i>(vulnerability disclosed · no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Varonis | <https://www.varonis.com/blog/reprompt> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-01-14` (raw: 2026-01-14, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-01-14-microsoft-copilot-personal-reprompt` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-01-12` [Claude Cowork ships with known vulnerabilities](2026-01-12-claude-cowork-dai-zhe-zhi.md)<br>  <sub>Claude Cowork ships with known vulnerabilities</sub>
- `2026-01-12` [Superhuman AI indirect prompt injection](2026-01-12-superhuman-jian-jie-ti-shi.md)<br>  <sub>Superhuman AI indirect prompt injection</sub>
- `2026-01-07` [Four productivity tools hit the lethal trifecta in nine days](2026-01-07-lethal-trifecta-four-tools.md)<br>  <sub>Four productivity tools hit the lethal trifecta in nine days</sub>
- `2026-02-09` [Clinejection](../2026-02/2026-02-09-clinejection.md)<br>  <sub>Clinejection</sub>

---

[← 2026-01 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-01/2026-01-14-microsoft-copilot-personal-reprompt.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
