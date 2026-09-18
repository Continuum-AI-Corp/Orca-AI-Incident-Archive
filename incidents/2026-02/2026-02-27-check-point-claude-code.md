---
id: 2026-02-27-check-point-claude-code
title: "Check Point publishes two Claude Code CVEs"
title_zh: "Check Point 公开 Claude Code 双 CVE"
title_ja: "Check PointがClaude Codeの2件のCVEを公表"
title_ko: "Check Point, Claude Code CVE 2건 공개"
title_de: "Check Point veröffentlicht zwei Claude-Code-CVEs"
title_fr: "Check Point publie deux CVE de Claude Code"
title_es: "Check Point publica dos CVE de Claude Code"
date: 2026-02-27
date_precision: day
date_raw: "2026-02-27"

kind: research
type: [SANDBOX, CRED]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  CVE-2025-59536 (a command can execute before the trust dialog appears) plus CVE-2026-21852 (`ANTHROPIC_BASE_URL` redirection steals the API key). **Anthropic fixed both before public disclosure**
  ⚠️ The v1 claim that "the attacker used Claude Code as a C2 for 18 days" could not be substantiated and appears to be a garbled version of this story; it was removed in v2


summary_zh: |
  CVE-2025-59536（启动信任对话框前即可执行命令）+ CVE-2026-21852（`ANTHROPIC_BASE_URL` 重定向窃 API key）。**Anthropic 在公开披露前已全部修复**
  ⚠️ v1 中「攻击者把 Claude Code 当 C2 用了 18 天」一条查无实据，疑为本条讹传，v2 已删除

summary_ja: |
  CVE-2025-59536（信頼ダイアログが表示される前にコマンドを実行できる）とCVE-2026-21852（`ANTHROPIC_BASE_URL`のリダイレクトでAPIキーを窃取）。**Anthropicは公開前に両方とも修正済み**。
  ⚠️ v1の「攻撃者がClaude Codeを18日間C2として使用した」という主張は裏付けが取れず、本件が歪められたものと思われるため、v2で削除された

summary_ko: |
  CVE-2025-59536(신뢰 대화상자가 뜨기 전에 명령이 실행될 수 있음)과 CVE-2026-21852(`ANTHROPIC_BASE_URL` 리다이렉션으로 API 키 탈취). **Anthropic은 공개 전에 둘 다 수정했다**
  ⚠️ v1의 "공격자가 18일 동안 Claude Code를 C2로 사용했다"는 주장은 입증되지 않았고 이 사건이 와전된 것으로 보이며, v2에서 삭제되었다

summary_de: |
  CVE-2025-59536 (ein Befehl kann ausgeführt werden, bevor der Vertrauensdialog erscheint) plus CVE-2026-21852 (die Umleitung von `ANTHROPIC_BASE_URL` stiehlt den API-Schlüssel). **Anthropic behob beide vor der öffentlichen Offenlegung**
  ⚠️ Die Behauptung aus v1, „der Angreifer nutzte Claude Code 18 Tage lang als C2“, ließ sich nicht belegen und scheint eine verzerrte Version dieser Geschichte zu sein; sie wurde in v2 entfernt

summary_fr: |
  CVE-2025-59536 (une commande peut s'exécuter avant l'apparition de la boîte de dialogue de confiance) plus CVE-2026-21852 (la redirection `ANTHROPIC_BASE_URL` vole la clé API). **Anthropic a corrigé les deux avant la divulgation publique**
  ⚠️ L'affirmation de la v1 selon laquelle « l'attaquant a utilisé Claude Code comme C2 pendant 18 jours » n'a pas pu être étayée et semble une version déformée de cette histoire ; elle a été retirée en v2

summary_es: |
  CVE-2025-59536 (un comando puede ejecutarse antes de que aparezca el diálogo de confianza) más CVE-2026-21852 (la redirección de `ANTHROPIC_BASE_URL` roba la clave de API). **Anthropic corrigió ambas antes de la divulgación pública**
  ⚠️ La afirmación de la v1 de que "el atacante usó Claude Code como C2 durante 18 días" no pudo sustanciarse y parece una versión distorsionada de esta historia; se eliminó en la v2

sources:
  - url: https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/
    label: Check Point
  - url: https://thehackernews.com/2026/02/claude-code-flaws-allow-remote-code.html
    label: THN

disputed: true
landmark: false
scan_month: 2026-02
scan_ref: "SCAN.md §6 2026-02"
---

# Check Point publishes two Claude Code CVEs

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

> [!WARNING]
> **This record contains disputed or not fully confirmed facts**; the claims of each party are kept side by side in the body, so do not cite any single one of them in isolation.

## Summary

CVE-2025-59536 (a command can execute before the trust dialog appears) plus CVE-2026-21852 (`ANTHROPIC_BASE_URL` redirection steals the API key). **Anthropic fixed both before public disclosure**

⚠️ The v1 claim that "the attacker used Claude Code as a C2 for 18 days" could not be substantiated and appears to be a garbled version of this story; it was removed in v2

## Attack chain

```mermaid
flowchart LR
    E["Evaluation / container environment"]:::entry
    S0["A leftover egress path"]:::step
    S1["agent retrieves and uses them"]:::step
    I["Credential abuse<br/><i>(lab demo · no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Check Point | <https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/> |
| 2 | THN | <https://thehackernews.com/2026/02/claude-code-flaws-allow-remote-code.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-02-27` (raw: 2026-02-27, precision `day`) |
| Kind | Research demo `research` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-02-27-check-point-claude-code` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2026-02-01` [Infostealers start harvesting OpenClaw configs and gateway tokens](2026-02-01-openclaw-xin-xi-qie-qu.md)<br>  <sub>Infostealers start harvesting OpenClaw configs and gateway tokens</sub>
- `2026-01-31` [Moltbook database fully open](../2026-01/2026-01-31-moltbook-open-database.md)<br>  <sub>Moltbook database fully open</sub>
- `2026-03-01` [Hades: a sustained campaign turning AI coding assistants into the attack surface](../2026-03/2026-03-01-hades-campaign-ai-coding-assistants.md)<br>  <sub>Hades: a sustained campaign turning AI coding assistants into the attack surface</sub>
- `2026-03-24` [Backdoored LiteLLM release](../2026-03/2026-03-24-litellm-backdoored-release.md)<br>  <sub>Backdoored LiteLLM release</sub>

---

[← 2026-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-02/2026-02-27-check-point-claude-code.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
