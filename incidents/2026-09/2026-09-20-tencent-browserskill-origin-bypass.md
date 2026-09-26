---
id: 2026-09-20-tencent-browserskill-origin-bypass
title: "Tencent BrowserSkill: any 32-character extension origin can pose as the browser client and feed the agent forged pages"
title_zh: "腾讯 BrowserSkill：任意 32 字符扩展来源都能冒充浏览器客户端，向 agent 投喂伪造页面"
title_ja: "Tencent BrowserSkill：32 文字の拡張オリジンならどれでもブラウザクライアントになりすまし、エージェントに偽ページを渡せる"
title_ko: "Tencent BrowserSkill: 32자 확장 오리진이면 무엇이든 브라우저 클라이언트로 위장해 에이전트에 조작된 페이지를 넘길 수 있다"
title_de: "Tencent BrowserSkill: Jede 32 Zeichen lange Extension-Origin kann sich als Browser-Client ausgeben und dem Agenten gefälschte Seiten liefern"
title_fr: "Tencent BrowserSkill : n'importe quelle origine d'extension de 32 caractères peut se faire passer pour le client navigateur et fournir à l'agent des pages falsifiées"
title_es: "Tencent BrowserSkill: cualquier origen de extensión de 32 caracteres puede hacerse pasar por el cliente del navegador y alimentar al agente con páginas falsificadas"
date: 2026-09-20
date_raw: "2026-09-20 (NVD, VulnCheck)"
date_precision: day

kind: vulnerability
type: [IPI, INFRA]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **CVE-2026-94111: Tencent BrowserSkill through 0.3.0 accepts any `chrome-extension` origin with 32 characters in the range a–p in its local daemon's WebSocket origin validation (CWE-346), so *"attackers can register a malicious extension as a browser client to intercept and manipulate page content, DOM, and screenshots returned to the AI agent."*** CVSS 4.0 **6.9** (`AV:L/AC:L/AT:N/PR:L/UI:N/VC:L/VI:H/VA:L`), credit George Chen, with the check located in `crates/bsk-cli/src/daemon/ws.rs`. The significance is the layer: this is not a page carrying an injected prompt but the **transport between the browser and the agent** — whoever speaks on that socket decides what the agent believes the page says. No exploitation in the wild is recorded. Recorded `vulnerability` / `IPI` + `INFRA` / `medium` / `real_harm: false`, following the archive's treatment of un-exploited agent-infrastructure CVEs

summary_zh: |
  **CVE-2026-94111：腾讯 BrowserSkill 0.3.0 及更早版本在本地守护进程的 WebSocket 来源校验中，接受任意长度为 32 字符、且字符落在 a–p 区间的 `chrome-extension` 来源（CWE-346），因此*「攻击者可以注册一个恶意扩展作为浏览器客户端，拦截并篡改返回给 AI agent 的页面内容、DOM 与截图。」*** CVSS 4.0 **6.9**（`AV:L/AC:L/AT:N/PR:L/UI:N/VC:L/VI:H/VA:L`），致谢 George Chen，问题代码位于 `crates/bsk-cli/src/daemon/ws.rs`。意义在于层级：这不是「页面里夹带注入提示」，而是**浏览器与 agent 之间的传输通道**——谁在这个 socket 上说话，就决定 agent 认为页面上写了什么。无在野利用记录。本条记为 `vulnerability` / `IPI` + `INFRA` / `medium` / `real_harm: false`，沿用档案对未在野 agent 基础设施 CVE 的处理口径

summary_ja: |
  **CVE-2026-94111：Tencent BrowserSkill 0.3.0 以前は、ローカルデーモンの WebSocket オリジン検証で 32 文字かつ a–p 範囲の `chrome-extension` オリジンを何でも受け入れる（CWE-346）。そのため*「攻撃者は悪意ある拡張をブラウザクライアントとして登録し、AIエージェントに返されるページ内容・DOM・スクリーンショットを傍受・改ざんできる。」*** CVSS 4.0 **6.9**（`AV:L/AC:L/AT:N/PR:L/UI:N/VC:L/VI:H/VA:L`）、報告者 George Chen、該当箇所は `crates/bsk-cli/src/daemon/ws.rs`。重要なのは階層である。これは「ページに仕込まれた注入プロンプト」ではなく、**ブラウザとエージェントの間の転送路**の問題——そのソケットで話す者が、エージェントがページに何と書いてあると信じるかを決める。実環境での悪用は記録されていない。`vulnerability` / `IPI` + `INFRA` / `medium` / `real_harm: false`

summary_ko: |
  **CVE-2026-94111: Tencent BrowserSkill 0.3.0 이하는 로컬 데몬의 WebSocket 오리진 검증에서 32자이며 a–p 범위의 `chrome-extension` 오리진을 모두 허용한다(CWE-346). 따라서 *"공격자는 악성 확장을 브라우저 클라이언트로 등록해 AI 에이전트에 반환되는 페이지 내용, DOM, 스크린샷을 가로채고 조작할 수 있다."*** CVSS 4.0 **6.9**(`AV:L/AC:L/AT:N/PR:L/UI:N/VC:L/VI:H/VA:L`), 제보자 George Chen, 취약 지점은 `crates/bsk-cli/src/daemon/ws.rs`. 중요한 것은 계층이다. 이것은 "페이지에 심긴 인젝션 프롬프트"가 아니라 **브라우저와 에이전트 사이의 전송 채널**의 문제다 — 그 소켓에서 말하는 자가 에이전트가 페이지에 무엇이 적혀 있다고 믿을지를 결정한다. 실제 악용은 기록되지 않았다. `vulnerability` / `IPI` + `INFRA` / `medium` / `real_harm: false`

summary_de: |
  **CVE-2026-94111: Tencent BrowserSkill bis 0.3.0 akzeptiert in der WebSocket-Origin-Prüfung des lokalen Daemons jede `chrome-extension`-Origin mit 32 Zeichen im Bereich a–p (CWE-346), sodass *„Angreifer eine bösartige Erweiterung als Browser-Client registrieren können, um Seiteninhalte, DOM und Screenshots abzufangen und zu manipulieren, die an den KI-Agenten zurückgegeben werden."*** CVSS 4.0 **6.9** (`AV:L/AC:L/AT:N/PR:L/UI:N/VC:L/VI:H/VA:L`), Credit: George Chen; die Prüfung liegt in `crates/bsk-cli/src/daemon/ws.rs`. Bedeutsam ist die Ebene: Es geht nicht um eine Seite mit eingeschleustem Prompt, sondern um den **Transportweg zwischen Browser und Agent** — wer auf diesem Socket spricht, bestimmt, was der Agent glaubt, dass auf der Seite steht. Keine Ausnutzung in freier Wildbahn bekannt. Verzeichnet als `vulnerability` / `IPI` + `INFRA` / `medium` / `real_harm: false`

summary_fr: |
  **CVE-2026-94111 : Tencent BrowserSkill jusqu'à 0.3.0 accepte, dans la validation d'origine WebSocket du démon local, n'importe quelle origine `chrome-extension` de 32 caractères comprise dans la plage a–p (CWE-346), si bien que *« des attaquants peuvent enregistrer une extension malveillante comme client navigateur afin d'intercepter et de manipuler le contenu de la page, le DOM et les captures d'écran renvoyés à l'agent IA. »*** CVSS 4.0 **6.9** (`AV:L/AC:L/AT:N/PR:L/UI:N/VC:L/VI:H/VA:L`), crédit George Chen, contrôle situé dans `crates/bsk-cli/src/daemon/ws.rs`. L'intérêt est la couche : il ne s'agit pas d'une page contenant un prompt injecté mais du **transport entre le navigateur et l'agent** — qui parle sur ce socket décide de ce que l'agent croit lire sur la page. Aucune exploitation constatée. Enregistré `vulnerability` / `IPI` + `INFRA` / `medium` / `real_harm: false`

summary_es: |
  **CVE-2026-94111: Tencent BrowserSkill hasta 0.3.0 acepta, en la validación de origen WebSocket del demonio local, cualquier origen `chrome-extension` de 32 caracteres en el rango a–p (CWE-346), de modo que *«los atacantes pueden registrar una extensión maliciosa como cliente del navegador para interceptar y manipular el contenido de la página, el DOM y las capturas de pantalla devueltas al agente de IA»*.** CVSS 4.0 **6.9** (`AV:L/AC:L/AT:N/PR:L/UI:N/VC:L/VI:H/VA:L`), crédito a George Chen, con la comprobación en `crates/bsk-cli/src/daemon/ws.rs`. Lo relevante es la capa: no es una página con un prompt inyectado, sino el **transporte entre el navegador y el agente** — quien hable en ese socket decide qué cree el agente que dice la página. No se registra explotación real. Registrado `vulnerability` / `IPI` + `INFRA` / `medium` / `real_harm: false`

sources:
  - url: https://nvd.nist.gov/vuln/detail/CVE-2026-94111
    label: NVD
  - url: https://www.vulncheck.com/advisories/tencent-browserskill-through-0.3.0-origin-validation-error-in-local-websocket-daemon
    label: VulnCheck
  - url: https://github.com/Tencent/BrowserSkill/issues/273
    label: Tencent BrowserSkill issue 273

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §13.20"
---

# Tencent BrowserSkill: any 32-character extension origin can pose as the browser client and feed the agent forged pages

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-8F6A3C?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-3C6E8F?style=flat-square)

## Summary

**CVE-2026-94111: Tencent BrowserSkill through 0.3.0 accepts any `chrome-extension` origin with 32 characters in the range a–p in its local daemon's WebSocket origin validation (CWE-346), so *"attackers can register a malicious extension as a browser client to intercept and manipulate page content, DOM, and screenshots returned to the AI agent."*** CVSS 4.0 **6.9** (`AV:L/AC:L/AT:N/PR:L/UI:N/VC:L/VI:H/VA:L`), credit George Chen, with the check located in `crates/bsk-cli/src/daemon/ws.rs`. The significance is the layer: this is not a page carrying an injected prompt but the **transport between the browser and the agent** — whoever speaks on that socket decides what the agent believes the page says. No exploitation in the wild is recorded. Recorded `vulnerability` / `IPI` + `INFRA` / `medium` / `real_harm: false`, following the archive's treatment of un-exploited agent-infrastructure CVEs.

## Attack chain

```mermaid
flowchart LR
    E["Malicious extension registers itself<br/>as a browser client (32-char a–p origin)"]:::entry
    S1["Daemon's WebSocket origin check accepts it"]:::step
    S2["Attacker intercepts and rewrites<br/>page content, DOM and screenshots"]:::step
    I["The agent acts on a forged view<br/>of the page"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The advisory.** VulnCheck's entry (dated 20 September 2026, severity *medium*, credit George Chen) carries the full text: *"Tencent BrowserSkill through 0.3.0 contains an authentication bypass vulnerability in the local daemon WebSocket origin validation that accepts any chrome-extension origin with 32 characters in range a-p. Attackers can register a malicious extension as a browser client to intercept and manipulate page content, DOM, and screenshots returned to the AI agent."* CVSS 4.0 base **6.9**, vector `AV:L/AC:L/AT:N/PR:L/UI:N/VC:L/VI:H/VA:L/SC:N/SI:N/SA:N`, weakness **CWE-346** (origin validation error). NVD mirrors it; the references point at GitHub issue 273 and `crates/bsk-cli/src/daemon/ws.rs#L36-L57`. The upstream issue, opened on **17 September 2026** and still open, supplies the context: the daemon is a WebSocket server on default port **52800** that gives *"any AI agent driving it"* full control of the user's real, already-logged-in browser — reading pages, taking screenshots, filling forms — and `origin_allowed()` checks the *shape* of the `Origin` header *"but never checks which extension it actually is"*. The reporter re-checked current `main` on **20 September 2026** and reported `origin_allowed()` unchanged, with the `TODO(M10/M12)` at `ws.rs:38-44` still present - the shape-only gate was still live nine days after the report. No exploitation in the wild is recorded.

**Why the layer matters.** Browser agents are judged by what they can *see*: a browser-agent stack turns page content, DOM and screenshots into the agent's only sensory input, and the local daemon is the pipe that carries it. When the pipe's origin check accepts a 32-character string in a fixed character range, an extension — one of the few things users install casually and in volume — becomes the agent's eyes. That is indirect prompt injection one level below the content: the attacker does not need to get text onto a page the agent reads, because they can replace the channel that delivers the page.

**Context and grading.** BrowserSkill is Tencent's open-source browser-agent CLI; the issue affects versions up to and including 0.3.0 and is tracked upstream as an open issue. Recorded `vulnerability` / `medium` / `real_harm: false` under the archive's ladder — a moderate, local, low-privilege flaw with no known exploitation (`high` would need CVSS 9+ or confirmed damage), dated to NVD publication (20 September 2026). Confidence **A**: the NVD record, an independent advisory, and the vendor repository's own issue.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | NVD — CVE-2026-94111 | <https://nvd.nist.gov/vuln/detail/CVE-2026-94111> |
| 2 | VulnCheck advisory | <https://www.vulncheck.com/advisories/tencent-browserskill-through-0.3.0-origin-validation-error-in-local-websocket-daemon> |
| 3 | Tencent BrowserSkill issue 273 | <https://github.com/Tencent/BrowserSkill/issues/273> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-20` (raw: NVD / VulnCheck 2026-09-20, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) [`INFRA`](../../taxonomy/types.md#infra) |
| Severity | **Medium** `medium` |
| Confidence | **A** — NVD, an independent advisory and the upstream issue |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-20-tencent-browserskill-origin-bypass` |

<sub>**Why this classification:** the exposed asset is the agent's local runtime plumbing (`INFRA`) and the effect is that external, attacker-controlled input reaches the agent as trusted observation (`IPI`) — without a poisoned page ever being involved. `real_harm: false` (no known exploitation) and `medium` per the severity ladder: CVSS 6.9, local, low privileges, no confirmed damage; `high` would require CVSS 9+ or confirmed harm. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure (INFRA)](../../topics/agent-infra.md)

**Related records:**

- `2026-09-16` [BragJack: one browser extension hijacks the AI agents in five major browsers](2026-09-16-bragjack-browser-agents.md)<br>  <sub>The other September case where an extension becomes the agent's input channel</sub>
- `2026-09-14` [Bifrost AI gateway: one unauthenticated MCP registration runs commands as the gateway user](2026-09-14-bifrost-ai-gateway-cve-2026-90898.md)<br>  <sub>Agent plumbing exposed without authentication</sub>
- `2026-09-23` [IBM FTM: unauthenticated RAG poisoning could steer the payment agent's MCP tools](2026-09-23-ibm-ftm-rag-poisoning.md)<br>  <sub>Injection reaching the agent through what it trusts, another route</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-20-tencent-browserskill-origin-bypass.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
