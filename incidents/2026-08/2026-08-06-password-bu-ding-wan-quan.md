---
id: 2026-08-06-password-bu-ding-wan-quan
title: "1Password: AI patches fully fix only 26% of the time"
title_zh: "1Password：AI 补丁完全修复率仅 26%"
title_ja: "1Password：AIパッチが完全に修正できるのは26%のみ"
title_ko: "1Password: AI 패치가 완전히 고치는 경우는 26%뿐"
title_de: "1Password: KI-Patches beheben nur in 26% der Fälle vollständig"
title_fr: "1Password : les correctifs générés par IA ne corrigent complètement que dans 26 % des cas"
title_es: "1Password: los parches de IA solo corrigen por completo el 26% de las veces"
date: 2026-08-06
date_precision: day
date_raw: "2026-08-06"

kind: report
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Off-by-1 Labs: 2 generative AI models produced 6,480 patches for 6 CVEs that require complex fixes; after excluding 400 that simply "copied upstream", 6,080 remained — **only 26.0% on average fully eliminated the vulnerability without changing behaviour**, and **53.9% left the vulnerability in place, introduced new flaws, or both**. Separately, Checkmarx's SusViBes benchmark: functional success rate 83–95%, but **only 24–36% were both secure and functionally correct**, and **65–75% of the working patches reproduced flaws that had already been fixed**


summary_zh: |
  Off-by-1 Labs：对 6 个需复杂修复的 CVE 用 2 个生成式 AI 模型产出 6,480 份补丁，剔除 400 份「抄上游」后统计 6,080 份 —— **在不改变行为的前提下彻底消除漏洞的平均只有 26.0%**，**53.9% 是漏洞仍在、引入新漏洞、或两者都有**。另 Checkmarx 的 SusViBes 基准：功能成功率 83–95%，但**安全且功能正确的只有 24–36%**，能跑的补丁里 **65–75% 复现了已被修复过的漏洞**

summary_ja: |
  Off-by-1 Labs：複雑な修正を要する6件のCVEに対して2つの生成AIモデルが6,480件のパッチを生成。単に「上流をコピー」した400件を除いた6,080件のうち、**平均で26.0%だけが動作を変えずに脆弱性を完全に解消**し、**53.9%は脆弱性を残すか、新たな欠陥を持ち込むか、その両方だった**。別途、CheckmarxのSusViBesベンチマーク：機能的成功率は83〜95%だが、**安全かつ機能的に正しいものは24〜36%のみ**で、**動作するパッチの65〜75%がすでに修正済みの欠陥を再現した**

summary_ko: |
  Off-by-1 Labs: 생성 AI 모델 2종이 복잡한 수정이 필요한 CVE 6건에 대해 6,480개의 패치를 만들었고, 단순히 "업스트림을 복사"한 400개를 제외한 6,080개 중 **평균 26.0%만이 동작을 바꾸지 않고 취약점을 완전히 제거**했으며 **53.9%는 취약점을 그대로 두거나 새로운 결함을 넣거나 둘 다였다**. 별도로 Checkmarx의 SusViBes 벤치마크: 기능적 성공률은 83~95%였지만 **안전성과 기능 정확성을 모두 만족한 것은 24~36%뿐**이었고 **동작하는 패치의 65~75%가 이미 수정된 결함을 재현했다**

summary_de: |
  Off-by-1 Labs: 2 generative KI-Modelle erzeugten 6,480 Patches für 6 CVEs, die komplexe Korrekturen erfordern; nach Ausschluss von 400, die einfach „das Upstream kopierten“, blieben 6,080 — **nur 26.0% im Durchschnitt beseitigten die Schwachstelle vollständig, ohne das Verhalten zu ändern**, und **53.9% ließen die Schwachstelle bestehen, führten neue Fehler ein oder beides**. Separat dazu der SusViBes-Benchmark von Checkmarx: funktionale Erfolgsrate 83–95%, doch **nur 24–36% waren zugleich sicher und funktional korrekt**, und **65–75% der funktionierenden Patches reproduzierten Fehler, die bereits behoben worden waren**

summary_fr: |
  Off-by-1 Labs : 2 modèles d'IA génératives ont produit 6 480 correctifs pour 6 CVE nécessitant des corrections complexes ; après exclusion de 400 qui « copiaient simplement l'amont », il en restait 6 080 — **seuls 26,0 % en moyenne éliminaient complètement la vulnérabilité sans changer le comportement**, et **53,9 % laissaient la vulnérabilité en place, introduisaient de nouveaux défauts, ou les deux**. Par ailleurs, le benchmark SusViBes de Checkmarx : taux de réussite fonctionnelle de 83 à 95 %, mais **seuls 24 à 36 % étaient à la fois sûrs et fonctionnellement corrects**, et **65 à 75 % des correctifs fonctionnels reproduisaient des défauts déjà corrigés**

summary_es: |
  Off-by-1 Labs: 2 modelos de IA generativa produjeron 6,480 parches para 6 CVE que requieren correcciones complejas; tras excluir 400 que simplemente "copiaron el upstream", quedaron 6,080 — **solo el 26.0% de media eliminó por completo la vulnerabilidad sin cambiar el comportamiento**, y **el 53.9% dejó la vulnerabilidad en su sitio, introdujo nuevos fallos, o ambas cosas**. Aparte, el benchmark SusViBes de Checkmarx: tasa de éxito funcional del 83–95%, pero **solo el 24–36% eran a la vez seguros y funcionalmente correctos**, y **el 65–75% de los parches que funcionaban reprodujeron fallos que ya se habían corregido**

sources:
  - url: https://1password.com/blog/why-ai-generated-patches-still-require-human-review
    label: 1Password
  - url: https://1password.com/files/resources/frontier-models-vulnerability-patches-flawed.pdf
    label: PDF
  - url: https://checkmarx.com/blog/zombie-cves-put-to-rest-by-humans-dug-back-up-by-ai-agents/
    label: Checkmarx

disputed: false
landmark: false
scan_month: 2026-08
scan_ref: "SCAN.md §6 2026-08"
---

# 1Password: AI patches fully fix only 26% of the time

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Off-by-1 Labs: 2 generative AI models produced 6,480 patches for 6 CVEs that require complex fixes; after excluding 400 that simply "copied upstream", 6,080 remained — **only 26.0% on average fully eliminated the vulnerability without changing behaviour**, and **53.9% left the vulnerability in place, introduced new flaws, or both**. Separately, Checkmarx's SusViBes benchmark: functional success rate 83–95%, but **only 24–36% were both secure and functionally correct**, and **65–75% of the working patches reproduced flaws that had already been fixed**

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
| 1 | 1Password | <https://1password.com/blog/why-ai-generated-patches-still-require-human-review> |
| 2 | PDF | <https://1password.com/files/resources/frontier-models-vulnerability-patches-flawed.pdf> |
| 3 | Checkmarx | <https://checkmarx.com/blog/zombie-cves-put-to-rest-by-humans-dug-back-up-by-ai-agents/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-08-06` (raw: 2026-08-06, precision `day`) |
| Kind | Threat report `report` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-08-06-password-bu-ding-wan-quan` |

<sub>**Why this classification:** Threat intelligence report covering several incidents; it is not counted as a single incident itself, so `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-08-03` [CrowdStrike 2026 threat hunting report](2026-08-03-crowdstrike-wei-xie-shou-lie.md)<br>  <sub>CrowdStrike 2026 threat hunting report</sub>
- `2026-08-04` [OSAA publishes the SAFE draft for AI incident sharing (RFC)](2026-08-04-osaa-safe-rfc.md)<br>  <sub>OSAA publishes the SAFE draft for AI incident sharing (RFC)</sub>
- `2026-08-07` [OpenAI: next-generation model Astra may reach Critical cyber capability](2026-08-07-astra-critical-yi-dai-mo.md)<br>  <sub>OpenAI: next-generation model Astra may reach Critical cyber capability</sub>
- `2026-08-18` [OpenAI slows development and pauses RL training for two weeks](2026-08-18-rl-xuan-bu-fang-man.md)<br>  <sub>OpenAI slows development and pauses RL training for two weeks</sub>

---

[← 2026-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-08/2026-08-06-password-bu-ding-wan-quan.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
