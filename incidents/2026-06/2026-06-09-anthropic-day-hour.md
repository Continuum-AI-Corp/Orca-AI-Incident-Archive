---
id: 2026-06-09-anthropic-day-hour
title: "Anthropic: N-day is really \"N-hour\""
title_zh: "Anthropic：N-day 实为「N-hour」"
title_ja: "Anthropic：N-dayは実質「N-hour」である"
title_ko: "Anthropic: N-day는 사실 \"N-hour\""
title_de: "Anthropic: N-Day ist in Wahrheit „N-Hour“"
title_fr: "Anthropic : le N-day est en réalité un « N-heure »"
title_es: "Anthropic: los N-day son en realidad \"N-hour\""
date: 2026-06-09
date_precision: day
date_raw: "2026-06-09"

kind: report
type: [WEAPON]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Given only the patch diff + severity + pre- and post-fix builds: of Firefox's 18 SpiderMonkey vulnerabilities, Claude Mythos Preview produced **14 PoCs**, of which **8 became code-execution exploits able to read files outside the sandbox within about 12 hours** (**the first in under 1 hour**, while the corresponding Firefox 148 release came 18 days later). Closed-source Windows: the 21 kernel privilege-escalation flaws from 2026-01 → 02 → **18 PoCs and 8 complete privilege-escalation chains**, total cost about **$15,700 (about $2,000 each)**. **13 of the 14 flaws Microsoft rated "unlikely to be exploited" also got PoCs**. The report also notes Windows Autopatch takes 7 days to reach 90% coverage and forced reboots land on day 11


summary_zh: |
  只给补丁 diff + 严重度 + 修复前后构建：Firefox 的 18 个 SpiderMonkey 漏洞 → Claude Mythos Preview 做出 **14 个 PoC**，其中 **8 个在约 12 小时内**做成可读沙箱外文件的代码执行利用（**第一个不到 1 小时**，而对应的 Firefox 148 发布在 18 天后）。闭源 Windows：2026 年 1–2 月的 21 个内核提权漏洞 → **18 个 PoC、8 条完整提权链**，总成本约 **$15,700（单个约 $2,000）**。**微软评为「不太可能被利用」的 14 个里有 13 个也做出了 PoC**。同时指出 Windows Autopatch 铺到 9 成要 7 天、强制重启在第 11 天

summary_ja: |
  パッチのdiff＋深刻度＋修正前後のビルドのみを与えたところ：FirefoxのSpiderMonkey脆弱性18件のうち、Claude Mythos Previewは**14件のPoC**を生成し、そのうち**8件は約12時間以内にサンドボックス外のファイルを読めるコード実行エクスプロイトになった**（**最初の1件は1時間未満**。対応するFirefox 148のリリースは18日後だった）。クローズドソースのWindows：2026-01 → 02のカーネル権限昇格欠陥21件から**18件のPoCと8本の完全な権限昇格チェーン**、総コスト約**1万5,700ドル（1件あたり約2,000ドル）**。**Microsoftが「悪用される可能性は低い」と評価した14件のうち13件でもPoCが得られた**。レポートはまた、Windows Autopatchが90%カバレッジに達するまで7日かかり、強制再起動が11日目になることも指摘している

summary_ko: |
  패치 diff + 심각도 + 수정 전후 빌드만 주어진 조건에서: Firefox의 SpiderMonkey 취약점 18건 중 Claude Mythos Preview가 **PoC 14건**을 만들어냈고, 그중 **8건이 약 12시간 안에 샌드박스 밖 파일을 읽을 수 있는 코드 실행 익스플로잇이 되었다**(**첫 번째는 1시간 이내**, 해당 Firefox 148 릴리스는 18일 뒤였다). 클로즈드 소스 Windows: 2026-01 → 02의 커널 권한 상승 결함 21건 → **PoC 18건과 완전한 권한 상승 체인 8개**, 총비용 약 **15,700달러(건당 약 2,000달러)**. **마이크로소프트가 "악용 가능성 낮음"으로 평가한 14건 중 13건에서도 PoC가 나왔다**. 보고서는 Windows Autopatch가 90% 적용까지 7일이 걸리고 강제 재부팅이 11일째에 이뤄진다는 점도 지적했다

summary_de: |
  Mit nur dem Patch-Diff + Schweregrad + Builds vor und nach der Korrektur: Von den 18 SpiderMonkey-Schwachstellen in Firefox erzeugte Claude Mythos Preview **14 PoCs**, von denen **8 innerhalb von etwa 12 Stunden zu Code-Ausführungs-Exploits wurden, die Dateien außerhalb der Sandbox lesen konnten** (**der erste in unter 1 Stunde**, während das entsprechende Firefox-148-Release 18 Tage später kam). Closed-Source-Windows: Bei den 21 Kernel-Rechteerweiterungsschwachstellen von 2026-01 → 02 → **18 PoCs und 8 vollständige Rechteerweiterungsketten**, Gesamtkosten etwa **$15,700 (etwa $2,000 pro Stück)**. **Auch 13 der 14 Schwachstellen, die Microsoft als „unwahrscheinlich ausnutzbar“ einstufte, erhielten PoCs**. Der Bericht merkt zudem an, dass Windows Autopatch 7 Tage braucht, um 90% Abdeckung zu erreichen, und erzwungene Neustarts am Tag 11 erfolgen

summary_fr: |
  À partir uniquement du diff du correctif + de la sévérité + des builds avant/après : sur les 18 vulnérabilités SpiderMonkey de Firefox, Claude Mythos Preview a produit **14 PoC**, dont **8 sont devenus des exploits d'exécution de code capables de lire des fichiers hors du bac à sable en environ 12 heures** (**le premier en moins d'1 heure**, alors que la version Firefox 148 correspondante est sortie 18 jours plus tard). Windows à code fermé : les 21 failles d'élévation de privilèges du noyau de 2026-01 → 02 → **18 PoC et 8 chaînes complètes d'élévation de privilèges**, pour un coût total d'environ **15 700 $ (environ 2 000 $ chacune)**. **13 des 14 failles que Microsoft jugeait « peu susceptibles d'être exploitées » ont aussi eu des PoC**. Le rapport note aussi que Windows Autopatch met 7 jours à atteindre 90 % de couverture et que les redémarrages forcés arrivent au jour 11

summary_es: |
  Dado solo el diff del parche + la gravedad + las compilaciones antes y después de la corrección: de las 18 vulnerabilidades de SpiderMonkey de Firefox, Claude Mythos Preview produjo **14 PoC**, de los cuales **8 se convirtieron en exploits de ejecución de código capaces de leer archivos fuera del sandbox en unas 12 horas** (**el primero en menos de 1 hora**, mientras que el lanzamiento correspondiente de Firefox 148 llegó 18 días después). Windows de código cerrado: los 21 fallos de escalada de privilegios del kernel de 2026-01 → 02 → **18 PoC y 8 cadenas completas de escalada de privilegios**, con un costo total de unos **$15,700 (unos $2,000 cada uno)**. **13 de los 14 fallos que Microsoft calificó como "poco probables de ser explotados" también obtuvieron PoC**. El informe también señala que Windows Autopatch tarda 7 días en alcanzar el 90% de cobertura y que los reinicios forzados llegan el día 11

sources:
  - url: https://red.anthropic.com/2026/n-days/
    label: red.anthropic.com

disputed: false
landmark: true
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# Anthropic: N-day is really "N-hour"

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

Given only the patch diff + severity + pre- and post-fix builds: of Firefox's 18 SpiderMonkey vulnerabilities, Claude Mythos Preview produced **14 PoCs**, of which **8 became code-execution exploits able to read files outside the sandbox within about 12 hours** (**the first in under 1 hour**, while the corresponding Firefox 148 release came 18 days later). Closed-source Windows: the 21 kernel privilege-escalation flaws from 2026-01 → 02 → **18 PoCs and 8 complete privilege-escalation chains**, total cost about **$15,700 (about $2,000 each)**. **13 of the 14 flaws Microsoft rated "unlikely to be exploited" also got PoCs**. The report also notes Windows Autopatch takes 7 days to reach 90% coverage and forced reboots land on day 11

## Attack chain

```mermaid
flowchart LR
    E["Attacker + jailbreak script"]:::entry
    S0["LLM orchestrator drives a cluster of sub-agents"]:::step
    I["Target systems compromised"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | red.anthropic.com | <https://red.anthropic.com/2026/n-days/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-09` (raw: 2026-06-09, precision `day`) |
| Kind | Threat report `report` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-09-anthropic-day-hour` |

<sub>**Why this classification:** Threat intelligence report covering several incidents; it is not counted as a single incident itself, so `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-06-15` [UNC6508 breaches North American research institutions via REDCap](2026-06-15-unc6508-redcap-jing-ru-qin.md)<br>  <sub>UNC6508 breaches North American research institutions via REDCap</sub>
- `2026-06-02` [CleverHans Lab adaptive AI worm PoC](2026-06-02-cleverhans-lab-poc.md)<br>  <sub>CleverHans Lab adaptive AI worm PoC</sub>
- `2026-06-24` [macOS.Gaslight: malware prompt-injects the AI analyst](2026-06-24-macos-gaslight-e-yi-ruan-jian.md)<br>  <sub>macOS.Gaslight: malware prompt-injects the AI analyst</sub>
- `2026-06-03` [Anthropic, "LLM ATT&CK Navigator"](2026-06-03-anthropic-llm-att-ck.md)<br>  <sub>Anthropic, "LLM ATT&CK Navigator"</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-09-anthropic-day-hour.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
