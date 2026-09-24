# Data structure

Every incident is **one Markdown file** under `incidents/YYYY-MM/`: structured fields in the YAML frontmatter, the narrative in the body.
Markdown rather than plain YAML, because it renders straight on GitHub — a database nobody wants to open is not a database.

```
incidents/2026-07/2026-07-09-openai-agents-breach-huggingface.md
             ^        ^          ^
             month dir   event date   ASCII slug (stable, does not change with the title)
```

## Frontmatter

```yaml
id: 2026-07-09-openai-agents-breach-huggingface   # = filename, unique across the archive
title: OpenAI's agents breach Hugging Face       # English title (source language)
title_zh: "<Chinese translation>"                # six translations, one per line;
title_ja: "<Japanese translation>"               #   order: zh, ja, ko, de, fr, es
title_ko: "<Korean translation>"
title_de: "<German translation>"
title_fr: "<French translation>"
title_es: "<Spanish translation>"

date: 2026-07-09              # day the event happened (not the disclosure date)
date_end: 2026-07-13          # optional, end date of an ongoing event
date_precision: day           # day | part | month | year | unknown
date_raw: "2026-07-09→13"     # original wording, kept for traceability

kind: incident                # incident | vulnerability | research | report | policy
type: [EVAL, WEAPON]          # multi-value, see taxonomy/types.md
severity: critical            # critical | high | medium | low | info
confidence: A                 # A | B | C | D
real_harm: true               # true | false | null
ai_involvement: confirmed     # confirmed | unverified | disputed | not-applicable

region: [GLOBAL, US]          # where the incident **landed**; cross-border product flaws get GLOBAL

summary: |
  A self-contained summary that reads on its own, without the body.

summary_zh: |
  <Chinese translation, same block-scalar form>
summary_ja: |
  <Japanese translation>
summary_ko: |
  <Korean translation>
summary_de: |
  <German translation>
summary_fr: |
  <French translation>
summary_es: |
  <Spanish translation>

sources:
  - url: https://openai.com/index/hugging-face-model-evaluation-security-incident/
    label: OpenAI

disputed: false               # true when facts or attribution are contested; the body then carries a warning block
landmark: true                # whether this is the month's landmark entry
scan_ref: "SCAN.md §6 2026-07"
```

The full Chinese text of a record lives in `incidents/i18n/zh/<month>/<id>.md` (frontmatter: `id`, `lang`, `source`, `title`, `summary`); `scripts/validate.py` checks that the mirror's `title` / `summary` match the record's `title_zh` / `summary_zh`.

## Field constraints

| Field | Type | Required | Constraint |
|---|---|---|---|
| `id` | string | ✅ | `^\d{4}-\d{2}-\d{2}-[a-z0-9][a-z0-9-]*$`, same as the filename |
| `title` | string | ✅ | English title (the source language); must contain Latin letters |
| `title_<lang>` `summary_<lang>` | string | ✅ | Translations for `zh` `ja` `ko` `de` `fr` `es`, placed directly after `title` / `summary` in that order; `zh` also keeps a full mirror under `incidents/i18n/zh/` |
| `date` | date | ✅ | ISO 8601; when the precision is lower, fill in the 1st of the month and note it in `date_precision` |
| `date_end` | date | | must be later than `date` |
| `date_precision` | enum | ✅ | `day` `part` `month` `year` `unknown` |
| `kind` | enum | ✅ | see above |
| `type` | list | ✅ | at least one; values in [taxonomy/types.md](taxonomy/types.md) |
| `severity` | enum | ✅ | must be `info` when `kind` is `policy` / `report` |
| `confidence` | enum | ✅ | `A` `B` `C` `D` |
| `real_harm` | bool/null | ✅ | must be `null` when `kind` is `policy` / `report` |
| `ai_involvement` | enum | ✅ | — |
| `region` | list | ✅ | ISO 3166-1 alpha-2, or `GLOBAL` `EU` `LATAM` `SEA` `APAC` |
| `sources` | list | ✅ | **at least one**. No source, no record |

Constraints are enforced by [`scripts/validate.py`](scripts/validate.py); CI runs it on every push.

## Body structure

| Section | When it appears |
|---|---|
| Warning block | `disputed: true`, `confidence` C/D, or `ai_involvement` other than `confirmed` |
| `## Summary` | required |
| `## Attack chain` | common (mermaid, generated from `type`) |
| `## Details` | when there is deep material |
| `## Sources` | required |
| `## Metadata` | common, includes **how it was classified** — why this severity |
| `## Related` | common |

## Export

`dist/` holds machine-readable versions generated from the frontmatter — do not hand-edit them:

| File | Purpose |
|---|---|
| `dist/incidents.json` | all fields, incl. sources; carries `schema_version: 2`, `languages` and `path_zh` |
| `dist/incidents.csv` | flattened, one row per record, `type` / `region` joined with `;`; one `title_<lang>` / `summary_<lang>` column per language and a `path_zh` column |
| `dist/stats.json` | counts per dimension |

> [!IMPORTANT]
> `dist/incidents.json` is also a live API. OrcaRouter's `/incident-archive` page fetches `main`'s copy on every visit and at every build, and rejects the whole file if it breaks the page's contract — the page then silently serves an older snapshot, and its builds fail. [`scripts/downstream_contract.py`](scripts/downstream_contract.py) checks that contract in CI.
> Adding records, correcting facts and adding sources are always fine. A new `schema_version`, a new `kind` / `severity` / `confidence` / `ai_involvement` value, a new `type` code, renamed fields or moved record files have to land on OrcaRouter's side first.

---

[← Back to home](README.md) · [Contributing](CONTRIBUTING.md)
