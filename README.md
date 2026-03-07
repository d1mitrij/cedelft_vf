# CE Delft Environmental Prices Handbook 2024 — Value Factor Pipeline

## Data Source & Attribution

> **This pipeline extracts and structures value factors from:**
>
> **Environmental Prices Handbook 2024: EU27 version**
> *Methodical justification of key indicators used for the valuation of emissions and environmental impact*
>
> **Authors (CE Delft):**
> Joukje de Vries, Sander de Bruyn, Sjoerd Boerdijk, Daan Juijn, Marijn Bijleveld,
> Coen van der Giesen, Marisa Korteland, Nikki Odenhoven, Ward van Santen, Simon Pápai
>
> **Publisher:** CE Delft, Delft, The Netherlands
> **Version:** 1.1 | **Reference:** 230107 | **Date:** April 2025
> **Price level:** EUR 2021 | **Geographic scope:** EU27

All environmental prices, values, and methodological content are the intellectual property
of CE Delft. This pipeline is a structured extraction tool only — it does not modify or
reinterpret the underlying values. When citing these value factors in research or policy
work, always cite the CE Delft handbook directly.

---

## Script Authorship

**Extraction pipeline developed by:**
Dimitrij Euler (Greenings) — dimitrij.euler@greenings.org

**With the support of:** Claude Code (Anthropic)

---

## Overview

This pipeline converts the CE Delft Environmental Prices Handbook 2024 into
machine-readable, analysis-ready CSV and Excel files. It covers **114 value factors**
across **6 table groups** (Tables 3–8 of the handbook), spanning emissions to air,
water and soil, land use, and LCA midpoint prices (ReCiPe 2016 and PEF).

All values are hard-coded from the verified handbook tables — no PDF parsing at runtime.
Each value factor has **lower**, **central**, and **upper** variants to represent
uncertainty.

---

## Quick Start

```bash
# Extract all 6 table groups
python extract_cedelft_values.py

# Extract specific groups
python extract_cedelft_values.py --only air_pollutants midpoints_recipe

# List available groups
python extract_cedelft_values.py --list

# Run a single table
python tables/01_air_pollutants.py
```

Outputs are written to `output/` as both CSV and formatted Excel files.

---

## Table Groups

| ID | Key | Source | Description | Rows | Unit |
|----|-----|--------|-------------|------|------|
| 01 | `air_pollutants` | Table 3 | Air emission prices: GHGs, classic pollutants, heavy metals, organics | 20 | EUR 2021/kg |
| 02 | `water_pollutants` | Table 4 | Water emission prices: freshwater and saltwater | 44 | EUR 2021/kg |
| 03 | `soil_pollutants` | Table 5 | Soil emission prices: metals, PAHs, nutrients | 21 | EUR 2021/kg |
| 04 | `land_use` | Table 6 | Land-use occupation: biodiversity loss relative to natural state | 1 | EUR 2021/m²/year |
| 05 | `midpoints_recipe` | Table 7 | ReCiPe 2016 midpoint prices for LCA (19 impact categories) | 19 | EUR 2021/unit |
| 06 | `midpoints_pef` | Table 8 | PEF CAT I & II midpoint prices (EU27 + Netherlands) | 9 | EUR 2021/unit |

**Total: 114 value factor rows**

---

## Repository Structure

```
vf_cedelft/
├── config.py                    # Table group definitions and publication metadata
├── pipeline.py                  # Hard-coded data, builder functions, Excel writer
├── extract_cedelft_values.py    # Orchestrator (CLI: --only, --list)
├── tables/
│   ├── _template.py             # Template for new table scripts
│   ├── 01_air_pollutants.py
│   ├── 02_water_pollutants.py
│   ├── 03_soil_pollutants.py
│   ├── 04_land_use.py
│   ├── 05_midpoints_recipe.py
│   └── 06_midpoints_pef.py
├── output/                      # Generated CSV and Excel files
│   ├── 01_cedelft_air_pollutants.{csv,xlsx}
│   ├── 02_cedelft_water_pollutants.{csv,xlsx}
│   ├── 03_cedelft_soil_pollutants.{csv,xlsx}
│   ├── 04_cedelft_land_use.{csv,xlsx}
│   ├── 05_cedelft_midpoints_recipe.{csv,xlsx}
│   └── 06_cedelft_midpoints_pef.{csv,xlsx}
├── Environmental_Prices_Handbook_2024_EU27_version.pdf   # Source document
├── Environmental_Prices_Handbook_2024_EU27_version.md    # Markdown conversion
├── README.md
├── METHODOLOGY.md
├── ARCHITECTURE_DECISIONS.md
└── VALIDATION_REPORT.md
```

---

## Value Factor Structure

Each output file uses a **tidy/long format** with one row per unique combination of
pollutant (or impact category) and, where applicable, receiving medium. All rows carry:

- `source_table` — which handbook table the value comes from
- `chapter` — handbook chapter/section reference
- `lower` / `central` / `upper` — three uncertainty variants
- `unit` — explicit unit string (e.g. `EUR_2021/kg`)

For SCBA applications, the **lower and upper** values are recommended to reflect
uncertainty in the analysis. For LCA and CSR applications, the **central** value
is recommended as the most likely estimate.

---

## Key Values at a Glance

**Selected air pollutant prices (EUR 2021/kg, central):**

| Pollutant | Central |
|-----------|---------|
| CO₂ | € 0.130 |
| PM2.5 | € 81.2 |
| NOₓ | € 19.3 |
| SO₂ | € 26.6 |
| NH₃ | € 25.2 |
| Cadmium | € 155,294 |
| Mercury | € 14,951 |
| Dioxins | € 50,367,195 |

**Selected ReCiPe 2016 midpoint prices (EUR 2021/unit, central):**

| Impact category | Unit | Central |
|-----------------|------|---------|
| Climate change | EUR/kg CO₂-eq. | € 0.13 |
| Particulate matter formation | EUR/kg PM2.5-eq. | € 84.7 |
| Freshwater eutrophication | EUR/kg P-eq. | € 3.74 |
| Human toxicity, cancer | EUR/kg 1.4-DCB-eq. | € 3.99 |

---

## Dependencies

```bash
pip install openpyxl
```

No PDF parsing or ML libraries required at runtime. All values are pre-transcribed
from the handbook into `pipeline.py`.

---

## Limitations

- **EU27 averages only:** Values not suitable for site-specific studies or countries
  outside the EU27 without value transfer adjustment.
- **No bioaccumulative substances (PFAS):** Explicitly excluded from the handbook.
- **CAT III PEF excluded:** Insufficient data within handbook scope.
- **Nitrogen in NL:** Cannot be applied where legally binding nitrogen caps exist.
- **Land-use change:** Table 6 covers occupation only, not change; separate analysis needed.

See `METHODOLOGY.md` for full details on the CE Delft methodology and limitations.
