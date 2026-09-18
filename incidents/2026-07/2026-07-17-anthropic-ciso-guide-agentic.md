---
id: 2026-07-17-anthropic-ciso-guide-agentic
title: "Anthropic, \"A CISO's guide to agentic AI\""
title_zh: "Anthropic《a CISO's guide to agentic AI》"
title_ja: "Anthropic「A CISO's guide to agentic AI」"
title_ko: "Anthropic, \"A CISO's guide to agentic AI\""
title_de: "Anthropic: „A CISO's guide to agentic AI“"
title_fr: "Anthropic : « A CISO's guide to agentic AI »"
title_es: "Anthropic, \"A CISO's guide to agentic AI\""
date: 2026-07-17
date_precision: day
date_raw: "2026-07-17"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Deputy CISO Jason Clinton. Core argument: **once an agent goes off intent, it is indistinguishable from an insider**. Cites Ponemon 2026: containing an insider threat takes **67 days** on average, so day-level response is too slow. The strongest control is an **egress-proxy allowlist that cannot be reconfigured or bypassed**; others: issue and revoke identities through the existing IdP, scope privileges by **action** rather than by connector, feed tool calls into the SIEM via OpenTelemetry, and keep valuable credentials out of the execution environment


summary_zh: |
  Deputy CISO Jason Clinton。核心论点：**agent 一旦偏离意图，就与内部作案无法区分**。引 Ponemon 2026：内部威胁平均封堵需 **67 天**，日级响应太慢。最强控制是**不可重配置、不可绕过的 egress 代理白名单**；其他：用既有 IdP 发放/吊销身份、按**动作**而非连接器削权、工具调用经 OpenTelemetry 汇入 SIEM、执行环境不放有价值凭据

summary_ja: |
  CISO代理のJason Clinton氏。核心的な主張：**エージェントが意図から外れると、インサイダーと区別がつかなくなる**。Ponemon 2026を引用：インサイダー脅威の封じ込めには平均**67日**かかるため、日単位の対応では遅すぎる。最も強力な制御は**再構成もバイパスもできない外向きプロキシの許可リスト**。その他：既存のIdPでIDを発行・失効させる、権限をコネクター単位ではなく**アクション**単位でスコープする、ツール呼び出しをOpenTelemetry経由でSIEMに送る、価値の高い認証情報を実行環境に置かない

summary_ko: |
  부CISO Jason Clinton. 핵심 논지: **에이전트가 의도에서 벗어나면 내부자와 구분할 수 없다**. Ponemon 2026 인용: 내부자 위협을 억제하는 데 평균 **67일**이 걸리므로 일 단위 대응은 너무 느리다. 가장 강력한 통제는 **재구성하거나 우회할 수 없는 이그레스 프록시 허용 목록**이며, 그 밖에 기존 IdP를 통한 신원 발급·회수, 커넥터가 아닌 **행위** 기준의 권한 범위 설정, OpenTelemetry로 도구 호출을 SIEM에 전달, 실행 환경에서 중요 자격 증명 배제를 제시한다

summary_de: |
  Deputy CISO Jason Clinton. Kernargument: **Sobald ein Agent von der Absicht abweicht, ist er von einem Insider nicht mehr zu unterscheiden**. Verweist auf Ponemon 2026: Die Eindämmung einer Insider-Bedrohung dauert im Schnitt **67 Tage**, eine Reaktion auf Tagesebene ist also zu langsam. Die stärkste Kontrolle ist eine **Egress-Proxy-Positivliste, die nicht umkonfiguriert oder umgangen werden kann**; weitere: Identitäten über das bestehende IdP ausgeben und entziehen, Rechte nach **Aktion** statt nach Connector zuschneiden, Tool-Aufrufe über OpenTelemetry ins SIEM einspeisen und wertvolle Zugangsdaten aus der Ausführungsumgebung heraushalten

summary_fr: |
  Le CISO adjoint Jason Clinton. Argument central : **une fois qu'un agent sort de l'intention, il est indiscernable d'un initié**. Cite Ponemon 2026 : contenir une menace interne prend **67 jours** en moyenne, donc une réponse à l'échelle du jour est trop lente. Le contrôle le plus fort est une **liste blanche de proxy sortant impossible à reconfigurer ou contourner** ; autres : émettre et révoquer les identités via l'IdP existant, périmètrer les privilèges par **action** plutôt que par connecteur, alimenter le SIEM en appels d'outils via OpenTelemetry, et garder les identifiants précieux hors de l'environnement d'exécution

summary_es: |
  El CISO adjunto Jason Clinton. Argumento central: **una vez que un agente se sale del propósito, es indistinguible de un insider**. Cita Ponemon 2026: contener una amenaza interna tarda **67 días** de media, así que una respuesta a nivel de días es demasiado lenta. El control más fuerte es una **lista de permitidos de proxy de salida que no pueda reconfigurarse ni eludirse**; otros: emitir y revocar identidades a través del IdP existente, acotar privilegios por **acción** en lugar de por conector, enviar las llamadas a herramientas al SIEM mediante OpenTelemetry y mantener las credenciales valiosas fuera del entorno de ejecución

sources:
  - url: https://claude.com/blog/ciso-guide-to-agentic-ai
    label: Anthropic

disputed: false
landmark: false
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# Anthropic, "A CISO's guide to agentic AI"

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Deputy CISO Jason Clinton. Core argument: **once an agent goes off intent, it is indistinguishable from an insider**. Cites Ponemon 2026: containing an insider threat takes **67 days** on average, so day-level response is too slow. The strongest control is an **egress-proxy allowlist that cannot be reconfigured or bypassed**; others: issue and revoke identities through the existing IdP, scope privileges by **action** rather than by connector, feed tool calls into the SIEM via OpenTelemetry, and keep valuable credentials out of the execution environment

## Attack chain

```mermaid
flowchart LR
    E["Regulatory or policy action"]:::entry
    S0["Falls on vendors and users"]:::step
    I["Compliance requirements change"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Anthropic | <https://claude.com/blog/ciso-guide-to-agentic-ai> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-17` (raw: 2026-07-17, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-07-17-anthropic-ciso-guide-agentic` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-07-23` [US representatives introduce the AI Kill Switch Act](2026-07-23-kill-switch-act.md)<br>  <sub>US representatives introduce the AI Kill Switch Act</sub>
- `2026-07-27` [NVIDIA convenes the Open Secure AI Alliance](2026-07-27-nvidia-open-secure-alliance.md)<br>  <sub>NVIDIA convenes the Open Secure AI Alliance</sub>
- `2026-07-28` ["Pacing the Frontier" open letter](2026-07-28-pacing-frontier-gong-kai-xin.md)<br>  <sub>"Pacing the Frontier" open letter</sub>
- `2026-07-29` [Perplexity open-sources Numbat for agent behaviour monitoring](2026-07-29-perplexity-agent-numbat.md)<br>  <sub>Perplexity open-sources Numbat for agent behaviour monitoring</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-17-anthropic-ciso-guide-agentic.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
