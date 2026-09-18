---
id: 2026-06-15-searchleak
title: "SearchLeak (CVE-2026-42824)"
title_zh: "SearchLeak（CVE-2026-42824）"
title_ja: "SearchLeak（CVE-2026-42824）"
title_ko: "SearchLeak (CVE-2026-42824)"
title_de: "SearchLeak (CVE-2026-42824)"
title_fr: "SearchLeak (CVE-2026-42824)"
title_es: "SearchLeak (CVE-2026-42824)"
date: 2026-06-15
date_precision: day
date_raw: "2026-06-15"

kind: research
type: [IPI, EXFIL]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Varonis's three-stage chain: ① the `q` parameter of a search URL is treated as instructions ② sanitization is **post-processing after generation**, so an `<img>` in the streaming render has already fired its request ③ CSP allows `*.bing.com`, and **Bing image search fetches the specified URL server-side, out of reach of the browser CSP**. The lure domain is microsoft.com, and Copilot runs with the user's privileges — a victim who **clicks one link** leaks mail, security codes, calendar, SharePoint and OneDrive. Microsoft has fixed it and users need do nothing; Varonis says Microsoft rated it critical while the MSRC page shows a base score of 6.5


summary_zh: |
  Varonis 三段链：① 搜索 URL 的 `q` 参数被当指令 ② 无害化是**生成后的后处理**，流式渲染中的 `<img>` 已先发出请求 ③ CSP 允许 `*.bing.com`，**Bing 图片搜索在服务端抓取指定 URL，浏览器 CSP 管不着**。诱导域名是 microsoft.com，Copilot 以用户权限运行 —— 受害者**点一次链接**即泄露邮件、安全验证码、日历、SharePoint、OneDrive。微软已修复、用户无需操作；Varonis 称微软给了 critical，MSRC 页面基本值 6.5

summary_ja: |
  Varonisの3段階チェーン：① 検索URLの`q`パラメータが指示として扱われる ② サニタイズが**生成後の後処理**であるため、ストリーミング描画内の`<img>`がすでにリクエストを発火させている ③ CSPが`*.bing.com`を許可しており、**Bing画像検索が指定URLをサーバー側で取得するため、ブラウザのCSPの範囲外になる**。誘導ドメインはmicrosoft.comで、Copilotはユーザーの権限で動作する——**リンクを1回クリックした**被害者はメール、セキュリティコード、カレンダー、SharePoint、OneDriveを漏らす。Microsoftは修正済みでユーザー側の対応は不要。VaronisはMicrosoftがcriticalと評価したと述べているが、MSRCのページにはベーススコア6.5と表示されている

summary_ko: |
  Varonis의 3단계 사슬: ① 검색 URL의 `q` 매개변수가 지시로 취급된다 ② 정제가 **생성 후 후처리**라서 스트리밍 렌더의 `<img>`는 이미 요청을 발사한 뒤다 ③ CSP가 `*.bing.com`을 허용하고, **Bing 이미지 검색이 지정된 URL을 서버 측에서 가져와 브라우저 CSP의 손이 닿지 않는다**. 유인 도메인은 microsoft.com이며 Copilot은 사용자 권한으로 실행되므로, **링크 하나를 클릭한** 피해자는 메일, 보안 코드, 캘린더, SharePoint, OneDrive를 유출당한다. 마이크로소프트는 수정했고 사용자가 할 일은 없다. Varonis는 마이크로소프트가 이를 치명적으로 평가했다고 하지만 MSRC 페이지의 기본 점수는 6.5다

summary_de: |
  Die dreistufige Kette von Varonis: ① Der `q`-Parameter einer Such-URL wird als Anweisung behandelt ② Die Bereinigung erfolgt **als Nachbearbeitung nach der Generierung**, sodass ein `<img>` im Streaming-Rendering seine Anfrage bereits abgefeuert hat ③ Die CSP erlaubt `*.bing.com`, und **die Bing-Bildersuche ruft die angegebene URL serverseitig ab, außerhalb der Reichweite der Browser-CSP**. Die Köder-Domain ist microsoft.com, und Copilot läuft mit den Rechten des Nutzers — ein Opfer, das **einen Link anklickt**, gibt E-Mails, Sicherheitscodes, Kalender, SharePoint und OneDrive preis. Microsoft hat es behoben, für Nutzer ist nichts zu tun; Varonis sagt, Microsoft habe es als kritisch eingestuft, während die MSRC-Seite einen Basiswert von 6.5 zeigt

summary_fr: |
  La chaîne en trois étapes de Varonis : ① le paramètre `q` d'une URL de recherche est traité comme des instructions ② la sanitisation est **un post-traitement après génération**, si bien qu'un `<img>` dans le rendu en flux a déjà déclenché sa requête ③ la CSP autorise `*.bing.com`, et **la recherche d'images Bing récupère l'URL spécifiée côté serveur, hors de portée de la CSP du navigateur**. Le domaine d'hameçon est microsoft.com, et Copilot s'exécute avec les privilèges de l'utilisateur — une victime qui **clique sur un lien** laisse fuiter courrier, codes de sécurité, calendrier, SharePoint et OneDrive. Microsoft a corrigé et les utilisateurs n'ont rien à faire ; Varonis indique que Microsoft a classé le problème critique tandis que la page MSRC affiche un score de base de 6,5

summary_es: |
  La cadena de tres etapas de Varonis: ① el parámetro `q` de una URL de búsqueda se trata como instrucciones ② la sanitización es **procesamiento posterior a la generación**, así que un `<img>` en el render en streaming ya ha disparado su solicitud ③ el CSP permite `*.bing.com`, y **la búsqueda de imágenes de Bing obtiene la URL indicada del lado del servidor, fuera del alcance del CSP del navegador**. El dominio señuelo es microsoft.com, y Copilot se ejecuta con los privilegios del usuario — una víctima que **hace clic en un solo enlace** filtra correo, códigos de seguridad, calendario, SharePoint y OneDrive. Microsoft ya lo ha corregido y los usuarios no tienen que hacer nada; Varonis dice que Microsoft lo calificó de crítico, mientras que la página del MSRC muestra una puntuación base de 6.5

sources:
  - url: https://www.varonis.com/blog/searchleak
    label: Varonis
  - url: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42824
    label: MSRC

disputed: false
landmark: true
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# SearchLeak (CVE-2026-42824)

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

Varonis's three-stage chain: ① the `q` parameter of a search URL is treated as instructions ② sanitization is **post-processing after generation**, so an `<img>` in the streaming render has already fired its request ③ CSP allows `*.bing.com`, and **Bing image search fetches the specified URL server-side, out of reach of the browser CSP**. The lure domain is microsoft.com, and Copilot runs with the user's privileges — a victim who **clicks one link** leaks mail, security codes, calendar, SharePoint and OneDrive. Microsoft has fixed it and users need do nothing; Varonis says Microsoft rated it critical while the MSRC page shows a base score of 6.5

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["Exfiltration via the vendor's trusted domain<br/>image rendering · API · proxy"]:::step
    I["Data ends up with the attacker<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Varonis | <https://www.varonis.com/blog/searchleak> |
| 2 | MSRC | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42824> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-15` (raw: 2026-06-15, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-15-searchleak` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-06-01` [Attackers simply ask Meta's AI support bot for Instagram accounts](2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br>  <sub>Attackers simply ask Meta's AI support bot for Instagram accounts</sub>
- `2026-06-12` [Agentjacking: one public DSN hijacks AI coding agents](2026-06-12-agentjacking-public-dsn.md)<br>  <sub>Agentjacking: one public DSN hijacks AI coding agents</sub>
- `2026-06-24` [BioShocking: dumb the agent down first, then take the password](2026-06-24-bioshocking-agent-xian-jiao-sha.md)<br>  <sub>BioShocking: dumb the agent down first, then take the password</sub>
- `2026-06-08` [AgentForger: one link forges an "AI insider"](2026-06-08-agentforger-yi-tiao-lian-jie.md)<br>  <sub>AgentForger: one link forges an "AI insider"</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-15-searchleak.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
