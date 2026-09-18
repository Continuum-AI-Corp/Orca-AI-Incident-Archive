---
id: 2026-07-30-rufroot-man-fen-zhao-huan
title: "RufRoot (CVE-2026-59726): perfect CVSS, summons a rogue AI swarm"
title_zh: "RufRoot（CVE-2026-59726）：CVSS 满分，可召唤流氓 AI 蜂群"
title_ja: "RufRoot（CVE-2026-59726）：満点CVSS、悪性AI群集を召喚"
title_ko: "RufRoot (CVE-2026-59726): 완벽한 CVSS, 악성 AI 군집을 소환하다"
title_de: "RufRoot (CVE-2026-59726): perfekter CVSS, beschwört einen bösartigen KI-Schwarm"
title_fr: "RufRoot (CVE-2026-59726) : un CVSS parfait, qui invoque un essaim d'IA rogue"
title_es: "RufRoot (CVE-2026-59726): CVSS perfecto, invoca un enjambre de IA descontrolado"
date: 2026-07-30
date_precision: day
date_raw: "2026-07-30"

kind: vulnerability
type: [MCP, INFRA]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Named by Noma Security, **CVSS 10.0**, affecting all Ruflo versions < 3.16.3. **The default docker-compose deployment exposes the MCP bridge's `POST /mcp` and `POST /mcp/:group` endpoints without authentication** — an unauthenticated network attacker can call `terminal_execute` directly via `tools/call`, get a shell as `node` inside the bridge container, read provider API keys, **summon an agent swarm with the victim's keys**, and **inject poisoning patterns into the AgentDB learning store, tampering with the AI output of every user**


summary_zh: |
  Noma Security 命名，**CVSS 10.0**，影响 Ruflo < 3.16.3 全部版本。**默认 docker-compose 部署把 MCP bridge 的 `POST /mcp` 与 `POST /mcp/:group` 端点无认证暴露** —— 未认证的网络攻击者直接 `tools/call` 调 `terminal_execute`，在 bridge 容器内以 `node` 身份拿 shell、读取提供方 API key、**用受害者的密钥召唤 agent 蜂群**，并**向 AgentDB 学习库注入投毒模式，从而篡改所有用户的 AI 输出**

summary_ja: |
  Noma Securityが命名、**CVSS 10.0**、Rufloの3.16.3未満のすべてのバージョンが対象。**デフォルトのdocker-composeデプロイはMCPブリッジの`POST /mcp`と`POST /mcp/:group`エンドポイントを認証なしで公開している**——未認証のネットワーク攻撃者が`tools/call`経由で`terminal_execute`を直接呼び出し、ブリッジコンテナ内で`node`としてシェルを取得、プロバイダーのAPIキーを読み取り、**被害者のキーでエージェント群集を召喚**し、**AgentDB学習ストアにポイズニングパターンを注入して全ユーザーのAI出力を改ざんできる**

summary_ko: |
  Noma Security가 명명했고 **CVSS 10.0**이며 Ruflo 3.16.3 미만 모든 버전이 영향받는다. **기본 docker-compose 배포가 MCP 브리지의 `POST /mcp`와 `POST /mcp/:group` 엔드포인트를 인증 없이 노출한다** — 무인증 네트워크 공격자가 `tools/call`로 `terminal_execute`를 직접 호출해 브리지 컨테이너 안에서 `node` 셸을 얻고, 제공자 API 키를 읽고, **피해자의 키로 에이전트 군집을 소환**하며, **AgentDB 학습 저장소에 오염 패턴을 주입해 모든 사용자의 AI 출력을 변조**할 수 있다

summary_de: |
  Benannt von Noma Security, **CVSS 10.0**, betrifft alle Ruflo-Versionen < 3.16.3. **Die standardmäßige docker-compose-Bereitstellung exponiert die Endpunkte `POST /mcp` und `POST /mcp/:group` der MCP-Bridge ohne Authentifizierung** — ein nicht authentifizierter Angreifer im Netzwerk kann `terminal_execute` direkt über `tools/call` aufrufen, eine Shell als `node` im Bridge-Container erlangen, Anbieter-API-Schlüssel lesen, **mit den Schlüsseln des Opfers einen Agentenschwarm beschwören** und **Vergiftungsmuster in den Lernspeicher AgentDB einspeisen, wodurch die KI-Ausgabe jedes Nutzers manipuliert wird**

summary_fr: |
  Nommé par Noma Security, **CVSS 10.0**, affecte toutes les versions de Ruflo < 3.16.3. **Le déploiement docker-compose par défaut expose les points de terminaison `POST /mcp` et `POST /mcp/:group` du pont MCP sans authentification** — un attaquant réseau non authentifié peut appeler `terminal_execute` directement via `tools/call`, obtenir un shell en `node` dans le conteneur du pont, lire les clés API du fournisseur, **invoquer un essaim d'agents avec les clés de la victime** et **injecter des motifs d'empoisonnement dans le magasin d'apprentissage AgentDB, altérant la sortie IA de tous les utilisateurs**

summary_es: |
  Nombrado por Noma Security, **CVSS 10.0**, afecta a todas las versiones de Ruflo < 3.16.3. **El despliegue predeterminado con docker-compose expone los endpoints `POST /mcp` y `POST /mcp/:group` del puente MCP sin autenticación** — un atacante de red no autenticado puede llamar directamente a `terminal_execute` mediante `tools/call`, obtener un shell como `node` dentro del contenedor del puente, leer las claves de API del proveedor, **invocar un enjambre de agentes con las claves de la víctima** e **inyectar patrones de envenenamiento en el almacén de aprendizaje AgentDB, manipulando la salida de IA de todos los usuarios**

sources:
  - url: https://thehackernews.com/2026/07/ruflo-mcp-flaw-lets-unauthenticated.html
    label: THN
  - url: https://www.securityweek.com/critical-ruflo-flaw-lets-attackers-spawn-rogue-ai-swarms/amp/
    label: SecurityWeek

disputed: false
landmark: true
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# RufRoot (CVE-2026-59726): perfect CVSS, summons a rogue AI swarm

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

Named by Noma Security, **CVSS 10.0**, affecting all Ruflo versions < 3.16.3. **The default docker-compose deployment exposes the MCP bridge's `POST /mcp` and `POST /mcp/:group` endpoints without authentication** — an unauthenticated network attacker can call `terminal_execute` directly via `tools/call`, get a shell as `node` inside the bridge container, read provider API keys, **summon an agent swarm with the victim's keys**, and **inject poisoning patterns into the AgentDB learning store, tampering with the AI output of every user**

## Attack chain

```mermaid
flowchart LR
    E["Malicious MCP server or tool description"]:::entry
    S0["The agent toolchain loads and trusts it"]:::step
    S1["Unauthenticated access"]:::step
    I["RCE / data leak<br/><i>(flaw disclosed, no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | THN | <https://thehackernews.com/2026/07/ruflo-mcp-flaw-lets-unauthenticated.html> |
| 2 | SecurityWeek | <https://www.securityweek.com/critical-ruflo-flaw-lets-attackers-spawn-rogue-ai-swarms/amp/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-30` (raw: 2026-07-30, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain · [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-07-30-rufroot-man-fen-zhao-huan` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md) · [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-07-01` [AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)](2026-07-01-aws-kiro-rce.md)<br>  <sub>AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)</sub>
- `2026-07-27` [JFrog patches nine Artifactory CVEs](2026-07-27-jfrog-artifactory-fa-bu-jiu.md)<br>  <sub>JFrog patches nine Artifactory CVEs</sub>
- `2026-08-06` [Unauthenticated Langflow RCE added to CISA KEV](../2026-08/2026-08-06-langflow-rce-cisa-kev.md)<br>  <sub>Unauthenticated Langflow RCE added to CISA KEV</sub>
- `2026-06-08` [LiteLLM CVE-2026-42271 MCP endpoint takeover](../2026-06/2026-06-08-litellm-mcp-duan-dian-jie.md)<br>  <sub>LiteLLM CVE-2026-42271 MCP endpoint takeover</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-30-rufroot-man-fen-zhao-huan.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
