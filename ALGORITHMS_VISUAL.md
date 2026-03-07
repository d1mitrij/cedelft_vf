# Algorithms — vf_cedelft

**CE Delft Environmental Prices Handbook 2024 — Value Factor Extraction Pipeline**
**Author:** Dimitrij Euler (Greenings), with the support of Claude Code (Anthropic)

---

## 1. Overall Data Flow

```
pipeline.py
  _AIR_DATA (list of dicts)          ─┐
  _WATER_DATA (list of dicts)         │  _build_*_rows()
  _SOIL_DATA (list of dicts)          ├─────────────────→ list[dict]
  _LAND_DATA (list of dicts)          │  builder functions
  _RECIPE_DATA (list of dicts)        │
  _PEF_DATA (list of dicts)          ─┘
            │
            ▼
       run_table(key)
            │
            ├──→ CSV  (output/NN_cedelft_*.csv)
            └──→ XLSX (output/NN_cedelft_*.xlsx)
                        │
                        ├── Sheet: "Value Factors"   (formatted data)
                        └── Sheet: "Metadata"        (publication attribution)
```

---

## 2. Builder Functions

Each table group has a dedicated builder function:

| Function | Table | Output columns |
|----------|-------|----------------|
| `_build_air_pollutants_rows()` | Table 3 | substance, cas_nr, unit, lower, central, upper |
| `_build_water_pollutants_rows()` | Table 4 | substance, receiving_water, unit, lower, central, upper |
| `_build_soil_pollutants_rows()` | Table 5 | substance, cas_nr, unit, lower, central, upper |
| `_build_land_use_rows()` | Table 6 | category, unit, central |
| `_build_midpoints_recipe_rows()` | Table 7 | impact_category, unit, reliability_category, category_description, lower, central, upper |
| `_build_midpoints_pef_rows()` | Table 8 | impact_category, unit, cat_level, eu27_central, nl_central |

---

## 3. run_table() Algorithm

```
run_table(key):
  1. Look up (builder_fn, fieldnames) from _BUILDERS[key]
  2. Call builder_fn() → rows: list[dict]
  3. Look up output paths from config.TABLE_GROUPS[key]
  4. Create output/ directory if needed
  5. Write CSV:
       open output_csv, newline=""
       writer = DictWriter(f, fieldnames, extrasaction="ignore")
       writer.writeheader()
       writer.writerows(rows)
  6. Write XLSX (calls _write_excel()):
       wb = Workbook()
       ws_data = "Value Factors" sheet
         → freeze pane at A2
         → header row: fill=dark blue, font=white, bold
         → data rows
       ws_meta = "Metadata" sheet
         → publication fields from config.PUBLICATION
         → table group fields from config.TABLE_GROUPS[key]
  7. Return output_csv path
```

---

## 4. Excel Writer Detail

```
_write_excel(rows, fieldnames, output_xlsx, table_key):
  header_fill  = PatternFill(fgColor="1F3864", fill_type="solid")
  header_font  = Font(color="FFFFFF", bold=True)

  ws_data:
    row 1 = fieldnames (styled)
    rows 2..N = data values
    freeze_panes = "A2"
    column widths = max(header_len, max_value_len) + 2

  ws_meta:
    rows: [
      ("Field", "Value"),
      ("Source", PUBLICATION["full_title"]),
      ("Authors", PUBLICATION["authors"]),
      ("Publisher", PUBLICATION["publisher"]),
      ...
      ("Table group", TABLE_GROUPS[key]["description"]),
      ("Unit", TABLE_GROUPS[key]["unit"]),
      ("Rows", len(rows)),
      ("Generated", datetime.now().isoformat()),
    ]
```

---

## 5. Uncertainty Representation

The CE Delft handbook provides three estimates per substance for most tables:

| Column | Meaning |
|--------|---------|
| `lower` | Conservative (low damage) estimate |
| `central` | Best estimate (recommended for standard use) |
| `upper` | High damage estimate |

For land use (Table 6) only a single `central` value is published.

For PEF midpoints (Table 8) only `central` values are published (no lower/upper),
split by `eu27_central` and `nl_central`.

---

## 6. Dispatch Table

```python
_BUILDERS = {
    "air_pollutants":    (_build_air_pollutants_rows,    AIR_FIELDS),
    "water_pollutants":  (_build_water_pollutants_rows,  WATER_FIELDS),
    "soil_pollutants":   (_build_soil_pollutants_rows,   SOIL_FIELDS),
    "land_use":          (_build_land_use_rows,           LAND_FIELDS),
    "midpoints_recipe":  (_build_midpoints_recipe_rows,  RECIPE_FIELDS),
    "midpoints_pef":     (_build_midpoints_pef_rows,     PEF_FIELDS),
}
```

`run_table(key)` uses this dict to look up the correct builder and field list
without any `if/elif` branching.

---

## 7. Orchestrator Flow

```
extract_cedelft_values.py:

  parse args (--only KEY | --list | default: all)

  if --list:
    print available keys → exit

  keys = [only_key] or list(_BUILDERS.keys())

  for key in keys:
    t0 = time.time()
    result = pipeline.run_table(key)
    elapsed = time.time() - t0
    log_line = f"[OK]  {key:35s} {n_rows:4d} rows  {elapsed:.2f}s"
    print(log_line)
    log_lines.append(log_line)

  write execution_log_{datetime}.txt
```
