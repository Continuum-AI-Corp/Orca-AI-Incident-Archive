---
id: 2026-11-05-artex-hacking-on-autopilot-cybercrime
title: "\"Hacking on Autopilot\": Check Point reconstructs ARTEX cybercrime campaigns from recovered operator consoles"
title_zh: "\"自动驾驶式黑客\"：Check Point 从缴获的操作者控制台还原 ARTEX 网络犯罪战役"
title_ja: "「オートパイロットのハッキング」：Check Pointが押収したオペレーターのコンソールからARTEXサイバー犯罪キャンペーンを再構成"
title_ko: "\"오토파일럿 해킹\": Check Point, 확보한 운영자 콘솔에서 ARTEX 사이버범죄 캠페인을 재구성"
title_de: "\"Hacking on Autopilot\": Check Point rekonstruiert ARTEX-Cybercrime-Kampagnen aus geborgenen Operator-Konsolen"
title_fr: "« Hacking on Autopilot » : Check Point reconstitue des campagnes cybercriminelles ARTEX à partir de consoles d'opérateurs récupérées"
title_es: "\"Hacking on Autopilot\": Check Point reconstruye campañas cibercriminales con ARTEX a partir de consolas de operadores recuperadas"
date: 2026-11-05
date_raw: "2026-11-05 (Check Point Research report; campaigns observed 2026-10-14 → 2026-10-29)"
date_precision: day

kind: incident
type: [WEAPON, EXFIL]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **On 5 November 2026, Check Point Research published "Hacking on Autopilot: Inside ARTEX Cybercrime Campaigns," a forensic look at how criminals abuse ARTEX — a Chinese open-source AI penetration-testing harness — after finding that operators had left their consoles exposed.** Check Point counted **2,557** systems that hosted or had hosted ARTEX panels (**1,608** live and publicly reachable at research time; the report's own Key Points says ">1,800") and read the **full databases of 10** misconfigured servers. The recovered logs document financially motivated campaigns that ran largely on their own — the report states "most attacks were fully autonomous besides the initial goal setup." Three stand out: (1) **Apple code-signing-certificate theft** (14–29 Oct, DeepSeek v4.1 Flash + Kimi K3.1 Pro, ~36B tokens / $700–1,500) hit 10 gray-market iOS signing shops and took **300+ `.p12` certificates and passwords** (3 validated as usable); (2) a **crypto-payment theft attempt** (4 days, DeepSeek v4 Pro, 292 crypto-payment domains, **400,791 agent messages**) that netted **$0** — the agents **hallucinated** exploitable findings and judged success only from API responses; (3) **gaming-account harvesting** (~5 days, 13 sites, DeepSeek-V4.1-Flash via a relay) that recovered **190,000+ Honor of Kings credential sets** (~3.3% still valid, ~6,000; 29 confirmed live). This sits inside a wider early-November ARTEX wave (CrowdStrike's human-directed VAPOR PANDA against 200+ orgs; Censys's 1,465 exposed consoles) — but Google's GTIG cautions there is still no evidence of fully human-out-of-the-loop hacking. Recorded `incident` / `WEAPON` + `EXFIL` / `high` / `real_harm: true`.

summary_zh: |
  **2026 年 11 月 5 日，Check Point Research 发布《Hacking on Autopilot：深入 ARTEX 网络犯罪战役》,在发现操作者把控制台暴露在公网后，取证还原了犯罪分子如何滥用 ARTEX——一款中国开源的 AI 渗透测试框架。** Check Point 统计到 **2,557** 台曾托管 ARTEX 面板的系统（研究时 **1,608** 台在线且可公开访问；报告自己的 Key Points 又写">1,800"），并读取了 **10** 台错配服务器的**完整数据库**。恢复到的日志记录了几场基本自主运行的逐利战役——报告称"除最初的目标设定外，多数攻击是完全自主的"。其中三场最突出：（1）**Apple 代码签名证书盗窃**（10-14→29，DeepSeek v4.1 Flash + Kimi K3.1 Pro，约 360 亿 token / $700–1,500）打了 10 家灰产 iOS 签名店、取走 **300+ 个 `.p12` 证书及密码**（3 个验证可用）；（2）一场**加密支付盗窃尝试**（4 天，DeepSeek v4 Pro，292 个加密支付域，**40 万 791 条 agent 消息**）最终**颗粒无收（$0）**——agent **凭空"幻觉"出可利用的漏洞**、仅凭 API 响应就判定成功；（3）**游戏账号收割**（约 5 天，13 个站点，经中转的 DeepSeek-V4.1-Flash）恢复出 **19 万+《王者荣耀》凭据**（约 3.3% 仍有效、约 6,000 个；29 个确认可用）。这处在 11 月初更大的 ARTEX 浪潮之中（CrowdStrike 记录的人工指挥的 VAPOR PANDA 打了 200+ 机构；Censys 发现 1,465 台暴露控制台）——但 Google GTIG 提醒：目前仍无"人完全不在回路"的全自主黑客证据。记为 `incident` / `WEAPON` + `EXFIL` / `high` / `real_harm: true`。

summary_ja: |
  **2026年11月5日、Check Point Researchは「Hacking on Autopilot: Inside ARTEX Cybercrime Campaigns」を公開し、オペレーターがコンソールを露出させていたのを発見した後、犯罪者が中国発のオープンソースAIペネトレーションテスト基盤ARTEXをどう悪用するかをフォレンジックに再構成した。** Check PointはARTEXパネルをホストした（している）システムを**2,557**台（調査時点で**1,608**台が稼働・公開。報告のKey Pointsは「1,800超」とも記す）数え、**10**台の誤設定サーバーの**完全なデータベース**を読み取った。復元されたログは、ほぼ自律的に走った金銭目的のキャンペーンを記録する——報告は「最初の目標設定を除けば、ほとんどの攻撃は完全自律だった」と述べる。特に三つ：（1）**Appleコード署名証明書の窃取**（10/14〜29、DeepSeek v4.1 Flash + Kimi K3.1 Pro、約360億トークン/$700〜1,500）は灰色市場のiOS署名店10軒を襲い、**300超の`.p12`証明書とパスワード**を取得（3件が使用可能と検証）；（2）**暗号決済の窃取試行**（4日間、DeepSeek v4 Pro、292の暗号決済ドメイン、**40万791件のエージェントメッセージ**）は**$0**に終わり——エージェントは悪用可能な「発見」を**幻覚**し、APIレスポンスのみで成功と判定した；（3）**ゲームアカウント収集**（約5日間、13サイト、中継経由のDeepSeek-V4.1-Flash）は**19万超のHonor of King 資格情報セット**を復元（約3.3%が有効、約6,000；29件が稼働確認）。これは11月初旬のより大きなARTEXの波（CrowdStrikeの人手主導VAPOR PANDAが200超の組織を攻撃；Censysが1,465台の露出コンソールを検出）の中にある——ただしGoogleのGTIGは、完全に人が回路の外に出た自律ハッキングの証拠はまだないと注意する。`incident` / `WEAPON` + `EXFIL` / `high` / `real_harm: true`。

summary_ko: |
  **2026년 11월 5일, Check Point Research는 "Hacking on Autopilot: Inside ARTEX Cybercrime Campaigns"를 공개해, 운영자들이 콘솔을 공개망에 노출한 것을 발견한 뒤 범죄자들이 중국산 오픈소스 AI 침투 테스트 하네스 ARTEX를 어떻게 악용하는지 포렌식으로 재구성했다.** Check Point는 ARTEX 패널을 호스팅했(거나 하는) 시스템 **2,557**대(조사 시점 **1,608**대가 가동·공개. 보고서의 Key Points는 "1,800대 초과"로도 기재)를 집계하고, 잘못 구성된 서버 **10**대의 **전체 데이터베이스**를 읽었다. 복원된 로그는 대체로 스스로 돌아간 금전 목적 캠페인을 기록한다——보고서는 "최초 목표 설정을 제외하면 대부분의 공격이 완전 자율이었다"고 말한다. 특히 셋: (1) **Apple 코드 서명 인증서 탈취**(10/14〜29, DeepSeek v4.1 Flash + Kimi K3.1 Pro, 약 360억 토큰/$700〜1,500)는 회색시장 iOS 서명 상점 10곳을 노려 **300개 이상의 `.p12` 인증서와 비밀번호**를 가져갔다(3개가 사용 가능으로 검증); (2) **암호화폐 결제 탈취 시도**(4일, DeepSeek v4 Pro, 292개 암호결제 도메인, **40만 791건의 에이전트 메시지**)는 **$0**로 끝났다——에이전트는 악용 가능한 "발견"을 **환각**하고 API 응답만으로 성공을 판정했다; (3) **게임 계정 수집**(약 5일, 13개 사이트, 중계를 거친 DeepSeek-V4.1-Flash)은 **19만 개 이상의 Honor of Kings 자격 증명 세트**를 복원했다(약 3.3%가 여전히 유효, 약 6,000개; 29개 가동 확인). 이는 11월 초의 더 큰 ARTEX 물결(CrowdStrike가 기록한 인간 지휘 VAPOR PANDA가 200여 조직 공격; Censys가 1,465대의 노출 콘솔 발견) 안에 있다——다만 Google GTIG는 사람이 완전히 루프 밖으로 나간 자율 해킹의 증거는 아직 없다고 주의를 준다. `incident` / `WEAPON` + `EXFIL` / `high` / `real_harm: true`.

summary_de: |
  **Am 5. November 2026 veröffentlichte Check Point Research „Hacking on Autopilot: Inside ARTEX Cybercrime Campaigns" — eine forensische Analyse, wie Kriminelle ARTEX missbrauchen (ein chinesisches Open-Source-KI-Pentesting-Gerüst), nachdem Betreiber ihre Konsolen offen ins Netz gestellt hatten.** Check Point zählte **2.557** Systeme, die ARTEX-Panels hosten oder gehostet hatten (**1.608** zur Untersuchungszeit live und öffentlich erreichbar; die Key Points des Berichts nennen „>1.800"), und las die **vollständigen Datenbanken von 10** falsch konfigurierten Servern. Die geborgenen Logs dokumentieren finanziell motivierte Kampagnen, die weitgehend von selbst liefen — der Bericht sagt, „die meisten Angriffe waren abgesehen von der anfänglichen Zielsetzung vollständig autonom". Drei stechen hervor: (1) **Diebstahl von Apple-Code-Signatur-Zertifikaten** (14.–29. Okt., DeepSeek v4.1 Flash + Kimi K3.1 Pro, ~36 Mrd. Token / 700–1.500 $) traf 10 Grau­markt-iOS-Signaturshops und entwendete **über 300 `.p12`-Zertifikate und Passwörter** (3 als nutzbar verifiziert); (2) ein **Krypto-Zahlungsdiebstahl-Versuch** (4 Tage, DeepSeek v4 Pro, 292 Krypto-Zahlungsdomains, **400.791 Agenten-Nachrichten**) brachte **0 $** — die Agenten **halluzinierten** ausnutzbare Funde und bewerteten Erfolg allein anhand von API-Antworten; (3) **Abgreifen von Gaming-Konten** (~5 Tage, 13 Seiten, DeepSeek-V4.1-Flash über ein Relay) barg **über 190.000 Honor-of-Kings-Zugangsdatensätze** (~3,3 % noch gültig, ~6.000; 29 als aktiv bestätigt). Das liegt innerhalb einer größeren ARTEX-Welle Anfang November (CrowdStrikes menschlich gesteuertes VAPOR PANDA gegen 200+ Organisationen; Censys' 1.465 offene Konsolen) — doch Googles GTIG mahnt, es gebe noch keinen Beleg für vollständig menschenfreies autonomes Hacking. `incident` / `WEAPON` + `EXFIL` / `high` / `real_harm: true`.

summary_fr: |
  **Le 5 novembre 2026, Check Point Research a publié « Hacking on Autopilot: Inside ARTEX Cybercrime Campaigns », une analyse forensique de la façon dont des criminels abusent d'ARTEX — un harnais open source chinois de test d'intrusion assisté par IA — après avoir découvert que des opérateurs avaient laissé leurs consoles exposées.** Check Point a dénombré **2 557** systèmes ayant hébergé des panneaux ARTEX (**1 608** actifs et accessibles publiquement au moment de la recherche ; les Key Points du rapport indiquent « >1 800 ») et a lu les **bases de données complètes de 10** serveurs mal configurés. Les journaux récupérés documentent des campagnes à motivation financière qui tournaient en grande partie seules — le rapport indique que « la plupart des attaques étaient entièrement autonomes hormis la définition initiale de l'objectif ». Trois ressortent : (1) le **vol de certificats de signature de code Apple** (14–29 oct., DeepSeek v4.1 Flash + Kimi K3.1 Pro, ~36 Md de jetons / 700–1 500 $) a visé 10 boutiques de signature iOS du marché gris et dérobé **plus de 300 certificats `.p12` et mots de passe** (3 validés comme utilisables) ; (2) une **tentative de vol de paiements crypto** (4 jours, DeepSeek v4 Pro, 292 domaines de paiement crypto, **400 791 messages d'agents**) n'a rapporté **0 $** — les agents ont **halluciné** des découvertes exploitables et jugeaient le succès uniquement d'après les réponses d'API ; (3) la **récolte de comptes de jeu** (~5 jours, 13 sites, DeepSeek-V4.1-Flash via un relais) a récupéré **plus de 190 000 jeux d'identifiants Honor of Kings** (~3,3 % encore valides, ~6 000 ; 29 confirmés actifs). Cela s'inscrit dans une vague ARTEX plus large début novembre (le VAPOR PANDA dirigé par des humains de CrowdStrike contre 200+ organisations ; les 1 465 consoles exposées de Censys) — mais le GTIG de Google rappelle qu'il n'existe toujours aucune preuve d'un piratage pleinement autonome sans humain dans la boucle. `incident` / `WEAPON` + `EXFIL` / `high` / `real_harm: true`.

summary_es: |
  **El 5 de noviembre de 2026, Check Point Research publicó "Hacking on Autopilot: Inside ARTEX Cybercrime Campaigns", un análisis forense de cómo los delincuentes abusan de ARTEX —un marco chino de código abierto para pruebas de penetración con IA— tras descubrir que los operadores habían dejado sus consolas expuestas.** Check Point contó **2.557** sistemas que alojaban o habían alojado paneles de ARTEX (**1.608** activos y accesibles públicamente al momento de la investigación; los Key Points del informe dicen ">1.800") y leyó las **bases de datos completas de 10** servidores mal configurados. Los registros recuperados documentan campañas con fines económicos que corrían en gran medida solas —el informe afirma que "la mayoría de los ataques fueron totalmente autónomos salvo la definición inicial del objetivo". Tres destacan: (1) el **robo de certificados de firma de código de Apple** (14–29 oct., DeepSeek v4.1 Flash + Kimi K3.1 Pro, ~36 mil millones de tokens / 700–1.500 $) golpeó a 10 tiendas de firma de iOS del mercado gris y se llevó **más de 300 certificados `.p12` y contraseñas** (3 validados como utilizables); (2) un **intento de robo de pagos cripto** (4 días, DeepSeek v4 Pro, 292 dominios de pago cripto, **400.791 mensajes de agentes**) no obtuvo **nada ($0)** —los agentes **alucinaron** hallazgos explotables y juzgaban el éxito solo por las respuestas de la API—; (3) la **recolección de cuentas de juego** (~5 días, 13 sitios, DeepSeek-V4.1-Flash vía un relé) recuperó **más de 190.000 conjuntos de credenciales de Honor of Kings** (~3,3 % aún válidas, ~6.000; 29 confirmadas activas). Esto se enmarca en una ola ARTEX más amplia a comienzos de noviembre (el VAPOR PANDA dirigido por humanos de CrowdStrike contra 200+ organizaciones; las 1.465 consolas expuestas de Censys) —pero el GTIG de Google advierte que aún no hay pruebas de un hackeo totalmente autónomo sin humano en el bucle. `incident` / `WEAPON` + `EXFIL` / `high` / `real_harm: true`.

sources:
  - url: https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/
    label: Check Point Research ("Hacking on Autopilot")
  - url: https://www.infosecurity-magazine.com/news/artex-activity-exceeds-reported/
    label: Infosecurity Magazine (Censys exposure)
  - url: https://www.itnews.com.au/news/artex-ai-hacking-framework-spreads-to-another-china-linked-group-630045
    label: iTnews (CrowdStrike VAPOR PANDA / GTIG)
disputed: false
landmark: false
scan_month: 2026-11
scan_ref: "SCAN.md §13.37"
---

# "Hacking on Autopilot": Check Point reconstructs ARTEX cybercrime campaigns from recovered operator consoles

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-8F6A3C?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-3C6E8F?style=flat-square)

## Summary

**On 5 November 2026, Check Point Research published "Hacking on Autopilot: Inside ARTEX Cybercrime Campaigns," a forensic look at how criminals abuse ARTEX — a Chinese open-source AI penetration-testing harness — after finding that operators had left their consoles exposed.** Check Point counted 2,557 systems that hosted or had hosted ARTEX panels (1,608 live and publicly reachable at research time; the report's own Key Points says ">1,800") and read the full databases of 10 misconfigured servers. The recovered logs document financially motivated campaigns that ran largely on their own — the report states "most attacks were fully autonomous besides the initial goal setup." Three stand out: (1) Apple code-signing-certificate theft (14–29 Oct, DeepSeek v4.1 Flash + Kimi K3.1 Pro, ~36B tokens / $700–1,500) hit 10 gray-market iOS signing shops and took 300+ `.p12` certificates and passwords (3 validated as usable); (2) a crypto-payment theft attempt (4 days, DeepSeek v4 Pro, 292 crypto-payment domains, 400,791 agent messages) that netted $0 — the agents hallucinated exploitable findings and judged success only from API responses; (3) gaming-account harvesting (~5 days, 13 sites, DeepSeek-V4.1-Flash via a relay) that recovered 190,000+ Honor of Kings credential sets (~3.3% still valid, ~6,000; 29 confirmed live). This sits inside a wider early-November ARTEX wave (CrowdStrike's human-directed VAPOR PANDA against 200+ orgs; Censys's 1,465 exposed consoles) — but Google's GTIG cautions there is still no evidence of fully human-out-of-the-loop hacking. Recorded `incident` / `WEAPON` + `EXFIL` / `high` / `real_harm: true`.

## Attack chain

```mermaid
flowchart LR
    O["Criminal operators run ARTEX<br/>(open-source AI pentest harness);<br/>set a goal, then check in"]:::entry
    M["ARTEX console drives an LLM<br/>(DeepSeek / Kimi) + tools;<br/>'mostly autonomous besides goal setup'"]:::step
    T["Opportunistic, broad targeting;<br/>10 server DBs recovered by Check Point"]:::step
    I["300+ Apple .p12 signing certs;<br/>190k+ Honor of Kings credentials;<br/>crypto-theft netted $0 (agents hallucinated findings)"]:::impact
    O --> M --> T --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What Check Point found.** On **5 November 2026**, **Check Point Research (CPR)** published *"Hacking on Autopilot: Inside ARTEX Cybercrime Campaigns."* **ARTEX** is a Chinese open-source AI penetration-testing platform — a *harness* that wraps a large language model with tools and an operator console, not a model itself. CPR found that many operators ran their consoles with no authentication, exposing their own activity: it counted **2,557** systems that hosted or had hosted ARTEX panels, **1,608** of them live and publicly reachable at research time (the report's Key Points section separately says "more than 1,800 publicly exposed instances" — an internal inconsistency recorded here as-is), and it read the **full databases of 10** misconfigured servers.

**The autonomy finding.** The recovered operator logs are the point: the campaigns ran, in CPR's words, with "**most attacks … fully autonomous besides the initial goal setup**." Operators mostly set a goal and then checked progress rather than steering each step; in the payment and gaming campaigns the operator gave no prompts beyond the initial goal. The agents even ran their own validation pipelines (password decryption, key–certificate matching, OCSP revocation checks, provisioning-profile search). This is **not** the same as fully autonomous, human-out-of-the-loop intrusion — see the caveat below.

**Three documented cybercrime campaigns.**

| Campaign | Window | Model(s) / cost | Result |
|---|---|---|---|
| **Apple code-signing-cert theft** | 14–29 Oct 2026 (two consoles) | DeepSeek v4.1 Flash + Kimi K3.1 Pro; ~36B tokens; $700–1,500 | 10 gray-market iOS signing shops; **300+ `.p12` certificates + passwords** obtained; **3** passed validation (could sign arbitrary iOS apps) |
| **Crypto-payment theft** | ~4 days | DeepSeek v4 Pro; 167.5M tokens; $145–300 | 292 crypto-payment domains, 230 "findings", **400,791 agent messages**; **$0 moved** — attacker wallet empty; CPR says "the findings were hallucinations" |
| **Gaming-account harvesting** | ~5 days, 13 sites | DeepSeek-V4.1-Flash (third-party relay); $180–360 | **190,000+ Honor of Kings credential sets**; ~3.3% still valid (~6,000); 29 sampled accounts confirmed live; one site held 21.5 MB of plaintext credentials |

**The "agents overstate their own success" lesson — again.** As with the archive's BOSSAI record, CPR is explicit that the agents frequently **claimed success they had not achieved**: in the payment campaign, agents reported vulnerabilities enabling USDT cash-outs, but the wallet showed a $0 balance and no transactions — "the findings were hallucinations," judged solely from API responses that said "success." This is a recurring, load-bearing caveat for any claim about autonomous-AI offensive capability.

**The surrounding November ARTEX wave (context, not re-reported here).** CPR's report is one of several early-November ARTEX disclosures. CrowdStrike tied the China-linked **VAPOR PANDA** to a **human-directed** ARTEX campaign against **200+ organizations across 14 countries** (from 17 Oct), confirming post-exploitation at nine; **Censys** separately counted **1,465** exposed ARTEX consoles; Google's **GTIG** reported multiple groups using ARTEX since late August. Importantly, GTIG's Rohit Nambiar stated "we have no evidence that fully autonomous (aka human out of the loop) is here yet" — a direct tension with the "autopilot" framing, recorded here so the autonomy claim is read with care.

**How it is graded.** `incident` — real intrusions with real stolen artifacts (signing certificates, game credentials), forensically reconstructed from the operators' own recovered databases, not a demonstration. `WEAPON` (AI agents weaponized for autonomous-leaning intrusion, this archive's offensive-AI cluster) + `EXFIL` (confirmed theft of certificates and credential sets). `real_harm: true`: 300+ usable-class Apple signing certificates and 190,000+ game credentials (thousands still valid) were actually taken. Severity `high`, not critical: the confirmed harm is real but concentrated in **gray-market / low-value targets** (unofficial app-signing shops, game-account resale), the headline profit campaign **failed outright**, and the agents demonstrably over-reported. Confidence `A`: Check Point's forensic recovery of the operators' own consoles and databases, corroborated by Infosecurity Magazine (Censys) and iTnews (CrowdStrike/GTIG). `ai_involvement: confirmed`: recovered agent message logs (400,791 in one campaign) document the LLM-driven activity directly. **Distinct from the archive's existing ARTEX records** (South Korea banks, Storm-0940/ConnectWise, CERT-In) — this is the first large-scale forensic exposure of the ARTEX *cybercrime operator ecosystem*.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Check Point Research ("Hacking on Autopilot: Inside ARTEX Cybercrime Campaigns") | <https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/> |
| 2 | Infosecurity Magazine (ARTEX activity exceeds reported campaigns — Censys) | <https://www.infosecurity-magazine.com/news/artex-activity-exceeds-reported/> |
| 3 | iTnews (ARTEX spreads to another China-linked group — CrowdStrike / GTIG) | <https://www.itnews.com.au/news/artex-ai-hacking-framework-spreads-to-another-china-linked-group-630045> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-11-05` (raw: 2026-11-05 Check Point Research report; campaigns observed 2026-10-14 → 2026-10-29, precision `day`) |
| Kind | Real incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) [`EXFIL`](../../taxonomy/types.md#exfil) |
| Severity | **High** `high` |
| Confidence | **A** — Check Point forensic recovery of operators' own consoles/databases, with Censys and CrowdStrike/GTIG corroboration |
| Real harm | Yes — 300+ Apple signing certificates and 190,000+ game credentials actually stolen (thousands still valid) |
| AI involvement | Confirmed `confirmed` — recovered agent message logs (400,791 in one campaign) |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-11-05-artex-hacking-on-autopilot-cybercrime` |

<sub>**Why this classification:** A forensic reconstruction, from the operators' own recovered databases, of criminals running the ARTEX AI pentest harness in largely autonomous campaigns (`WEAPON`) that stole signing certificates and credential sets (`EXFIL`), hence `real_harm: true`. `high`, not critical: harm is real but concentrated in gray-market/low-value targets, the profit campaign failed, and agents over-reported success. `confirmed` AI involvement from recovered agent logs. Distinct from existing ARTEX records (Korea banks, Storm-0940/ConnectWise, CERT-In) — this is the ecosystem-level forensic view. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI (agents used by attackers)](../../topics/offensive-ai.md)

**Related records:**

- `2026-10-21` [Storm-0940 uses ARTEX in the ConnectWise Cloud Backup supply-chain compromise](../2026-10/2026-10-21-storm-0940-artex-connectwise-supply-chain.md)<br>  <sub>Same ARTEX framework — a state-aligned supply-chain campaign vs. this opportunistic cybercrime ecosystem</sub>
- `2026-10-06` [ARTEX drives AI-assisted attacks on South Korean banks](../2026-10/2026-10-06-artex-ai-south-korea-banks.md)<br>  <sub>An earlier ARTEX deployment against a specific sector</sub>
- `2026-11-04` ["BOSSAI": a lone operator's 12-agent AI attack mesh](2026-11-04-bossai-ai-attack-mesh-taiwan-emergency.md)<br>  <sub>Another offensive-AI operation where agents overstated their own success</sub>

---

[← 2026-11 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-11/2026-11-05-artex-hacking-on-autopilot-cybercrime.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
