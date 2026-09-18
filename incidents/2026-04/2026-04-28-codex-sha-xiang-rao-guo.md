---
id: 2026-04-28-codex-sha-xiang-rao-guo
title: "OpenAI Codex sandbox-escape zero-day"
title_zh: "OpenAI Codex 沙箱绕过零日"
title_ja: "OpenAI Codexのサンドボックス脱出ゼロデイ"
title_ko: "OpenAI Codex 샌드박스 탈출 제로데이"
title_de: "OpenAI Codex: Sandbox-Escape-Zero-Day"
title_fr: "Zero-day d'évasion de bac à sable dans OpenAI Codex"
title_es: "Zero-day de escape del sandbox en OpenAI Codex"
date: 2026-04-28
date_precision: day
date_raw: "2026-04-28"

kind: research
type: [SANDBOX]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Trend ZDI-26-305, CVSS 8.6, improper isolation of the JS execution environment. Requires the user to work with a malicious repository. **OpenAI acknowledges the vulnerability but declined to fix it** (saying it is out of bounty scope and not part of the product's default exposure surface), so it has stayed unfixed, with restricted use the only mitigation


summary_zh: |
  Trend ZDI-26-305，CVSS 8.6，JS 执行环境隔离不当。需用户处理恶意仓库。**OpenAI 承认漏洞存在但拒绝修复**（称不在赏金范围且不属产品默认暴露面），因此长期未修复，唯一缓解是限制使用

summary_ja: |
  Trend ZDI-26-305、CVSS 8.6、JS実行環境の不適切な分離。ユーザーが悪性リポジトリを操作する必要がある。**OpenAIは脆弱性を認めたが修正を拒否した**（バウンティの対象外であり、製品のデフォルトの露出面ではないため）と述べたため未修正のままで、利用の制限だけが緩和策となっている

summary_ko: |
  Trend ZDI-26-305, CVSS 8.6, JS 실행 환경의 부적절한 격리. 사용자가 악성 저장소로 작업해야 한다. **OpenAI는 취약점을 인정하면서도 수정을 거부했다**(바운티 범위를 벗어나고 제품 기본 노출 표면에 해당하지 않는다는 이유). 따라서 미수정 상태로 남았고 사용 제한만이 유일한 완화책이다

summary_de: |
  Trend ZDI-26-305, CVSS 8.6, unzureichende Isolation der JS-Ausführungsumgebung. Erfordert, dass der Nutzer mit einem bösartigen Repository arbeitet. **OpenAI erkennt die Schwachstelle an, lehnt eine Behebung jedoch ab** (sie liege außerhalb des Bounty-Umfelds und gehöre nicht zur standardmäßigen Angriffsfläche des Produkts), sodass sie unbehoben blieb und nur die eingeschränkte Nutzung als Abhilfe bleibt

summary_fr: |
  Trend ZDI-26-305, CVSS 8.6, isolation incorrecte de l'environnement d'exécution JS. Nécessite que l'utilisateur travaille avec un dépôt malveillant. **OpenAI reconnaît la vulnérabilité mais a refusé de la corriger** (hors périmètre du bug bounty et hors de la surface d'exposition par défaut du produit, selon l'entreprise), elle est donc restée non corrigée, le seul atténuant étant un usage restreint

summary_es: |
  Trend ZDI-26-305, CVSS 8.6, aislamiento incorrecto del entorno de ejecución de JS. Requiere que el usuario trabaje con un repositorio malicioso. **OpenAI reconoce la vulnerabilidad pero se negó a corregirla** (dice que queda fuera del alcance del programa de recompensas y que no forma parte de la superficie de exposición por defecto del producto), así que ha quedado sin corregir, con el uso restringido como única mitigación

sources:
  - url: https://www.zerodayinitiative.com/advisories/ZDI-26-305/
    label: ZDI
  - url: https://forest.watch.impress.co.jp/docs/news/2105656.html
    label: Impress Watch

disputed: false
landmark: false
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# OpenAI Codex sandbox-escape zero-day

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## Summary

Trend ZDI-26-305, CVSS 8.6, improper isolation of the JS execution environment. Requires the user to work with a malicious repository. **OpenAI acknowledges the vulnerability but declined to fix it** (saying it is out of bounty scope and not part of the product's default exposure surface), so it has stayed unfixed, with restricted use the only mitigation

## Attack chain

```mermaid
flowchart LR
    E["Evaluation / container environment"]:::entry
    S0["Residual egress path"]:::step
    I["Escape to a real system<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | ZDI | <https://www.zerodayinitiative.com/advisories/ZDI-26-305/> |
| 2 | Impress Watch | <https://forest.watch.impress.co.jp/docs/news/2105656.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-04-28` (raw: 2026-04-28, precision `day`) |
| Kind | Research demo `research` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-04-28-codex-sha-xiang-rao-guo` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2026-04-15` [Windsurf zero-click MCP RCE (CVE-2026-30615)](2026-04-15-windsurf-mcp-rce.md)<br>  <sub>Windsurf zero-click MCP RCE (CVE-2026-30615)</sub>
- `2026-04-24` [Gemini CLI CVSS 10.0: one pull request compromises CI](2026-04-24-gemini-cli-pr-ci.md)<br>  <sub>Gemini CLI CVSS 10.0: one pull request compromises CI</sub>
- `2026-05-08` [Cline Kanban cross-origin WebSocket hijack (CVE-2026-44211)](../2026-05/2026-05-08-cline-kanban-websocket.md)<br>  <sub>Cline Kanban cross-origin WebSocket hijack (CVE-2026-44211)</sub>
- `2026-05-07` [TrustFall: RCE on a single keypress](../2026-05/2026-05-07-trustfall-rce-yi-ci-hui.md)<br>  <sub>TrustFall: RCE on a single keypress</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-28-codex-sha-xiang-rao-guo.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
