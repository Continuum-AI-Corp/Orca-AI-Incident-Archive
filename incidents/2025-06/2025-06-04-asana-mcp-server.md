---
id: 2025-06-04-asana-mcp-server
title: "Asana MCP server cross-tenant data exposure"
title_zh: "Asana MCP server 跨租户数据暴露"
title_ja: "Asana MCPサーバーのテナント間データ露出"
title_ko: "Asana MCP 서버 교차 테넌트 데이터 노출"
title_de: "Asana MCP-Server: mandantenübergreifende Datenexposition"
title_fr: "Exposition de données entre locataires sur le serveur MCP d'Asana"
title_es: "Exposición de datos entre inquilinos en el servidor MCP de Asana"
date: 2025-06-04
date_precision: day
date_raw: "2025-06-04"

kind: vulnerability
type: [MCP]
severity: medium
confidence: B
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  The feature went live on 2025-05-01; an access-control flaw was **found on 06-04**, exposing around **1,000 customers'** tasks, project metadata, comments and files to other tenants (subject to their respective permissions); **access restored on 06-17**


summary_zh: |
  功能 2025-05-01 上线，**06-04 发现**访问控制缺陷，约 **1,000 家客户**的任务、项目元数据、评论、文件可被其他租户看到（受各自权限约束），**06-17 恢复访问**

summary_ja: |
  機能は2025-05-01に公開。アクセス制御の欠陥が**06-04に発見**され、約**1,000社の顧客**のタスク、プロジェクトメタデータ、コメント、ファイルが他テナントに露出した（各権限の範囲内）。**06-17にアクセスが復旧**

summary_ko: |
  이 기능은 2025-05-01에 출시되었고, **06-04에 접근 제어 결함이 발견**되어 약 **1,000개 고객**의 작업, 프로젝트 메타데이터, 댓글, 파일이 다른 테넌트에 노출되었다(각자의 권한 범위 안에서). **06-17에 접근이 복구되었다**

summary_de: |
  Die Funktion ging am 2025-05-01 live; ein Zugriffskontrollfehler wurde **am 06-04 gefunden**, wodurch etwa **1,000 Kunden** Aufgaben, Projektmetadaten, Kommentare und Dateien für andere Mandanten sichtbar wurden (im Rahmen ihrer jeweiligen Berechtigungen); **Zugang am 06-17 wiederhergestellt**

summary_fr: |
  La fonctionnalité a été mise en service le 2025-05-01 ; une faille de contrôle d'accès a été **découverte le 06-04**, exposant les tâches, métadonnées de projet, commentaires et fichiers d'environ **1 000 clients** à d'autres locataires (selon leurs permissions respectives) ; **accès rétabli le 06-17**

summary_es: |
  La función se activó el 2025-05-01; un fallo de control de acceso se **descubrió el 06-04**, exponiendo las tareas, metadatos de proyectos, comentarios y archivos de alrededor de **1,000 clientes** a otros inquilinos (sujeto a sus respectivos permisos); **acceso restaurado el 06-17**

sources:
  - url: https://www.practical-devsecops.com/mcp-security-statistics-2026-report/
    label: Practical DevSecOps roundup

disputed: true
landmark: false
scan_month: 2025-06
scan_ref: "SCAN.md §5 2025-06"
---

# Asana MCP server cross-tenant data exposure

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square)

> [!WARNING]
> **This record contains disputed or not fully confirmed facts**; the claims of each party are kept side by side in the body, so do not cite any single one of them in isolation.

## Summary

The feature went live on 2025-05-01; an access-control flaw was **found on 06-04**, exposing around **1,000 customers'** tasks, project metadata, comments and files to other tenants (subject to their respective permissions); **access restored on 06-17**

## Attack chain

```mermaid
flowchart LR
    E["Malicious MCP server or tool description"]:::entry
    S0["The agent toolchain loads and trusts it"]:::step
    I["Unauthorized tool calls"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Practical DevSecOps roundup | <https://www.practical-devsecops.com/mcp-security-statistics-2026-report/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-06-04` (raw: 2025-06-04, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain |
| Severity | **Medium** `medium` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-06-04-asana-mcp-server` |

<sub>**Why this classification:** Vulnerability disclosure with confirmed in-the-wild exploitation, so `real_harm: true`. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-06-13` [MCP Inspector unauthenticated RCE](2025-06-13-mcp-inspector-rce.md)<br>  <sub>MCP Inspector unauthenticated RCE</sub>
- `2025-06-13` [Smithery.ai path traversal](2025-06-13-smithery-ai-lu-jing-chuan-yue.md)<br>  <sub>Smithery.ai path traversal</sub>
- `2025-07-06` [Supabase MCP prompt injection dumps a private table](../2025-07/2025-07-06-supabase-mcp-ti-shi-zhu.md)<br>  <sub>Supabase MCP prompt injection dumps a private table</sub>
- `2025-05-26` [GitHub MCP "toxic agent flow"](../2025-05/2025-05-26-github-mcp-toxic-agent.md)<br>  <sub>GitHub MCP "toxic agent flow"</sub>

---

[← 2025-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-06/2025-06-04-asana-mcp-server.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
