---
id: 2025-04-01-slopsquatting-gai-nian-cheng-xing
title: "\"Slopsquatting\" gets its name"
title_zh: "\"Slopsquatting\" 概念成型"
title_ja: "「Slopsquatting」に名前が付く"
title_ko: "\"Slopsquatting\"이라는 이름이 붙다"
title_de: "„Slopsquatting“ erhält seinen Namen"
title_fr: "Le « slopsquatting » trouve son nom"
title_es: "\"Slopsquatting\": se acuña el término"
date: 2025-04-01
date_precision: month
date_raw: "2025-04"

kind: policy
type: [SUPPLY]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  The term was coined by Python Software Foundation resident developer **Seth Larson**: it swaps the "human typo" of typosquatting for the "AI hallucination" — the model confidently recommends a package name that never existed, and an attacker registers it first. The scale was quantified by the USENIX Security 2025 paper "We Have a Package for You!": 16 code models produced 2.23 million samples, **19.7% of the recommended packages do not exist at all** (205,000 distinct hallucinated package names), with a mean hallucination rate of **21.7%** for open models and **5.2%** for commercial ones; **58% of hallucinated packages recur across 10 runs** — that is, predictable and squat-able


summary_zh: |
  术语由 Python 软件基金会驻场开发者 **Seth Larson** 提出：把 typosquatting 里的「人类打字错误」换成「AI 幻觉」—— 模型自信地推荐一个从不存在的包名，攻击者抢先注册。规模由 USENIX Security 2025 论文《We Have a Package for You!》量化：16 个代码模型生成 223 万个样本，**19.7% 的推荐包根本不存在**（20.5 万个不同的幻觉包名），开源模型幻觉率均值 **21.7%**、商用 **5.2%**；**58% 的幻觉包在 10 次运行中重复出现** —— 即可预测、可抢注

summary_ja: |
  この用語を考案したのはPython Software Foundationのレジデント開発者**Seth Larson**氏。typosquattingの「人間のタイプミス」を「AIのハルシネーション」に置き換えたもので、モデルが存在しないパッケージ名を自信を持って推薦し、攻撃者がそれを先に登録する。規模はUSENIX Security 2025論文「We Have a Package for You!」が定量化した：16のコードモデルが223万件のサンプルを生成し、**推薦されたパッケージの19.7%が実在しない**（幻覚パッケージ名は20万5,000種）。平均ハルシネーション率はオープンモデル**21.7%**、商用モデル**5.2%**。**幻覚パッケージの58%は10回の実行で繰り返し出現**——つまり予測可能で、先回り登録が可能だ

summary_ko: |
  이 용어는 Python Software Foundation 상주 개발자 **Seth Larson**이 만들었다. 타이포스쿼팅의 "사람의 오타"를 "AI 환각"으로 바꾼 것으로, 모델이 존재한 적 없는 패키지 이름을 자신 있게 추천하면 공격자가 먼저 등록하는 수법이다. 규모는 USENIX Security 2025 논문 "We Have a Package for You!"에서 정량화되었다. 코드 모델 16종이 223만 개의 샘플을 생성했고 **추천 패키지의 19.7%가 아예 존재하지 않았다**(서로 다른 환각 패키지 이름 20만 5천 개). 평균 환각률은 오픈 모델 **21.7%**, 상용 모델 **5.2%**였으며 **환각 패키지의 58%는 10회 실행에서 반복 등장**했다 — 즉 예측 가능하고 선점 가능하다

summary_de: |
  Der Begriff wurde von **Seth Larson**, Resident Developer der Python Software Foundation, geprägt: Er ersetzt den „menschlichen Tippfehler“ des Typosquatting durch die „KI-Halluzination“ — das Modell empfiehlt überzeugt einen Paketnamen, den es nie gab, und ein Angreifer registriert ihn zuerst. Das Ausmaß quantifizierte die USENIX-Security-2025-Arbeit „We Have a Package for You!“: 16 Codemodelle erzeugten 2.23 Millionen Stichproben, **19.7% der empfohlenen Pakete existieren überhaupt nicht** (205,000 verschiedene halluzinierte Paketnamen), mit einer mittleren Halluzinationsrate von **21.7%** bei offenen Modellen und **5.2%** bei kommerziellen; **58% der halluzinierten Pakete treten über 10 Läufe hinweg wiederholt auf** — also vorhersehbar und squatbar

summary_fr: |
  Le terme a été forgé par le développeur résident de la Python Software Foundation **Seth Larson** : il remplace la « faute de frappe humaine » du typosquatting par l'« hallucination d'IA » — le modèle recommande avec assurance un nom de paquet qui n'a jamais existé, et un attaquant l'enregistre le premier. L'ampleur a été quantifiée par l'article USENIX Security 2025 « We Have a Package for You! » : 16 modèles de code ont produit 2,23 millions d'échantillons, **19,7 % des paquets recommandés n'existent pas du tout** (205 000 noms de paquets hallucinés distincts), avec un taux moyen d'hallucination de **21,7 %** pour les modèles ouverts et de **5,2 %** pour les modèles commerciaux ; **58 % des paquets hallucinés réapparaissent sur 10 exécutions** — donc prévisibles et enregistrables

summary_es: |
  El término lo acuñó el desarrollador residente de la Python Software Foundation **Seth Larson**: cambia el "error tipográfico humano" del typosquatting por la "alucinación de IA" — el modelo recomienda con confianza un nombre de paquete que nunca existió, y un atacante lo registra primero. La magnitud la cuantificó el artículo de USENIX Security 2025 "We Have a Package for You!": 16 modelos de código produjeron 2.23 millones de muestras, **el 19.7% de los paquetes recomendados no existe en absoluto** (205,000 nombres de paquetes alucinados distintos), con una tasa media de alucinación del **21.7%** en modelos abiertos y del **5.2%** en comerciales; **el 58% de los paquetes alucinados se repite en 10 ejecuciones** — es decir, son predecibles y registrables

sources:
  - url: https://en.wikipedia.org/wiki/Slopsquatting
    label: Wikipedia
  - url: https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks
    label: Socket

disputed: false
landmark: false
scan_month: 2025-04
scan_ref: "SCAN.md §5 2025-04"
---

# "Slopsquatting" gets its name

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## Summary

The term was coined by Python Software Foundation resident developer **Seth Larson**: it swaps the "human typo" of typosquatting for the "AI hallucination" — the model confidently recommends a package name that never existed, and an attacker registers it first. The scale was quantified by the USENIX Security 2025 paper "We Have a Package for You!": 16 code models produced 2.23 million samples, **19.7% of the recommended packages do not exist at all** (205,000 distinct hallucinated package names), with a mean hallucination rate of **21.7%** for open models and **5.2%** for commercial ones; **58% of hallucinated packages recur across 10 runs** — that is, predictable and squat-able

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
| 1 | Wikipedia | <https://en.wikipedia.org/wiki/Slopsquatting> |
| 2 | Socket | <https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-04-01` (raw: 2025-04, precision `month`) |
| Kind | Policy & regulation `policy` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-04-01-slopsquatting-gai-nian-cheng-xing` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-03-18` [Cursor / Copilot "Rules File Backdoor"](../2025-03/2025-03-18-cursor-copilot-rules-file.md)<br>  <sub>Cursor / Copilot "Rules File Backdoor"</sub>
- `2025-02-06` [Hugging Face "nullifAI" malicious models](../2025-02/2025-02-06-hugging-face-nullifai.md)<br>  <sub>Hugging Face "nullifAI" malicious models</sub>
- `2025-07-13` [Amazon Q Developer extension poisoned](../2025-07/2025-07-13-amazon-q-extension-poisoned.md)<br>  <sub>Amazon Q Developer extension poisoned</sub>
- `2025-08-08` [Salesloft Drift OAuth token theft](../2025-08/2025-08-08-salesloft-drift-oauth-theft.md)<br>  <sub>Salesloft Drift OAuth token theft</sub>

---

[← 2025-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-04/2025-04-01-slopsquatting-gai-nian-cheng-xing.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
