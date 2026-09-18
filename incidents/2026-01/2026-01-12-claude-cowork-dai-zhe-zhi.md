---
id: 2026-01-12-claude-cowork-dai-zhe-zhi
title: "Claude Cowork ships with known vulnerabilities"
title_zh: "Claude Cowork 带着已知漏洞发布"
title_ja: "Claude Coworkは既知の脆弱性を抱えて出荷"
title_ko: "Claude Cowork, 알려진 취약점을 안고 출시되다"
title_de: "Claude Cowork erscheint mit bekannten Schwachstellen"
title_fr: "Claude Cowork sort avec des vulnérabilités connues"
title_es: "Claude Cowork se lanza con vulnerabilidades conocidas"
date: 2026-01-12
date_precision: day
date_raw: "2026-01-12"

kind: vulnerability
type: [IPI, EXFIL]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Cowork shipped on 01-12 and opened to all $20/month Pro users four days later. **Within 48 hours** PromptArmor showed that a Word document containing a 1pt white-text prompt injection was enough to make Cowork upload the user's financial files (**including partial Social Security numbers**) to the attacker's Anthropic account — no exploit, no malware, the user merely opened the file.
  ⚠️ **The key point is that this was not an accident**: the underlying prompt injection flaw had been reported to Anthropic and confirmed **three months before** Cowork shipped, and **was still unfixed at release**; Anthropic had confirmed the defect as early as **2025-10-30**. The flaw was rated **CVSS 10/10**. Anthropic's written response was that the defect "**falls outside our current threat model**", and it advised users not to connect Cowork to sensitive documents
  ⚠️ IPA issue 2026-03 tags this record `[2025-05]`, which contradicts the release date and appears to be a typo


summary_zh: |
  Cowork 01-12 发布、四天后向全部 $20/月 Pro 用户开放。**48 小时内**被 PromptArmor 证实：一份含 1pt 白字提示注入的 Word 文档即可让 Cowork 把用户财务文件（**含部分社保号**）上传到攻击者的 Anthropic 账户 —— 无 exploit、无恶意软件，用户只是打开了文件。
  ⚠️ **关键在于这不是意外**：底层提示注入漏洞在 Cowork 发布**三个月前**就已报告给 Anthropic 并获确认，**发布时仍未修复**；Anthropic 早在 **2025-10-30** 即确认该缺陷。漏洞被评为 **CVSS 10/10**。Anthropic 的书面回应是该缺陷「**落在我们当前的威胁模型之外**」，并建议用户不要把 Cowork 连到敏感文档
  ⚠️ IPA 2026-03 号将此条标为 `[2025-05]`，与发布时间矛盾，疑为笔误

summary_ja: |
  Coworkは01-12に出荷され、4日後に月額20ドルのProユーザー全員に開放された。**48時間以内**にPromptArmorが、1ptの白文字プロンプトインジェクションを含むWord文書だけで、Coworkにユーザーの財務ファイル（**社会保障番号の一部を含む**）を攻撃者のAnthropicアカウントへアップロードさせることを示した——エクスプロイトもマルウェアも不要で、ユーザーはただファイルを開いただけだった。
  ⚠️ **重要なのは、これが事故ではないこと**：基盤となるプロンプトインジェクション欠陥はCoworkの出荷の**3か月前に**Anthropicへ報告され確認済みであり、**リリース時点でも未修正**だった。Anthropicは早くも**2025-10-30**にこの欠陥を確認していた。欠陥は**CVSS 10/10**と評価された。Anthropicの書面での回答は、この欠陥は「**現在の脅威モデルの範囲外**」というもので、Coworkを機密文書に接続しないよう助言した
  ⚠️ IPA 2026-03号はこの記録に`[2025-05]`のタグを付けており、リリース日と矛盾するため誤記と思われる

summary_ko: |
  Cowork은 01-12에 출시되어 나흘 뒤 월 20달러 Pro 사용자 전체에 개방되었다. **48시간 이내에** PromptArmor는 1pt 흰색 텍스트 프롬프트 인젝션이 든 Word 문서만으로 Cowork이 사용자의 금융 파일(**부분적인 사회보장번호 포함**)을 공격자의 Anthropic 계정으로 업로드하게 만들 수 있음을 보였다 — 익스플로잇도 악성코드도 없이, 사용자가 파일을 열기만 하면 되었다.
  ⚠️ **핵심은 이것이 사고가 아니라는 점이다**: 근본이 되는 프롬프트 인젝션 결함은 Cowork 출시 **3개월 전에** Anthropic에 신고되어 확인되었고 **출시 시점에도 수정되지 않았다**. Anthropic은 **2025-10-30**에 이미 결함을 확인했다. 결함 등급은 **CVSS 10/10**이었다. Anthropic의 공식 서면 답변은 이 결함이 "**현재 위협 모델의 범위를 벗어난다**"는 것이었고, 사용자에게 Cowork을 민감한 문서에 연결하지 말라고 권고했다
  ⚠️ IPA 2026-03호는 이 기록에 `[2025-05]` 태그를 달았는데, 이는 출시일과 모순되며 오타로 보인다

summary_de: |
  Cowork erschien am 01-12 und wurde vier Tage später für alle Pro-Nutzer zu $20/Monat geöffnet. **Innerhalb von 48 Stunden** zeigte PromptArmor, dass ein Word-Dokument mit einer Prompt-Injection in 1pt weißem Text genügte, damit Cowork die Finanzdateien des Nutzers (**darunter teilweise Sozialversicherungsnummern**) auf das Anthropic-Konto des Angreifers hochlud — kein Exploit, keine Malware, der Nutzer öffnete lediglich die Datei.
  ⚠️ **Der entscheidende Punkt ist, dass dies kein Zufall war**: Die zugrunde liegende Prompt-Injection-Schwachstelle war **drei Monate vor** dem Erscheinen von Cowork an Anthropic gemeldet und bestätigt worden und **war bei der Veröffentlichung noch nicht behoben**; Anthropic hatte den Defekt bereits am **2025-10-30** bestätigt. Die Schwachstelle wurde mit **CVSS 10/10** bewertet. Anthropics schriftliche Antwort war, der Defekt „**falle außerhalb unseres aktuellen Bedrohungsmodells**“, und sie riet Nutzern davon ab, Cowork mit sensiblen Dokumenten zu verbinden
  ⚠️ Die IPA-Ausgabe 2026-03 versieht diesen Eintrag mit dem Tag `[2025-05]`, was dem Veröffentlichungsdatum widerspricht und ein Tippfehler zu sein scheint

summary_fr: |
  Cowork est sorti le 01-12 et s'est ouvert à tous les utilisateurs Pro à 20 $/mois quatre jours plus tard. **En 48 heures**, PromptArmor a montré qu'un document Word contenant une injection de prompt en texte blanc de 1 pt suffisait à faire téléverser par Cowork les fichiers financiers de l'utilisateur (**y compris des numéros de sécurité sociale partiels**) vers le compte Anthropic de l'attaquant — sans exploit ni malware, l'utilisateur ayant simplement ouvert le fichier.
  ⚠️ **Le point clé est qu'il ne s'agissait pas d'un accident** : la faille d'injection de prompt sous-jacente avait été signalée à Anthropic et confirmée **trois mois avant** la sortie de Cowork, et **n'était toujours pas corrigée à la publication** ; Anthropic avait confirmé le défaut dès le **2025-10-30**. La faille a été notée **CVSS 10/10**. La réponse écrite d'Anthropic était que le défaut « **sort de notre modèle de menace actuel** », et elle conseillait aux utilisateurs de ne pas connecter Cowork à des documents sensibles
  ⚠️ Le numéro 2026-03 de l'IPA étiquette cet enregistrement `[2025-05]`, ce qui contredit la date de sortie et semble être une coquille

summary_es: |
  Cowork se lanzó el 01-12 y se abrió a todos los usuarios Pro de $20/mes cuatro días después. **En 48 horas** PromptArmor demostró que un documento de Word con una inyección de prompt en texto blanco de 1pt bastaba para que Cowork subiera los archivos financieros del usuario (**incluidos números de Seguro Social parciales**) a la cuenta de Anthropic del atacante — sin exploit, sin malware, el usuario solo abrió el archivo.
  ⚠️ **Lo clave es que no fue un accidente**: el fallo subyacente de inyección de prompt había sido reportado a Anthropic y confirmado **tres meses antes** del lanzamiento de Cowork, y **seguía sin corregir en el lanzamiento**; Anthropic había confirmado el defecto ya el **2025-10-30**. El fallo se calificó **CVSS 10/10**. La respuesta escrita de Anthropic fue que el defecto "**queda fuera de nuestro modelo de amenaza actual**", y aconsejó a los usuarios no conectar Cowork a documentos sensibles
  ⚠️ El número 2026-03 de IPA etiqueta este registro como `[2025-05]`, lo que contradice la fecha de lanzamiento y parece un error tipográfico

sources:
  - url: https://www.promptarmor.com/resources/claude-cowork-exfiltrates-files
    label: PromptArmor
  - url: https://www.govinfosecurity.com/anthropics-cowork-shipped-known-vulnerability-a-30553
    label: GovInfoSecurity
  - url: https://securityboulevard.com/2026/01/vulnerability-in-anthropics-claude-code-shows-up-in-cowork/
    label: Security Boulevard

disputed: false
landmark: true
scan_month: 2026-01
scan_ref: "SCAN.md §6 2026-01"
---

# Claude Cowork ships with known vulnerabilities

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

Cowork shipped on 01-12 and opened to all $20/month Pro users four days later. **Within 48 hours** PromptArmor showed that a Word document containing a 1pt white-text prompt injection was enough to make Cowork upload the user's financial files (**including partial Social Security numbers**) to the attacker's Anthropic account — no exploit, no malware, the user merely opened the file.

⚠️ **The key point is that this was not an accident**: the underlying prompt injection flaw had been reported to Anthropic and confirmed **three months before** Cowork shipped, and **was still unfixed at release**; Anthropic had confirmed the defect as early as **2025-10-30**. The flaw was rated **CVSS 10/10**. Anthropic's written response was that the defect "**falls outside our current threat model**", and it advised users not to connect Cowork to sensitive documents

⚠️ IPA issue 2026-03 tags this record `[2025-05]`, which contradicts the release date and appears to be a typo

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["agent reads it and executes it as instructions"]:::step
    S1["Exfiltrated via vendor-trusted domains<br/>image rendering · APIs · proxies"]:::step
    I["Data ends up in the attacker's hands<br/><i>(vulnerability disclosed · no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | PromptArmor | <https://www.promptarmor.com/resources/claude-cowork-exfiltrates-files> |
| 2 | GovInfoSecurity | <https://www.govinfosecurity.com/anthropics-cowork-shipped-known-vulnerability-a-30553> |
| 3 | Security Boulevard | <https://securityboulevard.com/2026/01/vulnerability-in-anthropics-claude-code-shows-up-in-cowork/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-01-12` (raw: 2026-01-12, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-01-12-claude-cowork-dai-zhe-zhi` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-01-12` [Superhuman AI indirect prompt injection](2026-01-12-superhuman-jian-jie-ti-shi.md)<br>  <sub>Superhuman AI indirect prompt injection</sub>
- `2026-01-14` [Microsoft Copilot Personal "Reprompt"](2026-01-14-microsoft-copilot-personal-reprompt.md)<br>  <sub>Microsoft Copilot Personal "Reprompt"</sub>
- `2026-01-07` [Four productivity tools hit the lethal trifecta in nine days](2026-01-07-lethal-trifecta-four-tools.md)<br>  <sub>Four productivity tools hit the lethal trifecta in nine days</sub>
- `2026-02-09` [Clinejection](../2026-02/2026-02-09-clinejection.md)<br>  <sub>Clinejection</sub>

---

[← 2026-01 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-01/2026-01-12-claude-cowork-dai-zhe-zhi.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
