---
id: 2026-08-06-langflow-rce-cisa-kev
title: "Unauthenticated Langflow RCE added to CISA KEV"
title_zh: "Langflow 未认证 RCE 进 CISA KEV"
title_ja: "認証不要のLangflow RCEがCISA KEVに追加"
title_ko: "Langflow 무인증 RCE, CISA KEV에 등재"
title_de: "Nicht authentifizierte Langflow-RCE in die CISA KEV aufgenommen"
title_fr: "Le RCE non authentifié de Langflow ajouté au KEV de la CISA"
title_es: "El RCE sin autenticación de Langflow añadido al KEV de CISA"
date: 2026-08-06
date_precision: day
date_raw: "2026-08-06"

kind: incident
type: [INFRA]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  IBM: CVE-2026-9198, CVSS 9.8. `/api/v1/auto_login` issues a SUPERUSER token to any caller, and code sent to `/api/v1/validate/code` is run through `exec()`. **The validator evaluates decorators / default arguments / annotations at function-definition time, so "validation" itself amounts to arbitrary command execution**. Affects 1.0.0–1.10.0 in default configuration; fixed in 1.10.1


summary_zh: |
  IBM：CVE-2026-9198，CVSS 9.8。`/api/v1/auto_login` 向任意调用方签发 SUPERUSER token，拿它调 `/api/v1/validate/code` 的代码走 `exec()`。**校验器在函数定义时求值装饰器/默认参数/注解，于是「校验」本身就等于任意命令执行**。影响 1.0.0–1.10.0 默认配置，1.10.1 修复

summary_ja: |
  IBM：CVE-2026-9198、CVSS 9.8。`/api/v1/auto_login`が呼び出し元の誰にでもSUPERUSERトークンを発行し、`/api/v1/validate/code`に送られたコードは`exec()`で実行される。**バリデータは関数定義時にデコレーター／デフォルト引数／アノテーションを評価するため、「検証」自体が任意コマンド実行に等しい**。デフォルト構成の1.0.0〜1.10.0が影響を受け、1.10.1で修正

summary_ko: |
  IBM: CVE-2026-9198, CVSS 9.8. `/api/v1/auto_login`이 호출자 누구에게나 SUPERUSER 토큰을 발급하고, `/api/v1/validate/code`로 보낸 코드가 `exec()`로 실행된다. **검증기가 함수 정의 시점에 데코레이터 / 기본 인자 / 애너테이션을 평가하므로 "검증" 자체가 임의 명령 실행에 해당한다**. 기본 구성의 1.0.0~1.10.0이 영향받고 1.10.1에서 수정되었다

summary_de: |
  IBM: CVE-2026-9198, CVSS 9.8. `/api/v1/auto_login` gibt jedem Aufrufer ein SUPERUSER-Token aus, und Code, der an `/api/v1/validate/code` gesendet wird, läuft durch `exec()`. **Der Validator wertet Decorators / Standardargumente / Annotationen bereits zur Zeit der Funktionsdefinition aus, sodass die „Validierung“ selbst auf beliebige Befehlsausführung hinausläuft**. Betrifft 1.0.0–1.10.0 in der Standardkonfiguration; behoben in 1.10.1

summary_fr: |
  IBM : CVE-2026-9198, CVSS 9.8. `/api/v1/auto_login` délivre un jeton SUPERUSER à tout appelant, et le code envoyé à `/api/v1/validate/code` est exécuté via `exec()`. **Le validateur évalue les décorateurs / arguments par défaut / annotations au moment de la définition de la fonction, si bien que la « validation » équivaut elle-même à une exécution de commande arbitraire**. Affecte 1.0.0–1.10.0 en configuration par défaut ; corrigé en 1.10.1

summary_es: |
  IBM: CVE-2026-9198, CVSS 9.8. `/api/v1/auto_login` emite un token de SUPERUSER a cualquier llamador, y el código enviado a `/api/v1/validate/code` se ejecuta mediante `exec()`. **El validador evalúa decoradores / argumentos por defecto / anotaciones en el momento de definir la función, así que la propia "validación" equivale a ejecución arbitraria de comandos**. Afecta a 1.0.0–1.10.0 en configuración predeterminada; corregido en 1.10.1

sources:
  - url: https://www.ibm.com/support/pages/node/7278927
    label: IBM
  - url: https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-9198
    label: CISA KEV

disputed: false
landmark: true
scan_month: 2026-08
scan_ref: "SCAN.md §6 2026-08"
---

# Unauthenticated Langflow RCE added to CISA KEV

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

IBM: CVE-2026-9198, CVSS 9.8. `/api/v1/auto_login` issues a SUPERUSER token to any caller, and code sent to `/api/v1/validate/code` is run through `exec()`. **The validator evaluates decorators / default arguments / annotations at function-definition time, so "validation" itself amounts to arbitrary command execution**. Affects 1.0.0–1.10.0 in default configuration; fixed in 1.10.1

## Attack chain

```mermaid
flowchart LR
    E["Agent infrastructure exposed to the internet"]:::entry
    S0["Unauthenticated access"]:::step
    I["RCE / data leak"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | IBM | <https://www.ibm.com/support/pages/node/7278927> |
| 2 | CISA KEV | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-9198> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-08-06` (raw: 2026-08-06, precision `day`) |
| Kind | Incident `incident` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-08-06-langflow-rce-cisa-kev` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-08-25` [NemoClaw (CVE-2026-65105): DNS rebinding rewrites the model's chat template](2026-08-25-nemoclaw-dns-zhong-bang-ding.md)<br>  <sub>NemoClaw (CVE-2026-65105): DNS rebinding rewrites the model's chat template</sub>
- `2026-08-01` [Azure SRE Agent privilege escalation (CVE-2026-62830)](2026-08-01-azure-sre-agent.md)<br>  <sub>Azure SRE Agent privilege escalation (CVE-2026-62830)</sub>
- `2026-08-26` [GitLab Duo's Claude agent can run arbitrary commands in CI](2026-08-26-gitlab-duo-claude-agent.md)<br>  <sub>GitLab Duo's Claude agent can run arbitrary commands in CI</sub>
- `2026-09-02` [Langflow CVE-2026-0768: the 12th Langflow flaw exploited in the wild this year](../2026-09/2026-09-02-langflow-jin-di-ye-li.md)<br>  <sub>Langflow CVE-2026-0768: the 12th Langflow flaw exploited in the wild this year</sub>

---

[← 2026-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-08/2026-08-06-langflow-rce-cisa-kev.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
