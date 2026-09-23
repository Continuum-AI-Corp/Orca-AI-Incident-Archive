---
id: 2026-09-09-wiz-litellm-default-key-off-guard
title: "Wiz: nearly 1 in 10 exposed LiteLLM gateways accept the example admin key sk-1234"
title_zh: "Wiz：近十分之一的公网 LiteLLM 网关接受示例管理员密钥 sk-1234"
title_ja: "Wiz：公開LiteLLMゲートウェイのほぼ10台に1台がサンプル管理者キーsk-1234を受理"
title_ko: "Wiz: 공개된 LiteLLM 게이트웨이 10곳 중 1곳이 예제 관리자 키 sk-1234를 수락"
title_de: "Wiz: Fast jedes zehnte offene LiteLLM-Gateway akzeptiert den Beispiel-Admin-Schlüssel sk-1234"
title_fr: "Wiz : près d'une passerelle LiteLLM exposée sur dix accepte la clé d'admin d'exemple sk-1234"
title_es: "Wiz: casi 1 de cada 10 pasarelas LiteLLM expuestas acepta la clave de admin de ejemplo sk-1234"
date: 2026-09-09
date_raw: "2026-09-09"
date_precision: day

kind: research
type: [INFRA, CRED]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **Wiz Research** publishes *“Off Guard: Breaking LiteLLM from authentication bypass to cloud compromise”*, tying three findings into one chain from a public AI gateway to **root-level code execution and IAM theft**. Its scan of **3,074 internet-facing LiteLLM gateways** (Shodan, February 2026) found that **294 — nearly 1 in 10 — accepted the project's example admin key `sk-1234`**: whoever logs in with it controls the component that holds the model API keys and cloud credentials for everything behind it. The same research composes two flaws reported by Wiz's **Yaara Shriki**: **CVE-2026-59822**, the MCP authentication bypass (CVSS 4.0 **8.8**; KEV-listed 2 September), and **CVE-2026-59821**, in which LiteLLM's Custom Code Guardrails production endpoints skip the sandbox and validation used by the test endpoint — rated **low (2.1)** because it requires a privileged user, but part of the chain to code execution. Wiz's conclusion is that the gateway's defaults, not a single bug, are the systemic problem: default keys, unauthenticated MCP sessions and code-executing guardrails stack into cloud compromise. The companion lesson is scheduling: the flaw behind the KEV entry was reported in July and exploited in the wild by September

summary_zh: |
  **Wiz Research** 发布《Off Guard：从认证绕过到云环境沦陷，攻破 LiteLLM》，把三项发现串成一条从中暴露的 AI 网关直到 **root 级代码执行与 IAM 凭据窃取**的完整链条。其扫描了 **3,074 个公网暴露的 LiteLLM 网关**（2026 年 2 月，Shodan），发现其中 **294 个——近十分之一——接受项目文档里的示例管理员密钥 `sk-1234`**：用它登录的人就控制了那个保管着所有模型 API 密钥与云凭据的组件。同一研究把 Wiz 的 **Yaara Shriki** 报告的两个缺陷串了起来：**CVE-2026-59822**，MCP 认证绕过（CVSS 4.0 **8.8**，9 月 2 日进入 KEV）；以及 **CVE-2026-59821**——LiteLLM 的 Custom Code Guardrails 生产端点跳过了测试端点所用的沙箱与校验，因需要特权用户而被评为**低危（2.1）**，但它是通向代码执行链条的一环。Wiz 的结论是：系统性问题出在网关的默认配置，而不是单个漏洞——默认密钥、未认证的 MCP 会话与可执行代码的护栏层层叠加，最终指向云环境沦陷。附带的教训与时间表有关：KEV 条目背后的漏洞 7 月就已报告，到 9 月已在野被利用

summary_ja: |
  **Wiz Research** は「Off Guard: Breaking LiteLLM from authentication bypass to cloud compromise」を公開し、3つの発見を1本の連鎖にまとめた——公開AIゲートウェイから **root権限のコード実行とIAM窃取**まで。**インターネット公開のLiteLLMゲートウェイ3,074台**（2026年2月、Shodan）をスキャンした結果、**294台——ほぼ10台に1台——がプロジェクトのサンプル管理者キー`sk-1234`を受理**した。これでログインできる者は、背後すべてのモデルAPIキーとクラウド資格情報を保管するコンポーネントを掌握する。同じ研究は、Wizの**Yaara Shriki**が報告した2件の欠陥を組み合わせる：**CVE-2026-59822**（MCP認証バイパス、CVSS 4.0 **8.8**、9月2日KEV入り）と、**CVE-2026-59821**——LiteLLMのCustom Code Guardrails本番エンドポイントがテスト用エンドポイントのサンドボックスと検証を省略する問題で、特権ユーザーが必要なため**低（2.1）**評価だがコード実行への連鎖の一部。Wizの結論は、単一のバグではなくゲートウェイのデフォルト設定が構造的問題だというものだ。併せて示された教訓は時間軸にある——KEV入りの欠陥は7月に報告され、9月には実環境で悪用された

summary_ko: |
  **Wiz Research**가 'Off Guard: Breaking LiteLLM from authentication bypass to cloud compromise'를 발표하며 세 가지 발견을 하나의 사슬로 엮었다. 공개된 AI 게이트웨이에서 **루트 권한 코드 실행과 IAM 탈취**까지 이어진다. **인터넷에 노출된 LiteLLM 게이트웨이 3,074개**(2026년 2월, Shodan)를 스캔한 결과 **294개 — 약 10곳 중 1곳 — 가 프로젝트의 예제 관리자 키 `sk-1234`를 수락**했다. 이 키로 로그인하는 사람은 뒤의 모든 모델 API 키와 클라우드 자격 증명을 보관하는 구성 요소를 장악한다. 같은 연구는 Wiz의 **Yaara Shriki**가 보고한 두 결함을 조합한다. **CVE-2026-59822**(MCP 인증 우회, CVSS 4.0 **8.8**, 9월 2일 KEV 등재)와 **CVE-2026-59821** — LiteLLM의 Custom Code Guardrails 프로덕션 엔드포인트가 테스트 엔드포인트의 샌드박스와 검증을 건너뛰는 문제로, 권한 있는 사용자가 필요해 **낮음(2.1)** 평가지만 코드 실행 사슬의 일부다. Wiz의 결론은 단일 버그가 아니라 게이트웨이의 기본값이 구조적 문제라는 것이다. 함께 제시된 교훈은 시간표다. KEV에 오른 결함은 7월에 보고됐고 9월에는 실제로 악용됐다

summary_de: |
  **Wiz Research** veröffentlicht *„Off Guard: Breaking LiteLLM from authentication bypass to cloud compromise“* und verknüpft drei Befunde zu einer Kette von einem offenen KI-Gateway bis zu **Codeausführung mit Root-Rechten und IAM-Diebstahl**. Der Scan von **3.074 öffentlich erreichbaren LiteLLM-Gateways** (Shodan, Februar 2026) ergab, dass **294 – fast jedes zehnte – den Beispiel-Admin-Schlüssel `sk-1234` akzeptierten**: Wer sich damit anmeldet, kontrolliert die Komponente, die die Modell-API-Schlüssel und Cloud-Zugangsdaten für alles dahinter hält. Dieselbe Forschung kombiniert zwei von Wiz' **Yaara Shriki** gemeldete Schwachstellen: **CVE-2026-59822**, den MCP-Authentifizierungs-Bypass (CVSS 4.0 **8.8**; KEV-Listung am 2. September), und **CVE-2026-59821**, bei dem die Produktions-Endpunkte der Custom Code Guardrails die Sandbox und Validierung des Test-Endpunkts umgehen – als **niedrig (2.1)** eingestuft, weil ein privilegierter Nutzer nötig ist, aber Teil der Kette zur Codeausführung. Wiz' Fazit: Nicht ein einzelner Bug, sondern die Standardeinstellungen des Gateways sind das systemische Problem. Die begleitende Lehre betrifft den Zeitplan: Die Schwachstelle hinter dem KEV-Eintrag wurde im Juli gemeldet und im September in freier Wildbahn ausgenutzt

summary_fr: |
  **Wiz Research** publie *« Off Guard: Breaking LiteLLM from authentication bypass to cloud compromise »*, reliant trois découvertes en une chaîne menant d'une passerelle d'IA exposée à **l'exécution de code en root et au vol d'IAM**. Son scan de **3 074 passerelles LiteLLM exposées sur Internet** (Shodan, février 2026) a montré que **294 — près d'une sur dix — acceptaient la clé d'admin d'exemple `sk-1234`** : qui s'y connecte contrôle le composant qui détient les clés d'API des modèles et les identifiants cloud de tout ce qui se trouve derrière. La même recherche combine deux failles signalées par **Yaara Shriki** de Wiz : **CVE-2026-59822**, le contournement d'authentification MCP (CVSS 4.0 **8.8** ; ajouté au KEV le 2 septembre), et **CVE-2026-59821**, où les points de terminaison de production des Custom Code Guardrails de LiteLLM contournent le bac à sable et la validation du point de test — noté **faible (2.1)** car il exige un utilisateur privilégié, mais partie de la chaîne vers l'exécution de code. Conclusion de Wiz : ce sont les réglages par défaut de la passerelle, plus qu'un bug isolé, qui constituent le problème systémique. La leçon d'agenda : la faille derrière l'entrée KEV a été signalée en juillet et exploitée dans la nature dès septembre

summary_es: |
  **Wiz Research** publica *«Off Guard: Breaking LiteLLM from authentication bypass to cloud compromise»*, encadenando tres hallazgos desde una pasarela de IA expuesta hasta **ejecución de código como root y robo de IAM**. Su escaneo de **3.074 pasarelas LiteLLM expuestas a internet** (Shodan, febrero de 2026) encontró que **294 —casi 1 de cada 10— aceptaban la clave de administrador de ejemplo `sk-1234`**: quien entra con ella controla el componente que guarda las claves de API de los modelos y las credenciales de nube de todo lo que hay detrás. La misma investigación compone dos fallos reportados por **Yaara Shriki** de Wiz: **CVE-2026-59822**, el bypass de autenticación MCP (CVSS 4.0 **8.8**; añadido al KEV el 2 de septiembre), y **CVE-2026-59821**, donde los endpoints de producción de los Custom Code Guardrails de LiteLLM omiten el sandbox y la validación del endpoint de pruebas —valorado **bajo (2.1)** porque requiere un usuario privilegiado, pero parte de la cadena hacia la ejecución de código—. La conclusión de Wiz: el problema sistémico son los valores por defecto de la pasarela, no un solo bug. La lección de calendario: el fallo detrás de la entrada KEV se reportó en julio y se explotó en la naturaleza en septiembre

sources:
  - url: https://www.wiz.io/blog/off-guard-breaking-litellm-from-authentication-bypass-to-cloud-compromise
    label: Wiz Research
  - url: https://github.com/BerriAI/litellm/security/advisories/GHSA-7488-6r32-c95q
    label: GitHub Security Advisory (CVE-2026-59822)
  - url: https://github.com/BerriAI/litellm/security/advisories/GHSA-72m8-9m7m-h278
    label: GitHub Security Advisory (CVE-2026-59821)
  - url: https://labs.cloudsecurityalliance.org/research/csa-research-note-litellm-gateway-default-credentials-202609/
    label: Cloud Security Alliance
  - url: https://thehackernews.com/2026/09/nearly-1-in-10-exposed-litellm-gateways.html
    label: The Hacker News

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# Wiz: nearly 1 in 10 exposed LiteLLM gateways accept the example admin key sk-1234

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

**Wiz Research** publishes *“Off Guard: Breaking LiteLLM from authentication bypass to cloud compromise”*, tying three findings into one chain from a public AI gateway to **root-level code execution and IAM theft**. Its scan of **3,074 internet-facing LiteLLM gateways** (Shodan, February 2026) found that **294 — nearly 1 in 10 — accepted the project's example admin key `sk-1234`**: whoever logs in with it controls the component that holds the model API keys and cloud credentials for everything behind it. The same research composes two flaws reported by Wiz's **Yaara Shriki**: **CVE-2026-59822**, the MCP authentication bypass (CVSS 4.0 **8.8**; KEV-listed 2 September), and **CVE-2026-59821**, in which LiteLLM's Custom Code Guardrails production endpoints skip the sandbox and validation used by the test endpoint — rated **low (2.1)** because it requires a privileged user, but part of the chain to code execution. Wiz's conclusion is that the gateway's defaults, not a single bug, are the systemic problem: default keys, unauthenticated MCP sessions and code-executing guardrails stack into cloud compromise. The companion lesson is scheduling: the flaw behind the KEV entry was reported in July and exploited in the wild by September

## Attack chain

```mermaid
flowchart LR
    E["An internet-facing LiteLLM gateway whose example admin key is unchanged"]:::entry
    S0["Admin access, plus unauthenticated MCP sessions and code guardrails that skip the sandbox"]:::step
    I["Root-level code execution and IAM theft on the host that holds every model and cloud credential<br/><i>(294 of 3,074 scanned gateways took sk-1234)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The scan: 294 of 3,074.** Wiz's starting measurement is blunt. In February 2026 it scanned **3,074 internet-facing LiteLLM gateways** found on Shodan and tested the key that LiteLLM's own documentation uses in every example: `sk-1234`. **294 of them — 9.6% — accepted it as a working admin key.** The severity of that number comes from what a LiteLLM gateway is: the proxy that fronts every model provider an organisation uses, which is why it accumulates the API keys, spend limits and cloud credentials for everything downstream. Wiz's chain does not stop at "read access to a configuration": with admin on the gateway, the following steps — including the MCP and guardrail surfaces — become reachable paths to running code on the host and using its cloud identity. (The scan is a snapshot of February 2026 and counts gateways that accept the example key, not gateways attacked with it.)

**The two CVEs in the chain.** The research composes two separately tracked flaws, both reported by **Yaara Shriki** (credited as `yaaras` in GitHub's advisories). **CVE-2026-59822** is the MCP authentication bypass: LiteLLM's MCP Streamable HTTP endpoint could establish an authenticated session from an arbitrary Bearer token because the OAuth2 passthrough fallback substituted an empty `UserAPIKeyAuth()` object for a failed validation — CVSS 4.0 **8.8**, fixed in 1.84.0, and listed in CISA's KEV catalog on **2 September**. **CVE-2026-59821** is the quieter one: LiteLLM's Custom Code Guardrails production create/update paths *“did not apply the same sandboxing and validation used by the test endpoint,”* so a privileged user could submit custom Python that executed in the proxy environment — rated **low (2.1)** because it requires that privileged user, but precisely the kind of "privileged enough to run code" position that the default key hands out. Neither is exotic alone; stacked on a defaulted gateway, they are a path to code execution and credential theft.

**Why it is recorded separately from the KEV entry.** The archive already holds the 2 September KEV disclosure as its own record; this one records the measurement and the composition — the exposure rate among internet-facing gateways, and the analysis that the failures cluster at the gateway's authentication and trust defaults rather than in a model or protocol design. The scheduling detail is part of the finding: the advisory behind the KEV listing was public in July, and by early September CISA had confirmed exploitation. The caveat this record keeps: the 294 figure is a scan of accepting-defaults gateways, and no compromise of a named gateway is credited to `sk-1234` in the research itself.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Wiz Research | <https://www.wiz.io/blog/off-guard-breaking-litellm-from-authentication-bypass-to-cloud-compromise> |
| 2 | GitHub Security Advisory (CVE-2026-59822) | <https://github.com/BerriAI/litellm/security/advisories/GHSA-7488-6r32-c95q> |
| 3 | GitHub Security Advisory (CVE-2026-59821) | <https://github.com/BerriAI/litellm/security/advisories/GHSA-72m8-9m7m-h278> |
| 4 | Cloud Security Alliance | <https://labs.cloudsecurityalliance.org/research/csa-research-note-litellm-gateway-default-credentials-202609/> |
| 5 | The Hacker News | <https://thehackernews.com/2026/09/nearly-1-in-10-exposed-litellm-gateways.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-09` (raw: 2026-09-09, precision `day`) |
| Kind | Research demo `research` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source: the finder's write-up, with both upstream advisories and a CSA review |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-09-wiz-litellm-default-key-off-guard` |

<sub>**Why this classification:** A research report measuring exposure and composing known flaws; `real_harm: false` because no gateway is named as compromised by the default key, but `high` severity because the measured exposure — admin control of credential-holding gateways — is severe at scale, and one flaw in the chain is KEV-listed. Dated to the Wiz post (9 September 2026); the scan data is from February 2026. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-09-02` [Any bearer token opens LiteLLM's MCP endpoint: CVE-2026-59822 enters CISA KEV](../2026-09/2026-09-02-litellm-mcp-auth-bypass-kev.md)<br>  <sub>The KEV-listed bypass measured and composed here</sub>
- `2026-06-08` [LiteLLM CVE-2026-42271 MCP endpoint takeover](../2026-06/2026-06-08-litellm-mcp-duan-dian-jie.md)<br>  <sub>The earlier LiteLLM MCP flaw exploited in the wild</sub>
- `2026-05-28` [BadHost (CVE-2026-48710)](../2026-05/2026-05-28-badhost.md)<br>  <sub>The header-trust flaw chained with LiteLLM into unauthenticated RCE</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-09-wiz-litellm-default-key-off-guard.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
