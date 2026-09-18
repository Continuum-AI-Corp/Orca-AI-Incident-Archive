# Machine-readable exports

**This directory is generated — do not edit it by hand.** The source is the YAML frontmatter of `incidents/**/*.md`;
after changing a source file, run `python scripts/build.py` once and it is regenerated. CI checks that the two stay in sync.

| File | Contents |
|---|---|
| `incidents.json` | Every field, including each record's source list. The top level carries `schema_version` (currently `2`), `version` / `count` / `license`, and `languages` (the seven supported language codes, `en` first). Each record has `title` and `summary` in English plus `title_zh` / `title_ja` / `title_ko` / `title_de` / `title_fr` / `title_es` and the matching `summary_*` fields, as well as `path` / `path_zh` pointing at the English record and its Chinese mirror |
| `incidents.csv` | Flattened, one row per record; `type` / `region` / `sources` are `;`-separated. Ships the same seven-language title and summary columns |
| `stats.json` | Counts by dimension: by month, by severity, by kind, by type, by confidence, by region |
| `sources.txt` | Every unique URL, one per line, for batch reachability checks |

Field meanings are in [SCHEMA.md](../SCHEMA.md).

## Using it

```python
import json
d = json.load(open("dist/incidents.json", encoding="utf-8"))

# Only records with a confirmed victim
real = [x for x in d["incidents"] if x["real_harm"]]

# The "incident" scope once policy and intelligence reports are excluded
incidents = [x for x in d["incidents"] if x["kind"] in ("incident", "vulnerability")]
```

```bash
# Count by severity
python -c "import json,collections;print(collections.Counter(x['severity'] for x in json.load(open('dist/incidents.json',encoding='utf-8'))['incidents']))"
```

> [!IMPORTANT]
> Decide your counting rule first. `count` is **the total number of records**, including research demos, vulnerability disclosures with no known exploitation in the wild, and regulatory moves.
> Treating it directly as "the number of AI incidents this year" badly overstates the total — which is exactly why this archive defines the `kind` and `real_harm` fields.

---

[← Back to home](../README.md)
