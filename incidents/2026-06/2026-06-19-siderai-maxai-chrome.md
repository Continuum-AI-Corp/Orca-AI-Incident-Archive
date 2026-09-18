---
id: 2026-06-19-siderai-maxai-chrome
title: "Flaws in the SiderAI (10M) and MaxAI (1M) Chrome extensions"
title_zh: "SiderAI(1,000 万) / MaxAI(100 万) Chrome 扩展漏洞"
title_ja: "SiderAI（1,000万）とMaxAI（100万）のChrome拡張機能の欠陥"
title_ko: "SiderAI(1,000만)와 MaxAI(100만) Chrome 확장 프로그램의 결함"
title_de: "Schwachstellen in den Chrome-Erweiterungen SiderAI (10M) und MaxAI (1M)"
title_fr: "Failles dans les extensions Chrome SiderAI (10 M) et MaxAI (1 M)"
title_es: "Fallos en las extensiones de Chrome SiderAI (10M) y MaxAI (1M)"
date: 2026-06-19
date_precision: day
date_raw: "2026-06-19"

kind: research
type: [CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Rebora Security: neither extension's content script validates the origin of web-page messages. **MaXSS** lets any website invoke permissions that should be extension-only (listing tabs, taking screenshots, opening arbitrary sites in hidden tabs, and achieving arbitrary source-code execution by replacing scripts and stripping CSP headers); **Spyder** combines internal APIs that lift embedding restrictions with synthetic clicks/input to place an arbitrary site inside an invisible iframe and drive it (proof: instructing the victim's Gemini and carrying off the conversation share URL). Self-assessed CVSS3 score of 10.0. **Neither vendor responded, and the public versions were still unfixed when the report was published**


summary_zh: |
  Rebora Security：两者 content-script 均不校验网页消息来源。**MaXSS** 让任意网站调用本应仅限扩展的权限（列标签页、截屏、隐藏标签页打开任意站点，替换脚本 + 删 CSP 头达成任意源代码执行）；**Spyder** 组合解除嵌入限制的内部 API 与伪造点击/输入，把任意站点塞进不可见 iframe 操作（实证：向受害者的 Gemini 下指令并带走会话分享 URL）。CVSS3 自评 10.0。**两家厂商均未回应，报告时公开版仍未修复**

summary_ja: |
  Rebora Security：どちらの拡張機能も、コンテンツスクリプトがWebページからのメッセージの送信元を検証していない。**MaXSS**は任意のWebサイトに本来拡張機能専用の権限を呼び出させる（タブの列挙、スクリーンショット取得、隠しタブでの任意サイトのオープン、スクリプトの置き換えとCSPヘッダーの除去による任意のソースコード実行）。**Spyder**は埋め込み制限を解除する内部APIと合成クリック／入力を使って任意のサイトを不可視iframe内に配置して操作する（実証：被害者のGeminiに指示を出し会話の共有URLを持ち去る）。自己評価のCVSS3スコアは10.0。**どちらのベンダーも応答せず、報告の公開時点で公開版は未修正だった**

summary_ko: |
  Rebora Security: 두 확장 프로그램 모두 콘텐츠 스크립트가 웹 페이지 메시지의 출처를 검증하지 않는다. **MaXSS**는 어떤 웹사이트든 확장 프로그램 전용이어야 할 권한(탭 나열, 스크린샷 촬영, 숨겨진 탭에서 임의 사이트 열기, 스크립트 교체와 CSP 헤더 제거로 임의 소스 코드 실행)을 호출하게 한다. **Spyder**는 임베딩 제한을 해제하는 내부 API와 합성 클릭/입력을 결합해 임의 사이트를 보이지 않는 iframe에 넣고 조작한다(증명: 피해자의 Gemini에 지시를 내리고 대화 공유 URL을 빼내기). 자체 평가 CVSS3 점수는 10.0이다. **두 벤더 모두 응답하지 않았고 보고서 발간 시점에도 공개 버전은 미수정 상태였다**

summary_de: |
  Rebora Security: Keine der beiden Erweiterungen validiert im Content Script die Herkunft von Nachrichten der Webseite. **MaXSS** erlaubt jeder Website, Berechtigungen aufzurufen, die eigentlich nur der Erweiterung zustehen (Tabs auflisten, Screenshots erstellen, beliebige Seiten in versteckten Tabs öffnen und durch Ersetzen von Skripten und Entfernen von CSP-Headern beliebigen Quellcode ausführen); **Spyder** kombiniert interne APIs, die Einbettungsbeschränkungen aufheben, mit synthetischen Klicks/Eingaben, um eine beliebige Seite in einem unsichtbaren iframe zu platzieren und zu steuern (Nachweis: Anweisung an das Gemini des Opfers und Abgreifen der URL zum Teilen der Unterhaltung). Selbst eingeschätzter CVSS3-Score von 10.0. **Keiner der beiden Anbieter reagierte, und die öffentlichen Versionen waren bei Veröffentlichung des Berichts noch unbehoben**

summary_fr: |
  Rebora Security : le content script d'aucune des deux extensions ne valide l'origine des messages de la page web. **MaXSS** permet à n'importe quel site web d'invoquer des permissions qui devraient être réservées à l'extension (lister les onglets, prendre des captures d'écran, ouvrir des sites arbitraires dans des onglets cachés, et obtenir une exécution de code source arbitraire en remplaçant des scripts et en retirant les en-têtes CSP) ; **Spyder** combine des API internes qui lèvent les restrictions d'intégration avec des clics/saisies synthétiques pour placer un site arbitraire dans un iframe invisible et le piloter (preuve : donner des instructions au Gemini de la victime et emporter l'URL de partage de la conversation). Score CVSS3 auto-évalué de 10,0. **Aucun des deux fournisseurs n'a répondu, et les versions publiques n'étaient toujours pas corrigées à la publication du rapport**

summary_es: |
  Rebora Security: el content script de ninguna de las dos extensiones valida el origen de los mensajes de la página web. **MaXSS** permite que cualquier sitio web invoque permisos que deberían ser exclusivos de la extensión (listar pestañas, hacer capturas de pantalla, abrir sitios arbitrarios en pestañas ocultas y lograr ejecución de código fuente arbitrario reemplazando scripts y eliminando cabeceras CSP); **Spyder** combina API internas que levantan las restricciones de incrustación con clics y entradas sintéticas para colocar un sitio arbitrario dentro de un iframe invisible y controlarlo (prueba: dar instrucciones al Gemini de la víctima y llevarse la URL de la conversación compartida). Autoevaluación CVSS3 de 10.0. **Ninguno de los dos proveedores respondió, y las versiones públicas seguían sin corregir cuando se publicó el informe**

sources:
  - url: https://rebora.io/blog/spyder-and-maxss-chrome-extension-vulnerabilities-put-millions-at-risk
    label: Rebora Security

disputed: false
landmark: false
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# Flaws in the SiderAI (10M) and MaxAI (1M) Chrome extensions

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

Rebora Security: neither extension's content script validates the origin of web-page messages. **MaXSS** lets any website invoke permissions that should be extension-only (listing tabs, taking screenshots, opening arbitrary sites in hidden tabs, and achieving arbitrary source-code execution by replacing scripts and stripping CSP headers); **Spyder** combines internal APIs that lift embedding restrictions with synthetic clicks/input to place an arbitrary site inside an invisible iframe and drive it (proof: instructing the victim's Gemini and carrying off the conversation share URL). Self-assessed CVSS3 score of 10.0. **Neither vendor responded, and the public versions were still unfixed when the report was published**

## Attack chain

```mermaid
flowchart LR
    E["Credentials within an agent's reach"]:::entry
    S0["The agent picks them up and calls out"]:::step
    I["Credential abuse<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Rebora Security | <https://rebora.io/blog/spyder-and-maxss-chrome-extension-vulnerabilities-put-millions-at-risk> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-19` (raw: 2026-06-19, precision `day`) |
| Kind | Research demo `research` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-19-siderai-maxai-chrome` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2026-06-01` [Miasma worm](2026-06-01-miasma-worm.md)<br>  <sub>Miasma worm</sub>
- `2026-06-01` [Attackers simply ask Meta's AI support bot for Instagram accounts](2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br>  <sub>Attackers simply ask Meta's AI support bot for Instagram accounts</sub>
- `2026-06-17` [Sapphire Sleet poisons every Mastra AI scope in 88 minutes](2026-06-17-sapphire-sleet-mastra-88-minutes.md)<br>  <sub>Sapphire Sleet poisons every Mastra AI scope in 88 minutes</sub>
- `2026-06-04` [Claude Oceanus-v1-p illegally redistributed](2026-06-04-claude-oceanus-fei-fa-fen.md)<br>  <sub>Claude Oceanus-v1-p illegally redistributed</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-19-siderai-maxai-chrome.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
