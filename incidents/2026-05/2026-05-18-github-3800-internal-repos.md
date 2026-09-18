---
id: 2026-05-18-github-3800-internal-repos
title: "3,800 internal GitHub repositories compromised"
title_zh: "GitHub 内部 3,800 个仓库被攻陷"
title_ja: "GitHubの社内リポジトリ3,800件が侵害"
title_ko: "GitHub 내부 저장소 3,800개 침해"
title_de: "3,800 interne GitHub-Repositories kompromittiert"
title_fr: "3 800 dépôts GitHub internes compromis"
title_es: "3,800 repositorios internos de GitHub comprometidos"
date: 2026-05-18
date_precision: day
date_raw: "2026-05-18"

kind: incident
type: [SUPPLY, CRED]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  The starting point was a malicious version of the VS Code extension **Nx Console v18.95.0** — **exposed for only 18 minutes**, yet it infected GitHub employee workstations. The attacker (TeamPCP / UNC6780) exfiltrated internal source code and data. GitHub rotated secrets and the **GitHub Enterprise Server signing key**, and told enterprise customers to update manually


summary_zh: |
  起点是 VS Code 扩展 **Nx Console v18.95.0** 的恶意版本 —— **仅暴露 18 分钟**，就感染了 GitHub 员工工作站。攻击者（TeamPCP / UNC6780）外带内部源码与数据。GitHub 轮换机密与 **GitHub Enterprise Server 签名密钥**，要求企业客户手动更新

summary_ja: |
  起点はVS Code拡張機能**Nx Console v18.95.0**の悪性バージョン——**公開されていたのはわずか18分間**だったが、GitHub従業員のワークステーションに感染した。攻撃者（TeamPCP／UNC6780）は内部ソースコードとデータを持ち出した。GitHubはシークレットと**GitHub Enterprise Serverの署名鍵**をローテーションし、エンタープライズ顧客には手動での更新を求めた

summary_ko: |
  출발점은 VS Code 확장 프로그램 **Nx Console v18.95.0**의 악성 버전이었다 — **노출된 시간은 18분에 불과했지만** GitHub 직원 워크스테이션을 감염시켰다. 공격자(TeamPCP / UNC6780)는 내부 소스 코드와 데이터를 유출했다. GitHub은 시크릿과 **GitHub Enterprise Server 서명 키**를 교체하고 기업 고객에게 수동 업데이트를 안내했다

summary_de: |
  Ausgangspunkt war eine bösartige Version der VS-Code-Erweiterung **Nx Console v18.95.0** — **nur 18 Minuten lang exponiert**, infizierte aber Arbeitsrechner von GitHub-Mitarbeitern. Der Angreifer (TeamPCP / UNC6780) exfiltrierte internen Quellcode und Daten. GitHub rotierte Secrets und den **Signaturschlüssel von GitHub Enterprise Server** und forderte Unternehmenskunden auf, manuell zu aktualisieren

summary_fr: |
  Le point de départ était une version malveillante de l'extension VS Code **Nx Console v18.95.0** — **exposée seulement 18 minutes**, elle a pourtant infecté les postes de travail d'employés GitHub. L'attaquant (TeamPCP / UNC6780) a exfiltré du code source interne et des données. GitHub a renouvelé les secrets et la **clé de signature de GitHub Enterprise Server**, et a demandé aux clients entreprise de mettre à jour manuellement

summary_es: |
  El punto de partida fue una versión maliciosa de la extensión de VS Code **Nx Console v18.95.0** — **expuesta solo durante 18 minutos**, y aun así infectó estaciones de trabajo de empleados de GitHub. El atacante (TeamPCP / UNC6780) exfiltró código fuente interno y datos. GitHub rotó secretos y la **clave de firma de GitHub Enterprise Server**, y dijo a los clientes empresariales que actualizaran manualmente

sources:
  - url: https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w
    label: "nx-console advisory"
  - url: https://github.blog/security/investigating-unauthorized-access-to-githubs-internal-repositories/
    label: GitHub Blog
  - url: https://www.securityweek.com/github-confirms-hack-impacting-3800-internal-repositories/
    label: SecurityWeek

disputed: false
landmark: true
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# 3,800 internal GitHub repositories compromised

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

The starting point was a malicious version of the VS Code extension **Nx Console v18.95.0** — **exposed for only 18 minutes**, yet it infected GitHub employee workstations. The attacker (TeamPCP / UNC6780) exfiltrated internal source code and data. GitHub rotated secrets and the **GitHub Enterprise Server signing key**, and told enterprise customers to update manually

## Attack chain

```mermaid
flowchart LR
    E["Poisoned package / repository / agent config"]:::entry
    S0["Developer or agent installs it automatically"]:::step
    S1["The agent picks them up and calls out"]:::step
    I["Credentials are abused"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | nx-console advisory | <https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w> |
| 2 | GitHub Blog | <https://github.blog/security/investigating-unauthorized-access-to-githubs-internal-repositories/> |
| 3 | SecurityWeek | <https://www.securityweek.com/github-confirms-hack-impacting-3800-internal-repositories/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-18` (raw: 2026-05-18, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-18-github-3800-internal-repos` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-05-19` [TrapDoor: poisoning three ecosystems to corrupt AI assistant configs](2026-05-19-trapdoor-poisons-agent-configs.md)<br>  <sub>TrapDoor: poisoning three ecosystems to corrupt AI assistant configs</sub>
- `2026-05-21` [Composio: agent automation itself becomes the privilege-escalation path](2026-05-21-composio-agent-automation-privesc.md)<br>  <sub>Composio: agent automation itself becomes the privilege-escalation path</sub>
- `2026-05-11` [TanStack npm "Mini Shai-Hulud"](2026-05-11-tanstack-npm-mini-shai.md)<br>  <sub>TanStack npm "Mini Shai-Hulud"</sub>
- `2026-05-04` [Braintrust's AWS account compromised, all customers told to rotate AI keys](2026-05-04-braintrust-aws-zhang-hao-gong.md)<br>  <sub>Braintrust's AWS account compromised, all customers told to rotate AI keys</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-18-github-3800-internal-repos.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
