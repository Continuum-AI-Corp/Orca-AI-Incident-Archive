---
id: 2026-09-24-salesbleed-agentforce-zero-click-exfil
title: "SalesBleed: three Agentforce flaws turn a single web lead into zero-click CRM exfiltration and agent-impersonated phishing"
title_zh: "SalesBleed：三个 Agentforce 缺陷让一条网页线索变成零点击 CRM 外泄与 agent 冒充钓鱼"
title_ja: "SalesBleed：Agentforce の 3 件の欠陥が、1 件の Web リードをゼロクリックの CRM 持ち出しとエージェントなりすましフィッシングに変える"
title_ko: "SalesBleed: Agentforce 결함 3건이 웹 리드 하나를 제로클릭 CRM 유출과 에이전트 사칭 피싱으로 바꾼다"
title_de: "SalesBleed: Drei Agentforce-Schwachstellen machen aus einem Web-Lead Zero-Click-CRM-Abfluss und Phishing in Agenten-Identität"
title_fr: "SalesBleed : trois failles d'Agentforce transforment une simple piste web en exfiltration CRM zéro-clic et hameçonnage par usurpation d'agent"
title_es: "SalesBleed: tres fallos de Agentforce convierten un lead web en exfiltración CRM de clic cero y phishing suplantando al agente"
date: 2026-09-24
date_raw: "2026-09-24"
date_precision: day

kind: vulnerability
type: [IPI, EXFIL]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **Zenity Labs discloses "SalesBleed": three vulnerabilities in Salesforce Agentforce that let a single untrusted web-to-lead submission hijack a trusted enterprise agent.** Two of the flaws give **zero-click data exfiltration** — sensitive CRM data reaches attacker-controlled infrastructure *without an employee clicking or approving anything* — by abusing weaknesses in **Trusted URLs**, the Salesforce mechanism meant to stop Agentforce from rendering URLs and images from unapproved sources. The third weaponises the **trusted identity of the Agentforce-connected Slack agent** to push phishing to employees from inside the enterprise. Zenity reported the issues responsibly and *"Salesforce worked with the researchers to investigate and remediate"* them. CTO Michael Bargury: *"We found multiple ways to break through the security boundary designed to stop Agentforce from sending enterprise data to unapproved destinations… When those controls fail, we are left with a privileged access agent with high autonomy and no bounds."* Recorded `vulnerability` / `IPI` + `EXFIL` / `high` / `real_harm: false` — a significant capability demonstration on a widely deployed enterprise agent platform, with no evidence of in-the-wild use

summary_zh: |
  **Zenity Labs 披露「SalesBleed」：Salesforce Agentforce 中的三个漏洞，让一条不可信的 Web-to-lead 提交就能劫持一个受信任的企业 agent。** 其中两个缺陷造成**零点击数据外泄**——敏感 CRM 数据在**员工无需点击或批准任何东西**的情况下流向攻击者控制的设施，手法是滥用 **Trusted URLs**（Salesforce 用来阻止 Agentforce 渲染未批准来源的 URL 与图片的机制）中的弱点。第三个缺陷把 **Agentforce 已接入 Slack 的 agent 的受信任身份**武器化，从企业内部向员工推送钓鱼。Zenity 负责任地披露了该问题，*「Salesforce 与研究者合作调查并修复了」*这些缺陷。CTO Michael Bargury：*「我们找到了多种方式突破那道本用来阻止 Agentforce 把企业数据发往未批准目的地的边界……当这些控制失效，剩下的是一个拥有高权限、高度自主且没有边界的 agent。」* 本条记为 `vulnerability` / `IPI` + `EXFIL` / `high` / `real_harm: false`——在广泛部署的企业 agent 平台上的一次重要能力演示，无在野使用证据

summary_ja: |
  **Zenity Labsは「SalesBleed」を公表した。Salesforce Agentforceの3件の脆弱性により、信頼できないWeb-to-lead送信1件で、信頼された企業エージェントを乗っ取れる。** うち2件は**ゼロクリックのデータ持ち出し**を可能にする——従業員が何もクリックも承認もしなくても、機微なCRMデータが攻撃者の管理下にある基盤へ送られる——それは Agentforce が未承認ソースのURLや画像を描画しないようにするための仕組み **Trusted URLs** の弱点を悪用する。3件目は **Agentforce 連携 Slack エージェントの信頼されたアイデンティティ**を武器化し、企業内部から従業員へフィッシングを配信する。Zenityは責任ある開示を行い、*「Salesforceは研究者と協力して調査・是正した」*。CTOのMichael Bargury氏：*「Agentforceが企業データを未承認の送信先へ送るのを防ぐために設計された境界を突破する方法を、我々は複数見つけた……その制御が破綻すると、高い権限と自律性を持ち、境界のないagentだけが残る。」* 本件は `vulnerability` / `IPI` + `EXFIL` / `high` / `real_harm: false`

summary_ko: |
  **Zenity Labs는 "SalesBleed"를 공개했다: 신뢰할 수 없는 Web-to-lead 제출 하나로 신뢰받는 기업 에이전트를 장악할 수 있는 Salesforce Agentforce의 취약점 3건이다.** 이 중 2건은 **제로클릭 데이터 유출**을 가능하게 한다 — 직원이 아무것도 클릭하거나 승인하지 않아도 민감한 CRM 데이터가 공격자 통제 인프라로 전송된다 — 이는 Agentforce가 승인되지 않은 출처의 URL과 이미지를 렌더링하지 못하게 하는 **Trusted URLs** 메커니즘의 약점을 악용한다. 세 번째는 **Agentforce 연동 Slack 에이전트의 신뢰된 신원**을 무기화해 기업 내부에서 직원들에게 피싱을 유포한다. Zenity는 책임 있는 공개를 했고 *"Salesforce는 연구자와 협력해 조사하고 조치했다"*. CTO Michael Bargury: *"Agentforce가 기업 데이터를 승인되지 않은 목적지로 보내지 못하게 막으려 설계된 보안 경계를 뚫는 방법을 여러 개 찾았다… 그 제어가 실패하면 권한은 높고 자율적이며 경계 없는 agent만 남는다."* `vulnerability` / `IPI` + `EXFIL` / `high` / `real_harm: false`로 기록

summary_de: |
  **Zenity Labs legt "SalesBleed" offen: drei Schwachstellen in Salesforce Agentforce, mit denen eine einzige nicht vertrauenswürdige Web-to-Lead-Übermittlung einen vertrauenswürdigen Unternehmensagenten übernimmt.** Zwei der Schwachstellen ermöglichen **Zero-Click-Datenabfluss** — sensible CRM-Daten gelangen an vom Angreifer kontrollierte Infrastruktur, *ohne dass ein Mitarbeiter irgendetwas anklickt oder genehmigt* — indem Schwächen in **Trusted URLs** ausgenutzt werden, dem Salesforce-Mechanismus, der Agentforce daran hindern soll, URLs und Bilder aus nicht freigegebenen Quellen darzustellen. Die dritte missbraucht die **vertrauenswürdige Identität des angebundenen Slack-Agenten**, um Phishing aus dem Unternehmensinneren an Mitarbeiter zu verteilen. Zenity meldete die Fälle verantwortungsvoll; *„Salesforce arbeitete mit den Forschern zusammen, um sie zu untersuchen und zu beheben."* CTO Michael Bargury: *„Wir haben mehrere Wege gefunden, die Sicherheitsgrenze zu durchbrechen, die verhindern soll, dass Agentforce Unternehmensdaten an nicht freigegebene Ziele sendet … Wenn diese Kontrollen versagen, bleibt ein privilegierter Agent mit hoher Autonomie und ohne Grenzen."* Verzeichnet als `vulnerability` / `IPI` + `EXFIL` / `high` / `real_harm: false`

summary_fr: |
  **Zenity Labs divulgue « SalesBleed » : trois vulnérabilités de Salesforce Agentforce permettant à une simple soumission Web-to-lead non fiable de prendre le contrôle d'un agent d'entreprise de confiance.** Deux de ces failles offrent une **exfiltration de données zéro-clic** — des données CRM sensibles partent vers une infrastructure contrôlée par l'attaquant *sans qu'un employé clique ou approuve quoi que ce soit* — en abusant des faiblesses de **Trusted URLs**, le mécanisme censé empêcher Agentforce d'afficher des URL et des images de sources non approuvées. La troisième arme l'**identité de confiance de l'agent Agentforce connecté à Slack** pour diffuser du hameçonnage aux employés depuis l'intérieur de l'entreprise. Zenity a divulgué de façon responsable et *« Salesforce a travaillé avec les chercheurs pour investiguer et corriger »*. Le CTO Michael Bargury : *« Nous avons trouvé plusieurs façons de franchir la frontière de sécurité conçue pour empêcher Agentforce d'envoyer des données d'entreprise vers des destinations non approuvées… Quand ces contrôles échouent, il reste un agent privilégié, très autonome et sans limites. »* Enregistré `vulnerability` / `IPI` + `EXFIL` / `high` / `real_harm: false`

summary_es: |
  **Zenity Labs divulga "SalesBleed": tres vulnerabilidades de Salesforce Agentforce que permiten que un único envío Web-to-lead no confiable tome el control de un agente empresarial de confianza.** Dos de ellas permiten **exfiltración de datos de clic cero** — datos CRM sensibles llegan a infraestructura controlada por el atacante *sin que ningún empleado haga clic ni apruebe nada* — abusando de debilidades en **Trusted URLs**, el mecanismo destinado a impedir que Agentforce muestre URL e imágenes de fuentes no aprobadas. La tercera arma la **identidad de confianza del agente de Agentforce conectado a Slack** para distribuir phishing a los empleados desde dentro de la empresa. Zenity divulgó de forma responsable y *"Salesforce trabajó con los investigadores para investigar y corregir"*. El CTO Michael Bargury: *"Encontramos varias formas de romper la frontera de seguridad diseñada para impedir que Agentforce envíe datos empresariales a destinos no aprobados… Cuando esos controles fallan, queda un agente con acceso privilegiado, gran autonomía y sin límites."* Registrado `vulnerability` / `IPI` + `EXFIL` / `high` / `real_harm: false`

sources:
  - url: https://www.morningstar.com/news/business-wire/20260924811082/zenity-labs-uncovers-salesbleed-3-salesforce-agentforce-flaws-enabling-zero-click-crm-data-theft-and-ai-agent-impersonation
    label: Zenity Labs (Business Wire)
  - url: https://www.darkreading.com/application-security/salesbleed-exploits-salesforce-agents-slack-phishing
    label: Dark Reading
  - url: https://aviatrix.ai/threat-research-center/salesbleed-salesforce-agentforce-slack-phishing-2026/
    label: Aviatrix Threat Research

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §13.20"
---

# SalesBleed: three Agentforce flaws turn a single web lead into zero-click CRM exfiltration and agent-impersonated phishing

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-8F6A3C?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-3C6E8F?style=flat-square)

## Summary

**Zenity Labs discloses "SalesBleed": three vulnerabilities in Salesforce Agentforce that let a single untrusted web-to-lead submission hijack a trusted enterprise agent.** Two of the flaws give **zero-click data exfiltration** — sensitive CRM data reaches attacker-controlled infrastructure *without an employee clicking or approving anything* — by abusing weaknesses in **Trusted URLs**, the Salesforce mechanism meant to stop Agentforce from rendering URLs and images from unapproved sources. The third weaponises the **trusted identity of the Agentforce-connected Slack agent** to push phishing to employees from inside the enterprise. Zenity reported the issues responsibly and *"Salesforce worked with the researchers to investigate and remediate"* them. CTO Michael Bargury: *"We found multiple ways to break through the security boundary designed to stop Agentforce from sending enterprise data to unapproved destinations… When those controls fail, we are left with a privileged access agent with high autonomy and no bounds."* Recorded `vulnerability` / `IPI` + `EXFIL` / `high` / `real_harm: false` — a significant capability demonstration on a widely deployed enterprise agent platform, with no evidence of in-the-wild use.

## Attack chain

```mermaid
flowchart LR
    E["Attacker submits an untrusted<br/>Web-to-lead form"]:::entry
    S1["Agentforce processes the lead;<br/>injected instructions ride along as content"]:::step
    S2["Trusted-URL boundary bypassed —<br/>data rendered to an attacker destination"]:::step
    I["Zero-click CRM exfiltration; plus phishing<br/>sent through the trusted Slack agent identity"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The disclosure.** Zenity Labs announced SalesBleed on 24 September 2026: *"a set of three security vulnerabilities in Salesforce Agentforce that could allow a single untrusted lead to hijack trusted Agentforce agents, silently exfiltrate sensitive CRM data and turn an enterprise agent into a vehicle for delivering elaborate phishing attacks."* Two of the three enable zero-click exfiltration; the third *"allows attackers to weaponize the trusted identity of an Agentforce-connected Slack agent to distribute phishing messages to employees from inside the enterprise."* The technical root is in **Trusted URLs** — the control Salesforce provides precisely to stop agents from calling out to unapproved destinations — where the researchers *"found multiple weaknesses … that could be abused to send sensitive data to unapproved destinations."* Zenity describes those weaknesses concretely — *"including top-level domains the mechanism failed to recognize and character sequences that interfered with how URLs were parsed"* — and shows that they let injected instructions make Agentforce query Salesforce records and embed what it retrieved in image requests to an attacker-controlled server: *"the image requests automatically transmit the embedded CRM data, with no click or additional action from the employee."* In the demonstrated case Agentforce reported the content as blocked by the organisation's policies *after* the data had already been transmitted.

**Why the entry point matters.** The entire chain starts from a form anyone on the internet can fill in. That is the indirect-prompt-injection pattern in its purest enterprise form: the attacker never touches an employee, never sends an email, never needs a credential. The lead is *content*, the agent is the *interpreter*, and the agent's own permissions are the *payload delivery mechanism* — which is what makes the second-order step possible: phishing that arrives through the Slack identity employees already trust, not through a look-alike domain.

**Vendor response and grading.** Zenity disclosed responsibly and Salesforce worked with the researchers to investigate and remediate; no exploitation in the wild is reported, so `real_harm: false`. The archive grades it `high` on the "significant capability demonstration" limb of its severity ladder: zero-click exfiltration plus trusted-identity impersonation through a platform deployed across a large enterprise base. It is the archive's first **Agentforce** entry, and it extends the zero-click exfiltration lineage (EchoLeak, BragJack) from mail/browser surfaces to the CRM-and-chat surface where enterprise agents actually hold permissions.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Zenity Labs disclosure (Business Wire, 24 Sep 2026) | <https://www.morningstar.com/news/business-wire/20260924811082/zenity-labs-uncovers-salesbleed-3-salesforce-agentforce-flaws-enabling-zero-click-crm-data-theft-and-ai-agent-impersonation> |
| 2 | Dark Reading | <https://www.darkreading.com/application-security/salesbleed-exploits-salesforce-agents-slack-phishing> |
| 3 | Aviatrix Threat Research Center | <https://aviatrix.ai/threat-research-center/salesbleed-salesforce-agentforce-slack-phishing-2026/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-24` (raw: 2026-09-24, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) [`EXFIL`](../../taxonomy/types.md#exfil) |
| Severity | **High** `high` |
| Confidence | **A** — the disclosing researchers' own release plus independent reporting |
| Real harm | No — responsibly disclosed and remediated, no known in-the-wild use |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-24-salesbleed-agentforce-zero-click-exfil` |

<sub>**Why this classification:** the injection arrives as external content an agent reads (`IPI`) and the data actually crosses the trust boundary to the attacker (`EXFIL`). `vulnerability` + `real_harm: false` because nothing was exploited before remediation; `high` under the "significant capability demonstration" rule — zero-click exfiltration and trusted-identity abuse on a widely deployed enterprise agent platform — since `critical` is reserved for confirmed multi-organisation damage or a first-of-its-kind milestone with a real victim. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain (IPI + EXFIL)](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-09-16` [BragJack: one browser extension hijacks the AI agents in five major browsers](2026-09-16-bragjack-browser-agents.md)<br>  <sub>Same class of problem one layer down — the agent's input channel, not its output boundary</sub>
- `2026-09-09` [Workflow identity hijacking: Noma Labs turns an ordinary support email into privileged data access](2026-09-09-noma-workflow-identity-hijacking.md)<br>  <sub>When the agent acts with permissions nobody granted the sender</sub>
- `2025-06-11` [EchoLeak](../2025-06/2025-06-11-echoleak.md)<br>  <sub>The zero-click exfiltration template this lineage starts from</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-24-salesbleed-agentforce-zero-click-exfil.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
