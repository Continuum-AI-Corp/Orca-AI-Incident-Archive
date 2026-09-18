---
id: 2026-06-24-operation-endgame-europol-stealc
title: "Operation Endgame (Europol) takes down StealC and Amadey"
title_zh: "Operation Endgame（Europol）停掉 StealC/Amadey"
title_ja: "Operation Endgame（Europol）がStealCとAmadeyを壊滅させる"
title_ko: "Operation Endgame (유로폴), StealC와 Amadey 소탕"
title_de: "Operation Endgame (Europol) zerschlägt StealC und Amadey"
title_fr: "Opération Endgame (Europol) : démantèlement de StealC et Amadey"
title_es: "La Operación Endgame (Europol) desmantela StealC y Amadey"
date: 2026-06-24
date_precision: day
date_raw: "2026-06-24"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [EU]

summary: |
  326 servers, 142 domains, **27 million** stolen credentials. **Microsoft used Copilot for malware analysis** (exhaustively enumerating functions, generating string-decryption scripts, identifying C2 in reverse-engineered code and writing tools to confirm C2 liveness), and it filed a civil suit under RICO


summary_zh: |
  326 台服务器、142 域名、**2,700 万条**被窃凭据。**Microsoft 用 Copilot 做恶意软件分析**（函数穷举、字符串解密脚本生成、逆向代码中识别 C2、编写 C2 存活确认工具），并以 RICO 法民事起诉

summary_ja: |
  326のサーバー、142のドメイン、**2,700万件**の窃取された認証情報。**Microsoftはマルウェア分析にCopilotを使用**し（関数の網羅的な列挙、文字列復号スクリプトの生成、リバースエンジニアリングされたコード内のC2の特定、C2の生存確認ツールの作成）、RICOに基づく民事訴訟を提起した

summary_ko: |
  서버 326대, 도메인 142개, **2,700만 건**의 탈취 자격 증명. **마이크로소프트는 악성코드 분석에 Copilot을 활용했고**(함수 전수 열거, 문자열 복호화 스크립트 생성, 리버스 엔지니어링 코드에서 C2 식별, C2 생존 확인 도구 작성), RICO에 근거한 민사 소송을 제기했다

summary_de: |
  326 Server, 142 Domains, **27 Millionen** gestohlene Zugangsdaten. **Microsoft nutzte Copilot für die Malware-Analyse** (erschöpfende Auflistung von Funktionen, Erstellung von Skripten zur String-Entschlüsselung, Identifikation von C2 in reverse-engineertem Code und Entwicklung von Tools zur Bestätigung der C2-Erreichbarkeit) und reichte eine Zivilklage nach RICO ein

summary_fr: |
  326 serveurs, 142 domaines, **27 millions** d'identifiants volés. **Microsoft a utilisé Copilot pour l'analyse de malwares** (énumération exhaustive des fonctions, génération de scripts de déchiffrement de chaînes, identification des C2 dans du code désassemblé et écriture d'outils pour confirmer l'activité des C2), et a déposé une plainte civile au titre de la loi RICO

summary_es: |
  326 servidores, 142 dominios, **27 millones** de credenciales robadas. **Microsoft usó Copilot para el análisis de malware** (enumerar funciones exhaustivamente, generar scripts de descifrado de cadenas, identificar el C2 en código reversado y escribir herramientas para confirmar la actividad del C2), y presentó una demanda civil bajo la ley RICO

sources:
  - url: https://www.europol.europa.eu/media-press/newsroom/news/global-cyber-strike-disrupts-socgholish-amadey-and-stealc-malware-networks
    label: Europol
  - url: https://www.microsoft.com/en-us/security/blog/2026/06/24/stealc-and-amadey-breaking-down-infostealers-and-the-cybercrime-services-that-deliver-them/
    label: Microsoft

disputed: false
landmark: false
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# Operation Endgame (Europol) takes down StealC and Amadey

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

326 servers, 142 domains, **27 million** stolen credentials. **Microsoft used Copilot for malware analysis** (exhaustively enumerating functions, generating string-decryption scripts, identifying C2 in reverse-engineered code and writing tools to confirm C2 liveness), and it filed a civil suit under RICO

## Attack chain

```mermaid
flowchart LR
    E["Regulatory or policy action"]:::entry
    S0["Falls on vendors and users"]:::step
    I["Compliance requirements change"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Europol | <https://www.europol.europa.eu/media-press/newsroom/news/global-cyber-strike-disrupts-socgholish-amadey-and-stealc-malware-networks> |
| 2 | Microsoft | <https://www.microsoft.com/en-us/security/blog/2026/06/24/stealc-and-amadey-breaking-down-infostealers-and-the-cybercrime-services-that-deliver-them/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-24` (raw: 2026-06-24, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Europe](../../regions/eu.md) |
| Archive ID | `2026-06-24-operation-endgame-europol-stealc` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-06-09` [Anthropic Claude Fable 5 GA, Mythos 5 limited release](2026-06-09-anthropic-claude-fable-ga.md)<br>  <sub>Anthropic Claude Fable 5 GA, Mythos 5 limited release</sub>
- `2026-06-11` [CISA BOD 26-04](2026-06-11-cisa-bod.md)<br>  <sub>CISA BOD 26-04</sub>
- `2026-06-12` [US government issues export controls to Anthropic](2026-06-12-anthropic-mei-guo-zheng-fu.md)<br>  <sub>US government issues export controls to Anthropic</sub>
- `2026-06-12` [Google sues the China-linked "Outsider Enterprise" smishing network](2026-06-12-google-outsider-enterprise.md)<br>  <sub>Google sues the China-linked "Outsider Enterprise" smishing network</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-24-operation-endgame-europol-stealc.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
