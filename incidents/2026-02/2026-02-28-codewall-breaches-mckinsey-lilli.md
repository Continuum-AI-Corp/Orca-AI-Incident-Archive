---
id: 2026-02-28-codewall-breaches-mckinsey-lilli
title: "CodeWall breaches McKinsey's internal \"Lilli\" AI platform"
title_zh: "CodeWall 攻破麦肯锡 \"Lilli\" 内部 AI 平台"
title_ja: "CodeWallがマッキンゼー社内の「Lilli」AIプラットフォームを侵害"
title_ko: "CodeWall, 맥킨지 내부 \"Lilli\" AI 플랫폼 침해"
title_de: "CodeWall dringt in McKinseys interne KI-Plattform „Lilli“ ein"
title_fr: "CodeWall pénètre la plateforme IA interne « Lilli » de McKinsey"
title_es: "CodeWall vulnera la plataforma interna de IA \"Lilli\" de McKinsey"
date: 2026-02-28
date_precision: day
date_raw: "2026-02-28"

kind: incident
type: [WEAPON, INFRA]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [US]

summary: |
  The autonomous attack agent found an **unauthenticated SQL injection** in a public API endpoint → full read/write access to the production database → **46.5 million chat messages**, confidential documents and proprietary research data leaked. More seriously, it obtained **write access to the AI prompt layer** (able to manipulate answers and disable guardrails). Disclosed on 03-09


summary_zh: |
  自主攻击 agent 在公开 API 端点发现**未认证 SQL 注入** → 生产库完整读写权限 → **4,650 万条聊天消息**、机密文档、专有研究数据泄露。更严重的是拿到了 **AI 提示层的写权限**（可操纵回答、禁用护栏）。03-09 公开

summary_ja: |
  自律型攻撃エージェントが公開APIエンドポイントの**認証不要のSQLインジェクション**を発見→本番データベースへの完全な読み書きアクセス→**4,650万件のチャットメッセージ**、機密文書、独自調査データが漏えい。さらに深刻なことに、**AIプロンプトレイヤーへの書き込みアクセス**を取得した（回答の操作とガードレールの無効化が可能）。03-09に公表

summary_ko: |
  자율 공격 에이전트가 공개 API 엔드포인트에서 **무인증 SQL 인젝션**을 발견했다 → 프로덕션 데이터베이스 전체 읽기/쓰기 접근 → **4,650만 건의 채팅 메시지**, 기밀 문서, 독점 연구 데이터 유출. 더 심각하게는 **AI 프롬프트 계층에 대한 쓰기 권한**을 얻어 답변을 조작하고 가드레일을 비활성화할 수 있었다. 03-09에 공개되었다

summary_de: |
  Der autonome Angriffsagent fand eine **nicht authentifizierte SQL-Injection** in einem öffentlichen API-Endpunkt → vollständiger Lese-/Schreibzugriff auf die Produktionsdatenbank → **46.5 Millionen Chatnachrichten**, vertrauliche Dokumente und proprietäre Forschungsdaten gelangten an die Öffentlichkeit. Gravierender noch: Er erlangte **Schreibzugriff auf die KI-Prompt-Ebene** (konnte Antworten manipulieren und Guardrails deaktivieren). Offengelegt am 03-09

summary_fr: |
  L'agent d'attaque autonome a trouvé une **injection SQL non authentifiée** dans un point de terminaison d'API public → accès complet en lecture/écriture à la base de production → **46,5 millions de messages de chat**, documents confidentiels et données de recherche propriétaires divulgués. Plus grave, il a obtenu **un accès en écriture à la couche de prompts de l'IA** (pouvant manipuler les réponses et désactiver les garde-fous). Divulgué le 03-09

summary_es: |
  El agente de ataque autónomo encontró una **inyección SQL sin autenticación** en un endpoint de API público → acceso completo de lectura/escritura a la base de datos de producción → **46.5 millones de mensajes de chat**, documentos confidenciales y datos de investigación propietarios filtrados. Más grave aún, obtuvo **acceso de escritura a la capa de prompts de la IA** (podía manipular las respuestas y desactivar los guardrails). Divulgado el 03-09

sources:
  - url: https://codewall.ai/blog/how-we-hacked-mckinseys-ai-platform
    label: CodeWall

disputed: false
landmark: true
scan_month: 2026-02
scan_ref: "SCAN.md §6 2026-02"
---

# CodeWall breaches McKinsey's internal "Lilli" AI platform

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

The autonomous attack agent found an **unauthenticated SQL injection** in a public API endpoint → full read/write access to the production database → **46.5 million chat messages**, confidential documents and proprietary research data leaked. More seriously, it obtained **write access to the AI prompt layer** (able to manipulate answers and disable guardrails). Disclosed on 03-09

## Attack chain

```mermaid
flowchart LR
    E["Attacker + jailbreak script"]:::entry
    S0["LLM orchestrator drives a cluster of sub-agents"]:::step
    S1["Unauthenticated access"]:::step
    I["RCE / data leak"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | CodeWall | <https://codewall.ai/blog/how-we-hacked-mckinseys-ai-platform> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-02-28` (raw: 2026-02-28, precision `day`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon · [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [United States](../../regions/us.md) |
| Archive ID | `2026-02-28-codewall-breaches-mckinsey-lilli` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md) · [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-02-20` [AI-augmented actor compromises 600+ FortiGate devices](2026-02-20-fortigate-600-devices-compromised.md)<br>  <sub>AI-augmented actor compromises 600+ FortiGate devices</sub>
- `2026-02-25` [Nine Mexican government agencies breached](2026-02-25-mexico-nine-agencies-breached.md)<br>  <sub>Nine Mexican government agencies breached</sub>
- `2026-02-10` [15,200 OpenClaw control panels exposed](2026-02-10-openclaw-kong-zhi-mian-ban.md)<br>  <sub>15,200 OpenClaw control panels exposed</sub>
- `2026-02-25` [OpenClaw ClawJacked (CVE-2026-25253)](2026-02-25-openclaw-clawjacked.md)<br>  <sub>OpenClaw ClawJacked (CVE-2026-25253)</sub>

---

[← 2026-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-02/2026-02-28-codewall-breaches-mckinsey-lilli.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
