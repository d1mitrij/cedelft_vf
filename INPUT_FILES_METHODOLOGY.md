# Input Files — vf_cedelft

**CE Delft Environmental Prices Handbook 2024 — Value Factor Extraction Pipeline**
**Author:** Dimitrij Euler (Greenings), with the support of Claude Code (Anthropic)

---

## 1. Source File

### Environmental Prices Handbook EU27 version (April 2025)

| Field | Value |
|---|---|
| File name | `Environmental_Prices_Handbook_2024_EU27_version.pdf` |
| Markdown conversion | `Environmental_Prices_Handbook_2024_EU27_version.md` |
| Authors | Joukje de Vries, Sander de Bruyn, Sebastiaan Hesen, Marnix Koopman, Mila Larsson |
| Organisation | CE Delft |
| Publication date | April 2025 |
| Price level | EUR 2021 |

The source PDF is stored in the project root alongside its Markdown conversion.
The Markdown was produced by `pypdf` text extraction (non-ML) and is used for
reference and QA only. All pipeline values are hard-coded from the PDF, not
parsed at runtime from the Markdown.

---

## 2. Table Mapping

| pipeline.py variable | Handbook table | Content |
|---------------------|----------------|---------|
| `_AIR_DATA` | Table 3 | Air pollutant prices (EUR/kg) |
| `_WATER_DATA` | Table 4 | Water pollutant prices (EUR/kg), freshwater and saltwater |
| `_SOIL_DATA` | Table 5 | Soil pollutant prices (EUR/kg) |
| `_LAND_DATA` | Table 6 | Land use price (EUR/m²/year) |
| `_RECIPE_DATA` | Table 7 | ReCiPe 2016 midpoint prices (EUR/unit) |
| `_PEF_DATA` | Table 8 | PEF midpoint prices (EUR/unit), EU27 and NL |

---

## 3. Value Verification

All values in `pipeline.py` were verified against two independent locations in
the handbook:

1. **Summary tables** in Chapter 1 (overview values, rounded)
2. **Detailed tables** in Chapter 2 (Tables 3–8, full precision)

Where the two locations differ (rounding), the Chapter 2 detailed value is used.
The one confirmed discrepancy (NOx: summary €31.8 vs. Table 3 €31.1) is documented
in `VALIDATION_REPORT.md`.

---

## 4. Markdown Conversion Process

The PDF was converted to Markdown using the script at:

```
adb_china/convert_to_md.py
```

which uses the `pypdf` library for plain text extraction (no ML, no layout
analysis). The resulting Markdown preserves text content but loses table formatting.
Numeric values in the Markdown were used for cross-checking; the PDF remains the
authoritative source.

---

## 5. What the Pipeline Does NOT Read at Runtime

- The PDF file
- The Markdown conversion
- Any external database or API

All data is embedded in `pipeline.py` as Python data structures.

---

## 6. Updating Source Files

When a new edition of the handbook is published:

1. Replace the PDF in the project root.
2. Regenerate the Markdown with `python adb_china/convert_to_md.py`.
3. Update `pipeline.py` values — see `DATA_UPDATES.md` for the procedure.
4. Update `VALIDATION_REPORT.md` with new known-good reference values.
