---
id: 2026-08-25-nemoclaw-dns-zhong-bang-ding
title: "NemoClaw (CVE-2026-65105): DNS rebinding rewrites the model's chat template"
title_zh: "NemoClaw（CVE-2026-65105）：DNS 重绑定改掉模型的聊天模板"
title_ja: "NemoClaw（CVE-2026-65105）：DNSリバインディングがモデルのチャットテンプレートを書き換える"
title_ko: "NemoClaw (CVE-2026-65105): DNS 리바인딩으로 모델 채팅 템플릿 재작성"
title_de: "NemoClaw (CVE-2026-65105): DNS-Rebinding schreibt das Chat-Template des Modells um"
title_fr: "NemoClaw (CVE-2026-65105) : le DNS rebinding réécrit le template de chat du modèle"
title_es: "NemoClaw (CVE-2026-65105): el DNS rebinding reescribe la plantilla de chat del modelo"
date: 2026-08-25
date_precision: day
date_raw: "2026-08-25"

kind: research
type: [INFRA]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Oasis research team demo: **DNS rebinding** lets browser JavaScript reach Ollama under a fragile configuration, then uses the `/api/create` endpoint to **rewrite the model's chat template** (which decides how messages are formatted before inference). **The injected instructions persist across later conversations, still taking effect even when the agent supplies its own system prompt** — persistent poisoning at the model level. NVIDIA fixed it on 08-25


summary_zh: |
  Oasis 研究团队演示：**DNS 重绑定**让浏览器 JavaScript 在脆弱配置下触达 Ollama，再用 `/api/create` 端点**修改模型的 chat template**（决定消息在推理前如何被格式化）。**植入的指令在之后的对话中持续存在，即使 agent 另行提供了系统提示也依然生效** —— 这是模型层面的持久投毒。NVIDIA 于 08-25 修复

summary_ja: |
  Oasis研究チームのデモ：**DNSリバインディング**により、脆弱な構成下でブラウザのJavaScriptがOllamaに到達し、`/api/create`エンドポイントを使って**モデルのチャットテンプレート（推論前にメッセージをどう整形するかを決める）を書き換える**。**注入された指示は以降の会話にも持続し、エージェントが独自のシステムプロンプトを指定してもなお有効である**——モデルレベルでの永続的ポイズニング。NVIDIAは08-25に修正した

summary_ko: |
  Oasis 연구팀 시연: **DNS 리바인딩**으로 브라우저 JavaScript가 취약한 구성의 Ollama에 도달한 뒤 `/api/create` 엔드포인트를 사용해 **모델의 채팅 템플릿**(추론 전에 메시지 형식을 정한다)을 재작성한다. **주입된 지시는 이후 대화에서도 지속되며 에이전트가 자체 시스템 프롬프트를 제공해도 여전히 작동한다** — 모델 수준의 영구 오염이다. NVIDIA는 08-25에 수정했다

summary_de: |
  Demo des Oasis-Forschungsteams: **DNS-Rebinding** lässt Browser-JavaScript unter einer fragilen Konfiguration Ollama erreichen, das dann über den Endpunkt `/api/create` **das Chat-Template des Modells umschreibt** (das festlegt, wie Nachrichten vor der Inferenz formatiert werden). **Die injizierten Anweisungen bleiben über spätere Unterhaltungen hinweg bestehen und wirken selbst dann noch, wenn der Agent seinen eigenen System-Prompt mitliefert** — persistente Vergiftung auf Modellebene. NVIDIA behob es am 08-25

summary_fr: |
  Démo de l'équipe de recherche d'Oasis : **le DNS rebinding** permet au JavaScript du navigateur d'atteindre Ollama dans une configuration fragile, puis d'utiliser le point de terminaison `/api/create` pour **réécrire le template de chat du modèle** (qui décide du formatage des messages avant l'inférence). **Les instructions injectées persistent dans les conversations suivantes, restant actives même quand l'agent fournit son propre prompt système** — un empoisonnement persistant au niveau du modèle. NVIDIA l'a corrigé le 08-25

summary_es: |
  Demostración del equipo de investigación de Oasis: el **DNS rebinding** permite que el JavaScript del navegador alcance Ollama bajo una configuración frágil, y luego usa el endpoint `/api/create` para **reescribir la plantilla de chat del modelo** (que decide cómo se formatean los mensajes antes de la inferencia). **Las instrucciones inyectadas persisten en conversaciones posteriores y siguen surtiendo efecto incluso cuando el agente proporciona su propio system prompt** — envenenamiento persistente a nivel de modelo. NVIDIA lo corrigió el 08-25

sources:
  - url: https://www.esecurityplanet.com/vulnerabilities/news-nvidia-nemoclaw-cve-2026-65105/
    label: eSecurity Planet

disputed: false
landmark: false
scan_month: 2026-08
scan_ref: "SCAN.md §6 2026-08"
---

# NemoClaw (CVE-2026-65105): DNS rebinding rewrites the model's chat template

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

Oasis research team demo: **DNS rebinding** lets browser JavaScript reach Ollama under a fragile configuration, then uses the `/api/create` endpoint to **rewrite the model's chat template** (which decides how messages are formatted before inference). **The injected instructions persist across later conversations, still taking effect even when the agent supplies its own system prompt** — persistent poisoning at the model level. NVIDIA fixed it on 08-25

## Attack chain

```mermaid
flowchart LR
    E["Agent infrastructure exposed to the internet"]:::entry
    S0["Unauthenticated access"]:::step
    I["RCE / data leak<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | eSecurity Planet | <https://www.esecurityplanet.com/vulnerabilities/news-nvidia-nemoclaw-cve-2026-65105/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-08-25` (raw: 2026-08-25, precision `day`) |
| Kind | Research demo `research` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-08-25-nemoclaw-dns-zhong-bang-ding` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-08-06` [Unauthenticated Langflow RCE added to CISA KEV](2026-08-06-langflow-rce-cisa-kev.md)<br>  <sub>Unauthenticated Langflow RCE added to CISA KEV</sub>
- `2026-08-01` [Azure SRE Agent privilege escalation (CVE-2026-62830)](2026-08-01-azure-sre-agent.md)<br>  <sub>Azure SRE Agent privilege escalation (CVE-2026-62830)</sub>
- `2026-08-26` [GitLab Duo's Claude agent can run arbitrary commands in CI](2026-08-26-gitlab-duo-claude-agent.md)<br>  <sub>GitLab Duo's Claude agent can run arbitrary commands in CI</sub>
- `2026-09-02` [Langflow CVE-2026-0768: the 12th Langflow flaw exploited in the wild this year](../2026-09/2026-09-02-langflow-jin-di-ye-li.md)<br>  <sub>Langflow CVE-2026-0768: the 12th Langflow flaw exploited in the wild this year</sub>

---

[← 2026-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-08/2026-08-25-nemoclaw-dns-zhong-bang-ding.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
