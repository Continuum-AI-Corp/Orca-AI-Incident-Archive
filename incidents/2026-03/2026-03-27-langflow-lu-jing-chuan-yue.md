---
id: 2026-03-27-langflow-lu-jing-chuan-yue
title: "Langflow path traversal enables arbitrary file write"
title_zh: "Langflow 路径穿越任意文件写"
title_ja: "Langflowのパストラバーサルにより任意ファイル書き込みが可能に"
title_ko: "Langflow 경로 순회로 임의 파일 쓰기"
title_de: "Langflow: Path Traversal ermöglicht beliebiges Dateischreiben"
title_fr: "Une traversée de répertoires dans Langflow permet l'écriture de fichiers arbitraires"
title_es: "El path traversal de Langflow permite escritura arbitraria de archivos"
date: 2026-03-27
date_precision: day
date_raw: "2026-03-27"

kind: vulnerability
type: [INFRA]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Tenable: CVE-2026-5027 (CWE-22), `POST /api/v2/files` does not validate the filename. VulnCheck notes this can lead to RCE, and Langflow **ships with unauthenticated auto-login enabled by default**, with about **7,000** publicly reachable instances and in-the-wild exploitation attempts already observed. Fixed in v1.9.0


summary_zh: |
  Tenable：CVE-2026-5027（CWE-22），`POST /api/v2/files` 不校验 filename。VulnCheck 指出可导致 RCE，且 Langflow **默认开启未认证自动登录**，公网可达实例约 **7,000 个**，已观测到在野利用尝试。v1.9.0 修复

summary_ja: |
  Tenable：CVE-2026-5027（CWE-22）、`POST /api/v2/files`がファイル名を検証しない。VulnCheckはこれがRCEにつながり得ると指摘し、Langflowは**デフォルトで認証不要の自動ログインが有効**で、公開到達可能なインスタンスは約**7,000**、実悪用の試行もすでに観測されている。v1.9.0で修正

summary_ko: |
  Tenable: CVE-2026-5027(CWE-22), `POST /api/v2/files`가 파일명을 검증하지 않는다. VulnCheck는 이것이 RCE로 이어질 수 있다고 지적했고, Langflow는 **무인증 자동 로그인이 기본 활성화된 상태로 배포**되며 공개 접근 가능한 인스턴스가 약 **7,000개**, 실제 악용 시도도 이미 관찰되었다. v1.9.0에서 수정

summary_de: |
  Tenable: CVE-2026-5027 (CWE-22), `POST /api/v2/files` validiert den Dateinamen nicht. VulnCheck merkt an, dass dies zu RCE führen kann, und Langflow **wird mit standardmäßig aktiviertem, nicht authentifiziertem Auto-Login ausgeliefert**, mit etwa **7,000** öffentlich erreichbaren Instanzen und bereits beobachteten Ausnutzungsversuchen in freier Wildbahn. Behoben in v1.9.0

summary_fr: |
  Tenable : CVE-2026-5027 (CWE-22), `POST /api/v2/files` ne valide pas le nom de fichier. VulnCheck note que cela peut mener à un RCE, et Langflow **active par défaut une connexion automatique non authentifiée**, avec environ **7 000** instances publiquement joignables et des tentatives d'exploitation déjà observées en conditions réelles. Corrigé en v1.9.0

summary_es: |
  Tenable: CVE-2026-5027 (CWE-22), `POST /api/v2/files` no valida el nombre del archivo. VulnCheck señala que esto puede llevar a RCE, y Langflow **viene con el inicio de sesión automático sin autenticación habilitado por defecto**, con unas **7,000** instancias alcanzables públicamente y ya se han observado intentos de explotación en entornos reales. Corregido en la v1.9.0

sources:
  - url: https://www.tenable.com/security/research/tra-2026-26
    label: Tenable
  - url: https://www.securityweek.com/hackers-exploit-langflow-vulnerability-for-remote-code-execution/
    label: SecurityWeek

disputed: false
landmark: false
scan_month: 2026-03
scan_ref: "SCAN.md §6 2026-03"
---

# Langflow path traversal enables arbitrary file write

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

Tenable: CVE-2026-5027 (CWE-22), `POST /api/v2/files` does not validate the filename. VulnCheck notes this can lead to RCE, and Langflow **ships with unauthenticated auto-login enabled by default**, with about **7,000** publicly reachable instances and in-the-wild exploitation attempts already observed. Fixed in v1.9.0

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
| 1 | Tenable | <https://www.tenable.com/security/research/tra-2026-26> |
| 2 | SecurityWeek | <https://www.securityweek.com/hackers-exploit-langflow-vulnerability-for-remote-code-execution/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-03-27` (raw: 2026-03-27, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-03-27-langflow-lu-jing-chuan-yue` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-03-09` [McKinsey Lilli incident goes public](2026-03-09-lilli-mai-ken-xi-shi.md)<br>  <sub>McKinsey Lilli incident goes public</sub>
- `2026-02-28` [CodeWall breaches McKinsey's internal "Lilli" AI platform](../2026-02/2026-02-28-codewall-breaches-mckinsey-lilli.md)<br>  <sub>CodeWall breaches McKinsey's internal "Lilli" AI platform</sub>
- `2026-04-16` [MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild](../2026-04/2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br>  <sub>MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild</sub>
- `2026-02-10` [15,200 OpenClaw control panels exposed](../2026-02/2026-02-10-openclaw-kong-zhi-mian-ban.md)<br>  <sub>15,200 OpenClaw control panels exposed</sub>

---

[← 2026-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-03/2026-03-27-langflow-lu-jing-chuan-yue.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
