---
id: 2025-11-14-echogram-yi-ci-fan-zhuan
title: "EchoGram: one word flips an AI guardrail's verdict"
title_zh: "EchoGram：一个词就能翻转 AI 护栏的判决"
title_ja: "EchoGram：1語でAIガードレールの判定が反転"
title_ko: "EchoGram: 단어 하나로 AI 가드레일 판정이 뒤집히다"
title_de: "EchoGram: ein Wort kippt das Urteil einer KI-Guardrail"
title_fr: "EchoGram : un mot renverse le verdict d'un garde-fou d'IA"
title_es: "EchoGram: una palabra da la vuelta al veredicto de un guardrail de IA"
date: 2025-11-14
date_precision: day
date_raw: "2025-11-14"

kind: research
type: [OTHER]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  HiddenLayer: dataset distillation or white-box tokenizer probing uncovers "**flip tokens**" that, appended to the end of a prompt, systematically flip a text classifier's or LLM-as-a-judge's safety verdict from "unsafe" to "safe". Example: adding **`=coffee`** makes a guardrail judge a prompt injection as safe; others include `oz` and `UIScrollView`. On Qwen3Guard 0.6B and 4B, **chaining several flip tokens makes the guardrail judge high-risk prompts about weapons, authentication bypass and cyberattacks as safe or only mildly concerning**. Key finding: **a single weak token only flips the verdict partially, but combined the effect grows sharply**, and the generated sequences are mostly meaningless strings — the LLM behind the guardrail still processes the original attack as usual


summary_zh: |
  HiddenLayer：用数据集蒸馏或白盒分词器探测挖出「**翻转词元（flip tokens）**」，附加到提示末尾即可系统性地把文本分类器与 LLM-as-a-judge 的安全判决从「unsafe」翻成「safe」。实例：加上 **`=coffee`** 就让护栏把一次提示注入判为安全；其他还有 `oz`、`UIScrollView` 等。在 Qwen3Guard 的 0.6B 与 4B 上，**串联多个翻转词元可让护栏把武器、认证绕过、网络攻击类的高危提示判为安全或仅轻微关切**。关键发现：**单个弱词元只能部分翻转，但组合起来效果急剧放大**，且生成的序列大多是无意义字符串，护栏背后的 LLM 仍照常处理原始攻击

summary_ja: |
  HiddenLayer：データセット蒸留やホワイトボックスのトークナイザープロービングにより、プロンプト末尾に付加するとテキスト分類器やLLM-as-a-judgeの安全判定を「unsafe」から「safe」へ体系的に反転させる「**flip tokens**」を発見。例：**`=coffee`**を追加するとガードレールがプロンプトインジェクションを安全と判定する。他に`oz`や`UIScrollView`など。Qwen3Guard 0.6Bと4Bでは、**複数のflip tokenを連鎖させると、兵器、認証バイパス、サイバー攻撃に関する高リスクプロンプトをガードレールが安全または軽度の懸念にすぎないと判定する**。重要な発見：**弱いトークン単体では判定を部分的にしか反転させられないが、組み合わせると効果が急激に増大する**。また生成されるシーケンスはほとんどが無意味な文字列で、ガードレール背後のLLMは元の攻撃を通常どおり処理してしまう

summary_ko: |
  HiddenLayer: 데이터셋 증류 또는 화이트박스 토크나이저 탐침으로 "**플립 토큰**"을 찾아냈다. 프롬프트 끝에 붙이면 텍스트 분류기나 LLM 심사자의 안전 판정이 "위험"에서 "안전"으로 체계적으로 뒤집힌다. 예: **`=coffee`**를 추가하면 가드레일이 프롬프트 인젝션을 안전하다고 판정하며, `oz`, `UIScrollView` 등도 있다. Qwen3Guard 0.6B와 4B에서는 **플립 토큰 여러 개를 연쇄하면 무기, 인증 우회, 사이버 공격에 관한 고위험 프롬프트를 가드레일이 안전 또는 경미한 우려로 판정**했다. 핵심 발견: **약한 토큰 하나로는 판정이 부분적으로만 뒤집히지만 결합하면 효과가 급격히 커지며**, 생성된 문자열은 대부분 무의미하다 — 가드레일 뒤의 LLM은 원래 공격을 평소처럼 처리한다

summary_de: |
  HiddenLayer: Dataset-Distillation oder White-Box-Tokenizer-Sondierung decken „**Flip-Tokens**“ auf, die, an das Ende eines Prompts angehängt, das Sicherheitsurteil eines Textklassifikators oder eines LLM-as-a-Judge systematisch von „unsafe“ zu „safe“ kippen. Beispiel: Das Anhängen von **`=coffee`** bringt eine Guardrail dazu, eine Prompt-Injection als sicher zu bewerten; weitere Beispiele sind `oz` und `UIScrollView`. Bei Qwen3Guard 0.6B und 4B **bringt die Verkettung mehrerer Flip-Tokens die Guardrail dazu, Hochrisiko-Prompts zu Waffen, Authentifizierungsumgehung und Cyberangriffen als sicher oder nur leicht bedenklich zu bewerten**. Zentrale Erkenntnis: **Ein einzelnes schwaches Token kippt das Urteil nur teilweise, kombiniert wächst die Wirkung jedoch stark**, und die erzeugten Sequenzen sind meist bedeutungslose Zeichenketten — das LLM hinter der Guardrail verarbeitet den ursprünglichen Angriff weiterhin wie gewohnt

summary_fr: |
  HiddenLayer : la distillation de jeux de données ou le sondage de tokenizer en boîte blanche révèlent des « **jetons de bascule** » qui, ajoutés à la fin d'un prompt, font systématiquement basculer le verdict de sécurité d'un classifieur de texte ou d'un LLM-juge de « dangereux » à « sûr ». Exemple : ajouter **`=coffee`** fait juger sûre une injection de prompt par le garde-fou ; d'autres incluent `oz` et `UIScrollView`. Sur Qwen3Guard 0.6B et 4B, **enchaîner plusieurs jetons de bascule fait juger sûrs ou seulement légèrement préoccupants des prompts à haut risque sur les armes, le contournement d'authentification et les cyberattaques**. Constat clé : **un seul jeton faible ne renverse le verdict que partiellement, mais combinés l'effet croît fortement**, et les séquences générées sont pour l'essentiel des chaînes sans signification — le LLM derrière le garde-fou traite toujours l'attaque d'origine normalement

summary_es: |
  HiddenLayer: la destilación de conjuntos de datos o el sondeo de tokenizadores de caja blanca descubren "**tokens de volteo**" que, añadidos al final de un prompt, cambian sistemáticamente el veredicto de seguridad de un clasificador de texto o de un LLM como juez de "peligroso" a "seguro". Ejemplo: añadir **`=coffee`** hace que un guardrail juzgue segura una inyección de prompt; otros incluyen `oz` y `UIScrollView`. En Qwen3Guard 0.6B y 4B, **encadenar varios tokens de volteo hace que el guardrail juzgue seguros o solo levemente preocupantes prompts de alto riesgo sobre armas, elusión de autenticación y ciberataques**. Hallazgo clave: **un solo token débil solo voltea el veredicto parcialmente, pero combinados el efecto crece bruscamente**, y las secuencias generadas son en su mayoría cadenas sin sentido — el LLM detrás del guardrail sigue procesando el ataque original como de costumbre

sources:
  - url: https://www.hiddenlayer.com/research/echogram-the-hidden-vulnerability-undermining-ai-guardrails
    label: HiddenLayer
  - url: https://www.theregister.com/software/2025/11/14/echogram_tokens_like_coffee_flip_ai_guardrail_verdicts/2044945
    label: The Register

disputed: false
landmark: true
scan_month: 2025-11
scan_ref: "SCAN.md §5 2025-11"
---

# EchoGram: one word flips an AI guardrail's verdict

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

HiddenLayer: dataset distillation or white-box tokenizer probing uncovers "**flip tokens**" that, appended to the end of a prompt, systematically flip a text classifier's or LLM-as-a-judge's safety verdict from "unsafe" to "safe". Example: adding **`=coffee`** makes a guardrail judge a prompt injection as safe; others include `oz` and `UIScrollView`. On Qwen3Guard 0.6B and 4B, **chaining several flip tokens makes the guardrail judge high-risk prompts about weapons, authentication bypass and cyberattacks as safe or only mildly concerning**. Key finding: **a single weak token only flips the verdict partially, but combined the effect grows sharply**, and the generated sequences are mostly meaningless strings — the LLM behind the guardrail still processes the original attack as usual

## Attack chain

```mermaid
flowchart LR
    E["Entry point"]:::entry
    S0["Process"]:::step
    I["Result<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | HiddenLayer | <https://www.hiddenlayer.com/research/echogram-the-hidden-vulnerability-undermining-ai-guardrails> |
| 2 | The Register | <https://www.theregister.com/software/2025/11/14/echogram_tokens_like_coffee_flip_ai_guardrail_verdicts/2044945> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-11-14` (raw: 2025-11-14, precision `day`) |
| Kind | Research demo `research` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-11-14-echogram-yi-ci-fan-zhuan` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2025-11 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-11/2025-11-14-echogram-yi-ci-fan-zhuan.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
