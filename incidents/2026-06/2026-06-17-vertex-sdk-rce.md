---
id: 2026-06-17-vertex-sdk-rce
title: "Vertex AI SDK bucket takeover leads to cross-tenant RCE"
title_zh: "Vertex AI SDK 存储桶抢占 → 跨租户 RCE"
title_ja: "Vertex AI SDKのバケット乗っ取りがテナント間RCEに至る"
title_ko: "Vertex AI SDK 버킷 장악으로 교차 테넌트 RCE"
title_de: "Vertex AI SDK: Bucket-Übernahme führt zu mandantenübergreifender RCE"
title_fr: "La prise de contrôle d'un bucket du SDK Vertex AI mène à un RCE entre locataires"
title_es: "La toma de control de un bucket del SDK de Vertex AI lleva a RCE entre inquilinos"
date: 2026-06-17
date_precision: day
date_raw: "2026-06-17"

kind: research
type: [INFRA]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Unit 42: when no bucket name is specified, SDK v1.139.0/1.140.0 derives the name from the project ID + region, **checking existence but not validating ownership**. An attacker who creates a bucket with the same name first and opens it for read/write to any authenticated identity can receive the victim's uploaded models; by swapping them within a race window of about **2.5 seconds** (a Cloud Function responds in about 800ms, and in practice the swap completed about 1 second before the read), pickle deserialization gives RCE. Google fixed it in two stages: v1.144.0 added a uuid4, v1.148.0 added an ownership check


summary_zh: |
  Unit 42：SDK v1.139.0/1.140.0 未指定桶名时按项目 ID + 区域推导名字，**存在性检查但不校验所有者**。攻击者抢先建同名桶并对任意认证身份开放读写，即可接收受害者上传的模型；在约 **2.5 秒**竞争窗口内替换（Cloud Function 约 800ms 响应，实证在读取前约 1 秒完成替换），pickle 反序列化即 RCE。Google 两阶段修复：v1.144.0 加 uuid4、v1.148.0 加所有者校验

summary_ja: |
  Unit 42：バケット名を指定しない場合、SDK v1.139.0/1.140.0はプロジェクトID＋リージョンから名前を導出し、**存在確認はするが所有権を検証しない**。同じ名前のバケットを先に作成し、任意の認証済みIDに読み書きを開放した攻撃者は、被害者がアップロードしたモデルを受け取れてしまう。約**2.5秒**の競合ウィンドウ内で差し替えると（Cloud Functionは約800msで応答し、実際には読み取りの約1秒前に差し替えが完了した）、pickleのデシリアライズでRCEに至る。Googleは2段階で修正：v1.144.0でuuid4を追加、v1.148.0で所有権チェックを追加

summary_ko: |
  Unit 42: 버킷 이름을 지정하지 않으면 SDK v1.139.0/1.140.0이 프로젝트 ID + 리전으로 이름을 유도하는데, **존재 여부는 확인하지만 소유권은 검증하지 않는다**. 같은 이름의 버킷을 먼저 만들어 어떤 인증된 신원이든 읽기/쓰기로 개방한 공격자는 피해자가 업로드한 모델을 받을 수 있고, 약 **2.5초**의 경쟁 창 안에서 바꿔치기하면(Cloud Function은 약 800ms에 응답하며 실제로는 읽기 약 1초 전에 교체가 완료되었다) pickle 역직렬화로 RCE가 가능하다. 구글은 두 단계로 수정했다: v1.144.0에서 uuid4 추가, v1.148.0에서 소유권 검사 추가

summary_de: |
  Unit 42: Wenn kein Bucket-Name angegeben wird, leitet das SDK v1.139.0/1.140.0 den Namen aus Projekt-ID + Region ab und **prüft dessen Existenz, aber nicht die Eigentümerschaft**. Ein Angreifer, der zuerst einen Bucket mit demselben Namen anlegt und ihn für jede authentifizierte Identität zum Lesen/Schreiben öffnet, kann die vom Opfer hochgeladenen Modelle empfangen; tauscht er sie innerhalb eines Race-Fensters von etwa **2.5 Sekunden** aus (eine Cloud Function antwortet in etwa 800ms, und in der Praxis war der Austausch etwa 1 Sekunde vor dem Lesen abgeschlossen), liefert die Pickle-Deserialisierung RCE. Google behob es in zwei Stufen: v1.144.0 fügte eine uuid4 hinzu, v1.148.0 eine Eigentümerprüfung

summary_fr: |
  Unit 42 : quand aucun nom de bucket n'est spécifié, le SDK v1.139.0/1.140.0 le dérive de l'ID de projet + de la région, **vérifiant l'existence mais pas la propriété**. Un attaquant qui crée d'abord un bucket du même nom et l'ouvre en lecture/écriture à toute identité authentifiée peut recevoir les modèles téléversés par la victime ; en les substituant dans une fenêtre de course d'environ **2,5 secondes** (une Cloud Function répond en environ 800 ms, et en pratique la substitution s'est achevée environ 1 seconde avant la lecture), la désérialisation pickle donne un RCE. Google a corrigé en deux étapes : v1.144.0 a ajouté un uuid4, v1.148.0 a ajouté une vérification de propriété

summary_es: |
  Unit 42: cuando no se especifica un nombre de bucket, el SDK v1.139.0/1.140.0 deriva el nombre del ID del proyecto más la región, **comprobando su existencia pero no validando la propiedad**. Un atacante que cree primero un bucket con el mismo nombre y lo abra para lectura/escritura a cualquier identidad autenticada puede recibir los modelos que sube la víctima; al intercambiarlos dentro de una ventana de carrera de unos **2.5 segundos** (una Cloud Function responde en unos 800 ms, y en la práctica el intercambio se completó alrededor de 1 segundo antes de la lectura), la deserialización de pickle da RCE. Google lo corrigió en dos etapas: la v1.144.0 añadió un uuid4 y la v1.148.0 añadió una comprobación de propiedad

sources:
  - url: https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/
    label: Unit 42

disputed: false
landmark: false
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# Vertex AI SDK bucket takeover leads to cross-tenant RCE

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

Unit 42: when no bucket name is specified, SDK v1.139.0/1.140.0 derives the name from the project ID + region, **checking existence but not validating ownership**. An attacker who creates a bucket with the same name first and opens it for read/write to any authenticated identity can receive the victim's uploaded models; by swapping them within a race window of about **2.5 seconds** (a Cloud Function responds in about 800ms, and in practice the swap completed about 1 second before the read), pickle deserialization gives RCE. Google fixed it in two stages: v1.144.0 added a uuid4, v1.148.0 added an ownership check

## Attack chain

```mermaid
flowchart LR
    E["Agent infrastructure exposed to the internet"]:::entry
    S0["Unauthenticated access"]:::step
    I["RCE / data leak<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Unit 42 | <https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-17` (raw: 2026-06-17, precision `day`) |
| Kind | Research demo `research` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-17-vertex-sdk-rce` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-06-08` [LiteLLM CVE-2026-42271 MCP endpoint takeover](2026-06-08-litellm-mcp-duan-dian-jie.md)<br>  <sub>LiteLLM CVE-2026-42271 MCP endpoint takeover</sub>
- `2026-06-29` [DifyTap: four flaws leave 1M+ AI apps open to cross-tenant eavesdropping](2026-06-29-difytap-lou-dong-rang-wan.md)<br>  <sub>DifyTap: four flaws leave 1M+ AI apps open to cross-tenant eavesdropping</sub>
- `2026-06-28` [Langflow CVE-2026-33017 used for Monero mining](2026-06-28-langflow-yong-yu-men-luo.md)<br>  <sub>Langflow CVE-2026-33017 used for Monero mining</sub>
- `2026-06-18` [AutoJack: one web page from AutoGen Studio to the host](2026-06-18-autojack-autogen-studio.md)<br>  <sub>AutoJack: one web page from AutoGen Studio to the host</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-17-vertex-sdk-rce.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
