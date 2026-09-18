---
id: 2026-09-02-langflow-jin-di-ye-li
title: "Langflow CVE-2026-0768: the 12th Langflow flaw exploited in the wild this year"
title_zh: "Langflow CVE-2026-0768：今年第 12 个被在野利用的 Langflow 漏洞"
title_ja: "Langflow CVE-2026-0768：今年実悪用された12件目のLangflow欠陥"
title_ko: "Langflow CVE-2026-0768: 올해 실제 악용된 12번째 Langflow 결함"
title_de: "Langflow CVE-2026-0768: die 12. in diesem Jahr in freier Wildbahn ausgenutzte Langflow-Schwachstelle"
title_fr: "Langflow CVE-2026-0768 : la 12e faille de Langflow exploitée en conditions réelles cette année"
title_es: "Langflow CVE-2026-0768: el 12.º fallo de Langflow explotado en entornos reales este año"
date: 2026-09-02
date_precision: day
date_raw: "2026-09-02"

kind: incident
type: [INFRA, CRED]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Unauthenticated RCE, **executed with root privileges**, in the custom-component editor — the `validate` endpoint executes user-supplied Python from the `code` parameter without validation. A VulnCheck honeypot in the UK recorded **360 exploitation attempts, with traffic mainly from Russia**. The attackers looked specifically for environment variables: Langflow superuser credentials, AWS keys, **OpenAI API keys**, and also queried `/root/.cache/langflow/secret_key` and inspected `.ssh` and `.bash_history`.
  💡 **This statistic deserves its own note**: this is the **12th Langflow flaw exploited in the wild in 2026**; and **before 2026 the platform had only a single known exploited flaw in its entire history**. Exploitation attempts against its CVE portfolio **already exceed 15,000 across 2026**


summary_zh: |
  未认证 RCE，**以 root 权限执行**，位于自定义组件编辑器 —— `validate` 端点对用户提供的 `code` 参数未做校验即执行 Python。VulnCheck 的英国蜜罐记录到 **360 次利用尝试，流量主要来自俄罗斯**。攻击者专门找环境变量：Langflow 超级用户凭据、AWS 密钥、**OpenAI API key**，并查询 `/root/.cache/langflow/secret_key`、检查 `.ssh` 与 `.bash_history`。
  💡 **这条统计值得单独记**：这是 Langflow **2026 年第 12 个被在野利用的漏洞**；而**在 2026 年之前，该平台历史上只有整整 1 个已知被利用的缺陷**。2026 全年针对其 CVE 组合的利用尝试**已超过 15,000 次**

summary_ja: |
  カスタムコンポーネントエディターにおける認証不要のRCEで、**root権限で実行される**——`validate`エンドポイントが`code`パラメータのユーザー提供Pythonを検証なしに実行する。英国のVulnCheckハニーポットは**360件の悪用試行を記録し、トラフィックは主にロシア発**だった。攻撃者は環境変数を特に探していた：Langflowのスーパーユーザー認証情報、AWSキー、**OpenAI APIキー**。さらに`/root/.cache/langflow/secret_key`を照会し、`.ssh`と`.bash_history`も確認していた。
  💡 **この統計は特筆に値する**：これは**2026年に実悪用された12件目のLangflow欠陥**であり、**2026年以前、このプラットフォームには歴史上ただ1件の既知の悪用された欠陥しかなかった**。そのCVEポートフォリオに対する悪用試行は、**2026年だけですでに15,000件を超えている**

summary_ko: |
  커스텀 컴포넌트 편집기의 무인증 RCE로, **root 권한으로 실행된다** — `validate` 엔드포인트가 `code` 매개변수의 사용자 제공 Python을 검증 없이 실행한다. 영국의 VulnCheck 허니팟은 **360건의 악용 시도**를 기록했고 트래픽은 주로 러시아에서 왔다. 공격자들은 환경 변수, 특히 Langflow 슈퍼유저 자격 증명, AWS 키, **OpenAI API 키**를 집중적으로 찾았고 `/root/.cache/langflow/secret_key`를 조회하며 `.ssh`와 `.bash_history`도 살폈다.
  💡 **이 통계는 따로 짚을 가치가 있다**: 이것은 **2026년에 실제 악용된 12번째 Langflow 결함**이며, **2026년 이전에는 이 플랫폼의 전체 역사에서 알려진 악용 결함이 단 하나뿐이었다**. 2026년 한 해 동안 그 CVE 포트폴리오에 대한 악용 시도는 **이미 15,000건을 넘었다**

summary_de: |
  Nicht authentifizierte RCE, **mit root-Rechten ausgeführt**, im Editor für benutzerdefinierte Komponenten — der `validate`-Endpunkt führt vom Nutzer gelieferten Python-Code aus dem `code`-Parameter ohne Validierung aus. Ein VulnCheck-Honeypot im Vereinigten Königreich verzeichnete **360 Ausnutzungsversuche, der Verkehr kam überwiegend aus Russland**. Die Angreifer suchten gezielt nach Umgebungsvariablen: Langflow-Superuser-Zugangsdaten, AWS-Schlüssel, **OpenAI-API-Schlüssel**, und fragten zudem `/root/.cache/langflow/secret_key` ab und sahen `.ssh` und `.bash_history` durch.
  💡 **Diese Statistik verdient eine eigene Anmerkung**: Dies ist die **12. Langflow-Schwachstelle, die 2026 in freier Wildbahn ausgenutzt wurde**; und **vor 2026 hatte die Plattform in ihrer gesamten Geschichte nur eine einzige bekannt ausgenutzte Schwachstelle**. Die Ausnutzungsversuche gegen ihr CVE-Portfolio **übersteigen im Jahr 2026 bereits 15,000**

summary_fr: |
  RCE non authentifiée, **exécutée avec les privilèges root**, dans l'éditeur de composants personnalisés — le point de terminaison `validate` exécute du Python fourni par l'utilisateur depuis le paramètre `code` sans validation. Un honeypot VulnCheck au Royaume-Uni a enregistré **360 tentatives d'exploitation, le trafic venant principalement de Russie**. Les attaquants cherchaient spécifiquement des variables d'environnement : identifiants superuser de Langflow, clés AWS, **clés API OpenAI**, et interrogeaient aussi `/root/.cache/langflow/secret_key` et inspectaient `.ssh` et `.bash_history`.
  💡 **Cette statistique mérite une note à part** : c'est la **12e faille de Langflow exploitée en conditions réelles en 2026** ; et **avant 2026, la plateforme n'avait qu'une seule faille exploitée connue dans toute son histoire**. Les tentatives d'exploitation contre son portefeuille de CVE **dépassent déjà 15 000 sur l'année 2026**

summary_es: |
  RCE sin autenticación, **ejecutado con privilegios de root**, en el editor de componentes personalizados — el endpoint `validate` ejecuta el Python proporcionado por el usuario desde el parámetro `code` sin validación. Un honeypot de VulnCheck en el Reino Unido registró **360 intentos de explotación, con tráfico principalmente desde Rusia**. Los atacantes buscaban específicamente variables de entorno: credenciales de superusuario de Langflow, claves de AWS, **claves de API de OpenAI**, y también consultaron `/root/.cache/langflow/secret_key` e inspeccionaron `.ssh` y `.bash_history`.
  💡 **Esta estadística merece una nota propia**: este es el **12.º fallo de Langflow explotado en entornos reales en 2026**; y **antes de 2026 la plataforma solo tenía un único fallo explotado conocido en toda su historia**. Los intentos de explotación contra su portafolio de CVE **ya superan los 15,000 a lo largo de 2026**

sources:
  - url: https://www.bleepingcomputer.com/news/security/critical-langflow-flaw-exploited-to-steal-openai-and-aws-keys/
    label: BleepingComputer
  - url: https://securityaffairs.com/198270/hacking/hackers-target-langflow-in-cve-2026-0768-attacks/
    label: Security Affairs
  - url: https://labs.cloudsecurityalliance.org/research/csa-research-note-langflow-ai-framework-credential-harvestin/
    label: CSA

disputed: false
landmark: true
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# Langflow CVE-2026-0768: the 12th Langflow flaw exploited in the wild this year

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

Unauthenticated RCE, **executed with root privileges**, in the custom-component editor — the `validate` endpoint executes user-supplied Python from the `code` parameter without validation. A VulnCheck honeypot in the UK recorded **360 exploitation attempts, with traffic mainly from Russia**. The attackers looked specifically for environment variables: Langflow superuser credentials, AWS keys, **OpenAI API keys**, and also queried `/root/.cache/langflow/secret_key` and inspected `.ssh` and `.bash_history`.

💡 **This statistic deserves its own note**: this is the **12th Langflow flaw exploited in the wild in 2026**; and **before 2026 the platform had only a single known exploited flaw in its entire history**. Exploitation attempts against its CVE portfolio **already exceed 15,000 across 2026**

## Attack chain

```mermaid
flowchart LR
    E["Agent infrastructure exposed to the internet"]:::entry
    S0["Unauthenticated access"]:::step
    S1["The agent picks them up and calls out"]:::step
    I["Credential abuse"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/critical-langflow-flaw-exploited-to-steal-openai-and-aws-keys/> |
| 2 | Security Affairs | <https://securityaffairs.com/198270/hacking/hackers-target-langflow-in-cve-2026-0768-attacks/> |
| 3 | CSA | <https://labs.cloudsecurityalliance.org/research/csa-research-note-langflow-ai-framework-credential-harvestin/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-02` (raw: 2026-09-02, precision `day`) |
| Kind | Incident `incident` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-02-langflow-jin-di-ye-li` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-08-04` [CHAINDROP npm worm](../2026-08/2026-08-04-chaindrop-npm-ru-chong.md)<br>  <sub>CHAINDROP npm worm</sub>
- `2026-08-06` [Unauthenticated Langflow RCE added to CISA KEV](../2026-08/2026-08-06-langflow-rce-cisa-kev.md)<br>  <sub>Unauthenticated Langflow RCE added to CISA KEV</sub>
- `2026-08-25` [NemoClaw (CVE-2026-65105): DNS rebinding rewrites the model's chat template](../2026-08/2026-08-25-nemoclaw-dns-zhong-bang-ding.md)<br>  <sub>NemoClaw (CVE-2026-65105): DNS rebinding rewrites the model's chat template</sub>
- `2026-08-01` [Azure SRE Agent privilege escalation (CVE-2026-62830)](../2026-08/2026-08-01-azure-sre-agent.md)<br>  <sub>Azure SRE Agent privilege escalation (CVE-2026-62830)</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-02-langflow-jin-di-ye-li.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
