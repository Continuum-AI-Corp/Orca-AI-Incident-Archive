---
id: 2026-02-20-fortigate-600-devices-compromised
title: "AI-augmented actor compromises 600+ FortiGate devices"
title_zh: "AI 增强型威胁方批量攻陷 600+ FortiGate"
title_ja: "AIを活用したアクターが600台以上のFortiGate機器を侵害"
title_ko: "AI로 강화된 행위자, FortiGate 600대 이상 침해"
title_de: "KI-verstärkter Akteur kompromittiert 600+ FortiGate-Geräte"
title_fr: "Un acteur augmenté par l'IA compromet plus de 600 appareils FortiGate"
title_es: "Un actor potenciado por IA compromete más de 600 dispositivos FortiGate"
date: 2026-02-20
date_precision: day
date_raw: "2026-02-20"

kind: incident
type: [WEAPON]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  AWS Security: a Russian-speaking actor compromised 600+ FortiGate devices worldwide **in five weeks**. **No zero-days** were used — only scanning of publicly exposed management ports plus weak passwords. AI acted as a "force multiplier", automating reconnaissance, developing custom tooling and generating attack plans; a self-built MCP framework, **ARXON**, wired LLMs into the intrusion workflow (DCSync/Impacket credential theft, attacks on Veeam backups). The actor's own skill level is moderate, but AI greatly amplified the scale of the operation


summary_zh: |
  AWS Security：俄语系行为者 **5 周内**攻陷全球 600+ 台 FortiGate。**不用零日**，只扫公开管理端口 + 弱口令。AI 作为「战力倍增器」自动化侦察、开发定制工具、生成攻击计划；使用自研 MCP 框架 **ARXON** 把 LLM 接进入侵工作流（DCSync/Impacket 窃凭据、打 Veeam 备份）。行为者本身技术中等，但 AI 让运营规模大幅放大

summary_ja: |
  AWS Security：ロシア語話者のアクターが**5週間で**世界の600台以上のFortiGate機器を侵害した。**ゼロデイは不使用**——公開された管理ポートのスキャンと弱いパスワードのみ。AIは「フォースマルチプライヤー」として機能し、偵察の自動化、カスタムツールの開発、攻撃計画の生成を担った。自作のMCPフレームワーク**ARXON**がLLMを侵入ワークフロー（DCSync/Impacketによる認証情報窃取、Veeamバックアップへの攻撃）に組み込んでいた。アクター自身の技能は中程度だが、AIが作戦規模を大幅に増幅した

summary_ko: |
  AWS Security: 러시아어권 행위자가 **5주 만에** 전 세계 FortiGate 기기 600대 이상을 침해했다. **제로데이는 사용되지 않았고** 공개된 관리 포트 스캔과 취약한 비밀번호뿐이었다. AI는 "전력 증폭기"로 작동해 정찰 자동화, 맞춤 도구 개발, 공격 계획 생성을 수행했다. 자체 제작한 MCP 프레임워크 **ARXON**이 LLM을 침입 워크플로에 연결했고(DCSync/Impacket 자격 증명 탈취, Veeam 백업 공격) 활용되었다. 행위자 자체의 실력은 중간 수준이지만 AI가 작전 규모를 크게 증폭시켰다

summary_de: |
  AWS Security: Ein russischsprachiger Akteur kompromittierte **in fünf Wochen** 600+ FortiGate-Geräte weltweit. **Keine Zero-Days** kamen zum Einsatz — nur das Scannen öffentlich exponierter Management-Ports plus schwache Passwörter. KI wirkte als „Force Multiplier“, automatisierte Aufklärung, entwickelte eigenes Tooling und erzeugte Angriffspläne; ein selbst gebautes MCP-Framework, **ARXON**, verdrahtete LLMs mit dem Intrusionsablauf (DCSync/Impacket-Zugangsdatendiebstahl, Angriffe auf Veeam-Backups). Das eigene Können des Akteurs ist mittelmäßig, doch KI verstärkte den Umfang der Operation erheblich

summary_fr: |
  AWS Security : un acteur russophone a compromis plus de 600 appareils FortiGate dans le monde **en cinq semaines**. **Aucun zero-day** n'a été utilisé — seulement du scan de ports de gestion exposés publiquement et des mots de passe faibles. L'IA a agi comme un « multiplicateur de force », automatisant la reconnaissance, développant de l'outillage sur mesure et générant des plans d'attaque ; un framework MCP maison, **ARXON**, a intégré des LLM dans le flux d'intrusion (vol d'identifiants DCSync/Impacket, attaques contre les sauvegardes Veeam). Le niveau de compétence de l'acteur est moyen, mais l'IA a fortement amplifié l'échelle de l'opération

summary_es: |
  AWS Security: un actor de habla rusa comprometió más de 600 dispositivos FortiGate en todo el mundo **en cinco semanas**. **No se usó ningún zero-day** — solo escaneo de puertos de administración expuestos públicamente y contraseñas débiles. La IA actuó como "multiplicador de fuerza", automatizando el reconocimiento, desarrollando herramientas personalizadas y generando planes de ataque; un marco MCP propio, **ARXON**, conectó LLM al flujo de intrusión (robo de credenciales con DCSync/Impacket, ataques a copias de seguridad de Veeam). El nivel de habilidad del propio actor es moderado, pero la IA amplificó enormemente la escala de la operación

sources:
  - url: https://aws.amazon.com/jp/blogs/security/ai-augmented-threat-actor-accesses-fortigate-devices-at-scale/
    label: AWS Security
  - url: https://www.bleepingcomputer.com/news/security/amazon-ai-assisted-hacker-breached-600-fortigate-firewalls-in-5-weeks/
    label: BleepingComputer
  - url: https://cyberandramen.net/2026/02/21/llms-in-the-kill-chain-inside-a-custom-mcp-targeting-fortigate-devices-across-continents/
    label: "Cyber&Ramen technical analysis"

disputed: false
landmark: true
scan_month: 2026-02
scan_ref: "SCAN.md §6 2026-02"
---

# AI-augmented actor compromises 600+ FortiGate devices

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

AWS Security: a Russian-speaking actor compromised 600+ FortiGate devices worldwide **in five weeks**. **No zero-days** were used — only scanning of publicly exposed management ports plus weak passwords. AI acted as a "force multiplier", automating reconnaissance, developing custom tooling and generating attack plans; a self-built MCP framework, **ARXON**, wired LLMs into the intrusion workflow (DCSync/Impacket credential theft, attacks on Veeam backups). The actor's own skill level is moderate, but AI greatly amplified the scale of the operation

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
| 1 | AWS Security | <https://aws.amazon.com/jp/blogs/security/ai-augmented-threat-actor-accesses-fortigate-devices-at-scale/> |
| 2 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/amazon-ai-assisted-hacker-breached-600-fortigate-firewalls-in-5-weeks/> |
| 3 | Cyber&Ramen technical analysis | <https://cyberandramen.net/2026/02/21/llms-in-the-kill-chain-inside-a-custom-mcp-targeting-fortigate-devices-across-continents/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-02-20` (raw: 2026-02-20, precision `day`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-02-20-fortigate-600-devices-compromised` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-02-25` [Nine Mexican government agencies breached](2026-02-25-mexico-nine-agencies-breached.md)<br>  <sub>Nine Mexican government agencies breached</sub>
- `2026-02-28` [CodeWall breaches McKinsey's internal "Lilli" AI platform](2026-02-28-codewall-breaches-mckinsey-lilli.md)<br>  <sub>CodeWall breaches McKinsey's internal "Lilli" AI platform</sub>
- `2026-01-01` [Claude Code sprays credentials at a Mexican water utility's OT network](../2026-01/2026-01-01-ot-claude-code.md)<br>  <sub>Claude Code sprays credentials at a Mexican water utility's OT network</sub>
- `2026-03-06` [Microsoft, "AI as tradecraft"](../2026-03/2026-03-06-microsoft-as-tradecraft.md)<br>  <sub>Microsoft, "AI as tradecraft"</sub>

---

[← 2026-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-02/2026-02-20-fortigate-600-devices-compromised.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
