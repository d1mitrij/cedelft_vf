# Data Updates — vf_cedelft

**CE Delft Environmental Prices Handbook 2024 — Value Factor Extraction Pipeline**
**Author:** Dimitrij Euler (Greenings), with the support of Claude Code (Anthropic)

---

## Overview

This document describes the procedure for updating `pipeline.py` when a new
edition of the CE Delft Environmental Prices Handbook is published.

The current version of the handbook covered by this pipeline:

| Field | Value |
|---|---|
| Title | Environmental Prices Handbook EU27 version |
| Version date | April 2025 |
| Price level | EUR 2021 |
| Tables covered | Tables 3–8 (air, water, soil, land, ReCiPe, PEF) |

---

## Update Procedure

### Step 1 — Replace source files

1. Download the new handbook PDF.
2. Place it in the project root, replacing `Environmental_Prices_Handbook_2024_EU27_version.pdf`.
3. Regenerate the Markdown:
   ```bash
   python adb_china/convert_to_md.py Environmental_Prices_Handbook_2024_EU27_version.pdf
   ```

### Step 2 — Identify changed values

Open the new handbook and compare Tables 3–8 against the values in `pipeline.py`.
Focus on:
- New substances added to existing tables
- Changed central/lower/upper values for existing substances
- New midpoint categories (Tables 7 or 8)
- Changes to the price base year (currently EUR 2021)

### Step 3 — Update pipeline.py

Each data structure in `pipeline.py` corresponds to one table:

| Variable | Table | Location in pipeline.py |
|---|---|---|
| `_AIR_DATA` | Table 3 | Search `_AIR_DATA` |
| `_WATER_DATA` | Table 4 | Search `_WATER_DATA` |
| `_SOIL_DATA` | Table 5 | Search `_SOIL_DATA` |
| `_LAND_DATA` | Table 6 | Search `_LAND_DATA` |
| `_RECIPE_DATA` | Table 7 | Search `_RECIPE_DATA` |
| `_PEF_DATA` | Table 8 | Search `_PEF_DATA` |

For each changed value, update the corresponding entry in the data structure.
If the price base year changes (e.g. EUR 2021 → EUR 2024), update:
- All `unit` strings (e.g. `"EUR_2021/kg"` → `"EUR_2024/kg"`)
- The `PUBLICATIONS` dict in `config.py` (the `price_year` field)

### Step 4 — Update config.py

If publication metadata has changed (title, date, authors), update the
`PUBLICATION` dict in `config.py`.

### Step 5 — Run and verify

```bash
python extract_cedelft_values.py
```

Compare output CSV values against the new handbook. Update `VALIDATION_REPORT.md`
with new known-good reference values.

---

## Version History

| Date | Handbook version | Action | Author |
|------|-----------------|--------|--------|
| 2026-03-07 | April 2025 (EUR 2021) | Initial extraction | D. Euler / Claude Code |

---

## Notes on Price Level Uprating

The handbook provides values in EUR 2021. To uprate to a more recent price level:

```
Value(t) = Value(2021) × CPI(t) / CPI(2021)
```

where CPI is the EU27 Harmonised Index of Consumer Prices (HICP) from Eurostat.
This uprating is not applied by the pipeline — values are stored at EUR 2021 as
published. Downstream users apply uprating at the point of use.
