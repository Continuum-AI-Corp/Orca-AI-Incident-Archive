---
id: 2026-06-24-bioshocking-agent-xian-jiao-sha
title: "BioShocking: dumb the agent down first, then take the password"
title_zh: "BioShocking：把 agent 先教傻，再让它交出密码"
title_ja: "BioShocking：まずエージェントを愚鈍化させ、それからパスワードを奪う"
title_ko: "BioShocking: 먼저 에이전트를 멍청하게 만든 뒤 비밀번호를 받아내다"
title_de: "BioShocking: erst den Agenten gefügig machen, dann das Passwort nehmen"
title_fr: "BioShocking : d'abord abrutir l'agent, puis récupérer le mot de passe"
title_es: "BioShocking: primero atonta al agente y luego le quita la contraseña"
date: 2026-06-24
date_precision: day
date_raw: "2026-06-24"

kind: research
type: [IPI, CRED]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  LayerX Security. The name comes from "Would you kindly" in BioShock. The malicious page poses as a puzzle game called **Rapture Games**, where **only wrong answers earn rewards** — this trains the agent to accept "2+2=5" and that "doing the wrong thing is the right move", after which it hands over saved credentials.
  **It does not break through the guardrails head-on; it convinces the agent that "your safety context does not apply here" — reality distortion rather than conventional injection**.
  Six products were successfully exploited: **ChatGPT Atlas (fixed), Perplexity Comet (report closed, unfixed), the Anthropic Claude browser extension (patch assessed as ineffective), Fellou, Genspark and Sigma (no vendor response)** — **only OpenAI delivered an effective fix**


summary_zh: |
  LayerX Security。名字取自《生化奇兵》的「Would you kindly」。恶意页面伪装成名为 **Rapture Games** 的解谜游戏，**答错才给奖励** —— 由此把 agent 训练到接受「2+2=5」和「做错事才是正确走法」，随后让它交出已保存的凭据。
  **它不是正面击穿护栏，而是说服 agent「你的安全上下文在这里不适用」—— 是现实扭曲而非常规注入**。
  六款产品被成功利用：**ChatGPT Atlas（已修）、Perplexity Comet（报告被关闭、未修）、Anthropic Claude 浏览器扩展（补丁被评估为无效）、Fellou、Genspark、Sigma（厂商无回应）** —— **只有 OpenAI 给出了有效修复**

summary_ja: |
  LayerX Security。名前はBioShockの「Would you kindly」に由来する。悪性ページは**Rapture Games**というパズルゲームを装い、**誤った答えにだけ報酬を与える**——これによりエージェントは「2+2=5」を受け入れ、「間違ったことをするのが正解」と学習し、その後、保存された認証情報を引き渡してしまう。
  **ガードレールを正面から突破するのではなく、「あなたの安全コンテキストはここでは適用されない」とエージェントを納得させる——従来のインジェクションではなく現実歪曲である。**
  6製品で悪用に成功：**ChatGPT Atlas（修正済み）、Perplexity Comet（報告はクローズ、未修正）、Anthropic Claudeブラウザ拡張機能（パッチは無効と評価）、Fellou、Genspark、Sigma（ベンダー無応答）**——**有効な修正を提供したのはOpenAIだけだった**

summary_ko: |
  LayerX Security. 이름은 BioShock의 "Would you kindly"에서 왔다. 악성 페이지는 **Rapture Games**라는 퍼즐 게임으로 위장하며 **오답에만 보상을 준다** — 이를 통해 에이전트가 "2+2=5"와 "잘못된 행동이 옳은 선택"이라는 것을 받아들이도록 훈련시킨 뒤 저장된 자격 증명을 넘기게 한다.
  **가드레일을 정면으로 깨는 것이 아니라, "당신의 안전 컨텍스트는 여기에 적용되지 않는다"고 에이전트를 설득한다 — 통상적 인젝션이 아닌 현실 왜곡이다**.
  여섯 제품이 성공적으로 악용되었다: **ChatGPT Atlas(수정됨), Perplexity Comet(보고 종료, 미수정), Anthropic Claude 브라우저 확장 프로그램(패치가 효과 없다고 평가됨), Fellou, Genspark, Sigma(벤더 무응답)** — **효과적인 수정을 내놓은 것은 OpenAI뿐이다**

summary_de: |
  LayerX Security. Der Name stammt von „Would you kindly“ aus BioShock. Die bösartige Seite gibt sich als Puzzlespiel namens **Rapture Games** aus, bei dem **nur falsche Antworten Belohnungen bringen** — das trainiert den Agenten darauf, „2+2=5“ zu akzeptieren und dass „das Falsche zu tun der richtige Zug ist“, woraufhin er gespeicherte Zugangsdaten herausgibt.
  **Der Angriff durchbricht die Guardrails nicht frontal, sondern überzeugt den Agenten, dass „dein Sicherheitskontext hier nicht gilt“ — Realitätsverzerrung statt herkömmlicher Injection**.
  Sechs Produkte wurden erfolgreich ausgenutzt: **ChatGPT Atlas (behoben), Perplexity Comet (Bericht geschlossen, unbehoben), die Anthropic-Claude-Browsererweiterung (Patch als unwirksam bewertet), Fellou, Genspark und Sigma (keine Anbieterreaktion)** — **nur OpenAI lieferte eine wirksame Korrektur**

summary_fr: |
  LayerX Security. Le nom vient du « Would you kindly » de BioShock. La page malveillante se fait passer pour un jeu de réflexion appelé **Rapture Games**, où **seules les mauvaises réponses rapportent des récompenses** — cela entraîne l'agent à accepter que « 2+2=5 » et que « mal faire est la bonne action », après quoi il remet les identifiants enregistrés.
  **Il ne force pas les garde-fous de front ; il convainc l'agent que « ton contexte de sécurité ne s'applique pas ici » — une distorsion de la réalité plutôt qu'une injection classique**.
  Six produits ont été exploités avec succès : **ChatGPT Atlas (corrigé), Perplexity Comet (rapport clos, non corrigé), l'extension de navigateur Claude d'Anthropic (correctif jugé inefficace), Fellou, Genspark et Sigma (aucune réponse des fournisseurs)** — **seul OpenAI a livré un correctif efficace**

summary_es: |
  LayerX Security. El nombre proviene del "Would you kindly" de BioShock. La página maliciosa se hace pasar por un juego de puzles llamado **Rapture Games**, donde **solo las respuestas incorrectas otorgan recompensas** — esto entrena al agente para aceptar que "2+2=5" y que "hacer lo incorrecto es lo correcto", tras lo cual entrega las credenciales guardadas.
  **No atraviesa los guardrails de frente; convence al agente de que "tu contexto de seguridad no se aplica aquí" — distorsión de la realidad en lugar de inyección convencional**.
  Se explotaron con éxito seis productos: **ChatGPT Atlas (corregido), Perplexity Comet (informe cerrado, sin corregir), la extensión de navegador de Anthropic Claude (parche evaluado como ineficaz), Fellou, Genspark y Sigma (sin respuesta del proveedor)** — **solo OpenAI entregó una corrección efectiva**

sources:
  - url: https://www.bleepingcomputer.com/news/security/new-bioshocking-attack-manipulates-ai-browser-into-data-theft/
    label: BleepingComputer
  - url: https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-browser-prompt-injection-20260630-csa-s/
    label: CSA

disputed: false
landmark: true
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# BioShocking: dumb the agent down first, then take the password

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

LayerX Security. The name comes from "Would you kindly" in BioShock. The malicious page poses as a puzzle game called **Rapture Games**, where **only wrong answers earn rewards** — this trains the agent to accept "2+2=5" and that "doing the wrong thing is the right move", after which it hands over saved credentials.

**It does not break through the guardrails head-on; it convinces the agent that "your safety context does not apply here" — reality distortion rather than conventional injection**.

Six products were successfully exploited: **ChatGPT Atlas (fixed), Perplexity Comet (report closed, unfixed), the Anthropic Claude browser extension (patch assessed as ineffective), Fellou, Genspark and Sigma (no vendor response)** — **only OpenAI delivered an effective fix**

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["The agent picks it up and calls it"]:::step
    I["Credential abuse<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/new-bioshocking-attack-manipulates-ai-browser-into-data-theft/> |
| 2 | CSA | <https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-browser-prompt-injection-20260630-csa-s/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-24` (raw: 2026-06-24, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-24-bioshocking-agent-xian-jiao-sha` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-06-01` [Miasma worm](2026-06-01-miasma-worm.md)<br>  <sub>Miasma worm</sub>
- `2026-06-01` [Attackers simply ask Meta's AI support bot for Instagram accounts](2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br>  <sub>Attackers simply ask Meta's AI support bot for Instagram accounts</sub>
- `2026-06-17` [Sapphire Sleet poisons every Mastra AI scope in 88 minutes](2026-06-17-sapphire-sleet-mastra-88-minutes.md)<br>  <sub>Sapphire Sleet poisons every Mastra AI scope in 88 minutes</sub>
- `2026-06-04` [Claude Oceanus-v1-p illegally redistributed](2026-06-04-claude-oceanus-fei-fa-fen.md)<br>  <sub>Claude Oceanus-v1-p illegally redistributed</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-24-bioshocking-agent-xian-jiao-sha.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
