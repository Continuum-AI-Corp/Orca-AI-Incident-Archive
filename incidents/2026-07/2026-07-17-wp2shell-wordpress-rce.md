---
id: 2026-07-17-wp2shell-wordpress-rce
title: "wp2shell: pre-auth RCE in WordPress core"
title_zh: "wp2shell：WordPress 核心预认证 RCE"
title_ja: "wp2shell：WordPressコアの認証前RCE"
title_ko: "wp2shell: WordPress 코어의 인증 전 RCE"
title_de: "wp2shell: Pre-Auth-RCE im WordPress-Kern"
title_fr: "wp2shell : RCE pré-auth dans le cœur de WordPress"
title_es: "wp2shell: RCE preautenticación en el núcleo de WordPress"
date: 2026-07-17
date_precision: day
date_raw: "2026-07-17"

kind: research
type: [WEAPON]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Searchlight Cyber: CVE-2026-60137 (an SQL injection in `WP_Query`'s `author__not_in`) + CVE-2026-63030 (a REST API batch-path confusion) chained into anonymous RCE on a standard, plugin-free setup. **Researcher Adam Kues switched to OpenAI's public prompt and used GPT-5.6 Sol Ultra with up to 4 agents exploring for 6 hours to find the exploit chain**, then about 4 more hours to confirm privilege escalation to administrator; the full exploit took about 10 hours. AI usage was 50% of the weekly quota, **about $25 at the $200 subscription rate**. Article title: "Exploit brokers pay $500,000 for a WordPress RCE; I found one with GPT-5.6 and $25". Both CVEs are in CISA KEV


summary_zh: |
  Searchlight Cyber：CVE-2026-60137（`WP_Query` 的 `author__not_in` SQL 注入）+ CVE-2026-63030（REST API 批处理路径混淆）链式达成无插件标准配置下的匿名 RCE。**研究员 Adam Kues 转用 OpenAI 公开的提示，用 GPT-5.6 Sol Ultra 最多 4 个 agent 探索 6 小时找到利用链**，再约 4 小时确认可提权到管理员，完整利用约 10 小时。AI 用量为周额度的 50%，**按 $200 订阅折算约 $25**。文章标题：《漏洞掮客为 WordPress RCE 出价 50 万美元，我用 GPT-5.6 和 25 美元找到了一个》。两 CVE 均入 CISA KEV

summary_ja: |
  Searchlight Cyber：CVE-2026-60137（`WP_Query`の`author__not_in`におけるSQLインジェクション）＋CVE-2026-63030（REST APIのバッチパス混乱）を連鎖させ、プラグインなしの標準構成で匿名RCEを達成。**研究者のAdam Kues氏はOpenAIの公開プロンプトに切り替え、最大4エージェントが6時間探索するGPT-5.6 Sol Ultraでエクスプロイトチェーンを発見**し、管理者への権限昇格の確認にさらに約4時間、フルエクスプロイトは約10時間だった。AI使用量は週次クォータの50%で、**200ドルサブスクリプション換算で約25ドル**。記事タイトル：「エクスプロイトブローカーはWordPress RCEに50万ドルを払う。私はGPT-5.6と25ドルで見つけた」。両CVEともCISA KEVに収載

summary_ko: |
  Searchlight Cyber: CVE-2026-60137(`WP_Query`의 `author__not_in` SQL 인젝션) + CVE-2026-63030(REST API 배치 경로 혼동)을 연쇄해 플러그인 없는 표준 구성에서 익명 RCE를 달성했다. **연구자 Adam Kues는 OpenAI의 공개 프롬프트로 전환해 GPT-5.6 Sol Ultra에서 최대 4개 에이전트가 6시간 동안 탐색하게 해 익스플로잇 체인을 찾았고**, 관리자 권한 상승을 확인하는 데 약 4시간이 더 걸려 전체 익스플로잇에 약 10시간이 소요되었다. AI 사용량은 주간 할당량의 50%, **200달러 구독 기준 약 25달러**였다. 기사 제목: "익스플로잇 브로커는 WordPress RCE에 50만 달러를 지불한다; 나는 GPT-5.6과 25달러로 찾았다". 두 CVE 모두 CISA KEV에 등재되어 있다

summary_de: |
  Searchlight Cyber: CVE-2026-60137 (eine SQL-Injection in `author__not_in` von `WP_Query`) + CVE-2026-63030 (eine Pfadverwechslung im REST-API-Batch) verkettet zu anonymer RCE auf einer standardmäßigen, plugin-freien Installation. **Der Forscher Adam Kues wechselte zu OpenAIs öffentlichem Prompt und nutzte GPT-5.6 Sol Ultra mit bis zu 4 Agenten, die 6 Stunden lang erkundeten, um die Exploit-Kette zu finden**, danach etwa 4 weitere Stunden, um die Rechteerweiterung zum Administrator zu bestätigen; der vollständige Exploit dauerte rund 10 Stunden. Der KI-Einsatz machte 50% des Wochenkontingents aus, **etwa $25 beim Abopreis von $200**. Artikeltitel: „Exploit brokers pay $500,000 for a WordPress RCE; I found one with GPT-5.6 and $25“. Beide CVEs stehen in der CISA KEV

summary_fr: |
  Searchlight Cyber : CVE-2026-60137 (une injection SQL dans `author__not_in` de `WP_Query`) + CVE-2026-63030 (une confusion de chemin par lots de l'API REST) enchaînées en un RCE anonyme sur une installation standard sans plugin. **Le chercheur Adam Kues est passé au prompt public d'OpenAI et a utilisé GPT-5.6 Sol Ultra avec jusqu'à 4 agents explorant pendant 6 heures pour trouver la chaîne d'exploit**, puis environ 4 heures de plus pour confirmer l'élévation de privilèges vers administrateur ; l'exploit complet a pris environ 10 heures. L'usage de l'IA a représenté 50 % du quota hebdomadaire, **environ 25 $ au tarif de l'abonnement à 200 $**. Titre de l'article : « Exploit brokers pay $500,000 for a WordPress RCE; I found one with GPT-5.6 and $25 ». Les deux CVE figurent dans le KEV de la CISA

summary_es: |
  Searchlight Cyber: CVE-2026-60137 (una inyección SQL en `author__not_in` de `WP_Query`) + CVE-2026-63030 (una confusión en la ruta por lotes de la API REST) encadenadas hasta RCE anónimo en una instalación estándar y sin plugins. **El investigador Adam Kues cambió al prompt público de OpenAI y usó GPT-5.6 Sol Ultra con hasta 4 agentes explorando durante 6 horas para encontrar la cadena de explotación**, y luego unas 4 horas más para confirmar la escalada de privilegios a administrador; el exploit completo tardó unas 10 horas. El uso de IA fue el 50% de la cuota semanal, **unos $25 al precio de la suscripción de $200**. Título del artículo: "Los intermediarios de exploits pagan $500,000 por un RCE de WordPress; yo encontré uno con GPT-5.6 y $25". Ambos CVE están en el catálogo KEV de CISA

sources:
  - url: https://slcyber.io/research-center/wp2shell-pre-authentication-rce-in-wordpress-core/
    label: Searchlight Cyber
  - url: https://slcyber.io/research-center/exploit-brokers-pay-500000-for-a-wordpress-rce-i-found-one-with-gpt5-6/
    label: Cost write-up

disputed: false
landmark: false
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# wp2shell: pre-auth RCE in WordPress core

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

Searchlight Cyber: CVE-2026-60137 (an SQL injection in `WP_Query`'s `author__not_in`) + CVE-2026-63030 (a REST API batch-path confusion) chained into anonymous RCE on a standard, plugin-free setup. **Researcher Adam Kues switched to OpenAI's public prompt and used GPT-5.6 Sol Ultra with up to 4 agents exploring for 6 hours to find the exploit chain**, then about 4 more hours to confirm privilege escalation to administrator; the full exploit took about 10 hours. AI usage was 50% of the weekly quota, **about $25 at the $200 subscription rate**. Article title: "Exploit brokers pay $500,000 for a WordPress RCE; I found one with GPT-5.6 and $25". Both CVEs are in CISA KEV

## Attack chain

```mermaid
flowchart LR
    E["Attacker + jailbreak script"]:::entry
    S0["LLM orchestrator drives a cluster of sub-agents"]:::step
    I["Target systems compromised<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Searchlight Cyber | <https://slcyber.io/research-center/wp2shell-pre-authentication-rce-in-wordpress-core/> |
| 2 | Cost write-up | <https://slcyber.io/research-center/exploit-brokers-pay-500000-for-a-wordpress-rce-i-found-one-with-gpt5-6/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-17` (raw: 2026-07-17, precision `day`) |
| Kind | Research demo `research` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-07-17-wp2shell-wordpress-rce` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-07-01` [Taiwan's nuclear safety commission and other agencies breached by an agent swarm](2026-07-01-taiwan-government-agent-swarm.md)<br>  <sub>Taiwan's nuclear safety commission and other agencies breached by an agent swarm</sub>
- `2026-07-01` [JADEPUFFER: first ransomware driven end-to-end by an LLM](2026-07-01-jadepuffer-first-llm-driven-ransomware.md)<br>  <sub>JADEPUFFER: first ransomware driven end-to-end by an LLM</sub>
- `2026-07-09` [OpenAI's agents breach Hugging Face](2026-07-09-openai-agents-breach-huggingface.md)<br>  <sub>OpenAI's agents breach Hugging Face</sub>
- `2026-07-30` [Hermes Agent attacks Thailand's Ministry of Finance unattended](2026-07-30-hermes-agent-thailand-finance-ministry.md)<br>  <sub>Hermes Agent attacks Thailand's Ministry of Finance unattended</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-17-wp2shell-wordpress-rce.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
