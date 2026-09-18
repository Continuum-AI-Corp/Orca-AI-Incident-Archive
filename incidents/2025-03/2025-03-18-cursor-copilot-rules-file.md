---
id: 2025-03-18-cursor-copilot-rules-file
title: "Cursor / Copilot \"Rules File Backdoor\""
title_zh: "Cursor / Copilot「Rules File Backdoor」"
title_ja: "Cursor／Copilotの「ルールファイル・バックドア」"
title_ko: "Cursor / Copilot \"규칙 파일 백도어\""
title_de: "Cursor / Copilot „Rules File Backdoor“"
title_fr: "« Rules File Backdoor » dans Cursor / Copilot"
title_es: "Backdoor en archivos de reglas de Cursor / Copilot"
date: 2025-03-18
date_precision: day
date_raw: "2025-03-18"

kind: incident
type: [SUPPLY]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Pillar Security disclosed that **invisible Unicode characters** can be embedded in `.cursorrules`, `.cursor/rules/` and `.github/copilot-instructions.md` — blank to the human eye but fully readable by the model. The instructions make the model inject backdoors, hardcoded credentials or exfiltration code into every suggestion, **and this stays invisible in PR review**. Cursor was notified in 2025-02 and GitHub in 03; **Cursor responded that it is not a platform vulnerability and that users should manage the risk themselves**; GitHub shipped a hidden-Unicode warning on 2025-05-01


summary_zh: |
  Pillar Security 披露：在 `.cursorrules`、`.cursor/rules/`、`.github/copilot-instructions.md` 中嵌入**不可见 Unicode 字符**——人眼看是空白，模型完全可读。指令让模型在每次建议中注入后门、硬编码凭据或外带代码，**且在 PR review 中不可见**。2025-02 报 Cursor、03 报 GitHub；**Cursor 回应称不属平台漏洞、应由用户自行管理风险**；GitHub 于 2025-05-01 上线隐藏 Unicode 警告

summary_ja: |
  Pillar Securityが、**目に見えないUnicode文字**を`.cursorrules`、`.cursor/rules/`、`.github/copilot-instructions.md`に埋め込めることを公表した。人間の目には空白だが、モデルは完全に読める。この指示によりモデルはすべての提案にバックドア、ハードコードされた認証情報、外部送信コードを注入し、**PRレビューでも見えないままとなる**。Cursorには2025-02に、GitHubには03に通知。**Cursorはプラットフォームの脆弱性ではなく、ユーザー自身がリスクを管理すべきだと回答**。GitHubは2025-05-01に隠しUnicodeの警告を実装した

summary_ko: |
  Pillar Security는 `.cursorrules`, `.cursor/rules/`, `.github/copilot-instructions.md`에 **눈에 보이지 않는 유니코드 문자**를 삽입할 수 있다고 공개했다 — 사람 눈에는 비어 있지만 모델은 온전히 읽을 수 있다. 이 지시는 모델이 모든 제안에 백도어, 하드코딩된 자격 증명, 유출 코드를 넣게 만들며, **PR 리뷰에서도 보이지 않는다**. Cursor에는 2025-02, GitHub에는 03에 통보했고, **Cursor는 플랫폼 취약점이 아니며 사용자가 스스로 위험을 관리해야 한다고 답했다**. GitHub은 2025-05-01 숨겨진 유니코드 경고 기능을 배포했다

summary_de: |
  Pillar Security legte offen, dass **unsichtbare Unicode-Zeichen** in `.cursorrules`, `.cursor/rules/` und `.github/copilot-instructions.md` eingebettet werden können — für das menschliche Auge leer, aber vom Modell vollständig lesbar. Die Anweisungen bringen das Modell dazu, in jeden Vorschlag Backdoors, fest codierte Zugangsdaten oder Exfiltrationscode einzufügen, **und dies bleibt im PR-Review unsichtbar**. Cursor wurde 2025-02 informiert, GitHub im 03; **Cursor antwortete, es sei keine Plattform-Schwachstelle, und die Nutzer müssten das Risiko selbst managen**; GitHub lieferte am 2025-05-01 eine Warnung vor verstecktem Unicode aus

summary_fr: |
  Pillar Security a révélé que des **caractères Unicode invisibles** peuvent être intégrés dans `.cursorrules`, `.cursor/rules/` et `.github/copilot-instructions.md` — invisibles à l'œil humain mais parfaitement lisibles par le modèle. Ces instructions poussent le modèle à injecter des backdoors, des identifiants codés en dur ou du code d'exfiltration dans chaque suggestion, **et cela reste invisible lors de la revue de PR**. Cursor a été notifié en 2025-02 et GitHub en 03 ; **Cursor a répondu qu'il ne s'agit pas d'une vulnérabilité de la plateforme et que les utilisateurs doivent gérer ce risque eux-mêmes** ; GitHub a déployé le 2025-05-01 un avertissement pour les caractères Unicode cachés

summary_es: |
  Pillar Security reveló que se pueden incrustar **caracteres Unicode invisibles** en `.cursorrules`, `.cursor/rules/` y `.github/copilot-instructions.md` — invisibles al ojo humano pero totalmente legibles para el modelo. Las instrucciones hacen que el modelo inyecte puertas traseras, credenciales codificadas de forma fija o código de exfiltración en cada sugerencia, **y esto permanece invisible en la revisión del PR**. Cursor fue notificado en 2025-02 y GitHub en 03; **Cursor respondió que no es una vulnerabilidad de la plataforma y que los usuarios deben gestionar el riesgo por sí mismos**; GitHub publicó una advertencia de Unicode oculto el 2025-05-01

sources:
  - url: https://www.pillar.security/blog/new-vulnerability-in-github-copilot-and-cursor-how-hackers-can-weaponize-code-agents
    label: Pillar Security
  - url: https://www.scworld.com/news/how-ai-coding-assistants-could-be-compromised-via-rules-file
    label: SC Media

disputed: false
landmark: true
scan_month: 2025-03
scan_ref: "SCAN.md §5 2025-03"
---

# Cursor / Copilot "Rules File Backdoor"

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## Summary

Pillar Security disclosed that **invisible Unicode characters** can be embedded in `.cursorrules`, `.cursor/rules/` and `.github/copilot-instructions.md` — blank to the human eye but fully readable by the model. The instructions make the model inject backdoors, hardcoded credentials or exfiltration code into every suggestion, **and this stays invisible in PR review**. Cursor was notified in 2025-02 and GitHub in 03; **Cursor responded that it is not a platform vulnerability and that users should manage the risk themselves**; GitHub shipped a hidden-Unicode warning on 2025-05-01

## Attack chain

```mermaid
flowchart LR
    E["Poisoned package / repository / agent config"]:::entry
    S0["Developer or agent installs it automatically"]:::step
    I["Credential theft and self-propagation"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Pillar Security | <https://www.pillar.security/blog/new-vulnerability-in-github-copilot-and-cursor-how-hackers-can-weaponize-code-agents> |
| 2 | SC Media | <https://www.scworld.com/news/how-ai-coding-assistants-could-be-compromised-via-rules-file> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-03-18` (raw: 2025-03-18, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-03-18-cursor-copilot-rules-file` |

<sub>**Why this classification:** Real incident without a confirmed specific victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-02-06` [Hugging Face "nullifAI" malicious models](../2025-02/2025-02-06-hugging-face-nullifai.md)<br>  <sub>Hugging Face "nullifAI" malicious models</sub>
- `2025-04-01` ["Slopsquatting" gets its name](../2025-04/2025-04-01-slopsquatting-gai-nian-cheng-xing.md)<br>  <sub>"Slopsquatting" gets its name</sub>
- `2025-07-13` [Amazon Q Developer extension poisoned](../2025-07/2025-07-13-amazon-q-extension-poisoned.md)<br>  <sub>Amazon Q Developer extension poisoned</sub>
- `2025-08-08` [Salesloft Drift OAuth token theft](../2025-08/2025-08-08-salesloft-drift-oauth-theft.md)<br>  <sub>Salesloft Drift OAuth token theft</sub>

---

[← 2025-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-03/2025-03-18-cursor-copilot-rules-file.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
