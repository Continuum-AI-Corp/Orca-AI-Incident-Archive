---
id: 2025-01-31-github-copilot-shuang-lou-dong
title: "Two GitHub Copilot flaws"
title_zh: "GitHub Copilot 双漏洞"
title_ja: "GitHub Copilotの2つの脆弱性"
title_ko: "GitHub Copilot 취약점 2건"
title_de: "Zwei Schwachstellen in GitHub Copilot"
title_fr: "Deux failles dans GitHub Copilot"
title_es: "Dos fallos en GitHub Copilot"
date: 2025-01-31
date_precision: day
date_raw: "2025-01-31"

kind: vulnerability
type: [SANDBOX]
severity: medium
confidence: B
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  ① an "affirmation jailbreak" (bypassing ethical filters with agreeable phrasing) ② proxy-token interception to freeload on OpenAI's premium models


summary_zh: |
  ① "affirmation jailbreak"（用附和语绕过伦理过滤）② 代理令牌拦截，白嫖 OpenAI 高级模型

summary_ja: |
  ①「同意型ジェイルブレイク」（同調的な言い回しで倫理フィルターを回避）②プロキシトークンを傍受してOpenAIのプレミアムモデルにただ乗り

summary_ko: |
  ① "긍정 탈옥"(동조적인 표현으로 윤리 필터를 우회) ② 프록시 토큰을 가로채 OpenAI 프리미엄 모델에 무임승차

summary_de: |
  ① ein „Affirmation Jailbreak“ (Umgehung ethischer Filter durch zustimmende Formulierungen) ② Abfangen von Proxy-Token, um OpenAIs Premium-Modelle kostenlos mitzunutzen

summary_fr: |
  ① un « jailbreak par affirmation » (contourner les filtres éthiques en formulant les demandes de manière agréable) ② l'interception de jetons de proxy pour profiter gratuitement des modèles premium d'OpenAI

summary_es: |
  ① un "jailbreak de afirmación" (eludir los filtros éticos con frases complacientes) ② interceptación de tokens de proxy para usar gratis los modelos premium de OpenAI

sources:
  - url: https://genai.owasp.org/2025/03/06/owasp-gen-ai-incident-exploit-round-up-jan-feb-2025/
    label: "OWASP Jan-Feb'25"

disputed: false
landmark: false
scan_month: 2025-01
scan_ref: "SCAN.md §5 2025-01"
---

# Two GitHub Copilot flaws

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## Summary

① an "affirmation jailbreak" (bypassing ethical filters with agreeable phrasing) ② proxy-token interception to freeload on OpenAI's premium models

## Attack chain

```mermaid
flowchart LR
    E["Evaluation / container environment"]:::entry
    S0["Residual egress path"]:::step
    I["Escape to a real system<br/><i>(flaw disclosed, no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | OWASP Jan-Feb'25 | <https://genai.owasp.org/2025/03/06/owasp-gen-ai-incident-exploit-round-up-jan-feb-2025/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-01-31` (raw: 2025-01-31, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape |
| Severity | **Medium** `medium` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-01-31-github-copilot-shuang-lou-dong` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2025-03-01` [Manus AI leaks in-sandbox prompts and runtime code](../2025-03/2025-03-01-manus-sha-xiang-nei-ti.md)<br>  <sub>Manus AI leaks in-sandbox prompts and runtime code</sub>
- `2025-07-21` [Claude Code hooks RCE](../2025-07/2025-07-21-claude-code-hooks-rce.md)<br>  <sub>Claude Code hooks RCE</sub>
- `2025-07-28` [Gemini CLI silent code execution](../2025-07/2025-07-28-gemini-cli-jing-mo-dai.md)<br>  <sub>Gemini CLI silent code execution</sub>
- `2025-08-01` [Cursor CurXecute (CVE-2025-54135)](../2025-08/2025-08-01-cursor-curxecute.md)<br>  <sub>Cursor CurXecute (CVE-2025-54135)</sub>

---

[← 2025-01 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-01/2025-01-31-github-copilot-shuang-lou-dong.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
