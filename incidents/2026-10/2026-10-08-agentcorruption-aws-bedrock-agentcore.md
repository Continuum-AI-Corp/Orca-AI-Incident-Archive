---
id: 2026-10-08-agentcorruption-aws-bedrock-agentcore
title: "AgentCorruption: one prompt turns an AWS Bedrock AgentCore agent into an account-wide takeover"
title_zh: "AgentCorruption：一句 prompt 把 AWS Bedrock AgentCore agent 变成账户级接管"
title_ja: "AgentCorruption：一つのプロンプトでAWS Bedrock AgentCoreエージェントがアカウント全体の乗っ取りに"
title_ko: "AgentCorruption: 프롬프트 하나로 AWS Bedrock AgentCore 에이전트가 계정 전체 탈취로"
title_de: "AgentCorruption: Ein Prompt macht aus einem AWS-Bedrock-AgentCore-Agenten eine kontoweite Übernahme"
title_fr: "AgentCorruption : un seul prompt transforme un agent AWS Bedrock AgentCore en prise de contrôle à l'échelle du compte"
title_es: "AgentCorruption: un solo prompt convierte a un agente de AWS Bedrock AgentCore en una toma de control de toda la cuenta"
date: 2026-10-08
date_raw: "2026-10-08 (Zenity Labs / SecTor 2026 disclosure; underlying IMDS issue reported to AWS 2025-12-25)"
date_precision: day

kind: vulnerability
type: [INFRA, EXFIL]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **Zenity Labs disclosed **AgentCorruption** on 8 October 2026 (at SecTor 2026, Toronto): a single natural-language prompt to a public-facing **Amazon Bedrock AgentCore** agent — one equipped with a common outbound-web tool — makes it call the **IMDS metadata endpoint** and hand over its own cloud credentials, which, because the default AgentCore execution IAM role is far broader than any one agent, reach **every AgentCore agent in the same AWS account and region**.** With those credentials Zenity's researchers could read other agents' **private conversations and long-term memories**, pull their **source code and container images**, retrieve **credentials stored in Secrets Manager**, and **plant malicious "memories"** that silently redirect an agent's future conversations to an attacker-controlled destination. The root cause is the combination of an agent's ability to make HTTP requests, IMDS-reachable metadata credentials, and an over-privileged default execution role. **No CVE was assigned.** AWS characterises the behaviour as documented and expected (and points to customer-side permission scoping), but has since made **IMDSv2 the default** for newly-deployed agents and **narrowed the default execution role**. Research demonstration, no in-the-wild exploitation. Recorded `vulnerability` / `INFRA` + `EXFIL` / `high` / `real_harm: false`.

summary_zh: |
  **Zenity Labs 于 2026 年 10 月 8 日（SecTor 2026，多伦多）公开 **AgentCorruption**：向一个面向公网的 **Amazon Bedrock AgentCore** agent（带有常见的可外联工具）发出**一句自然语言 prompt**，即可令其访问 **IMDS 元数据端点**、交出自身云凭证；而由于 AgentCore 的默认执行 IAM 角色远宽于单个 agent，这些凭证可触达**同一 AWS 账户、同一区域内的每一个 AgentCore agent**。** 凭这些凭证，Zenity 研究者得以读取其它 agent 的**私密对话与长期记忆**、拉取其**源代码与容器镜像**、取出 **Secrets Manager 中存储的凭证**，并**植入恶意"记忆"**，悄悄把某个 agent 之后的对话改向攻击者控制的目标。根因是三者叠加：agent 能发 HTTP 请求、IMDS 可达的元数据凭证、以及过宽的默认执行角色。**未分配 CVE。** AWS 将该行为定性为"已记录、预期之内"（并指向由客户侧收窄权限），但此后已将新部署 agent 的 **IMDSv2 设为默认**、并**收窄了默认执行角色**。研究演示，无在野利用。记为 `vulnerability` / `INFRA` + `EXFIL` / `high` / `real_harm: false`。

summary_ja: |
  **Zenity Labsは2026年10月8日（SecTor 2026、トロント）に **AgentCorruption** を公表した：公開された **Amazon Bedrock AgentCore** エージェント（一般的な外部リクエスト用ツールを備えたもの）への**一つの自然言語プロンプト**で、**IMDSメタデータエンドポイント**にアクセスさせ自身のクラウド認証情報を引き渡させることができ、AgentCoreの既定実行IAMロールが単一エージェントよりはるかに広いため、その認証情報は**同一AWSアカウント・同一リージョン内のすべてのAgentCoreエージェント**に届く。** これによりZenityの研究者は、他エージェントの**非公開の会話と長期記憶**を読み、**ソースコードとコンテナイメージ**を取得し、**Secrets Managerに保存された認証情報**を取り出し、さらに将来の会話を攻撃者の宛先へ密かに転送する**悪意ある「記憶」を植え付ける**ことができた。根本原因は、エージェントのHTTPリクエスト能力、IMDS到達可能なメタデータ認証情報、過剰な既定実行ロールの組み合わせである。**CVEは割り当てられていない。** AWSはこの挙動を文書化済みで想定内と位置づける（権限の絞り込みは顧客側の責任とする）一方、以降は新規デプロイのエージェントで **IMDSv2を既定** にし、**既定実行ロールを縮小** した。研究実証であり実環境での悪用はない。`vulnerability` / `INFRA` + `EXFIL` / `high` / `real_harm: false`

summary_ko: |
  **Zenity Labs는 2026년 10월 8일(SecTor 2026, 토론토)에 **AgentCorruption**을 공개했다: 공개된 **Amazon Bedrock AgentCore** 에이전트(일반적인 외부 요청 도구를 갖춘)에 보낸 **자연어 프롬프트 하나**로 **IMDS 메타데이터 엔드포인트**에 접근시켜 자신의 클라우드 자격 증명을 넘기게 할 수 있으며, AgentCore의 기본 실행 IAM 역할이 단일 에이전트보다 훨씬 넓기 때문에 그 자격 증명은 **동일 AWS 계정·동일 리전의 모든 AgentCore 에이전트**에 도달한다.** 이 자격 증명으로 Zenity 연구진은 다른 에이전트의 **비공개 대화와 장기 기억**을 읽고, **소스 코드와 컨테이너 이미지**를 가져오고, **Secrets Manager에 저장된 자격 증명**을 꺼내며, 향후 대화를 공격자 목적지로 몰래 돌리는 **악성 "기억"을 심을** 수 있었다. 근본 원인은 에이전트의 HTTP 요청 능력, IMDS로 도달 가능한 메타데이터 자격 증명, 과도한 기본 실행 역할의 조합이다. **CVE는 할당되지 않았다.** AWS는 이 동작을 문서화된 예상 범위로 규정하며(권한 축소는 고객 측 책임) 이후 신규 배포 에이전트에 **IMDSv2를 기본값**으로 하고 **기본 실행 역할을 축소**했다. 연구 실증이며 실제 악용은 없다. `vulnerability` / `INFRA` + `EXFIL` / `high` / `real_harm: false`

summary_de: |
  **Zenity Labs veröffentlichte am 8. Oktober 2026 (auf der SecTor 2026 in Toronto) **AgentCorruption**: Ein einziger natürlichsprachlicher Prompt an einen öffentlich erreichbaren **Amazon-Bedrock-AgentCore**-Agenten — ausgestattet mit einem gängigen Werkzeug für ausgehende Web-Anfragen — bringt ihn dazu, den **IMDS-Metadaten-Endpunkt** aufzurufen und seine eigenen Cloud-Anmeldedaten preiszugeben; weil die Standard-Ausführungs-IAM-Rolle von AgentCore weit über einen einzelnen Agenten hinausreicht, erreichen diese Anmeldedaten **jeden AgentCore-Agenten im selben AWS-Konto und derselben Region**.** Mit diesen Anmeldedaten konnten Zenitys Forscher die **privaten Konversationen und Langzeiterinnerungen** anderer Agenten lesen, deren **Quellcode und Container-Images** abziehen, in **Secrets Manager gespeicherte Anmeldedaten** abrufen und **bösartige „Erinnerungen" einpflanzen**, die künftige Konversationen eines Agenten unbemerkt zu einem vom Angreifer kontrollierten Ziel umleiten. Ursache ist das Zusammenspiel aus der Fähigkeit eines Agenten, HTTP-Anfragen zu stellen, IMDS-erreichbaren Metadaten-Anmeldedaten und einer überprivilegierten Standard-Ausführungsrolle. **Es wurde kein CVE vergeben.** AWS stuft das Verhalten als dokumentiert und erwartet ein (und verweist auf kundenseitige Rechtebeschränkung), hat seither aber **IMDSv2 zum Standard** für neu bereitgestellte Agenten gemacht und die **Standard-Ausführungsrolle verengt**. Forschungsdemonstration, keine Ausnutzung in freier Wildbahn. `vulnerability` / `INFRA` + `EXFIL` / `high` / `real_harm: false`

summary_fr: |
  **Zenity Labs a divulgué **AgentCorruption** le 8 octobre 2026 (à la SecTor 2026, Toronto) : un seul prompt en langage naturel adressé à un agent **Amazon Bedrock AgentCore** exposé sur Internet — doté d'un outil courant de requêtes web sortantes — le pousse à appeler le **point de terminaison de métadonnées IMDS** et à livrer ses propres identifiants cloud ; comme le rôle IAM d'exécution par défaut d'AgentCore est bien plus large qu'un seul agent, ces identifiants atteignent **tous les agents AgentCore du même compte AWS et de la même région**.** Avec ces identifiants, les chercheurs de Zenity ont pu lire les **conversations privées et les mémoires à long terme** d'autres agents, extraire leur **code source et leurs images de conteneur**, récupérer les **identifiants stockés dans Secrets Manager** et **implanter des « mémoires » malveillantes** qui redirigent discrètement les futures conversations d'un agent vers une destination contrôlée par l'attaquant. La cause profonde est la combinaison de la capacité d'un agent à émettre des requêtes HTTP, d'identifiants de métadonnées accessibles via IMDS et d'un rôle d'exécution par défaut surprivilégié. **Aucun CVE n'a été attribué.** AWS qualifie ce comportement de documenté et attendu (et renvoie au cadrage des permissions côté client), mais a depuis fait d'**IMDSv2 la valeur par défaut** pour les agents nouvellement déployés et **restreint le rôle d'exécution par défaut**. Démonstration de recherche, aucune exploitation dans la nature. `vulnerability` / `INFRA` + `EXFIL` / `high` / `real_harm: false`

summary_es: |
  **Zenity Labs divulgó **AgentCorruption** el 8 de octubre de 2026 (en SecTor 2026, Toronto): un solo prompt en lenguaje natural a un agente de **Amazon Bedrock AgentCore** expuesto a Internet —uno equipado con una herramienta común de peticiones web salientes— lo lleva a llamar al **endpoint de metadatos IMDS** y a entregar sus propias credenciales de nube que, como el rol IAM de ejecución por defecto de AgentCore es mucho más amplio que un solo agente, alcanzan a **todos los agentes de AgentCore de la misma cuenta y región de AWS**.** Con esas credenciales, los investigadores de Zenity pudieron leer las **conversaciones privadas y las memorias a largo plazo** de otros agentes, extraer su **código fuente e imágenes de contenedor**, recuperar **credenciales almacenadas en Secrets Manager** e **implantar "memorias" maliciosas** que redirigen de forma silenciosa las conversaciones futuras de un agente a un destino controlado por el atacante. La causa raíz es la combinación de la capacidad de un agente para hacer peticiones HTTP, credenciales de metadatos accesibles por IMDS y un rol de ejecución por defecto con privilegios excesivos. **No se asignó ningún CVE.** AWS califica el comportamiento como documentado y esperado (y remite al ajuste de permisos del lado del cliente), pero desde entonces ha hecho de **IMDSv2 el valor por defecto** para los agentes recién desplegados y ha **estrechado el rol de ejecución por defecto**. Demostración de investigación, sin explotación en la naturaleza. `vulnerability` / `INFRA` + `EXFIL` / `high` / `real_harm: false`

sources:
  - url: https://zenity.io/press-release/zenity-labs-discloses-agentcorruption-a-chain-of-aws-agentcore-flaws
    label: Zenity Labs (discoverer)
  - url: https://darkreading.com/cloud-security/agentcorruption-aws-environments-at-risk-single-prompt
    label: Dark Reading
  - url: https://thenextweb.com/news/aws-agentcore-zenity-agentcorruption-one-prompt-agents
    label: The Next Web
disputed: false
landmark: false
scan_month: 2026-10
scan_ref: "SCAN.md §13.28"
---

# AgentCorruption: one prompt turns an AWS Bedrock AgentCore agent into an account-wide takeover

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-8F6A3C?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-3C6E8F?style=flat-square)

## Summary

**Zenity Labs disclosed AgentCorruption on 8 October 2026 (at SecTor 2026, Toronto): a single natural-language prompt to a public-facing Amazon Bedrock AgentCore agent — one equipped with a common outbound-web tool — makes it call the IMDS metadata endpoint and hand over its own cloud credentials, which, because the default AgentCore execution IAM role is far broader than any one agent, reach every AgentCore agent in the same AWS account and region.** With those credentials Zenity's researchers could read other agents' private conversations and long-term memories, pull their source code and container images, retrieve credentials stored in Secrets Manager, and plant malicious "memories" that silently redirect an agent's future conversations to an attacker-controlled destination. The root cause is the combination of an agent's ability to make HTTP requests, IMDS-reachable metadata credentials, and an over-privileged default execution role. **No CVE was assigned.** AWS characterises the behaviour as documented and expected (and points to customer-side permission scoping), but has since made IMDSv2 the default for newly-deployed agents and narrowed the default execution role. Research demonstration, no in-the-wild exploitation. Recorded `vulnerability` / `INFRA` + `EXFIL` / `high` / `real_harm: false`.

## Attack chain

```mermaid
flowchart LR
    E["One prompt to a public-facing AgentCore<br/>agent with an outbound-web tool"]:::entry
    S1["Agent calls the IMDS metadata endpoint<br/>→ surrenders its cloud credentials"]:::step
    S2["Over-broad default execution IAM role →<br/>reach every AgentCore agent in account+region"]:::step
    I["Read private chats & memories, pull source<br/>& images, steal Secrets Manager creds,<br/>plant malicious memories"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The technique.** Zenity Labs presented AgentCorruption at SecTor 2026 (Toronto) and published it on 8 October 2026 as a multi-part research series. The chain starts when an attacker sends a plain-language prompt to a **public-facing Amazon Bedrock AgentCore agent** that has a commonly-used tool capable of making outbound HTTP requests. The prompt instructs the agent to reach the **AWS Instance Metadata Service (IMDS)**, which returns the credentials of the agent's execution role. Because AgentCore's **default execution IAM role is scoped to far more than one agent**, those credentials give access to **every AgentCore agent in the same account and region** — not just the one that was prompted.

**What the credentials unlock.** With the harvested role, Zenity's researchers could read other agents' **private conversations and long-term memories**, copy their **source code and container images**, and retrieve **secrets held in AWS Secrets Manager**. They also **implanted malicious long-term "memories"** into agents they were not authorised to use, so that an agent's *future* conversations would be steered toward an attacker-controlled destination — a persistent, stealthy foothold rather than a one-shot read.

**Disclosure and AWS's position.** Zenity reported the underlying IMDS-access issue to AWS on **25 December 2025**; AWS responded and closed that report as *informative*, taking the position that the behaviour is **documented and expected** and that customers should grant execution roles only the permissions their agents need. The public disclosure (AgentCorruption) followed on **8 October 2026**. AWS has since **made IMDSv2 the default** for newly-deployed AgentCore agents and **reduced the default execution role's permissions** (removing the ability to invoke other agents, read private conversations and reach Secrets Manager, and narrowing others).

**How it is graded.** Recorded `vulnerability` — a disclosed flaw chain demonstrated by researchers, not a used-in-anger incident. `INFRA` (the agent runtime/cloud platform, AgentCore, and its IAM/IMDS posture) and `EXFIL` (private conversations, source code, container images and Secrets Manager credentials leave the victim agents). `real_harm: false`: a controlled research demonstration with no known in-the-wild exploitation and vendor mitigations already shipped. Severity `high` rather than `critical`: account-wide reach is severe, but it is partly configuration-dependent (a public-facing agent with an outbound tool and the broad default role) and there is no confirmed victim. It is **not** marked `disputed`: AWS and Zenity disagree only on whether the behaviour counts as a *product vulnerability* versus *expected behaviour*, not on whether the attack works. Confidence `A`: Zenity's detailed first-party disclosure plus independent reporting (Dark Reading, The Next Web).

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Zenity Labs — AgentCorruption (discoverer) | <https://zenity.io/press-release/zenity-labs-discloses-agentcorruption-a-chain-of-aws-agentcore-flaws> |
| 2 | Dark Reading | <https://darkreading.com/cloud-security/agentcorruption-aws-environments-at-risk-single-prompt> |
| 3 | The Next Web | <https://thenextweb.com/news/aws-agentcore-zenity-agentcorruption-one-prompt-agents> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-10-08` (raw: 2026-10-08 Zenity Labs / SecTor 2026 disclosure; underlying IMDS issue reported to AWS 2025-12-25, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) [`EXFIL`](../../taxonomy/types.md#exfil) |
| Severity | **High** `high` |
| Confidence | **A** — Zenity Labs disclosure (discoverer) + independent reporting |
| Real harm | No — research demonstration; no known in-the-wild exploitation; AWS mitigations shipped |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-10-08-agentcorruption-aws-bedrock-agentcore` |

<sub>**Why this classification:** A researcher-disclosed flaw chain in Amazon Bedrock AgentCore (`INFRA` — agent runtime/cloud platform and its IAM/IMDS posture; `EXFIL` — conversations, source, images and secrets leave the victim agents). `vulnerability`, not an incident. `real_harm: false` — controlled demonstration, no known exploitation, AWS mitigations shipped. `high` not `critical`: account-wide reach is severe but partly configuration-dependent and with no confirmed victim. Not `disputed` — AWS and Zenity disagree on labelling (product vulnerability vs expected behaviour), not on whether the attack works. Dated to the Zenity/SecTor disclosure (8 October 2026). Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure (INFRA)](../../topics/agent-infra.md)

**Related records:**

- `2026-10-02` [GitLab Duo AI Gateway prompt-template sandbox escape (CVE-2026-90970)](2026-10-02-gitlab-duo-ai-gateway-rce.md)<br>  <sub>Another agent-infrastructure flaw disclosed the same month</sub>
- `2026-09-09` [Noma: workflow-identity hijacking in agent platforms](../2026-09/2026-09-09-noma-workflow-identity-hijacking.md)<br>  <sub>Over-broad agent identities turned into lateral movement</sub>
- `2026-09-14` [Bifrost AI gateway (CVE-2026-90898)](../2026-09/2026-09-14-bifrost-ai-gateway-cve-2026-90898.md)<br>  <sub>Another AI-gateway infrastructure weakness</sub>

---

[← 2026-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-10/2026-10-08-agentcorruption-aws-bedrock-agentcore.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
