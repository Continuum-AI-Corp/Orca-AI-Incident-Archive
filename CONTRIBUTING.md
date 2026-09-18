# Contributing guide

Everything this archive is worth comes from being **verifiable**. So the rules are few, but they are hard.

## Three hard rules

### 1. Every record needs a primary source you can click

Entries with no source will not be merged. Source priority:

| Priority | Type | Example |
|---|---|---|
| Highest | The vendor's or victim's own announcement | incident reports from OpenAI, Anthropic, Hugging Face |
| High | Law-enforcement and regulatory documents, official PDFs | CISA KEV, court filings, IPA reports |
| Medium | Original research from security research firms | Trail of Bits, Zenity, Noma, Sysdig |
| Low | Mainstream media coverage | only when it carries verifiable technical detail |
| **Not accepted** | AI-generated "incident roundup" pages | see below |

> [!CAUTION]
> **In 2026 many "AI security incident roundup" pages are themselves AI-generated SEO content** carrying
> fabricated CVE numbers and harm figures. Four verification rounds on this archive confirmed three such
> contaminated sources. If a fact can only be found on a page like that, please do not submit it — or submit
> it with an explicit `confidence: C`.

### 2. When unsure, flag it — do not delete it

- Facts or attribution disputed → `disputed: true`, and present the parties' accounts **side by side** in the body, not just the one you believe
- AI involvement with no primary confirmation → `ai_involvement: unverified`
- Vendor and press accounts conflict → `ai_involvement: disputed`

Widely circulated but unconfirmed "AI incidents" **should stay in the archive and be flagged** rather than deleted —
so that someone searching for them finds the rebuttal material, not just the rumour.

### 3. Corrections go into the record, never silently overwritten

Say what you changed and why in the PR description. Corrections to key facts (numbers, attribution, dates)
are also logged in [`docs/data-quality.md`](docs/data-quality.md).

## Submitting a new incident

1. Pick the month directory `incidents/YYYY-MM/` (the month the event **happened**, not the month it was disclosed)
2. Filename = `YYYY-MM-DD-<ascii-slug>.md`; the slug uses lowercase letters, digits and hyphens only
3. Write the frontmatter as described in [SCHEMA.md](SCHEMA.md) — **every required field, none missing**
4. The body must contain at least `## Summary` and `## Sources`
5. Run the checks locally:

```bash
python scripts/validate.py          # frontmatter and link format
python scripts/build.py             # regenerate dist/ and the indexes
```

CI runs the same checks on every push.

## Editing an existing record

**Do not hand-edit `dist/` or the README files at any level** — they are generated from the frontmatter by
`scripts/build.py`, and manual edits are overwritten on the next build. Change the source (the frontmatter in
`incidents/**/*.md`), then rebuild.

What you may edit by hand:
- the frontmatter and body of `incidents/**/*.md`
- the narrative parts of `topics/*.md` and `regions/*.md` that are **not** in the "all records" tables
- `docs/`, `taxonomy/`, `SCHEMA.md`, and this file

## How severity is decided

The field that starts the most arguments. The criteria live in [`taxonomy/severity.md`](taxonomy/severity.md), and the core is one sentence:

> **severity does not grade how dangerous a vulnerability is — it grades what has already happened.**

CVSS 9.8 but never exploited → `high` + `real_harm: false`.
No CVE, but it took down nine government agencies in one country → `critical`.

If you think a record is graded wrong, open an issue explaining why and attach the sources that support your view.

## What we do not accept

- Pure LLM content-safety problems (a jailbreak that makes a model output something inappropriate, with no agent behaviour)
- Conventional vulnerabilities with no agent involvement
- Rumours that cannot be traced to any primary source
- **Any undisclosed vulnerability details, exploit code or attack tooling** — the archive only records publicly disclosed events

## Language

English is the source language of this archive; every other language is a translation layer on top of it.

- **Record title**: `title` is the English title (source language) and required; `title_zh` / `title_ja` / `title_ko` / `title_de` / `title_fr` / `title_es` are the six required translations.
- **Record body**: English. The complete Chinese text of every record lives in the mirror directory `incidents/i18n/zh/<month>/<id>.md`; the other languages fall back to English until translated.
- **Translation rules**: read [`docs/i18n/translation-guide.md`](docs/i18n/translation-guide.md) — it fixes the section names, the terminology and what must stay byte-identical. **Do not machine-translate**: a mistranslated technical detail is worse than no translation.
- **`zh`**: uses the mirror directory `incidents/i18n/zh/`; the mirror's `title` / `summary` must match the record's `title_zh` / `summary_zh` (checked by `scripts/validate.py`).
- **Other languages (`ja` `ko` `de` `fr` `es`)**: translations live inline as `title_<lang>` / `summary_<lang>` in the record's frontmatter, directly after `title` / `summary`.
- **READMEs**: the English one is the root `README.md`; the rest live in [`docs/i18n/`](docs/i18n/) as `README.<lang>.md` (`zh` is `README.zh-CN.md`). The text between `<!-- BEGIN:xxx -->` markers is generated by `scripts/build.py`, so edit the copy in [`scripts/readme_i18n.py`](scripts/readme_i18n.py), never the README itself.
- **Adding a language**: register it in [`scripts/l10n.py`](scripts/l10n.py) (`LANGS`, native label, display names), add a `README_L10N` entry in `scripts/readme_i18n.py` with `up="../../"`, create `docs/i18n/README.<lang>.md` with the same markers, add the inline `title_<lang>` / `summary_<lang>` fields to the records, and extend the language switcher at the top of every README.

---

[← Back to home](README.md) · [Data structure](SCHEMA.md) · [Taxonomy](taxonomy/README.md)
