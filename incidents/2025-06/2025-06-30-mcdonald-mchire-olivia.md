---
id: 2025-06-30-mcdonald-mchire-olivia
title: "McDonald's McHire \"Olivia\" hiring bot"
title_zh: "McDonald's McHire「Olivia」招聘机器人"
title_ja: "マクドナルドのMcHire採用ボット「Olivia」"
title_ko: "맥도날드 McHire \"Olivia\" 채용 봇"
title_de: "McDonald's McHire: der Einstellungs-Bot „Olivia“"
title_fr: "Le bot de recrutement « Olivia » de McHire (McDonald's)"
title_es: "El bot de contratación \"Olivia\" de McDonald's McHire"
date: 2025-06-30
date_precision: day
date_raw: "2025-06-30"

kind: incident
type: [CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [US]

summary: |
  Researchers Ian Carroll + Sam Curry found that a Paradox.ai test admin account had the username/password `123456` and no MFA; combined with an IDOR (changing the applicant ID in the URL) it could read other people's names/emails/phone numbers/chat logs. **Up to 64 million records were theoretically reachable**. ⚠️ **Paradox claims only 5 were actually accessed**; fixed within a day


summary_zh: |
  研究者 Ian Carroll + Sam Curry 发现 Paradox.ai 测试管理账号用户名/密码均为 `123456` 且无 MFA，配合 IDOR（改 URL 里的申请者 ID）可读取他人姓名/邮箱/电话/聊天记录。**理论可及 6,400 万条记录**。⚠️ **Paradox 声称实际仅 5 条被访问**，一天内修复

summary_ja: |
  研究者のIan Carroll氏とSam Curry氏が、Paradox.aiのテスト管理者アカウントのユーザー名/パスワードが`123456`でMFAもなかったことを発見。IDOR（URL内の応募者IDを変更）と組み合わせると、他人の氏名/メール/電話番号/チャットログを読み取れた。**理論上は最大6,400万件のレコードに到達可能**。⚠️ **Paradoxは実際にアクセスされたのは5件のみと主張**。1日以内に修正

summary_ko: |
  연구자 Ian Carroll과 Sam Curry는 Paradox.ai의 테스트 관리자 계정 아이디/비밀번호가 `123456`이고 MFA가 없음을 발견했다. 여기에 IDOR(URL의 지원자 ID 변경)를 결합하면 다른 사람의 이름/이메일/전화번호/채팅 기록을 읽을 수 있었다. **이론적으로 최대 6,400만 건의 레코드에 도달 가능**했다. ⚠️ **Paradox는 실제로 접근된 것은 5건뿐이라고 주장한다**. 하루 만에 수정되었다

summary_de: |
  Die Forscher Ian Carroll + Sam Curry fanden heraus, dass ein Test-Admin-Konto von Paradox.ai den Benutzernamen/das Passwort `123456` und kein MFA hatte; zusammen mit einer IDOR (Ändern der Bewerber-ID in der URL) konnten so Namen/E-Mails/Telefonnummern/Chatprotokolle anderer Personen gelesen werden. **Bis zu 64 Millionen Datensätze waren theoretisch erreichbar**. ⚠️ **Paradox behauptet, es seien tatsächlich nur 5 abgerufen worden**; innerhalb eines Tages behoben

summary_fr: |
  Les chercheurs Ian Carroll et Sam Curry ont découvert qu'un compte admin de test Paradox.ai avait pour identifiant/mot de passe `123456` et pas de MFA ; combiné à un IDOR (changer l'ID de candidat dans l'URL), il permettait de lire les noms/e-mails/téléphones/journaux de chat d'autres personnes. **Jusqu'à 64 millions d'enregistrements étaient théoriquement accessibles**. ⚠️ **Paradox affirme que seuls 5 l'ont réellement été** ; corrigé en une journée

summary_es: |
  Los investigadores Ian Carroll + Sam Curry descubrieron que una cuenta de administrador de prueba de Paradox.ai tenía usuario/contraseña `123456` y no tenía MFA; combinado con un IDOR (cambiar el ID del solicitante en la URL) podía leer nombres, correos, teléfonos y registros de chat de otras personas. **Hasta 64 millones de registros eran alcanzables en teoría**. ⚠️ **Paradox afirma que solo se accedió a 5**; corregido en un día

sources:
  - url: https://incidentdatabase.ai/cite/1179/
    label: "AIID #1179"
  - url: https://www.csoonline.com/article/4020919/mcdonalds-ai-hiring-tools-password-123456-exposes-data-of-64m-applicants.html
    label: CSO

disputed: false
landmark: true
scan_month: 2025-06
scan_ref: "SCAN.md §5 2025-06"
---

# McDonald's McHire "Olivia" hiring bot

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

Researchers Ian Carroll + Sam Curry found that a Paradox.ai test admin account had the username/password `123456` and no MFA; combined with an IDOR (changing the applicant ID in the URL) it could read other people's names/emails/phone numbers/chat logs. **Up to 64 million records were theoretically reachable**. ⚠️ **Paradox claims only 5 were actually accessed**; fixed within a day

## Attack chain

```mermaid
flowchart LR
    E["Credentials within the agent's reach"]:::entry
    S0["The agent retrieves and uses it"]:::step
    I["Credential abuse"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | AIID #1179 | <https://incidentdatabase.ai/cite/1179/> |
| 2 | CSO | <https://www.csoonline.com/article/4020919/mcdonalds-ai-hiring-tools-password-123456-exposes-data-of-64m-applicants.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-06-30` (raw: 2025-06-30, precision `day`) |
| Kind | Incident `incident` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [United States](../../regions/us.md) |
| Archive ID | `2025-06-30-mcdonald-mchire-olivia` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2025-06-13` [Smithery.ai path traversal](2025-06-13-smithery-ai-lu-jing-chuan-yue.md)<br>  <sub>Smithery.ai path traversal</sub>
- `2025-07-01` [RoguePilot](../2025-07/2025-07-01-roguepilot.md)<br>  <sub>RoguePilot</sub>
- `2025-07-09` [McHire flaw goes public](../2025-07/2025-07-09-mchire-lou-dong-gong-kai.md)<br>  <sub>McHire flaw goes public</sub>
- `2025-08-08` [Salesloft Drift OAuth token theft](../2025-08/2025-08-08-salesloft-drift-oauth-theft.md)<br>  <sub>Salesloft Drift OAuth token theft</sub>

---

[← 2025-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-06/2025-06-30-mcdonald-mchire-olivia.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
