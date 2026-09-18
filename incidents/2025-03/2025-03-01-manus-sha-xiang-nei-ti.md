---
id: 2025-03-01-manus-sha-xiang-nei-ti
title: "Manus AI leaks in-sandbox prompts and runtime code"
title_zh: "Manus AI 沙箱内提示与运行时代码泄露"
title_ja: "Manus AI、サンドボックス内のプロンプトとランタイムコードが漏えい"
title_ko: "Manus AI, 샌드박스 내부 프롬프트와 런타임 코드 유출"
title_de: "Manus AI gibt In-Sandbox-Prompts und Laufzeitcode preis"
title_fr: "Manus AI expose des prompts en bac à sable et du code d'exécution"
title_es: "Manus AI filtra prompts y código de ejecución dentro del sandbox"
date: 2025-03-01
date_precision: month
date_raw: "2025-03"

kind: vulnerability
type: [SANDBOX]
severity: medium
confidence: B
real_harm: false
ai_involvement: confirmed

region: [CN]

summary: |
  A user only had to ask Manus to print the contents of an internal directory (such as `/opt/.manus/`) to get back parts of the system prompt and runtime code. Co-founder and chief scientist Peak Ji responded that **users could already access the sandbox directly**, that each session's sandbox is isolated, that the code inside the sandbox only receives instructions and was therefore only lightly obfuscated, and that the tool was never designed to be secret.
  💡 Why it is listed: this is a rare first-half-2025 example of a **boundary issue in a Chinese agent product itself**, and the vendor's response treats "the sandbox is accessible" as a design premise — the same risk model that later appeared with OpenClaw


summary_zh: |
  用户只要让 Manus 输出内部目录（如 `/opt/.manus/`）的内容，即可取回部分系统提示与运行时代码。联合创始人兼首席科学家季逸超回应称**用户本就可直接访问沙箱**、每个会话沙箱隔离、沙箱内代码只负责接收指令因此只做了轻度混淆，并称工具设计本就不保密。
  💡 收录理由：这是 2025 年上半年少见的**中国 agent 产品自身的边界问题**，且厂商回应把「沙箱可访问」当作设计前提 —— 与后来 OpenClaw 的风险模型同源

summary_ja: |
  ユーザーがManusに内部ディレクトリ（例：`/opt/.manus/`）の内容を出力するよう頼むだけで、システムプロンプトの一部とランタイムコードが返ってきた。共同創業者兼チーフサイエンティストのPeak Ji氏は、**ユーザーは以前からサンドボックスに直接アクセスできた**こと、各セッションのサンドボックスは分離されていること、サンドボックス内のコードは指示を受け取るだけなので軽度の難読化にとどめたこと、ツールは決して秘密にする設計ではなかったと回答した。
  💡 掲載理由：2025年前半では珍しい、**中国のエージェント製品自体の境界問題**の事例であり、ベンダーの回答は「サンドボックスにアクセスできる」ことを設計前提として扱っている——後にOpenClawで現れたのと同じリスクモデルである

summary_ko: |
  사용자가 Manus에게 내부 디렉터리(예: `/opt/.manus/`)의 내용을 출력해 달라고 요청하기만 하면 시스템 프롬프트와 런타임 코드의 일부를 돌려받을 수 있었다. 공동창업자 겸 최고과학자 Peak Ji는 **사용자가 이미 샌드박스에 직접 접근할 수 있었고**, 세션별 샌드박스는 격리되며, 샌드박스 내부 코드는 지시만 받아 난독화가 가볍게만 되어 있었고, 애초에 비밀로 설계된 도구가 아니라고 답했다.
  💡 등재 이유: 2025년 상반기 중국계 에이전트 제품 자체의 **경계 문제**를 보여준 드문 사례이며, 벤더의 대응이 "샌드박스는 접근 가능하다"를 설계 전제로 삼았다 — 이후 OpenClaw에서 나타난 것과 같은 위험 모델이다

summary_de: |
  Ein Nutzer musste Manus nur bitten, den Inhalt eines internen Verzeichnisses (etwa `/opt/.manus/`) auszugeben, um Teile des System-Prompts und des Laufzeitcodes zurückzubekommen. Mitgründer und Chefwissenschaftler Peak Ji entgegnete, **Nutzer könnten bereits direkt auf die Sandbox zugreifen**, die Sandbox jeder Sitzung sei isoliert, der Code in der Sandbox erhalte nur Anweisungen und sei daher nur leicht verschleiert, und das Tool sei nie als Geheimnis gedacht gewesen.
  💡 Warum es aufgeführt wird: Dies ist ein seltenes Beispiel aus der ersten Hälfte von 2025 für ein **Grenzproblem im chinesischen Agentenprodukt selbst**, und die Antwort des Anbieters behandelt „die Sandbox ist zugänglich“ als Designprämisse — dasselbe Risikomodell, das später bei OpenClaw auftauchte

summary_fr: |
  Un utilisateur a simplement demandé à Manus d'afficher le contenu d'un répertoire interne (comme `/opt/.manus/`) pour récupérer des parties du prompt système et du code d'exécution. Le cofondateur et directeur scientifique Peak Ji a répondu que **les utilisateurs pouvaient déjà accéder directement au bac à sable**, que le bac à sable de chaque session est isolé, que le code à l'intérieur ne reçoit que des instructions et n'était donc que légèrement obfusqué, et que l'outil n'a jamais été conçu pour être secret.
  💡 Pourquoi il est répertorié : c'est un rare exemple du premier semestre 2025 d'un **problème de frontière dans un produit d'agent chinois lui-même**, et la réponse du fournisseur traite « le bac à sable est accessible » comme une prémisse de conception — le même modèle de risque réapparu plus tard avec OpenClaw

summary_es: |
  A un usuario le bastó pedirle a Manus que imprimiera el contenido de un directorio interno (como `/opt/.manus/`) para obtener partes del system prompt y del código de ejecución. El cofundador y científico jefe Peak Ji respondió que **los usuarios ya podían acceder directamente al sandbox**, que el sandbox de cada sesión está aislado, que el código dentro del sandbox solo recibe instrucciones y por eso estaba apenas ligeramente ofuscado, y que la herramienta nunca fue diseñada para ser secreta.
  💡 Por qué está listado: es un ejemplo poco común de la primera mitad de 2025 de un **problema de límites en el propio producto de un agente chino**, y la respuesta del proveedor trata "el sandbox es accesible" como una premisa de diseño — el mismo modelo de riesgo que apareció después con OpenClaw

sources:
  - url: https://www.aibase.com/news/16138
    label: AIBase

disputed: false
landmark: false
scan_month: 2025-03
scan_ref: "SCAN.md §5 2025-03"
---

# Manus AI leaks in-sandbox prompts and runtime code

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## Summary

A user only had to ask Manus to print the contents of an internal directory (such as `/opt/.manus/`) to get back parts of the system prompt and runtime code. Co-founder and chief scientist Peak Ji responded that **users could already access the sandbox directly**, that each session's sandbox is isolated, that the code inside the sandbox only receives instructions and was therefore only lightly obfuscated, and that the tool was never designed to be secret.

💡 Why it is listed: this is a rare first-half-2025 example of a **boundary issue in a Chinese agent product itself**, and the vendor's response treats "the sandbox is accessible" as a design premise — the same risk model that later appeared with OpenClaw

## Attack chain

```mermaid
flowchart LR
    E["Evaluation / container environment"]:::entry
    S0["Residual egress path"]:::step
    I["Escape to a real system<br/><i>(flaw disclosed, no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | AIBase | <https://www.aibase.com/news/16138> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-03-01` (raw: 2025-03, precision `month`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape |
| Severity | **Medium** `medium` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [China](../../regions/cn.md) |
| Archive ID | `2025-03-01-manus-sha-xiang-nei-ti` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2025-01-31` [Two GitHub Copilot flaws](../2025-01/2025-01-31-github-copilot-shuang-lou-dong.md)<br>  <sub>Two GitHub Copilot flaws</sub>
- `2025-07-21` [Claude Code hooks RCE](../2025-07/2025-07-21-claude-code-hooks-rce.md)<br>  <sub>Claude Code hooks RCE</sub>
- `2025-07-28` [Gemini CLI silent code execution](../2025-07/2025-07-28-gemini-cli-jing-mo-dai.md)<br>  <sub>Gemini CLI silent code execution</sub>
- `2025-08-01` [Cursor CurXecute (CVE-2025-54135)](../2025-08/2025-08-01-cursor-curxecute.md)<br>  <sub>Cursor CurXecute (CVE-2025-54135)</sub>

---

[← 2025-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-03/2025-03-01-manus-sha-xiang-nei-ti.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
