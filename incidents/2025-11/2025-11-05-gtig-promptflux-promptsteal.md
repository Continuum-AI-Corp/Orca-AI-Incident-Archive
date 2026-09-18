---
id: 2025-11-05-gtig-promptflux-promptsteal
title: "GTIG: PROMPTFLUX / PROMPTSTEAL"
title_zh: "GTIG：PROMPTFLUX / PROMPTSTEAL"
title_ja: "GTIG：PROMPTFLUX／PROMPTSTEAL"
title_ko: "GTIG: PROMPTFLUX / PROMPTSTEAL"
title_de: "GTIG: PROMPTFLUX / PROMPTSTEAL"
title_fr: "GTIG : PROMPTFLUX / PROMPTSTEAL"
title_es: "GTIG: PROMPTFLUX / PROMPTSTEAL"
date: 2025-11-05
date_precision: day
date_raw: "2025-11-05"

kind: incident
type: [WEAPON]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **First malware families observed calling an LLM at runtime**. **PROMPTSTEAL** was used by Russia's **APT28 (FROZENLAKE)** **in live operations against Ukraine**, calling **Qwen2.5-Coder-32B-Instruct** through the Hugging Face API to generate commands dynamically; **PROMPTFLUX** (first seen 2025-06) is a VBScript dropper that calls the Gemini API for obfuscation and evasion techniques, and **is still in development/testing, without real compromise capability**. Attackers were also found using pretexts such as "CTF student" and "security researcher" to bypass Gemini guardrails


summary_zh: |
  **首次发现在运行时调用 LLM 的恶意软件家族**。**PROMPTSTEAL** 由俄 **APT28（FROZENLAKE）** 在**对乌克兰的实战中**使用，经 Hugging Face API 调 **Qwen2.5-Coder-32B-Instruct** 动态生成命令；**PROMPTFLUX**（2025-06 首见）为 VBScript dropper，调 Gemini API 请求混淆与规避技术，**仍在开发/测试阶段，不具备实际攻陷能力**。另发现攻击者用「CTF 参赛学生」「安全研究员」等托词绕过 Gemini 护栏

summary_ja: |
  **実行時にLLMを呼び出すマルウェアファミリーの初観測例**。**PROMPTSTEAL**はロシアの**APT28（FROZENLAKE）**が**ウクライナに対する実作戦で使用**し、Hugging Face API経由で**Qwen2.5-Coder-32B-Instruct**を呼び出してコマンドを動的生成。**PROMPTFLUX**（初観測2025-06）はVBScriptドロッパーで、難読化と回避手法のためにGemini APIを呼び出し、**現在も開発・テスト段階にあり、実際の侵害能力はない**。攻撃者は「CTF学生」「セキュリティ研究者」などの名目でGeminiのガードレールを回避していたことも確認された

summary_ko: |
  **런타임에 LLM을 호출하는 것이 관찰된 최초의 악성코드 계열**. **PROMPTSTEAL**은 러시아의 **APT28 (FROZENLAKE)**이 **우크라이나를 대상으로 한 실제 작전**에서 사용했으며, Hugging Face API를 통해 **Qwen2.5-Coder-32B-Instruct**를 호출해 명령을 동적으로 생성했다. **PROMPTFLUX**(2025-06 최초 관찰)는 VBScript 드로퍼로 Gemini API를 호출해 난독화와 회피 기법을 얻으며, **아직 개발/테스트 단계로 실제 침해 능력은 없다**. 공격자들이 "CTF 학생", "보안 연구자" 같은 명목으로 Gemini 가드레일을 우회한 사례도 발견되었다

summary_de: |
  **Die ersten Malware-Familien, die zur Laufzeit ein LLM aufrufen**. **PROMPTSTEAL** wurde von Russlands **APT28 (FROZENLAKE)** **in laufenden Operationen gegen die Ukraine** eingesetzt und rief **Qwen2.5-Coder-32B-Instruct** über die Hugging-Face-API auf, um Befehle dynamisch zu erzeugen; **PROMPTFLUX** (erstmals gesehen 2025-06) ist ein VBScript-Dropper, der die Gemini-API für Verschleierungs- und Evasion-Techniken aufruft und **sich noch in Entwicklung/Test befindet, ohne echte Kompromittierungsfähigkeit**. Angreifer wurden zudem dabei beobachtet, mit Vorwänden wie „CTF-Student“ und „Sicherheitsforscher“ die Gemini-Guardrails zu umgehen

summary_fr: |
  **Premières familles de malwares observées appelant un LLM à l'exécution**. **PROMPTSTEAL** a été utilisé par l'**APT28 (FROZENLAKE)** russe **dans des opérations réelles contre l'Ukraine**, appelant **Qwen2.5-Coder-32B-Instruct** via l'API Hugging Face pour générer des commandes dynamiquement ; **PROMPTFLUX** (vu pour la première fois en 2025-06) est un dropper VBScript qui appelle l'API Gemini pour des techniques d'obfuscation et d'évasion, et **reste en développement/test, sans capacité de compromission réelle**. Des attaquants ont aussi été observés utilisant des prétextes comme « étudiant en CTF » et « chercheur en sécurité » pour contourner les garde-fous de Gemini

summary_es: |
  **Las primeras familias de malware observadas que llaman a un LLM en tiempo de ejecución**. **PROMPTSTEAL** fue usado por **APT28 (FROZENLAKE)** de Rusia **en operaciones reales contra Ucrania**, llamando a **Qwen2.5-Coder-32B-Instruct** a través de la API de Hugging Face para generar comandos de forma dinámica; **PROMPTFLUX** (visto por primera vez en 2025-06) es un dropper en VBScript que llama a la API de Gemini para obtener técnicas de ofuscación y evasión, y **sigue en desarrollo/pruebas, sin capacidad de compromiso real**. También se observó a atacantes usando pretextos como "estudiante de CTF" e "investigador de seguridad" para eludir los guardrails de Gemini

sources:
  - url: https://services.google.com/fh/files/misc/advances-in-threat-actor-usage-of-ai-tools-en.pdf
    label: GTIG PDF

disputed: false
landmark: true
scan_month: 2025-11
scan_ref: "SCAN.md §5 2025-11"
---

# GTIG: PROMPTFLUX / PROMPTSTEAL

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

**First malware families observed calling an LLM at runtime**. **PROMPTSTEAL** was used by Russia's **APT28 (FROZENLAKE)** **in live operations against Ukraine**, calling **Qwen2.5-Coder-32B-Instruct** through the Hugging Face API to generate commands dynamically; **PROMPTFLUX** (first seen 2025-06) is a VBScript dropper that calls the Gemini API for obfuscation and evasion techniques, and **is still in development/testing, without real compromise capability**. Attackers were also found using pretexts such as "CTF student" and "security researcher" to bypass Gemini guardrails

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
| 1 | GTIG PDF | <https://services.google.com/fh/files/misc/advances-in-threat-actor-usage-of-ai-tools-en.pdf> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-11-05` (raw: 2025-11-05, precision `day`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-11-05-gtig-promptflux-promptsteal` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2025-11-13` [GTG-1002: first AI-orchestrated cyber-espionage campaign](2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md)<br>  <sub>GTG-1002: first AI-orchestrated cyber-espionage campaign</sub>
- `2025-11-03` [SesameOp](2025-11-03-sesameop.md)<br>  <sub>SesameOp</sub>
- `2025-12-28` [Mexico government intrusion campaign begins](../2025-12/2025-12-28-mexico-government-intrusion-begins.md)<br>  <sub>Mexico government intrusion campaign begins</sub>
- `2025-10-07` [OpenAI October threat report](../2025-10/2025-10-07-shi-wei-xie-bao-gao.md)<br>  <sub>OpenAI October threat report</sub>

---

[← 2025-11 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-11/2025-11-05-gtig-promptflux-promptsteal.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
