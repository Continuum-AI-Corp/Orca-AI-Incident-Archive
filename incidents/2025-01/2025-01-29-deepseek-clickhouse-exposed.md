---
id: 2025-01-29-deepseek-clickhouse-exposed
title: "DeepSeek ClickHouse database left wide open"
title_zh: "DeepSeek ClickHouse 数据库裸奔"
title_ja: "DeepSeekのClickHouseデータベースが無防備なまま公開"
title_ko: "DeepSeek ClickHouse 데이터베이스, 무방비로 노출"
title_de: "DeepSeek-ClickHouse-Datenbank stand weit offen"
title_fr: "La base ClickHouse de DeepSeek laissée grande ouverte"
title_es: "Base de datos ClickHouse de DeepSeek expuesta sin protección"
date: 2025-01-29
date_precision: day
date_raw: "2025-01-29"

kind: incident
type: [INFRA]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [CN]

summary: |
  Wiz found unauthenticated public ClickHouse instances (`oauth2callback.deepseek.com:9000`, `dev.deepseek.com:9000`) where the `/play` path allowed running arbitrary SQL. The `log_stream` table held **over 1M log entries** (earliest 2025-01-06) with plaintext chat records, API keys and backend details. DeepSeek shut it down quickly after the report


summary_zh: |
  Wiz 发现无认证公网 ClickHouse（`oauth2callback.deepseek.com:9000`、`dev.deepseek.com:9000`），经 `/play` 路径可直接跑任意 SQL。`log_stream` 表 **100 万+ 条日志**（最早 2025-01-06），含明文聊天记录、API 密钥、后端细节。DeepSeek 接报后迅速关闭

summary_ja: |
  Wizは認証なしで公開されていたClickHouseインスタンス（`oauth2callback.deepseek.com:9000`、`dev.deepseek.com:9000`）を発見した。`/play`パスでは任意のSQLを実行できた。`log_stream`テーブルには**100万件超のログエントリ**（最古は2025-01-06）があり、平文のチャット記録、APIキー、バックエンドの詳細が含まれていた。DeepSeekは報告後すぐに閉鎖した

summary_ko: |
  Wiz는 인증이 필요 없는 공개 ClickHouse 인스턴스(`oauth2callback.deepseek.com:9000`, `dev.deepseek.com:9000`)를 발견했으며 `/play` 경로에서 임의 SQL을 실행할 수 있었다. `log_stream` 테이블에는 평문 채팅 기록, API 키, 백엔드 정보가 담긴 **100만 건 이상의 로그**가 있었다(가장 오래된 것은 2025-01-06). DeepSeek는 신고 후 신속히 차단했다

summary_de: |
  Wiz fand nicht authentifizierte öffentliche ClickHouse-Instanzen (`oauth2callback.deepseek.com:9000`, `dev.deepseek.com:9000`), bei denen der Pfad `/play` das Ausführen beliebigen SQL erlaubte. Die Tabelle `log_stream` enthielt **über 1M Log-Einträge** (frühester 2025-01-06) mit Klartext-Chatprotokollen, API-Schlüsseln und Backend-Details. DeepSeek schaltete sie nach dem Bericht schnell ab

summary_fr: |
  Wiz a trouvé des instances ClickHouse publiques non authentifiées (`oauth2callback.deepseek.com:9000`, `dev.deepseek.com:9000`) où le chemin `/play` permettait d'exécuter du SQL arbitraire. La table `log_stream` contenait **plus d'un million d'entrées de journal** (la plus ancienne du 2025-01-06) avec des historiques de chat en clair, des clés API et des détails d'infrastructure. DeepSeek l'a fermée rapidement après le signalement

summary_es: |
  Wiz encontró instancias públicas de ClickHouse sin autenticación (`oauth2callback.deepseek.com:9000`, `dev.deepseek.com:9000`) donde la ruta `/play` permitía ejecutar SQL arbitrario. La tabla `log_stream` contenía **más de 1M de entradas de registro** (la más antigua del 2025-01-06) con registros de chat en texto plano, claves de API y detalles del backend. DeepSeek la cerró rápidamente tras el informe

sources:
  - url: https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak
    label: Wiz
  - url: https://thehackernews.com/2025/01/deepseek-ai-database-exposed-over-1.html
    label: THN

disputed: false
landmark: true
scan_month: 2025-01
scan_ref: "SCAN.md §5 2025-01"
---

# DeepSeek ClickHouse database left wide open

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

Wiz found unauthenticated public ClickHouse instances (`oauth2callback.deepseek.com:9000`, `dev.deepseek.com:9000`) where the `/play` path allowed running arbitrary SQL. The `log_stream` table held **over 1M log entries** (earliest 2025-01-06) with plaintext chat records, API keys and backend details. DeepSeek shut it down quickly after the report

## Attack chain

```mermaid
flowchart LR
    E["Agent infrastructure exposed to the internet"]:::entry
    S0["Unauthenticated access"]:::step
    I["RCE / data leak"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Wiz | <https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak> |
| 2 | THN | <https://thehackernews.com/2025/01/deepseek-ai-database-exposed-over-1.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-01-29` (raw: 2025-01-29, precision `day`) |
| Kind | Incident `incident` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [China](../../regions/cn.md) |
| Archive ID | `2025-01-29-deepseek-clickhouse-exposed` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2025-02-01` [Thousands of Ollama servers exposed without auth](../2025-02/2025-02-01-ollama-fu-wu-qi-gui.md)<br>  <sub>Thousands of Ollama servers exposed without auth</sub>
- `2025-03-01` [ChatGPT SSRF CVE-2024-27564 exploited in the wild](../2025-03/2025-03-01-chatgpt-ssrf-ye-li-yong.md)<br>  <sub>ChatGPT SSRF CVE-2024-27564 exploited in the wild</sub>
- `2025-03-03` [DeepSeek exposure window closes](../2025-03/2025-03-03-deepseek-bao-lu-chuang-kou.md)<br>  <sub>DeepSeek exposure window closes</sub>
- `2025-04-29` [NVIDIA TensorRT-LLM deserialization RCE](../2025-04/2025-04-29-nvidia-tensorrt-llm-rce.md)<br>  <sub>NVIDIA TensorRT-LLM deserialization RCE</sub>

---

[← 2025-01 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-01/2025-01-29-deepseek-clickhouse-exposed.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
