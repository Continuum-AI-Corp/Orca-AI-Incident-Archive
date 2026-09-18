---
id: 2026-04-23-openclaw-claw-chain
title: "OpenClaw \"Claw Chain\": four chained flaws, 245,000 servers exposed"
title_zh: "OpenClaw「Claw Chain」四漏洞链，24.5 万台服务器暴露"
title_ja: "OpenClaw「Claw Chain」：4つの連鎖する欠陥、24万5,000台のサーバーが露出"
title_ko: "OpenClaw \"Claw Chain\": 결함 4건 연쇄, 서버 24만 5천 대 노출"
title_de: "OpenClaw „Claw Chain“: vier verkettete Schwachstellen, 245,000 Server exponiert"
title_fr: "OpenClaw « Claw Chain » : quatre failles enchaînées, 245 000 serveurs exposés"
title_es: "OpenClaw \"Claw Chain\": cuatro fallos encadenados y 245,000 servidores expuestos"
date: 2026-04-23
date_precision: day
date_raw: "2026-04-23"

kind: vulnerability
type: [INFRA]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  The **Cyera** research team disclosed four previously unpublished vulnerabilities to the maintainers in 2026-04 (all now fixed):
  **CVE-2026-44112** (CVSS 9.6) a **TOCTOU race condition** in the OpenShell sandbox that can redirect writes outside the sandbox, enabling configuration tampering and a persistent host backdoor
  **CVE-2026-44115** (8.8) a gap between command validation and shell execution, where **environment variables (API keys, tokens, credentials) can leak through an unquoted heredoc that looks harmless at validation time**
  **CVE-2026-44118** (7.8) blindly trusting the client-controlled `senderIsOwner` flag without checking the authenticated session, so a local process holding a valid bearer token can escalate to owner level
  Exposure: Shodan ~65,000 + ZoomEye ~180,000 ≈ **245,000 reachable with no internal-network precondition at all**. Financial, healthcare and legal sectors are at highest risk


summary_zh: |
  **Cyera** 研究团队 2026-04 向维护者披露四个此前未公开的漏洞（均已修复）：
  **CVE-2026-44112**（CVSS 9.6）OpenShell 沙箱的 **TOCTOU 竞争条件**，可把写操作重定向到沙箱外，实现配置篡改与宿主持久后门
  **CVE-2026-44115**（8.8）命令校验与 shell 执行之间的落差，**环境变量（API key、token、凭据）可经校验时看起来无害的未加引号 heredoc 泄露**
  **CVE-2026-44118**（7.8）盲信客户端可控的 `senderIsOwner` 标志而不比对已认证会话，持有有效 bearer token 的本地进程即可提权到 owner 级
  暴露面：Shodan 约 6.5 万 + ZoomEye 约 18 万 ≈ **24.5 万台无需任何内网前置条件即可触达**。金融、医疗、法律行业风险最高

summary_ja: |
  **Cyera**の研究チームが2026-04に4件の未公表脆弱性をメンテナーへ開示した（すべて修正済み）：
  **CVE-2026-44112**（CVSS 9.6）OpenShellサンドボックスの**TOCTOU競合状態**により、サンドボックス外への書き込みをリダイレクトでき、設定改ざんとホストへの永続的バックドアが可能になる
  **CVE-2026-44115**（8.8）コマンド検証とシェル実行の間のギャップ。**検証時には無害に見える引用符なしのheredocを通じて、環境変数（APIキー、トークン、認証情報）が漏えいし得る**
  **CVE-2026-44118**（7.8）クライアント制御の`senderIsOwner`フラグを、認証済みセッションを確認せずに盲信するため、有効なベアラートークンを持つローカルプロセスがオーナー権限に昇格できる
  露出：Shodan約65,000＋ZoomEye約180,000≒**245,000台が内部ネットワークの前提条件なしで到達可能**。金融、医療、法務セクターが最もリスクが高い

summary_ko: |
  **Cyera** 연구팀이 2026-04에 이전에 공개되지 않은 취약점 4건을 유지관리자에게 알렸다(모두 현재 수정됨):
  **CVE-2026-44112**(CVSS 9.6) OpenShell 샌드박스의 **TOCTOU 경쟁 조건**으로, 샌드박스 밖으로 쓰기를 돌려 설정 변조와 호스트 영구 백도어를 가능하게 한다
  **CVE-2026-44115**(8.8) 명령 검증과 셸 실행 사이의 틈으로, **검증 시점에는 무해해 보이는 따옴표 없는 heredoc을 통해 환경 변수(API 키, 토큰, 자격 증명)가 유출될 수 있다**
  **CVE-2026-44118**(7.8) 클라이언트가 제어하는 `senderIsOwner` 플래그를 인증된 세션 확인 없이 맹신해, 유효한 베어러 토큰을 가진 로컬 프로세스가 소유자 수준으로 권한을 상승시킬 수 있다
  노출 규모: Shodan 약 65,000 + ZoomEye 약 180,000 ≈ **내부망 전제 조건 없이 24만 5천 대 접근 가능**. 금융, 의료, 법률 부문이 가장 위험하다

summary_de: |
  Das Forschungsteam von **Cyera** meldete im 2026-04 vier bis dahin unveröffentlichte Schwachstellen an die Maintainer (alle inzwischen behoben):
  **CVE-2026-44112** (CVSS 9.6) eine **TOCTOU-Race-Condition** in der OpenShell-Sandbox, die Schreibvorgänge aus der Sandbox herauslenken kann, was Konfigurationsmanipulation und eine persistente Host-Backdoor ermöglicht
  **CVE-2026-44115** (8.8) eine Lücke zwischen Befehlsvalidierung und Shell-Ausführung, bei der **Umgebungsvariablen (API-Schlüssel, Token, Zugangsdaten) durch ein nicht in Anführungszeichen gesetztes Heredoc abfließen können, das zum Zeitpunkt der Validierung harmlos aussieht**
  **CVE-2026-44118** (7.8) blindes Vertrauen in das vom Client kontrollierte Flag `senderIsOwner` ohne Prüfung der authentifizierten Sitzung, sodass ein lokaler Prozess mit einem gültigen Bearer-Token auf Owner-Ebene eskalieren kann
  Exposition: Shodan ~65,000 + ZoomEye ~180,000 ≈ **245,000 erreichbar, ganz ohne Vorbedingung eines internen Netzwerks**. Die Sektoren Finanzen, Gesundheitswesen und Recht sind am stärksten gefährdet

summary_fr: |
  L'équipe de recherche **Cyera** a divulgué quatre vulnérabilités inédites aux mainteneurs en 2026-04 (toutes corrigées depuis) :
  **CVE-2026-44112** (CVSS 9.6) une **condition de course TOCTOU** dans le bac à sable OpenShell qui peut rediriger des écritures hors du bac à sable, permettant la falsification de configuration et une backdoor persistante sur l'hôte
  **CVE-2026-44115** (8.8) un écart entre la validation des commandes et l'exécution du shell, où **des variables d'environnement (clés API, jetons, identifiants) peuvent fuiter via un heredoc non mis entre guillemets qui paraît inoffensif au moment de la validation**
  **CVE-2026-44118** (7.8) la confiance aveugle dans le drapeau `senderIsOwner` contrôlé par le client, sans vérification de la session authentifiée, si bien qu'un processus local disposant d'un jeton bearer valide peut s'élever au niveau propriétaire
  Exposition : Shodan ~65 000 + ZoomEye ~180 000 ≈ **245 000 joignables sans aucune précondition de réseau interne**. Les secteurs financier, de la santé et juridique sont les plus à risque

summary_es: |
  El equipo de investigación de **Cyera** divulgó cuatro vulnerabilidades no publicadas antes a los mantenedores en 2026-04 (todas ya corregidas):
  **CVE-2026-44112** (CVSS 9.6) una **condición de carrera TOCTOU** en el sandbox de OpenShell que puede redirigir escrituras fuera del sandbox, permitiendo la manipulación de la configuración y una puerta trasera persistente en el host
  **CVE-2026-44115** (8.8) una brecha entre la validación de comandos y la ejecución del shell, donde **las variables de entorno (claves de API, tokens, credenciales) pueden filtrarse a través de un heredoc sin comillas que parece inofensivo en el momento de la validación**
  **CVE-2026-44118** (7.8) confiar ciegamente en la marca `senderIsOwner` controlada por el cliente sin comprobar la sesión autenticada, de modo que un proceso local con un bearer token válido puede escalar al nivel de propietario
  Exposición: Shodan ~65,000 + ZoomEye ~180,000 ≈ **245,000 alcanzables sin ninguna precondición de red interna**. Los sectores financiero, sanitario y legal son los de mayor riesgo

sources:
  - url: https://cybersecuritynews.com/openclaw-chain-vulnerabilities/
    label: CybersecurityNews
  - url: https://labs.cloudsecurityalliance.org/research/csa-research-note-openclaw-claw-chain-cve-20260517-csa-style/
    label: CSA

disputed: false
landmark: true
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# OpenClaw "Claw Chain": four chained flaws, 245,000 servers exposed

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

The **Cyera** research team disclosed four previously unpublished vulnerabilities to the maintainers in 2026-04 (all now fixed):

**CVE-2026-44112** (CVSS 9.6) a **TOCTOU race condition** in the OpenShell sandbox that can redirect writes outside the sandbox, enabling configuration tampering and a persistent host backdoor

**CVE-2026-44115** (8.8) a gap between command validation and shell execution, where **environment variables (API keys, tokens, credentials) can leak through an unquoted heredoc that looks harmless at validation time**

**CVE-2026-44118** (7.8) blindly trusting the client-controlled `senderIsOwner` flag without checking the authenticated session, so a local process holding a valid bearer token can escalate to owner level

Exposure: Shodan ~65,000 + ZoomEye ~180,000 ≈ **245,000 reachable with no internal-network precondition at all**. Financial, healthcare and legal sectors are at highest risk

## Attack chain

```mermaid
flowchart LR
    E["Agent infrastructure exposed to the internet"]:::entry
    S0["Unauthenticated access"]:::step
    I["RCE / data leak<br/><i>(flaw disclosed, no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | CybersecurityNews | <https://cybersecuritynews.com/openclaw-chain-vulnerabilities/> |
| 2 | CSA | <https://labs.cloudsecurityalliance.org/research/csa-research-note-openclaw-claw-chain-cve-20260517-csa-style/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-04-23` (raw: 2026-04-23, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-04-23-openclaw-claw-chain` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-04-16` [MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild](2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br>  <sub>MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild</sub>
- `2026-04-07` [Flowise CVE-2025-59528 exploited in the wild](2026-04-07-flowise-ye-li-yong.md)<br>  <sub>Flowise CVE-2025-59528 exploited in the wild</sub>
- `2026-04-01` [Google Vertex AI "Double Agent" permission abuse](2026-04-01-google-vertex-double-agent.md)<br>  <sub>Google Vertex AI "Double Agent" permission abuse</sub>
- `2026-04-06` [OpenClaw's CVE rate: 2.2 per day](2026-04-06-openclaw-chan-chu-su-lv.md)<br>  <sub>OpenClaw's CVE rate: 2.2 per day</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-23-openclaw-claw-chain.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
