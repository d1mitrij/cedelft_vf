# Input Files Methodology — vf_cedelft

**CE Delft Environmental Prices Handbook 2024 — Value Factor Extraction Pipeline**

**Pipeline author:** Dr Dimitrij Euler (Greenings), with the support of Claude Code (Anthropic)

---

## 1. Primary Source

### Environmental Prices Handbook 2024: EU27 version

| Field | Value |
|---|---|
| File | `Environmental_Prices_Handbook_2024_EU27_version.pdf` |
| Markdown conversion | `Environmental_Prices_Handbook_2024_EU27_version.md` |
| Authors | Joukje de Vries, Sander de Bruyn, Sjoerd Boerdijk, Daan Juijn, Marijn Bijleveld, Coen van der Giesen, Marisa Korteland, Nikki Odenhoven, Ward van Santen, Simon Pápai |
| Organisation | CE Delft, Delft, The Netherlands |
| Publication date | April 2025 |
| Version | 1.1 |
| Reference number | 230107 |
| Price level | EUR 2021 |
| Geographic scope | EU27 |

The source PDF is stored in the project root alongside its Markdown conversion.
The Markdown was produced from the official PDF and is used for reference and QA only.
All pipeline values are **hard-coded** from the PDF tables — not parsed at runtime.

---

## 2. External Methodology Sources

The CE Delft handbook itself draws on several external methodological sources
that underlie the derivation of the environmental prices. These are secondary
inputs to the handbook authors, not direct inputs to this pipeline.

| Source | Role in handbook | License |
|---|---|---|
| **ReCiPe 2016 H** (Huijbregts et al. 2017) | Midpoint characterisation factors (Tables 7–8); secondary pollutant derivation (Step 4) | CC-BY 4.0 — see https://doi.org/10.1007/s11367-016-1246-z |
| **EC JRC Product Environmental Footprint (PEF)** | CAT I/II classification for Table 8; EF 3.0 characterisation factors | EC legal notice — non-commercial reuse with attribution |
| **EEA/GAINS dispersion model (2021)** | Air pollutant concentration mapping (22×33 km grid) used in IPA Step 2 | EEA legal notice — non-commercial reuse; https://www.eea.europa.eu/en/legal-notice |
| **IIASA GAINS model** | Emission inventories and source-receptor relationships for PM/NOx/SO2/NH3 | IIASA terms — see https://gains.iiasa.ac.at |
| **WHO / Chen & Hoek (2020) CRFs** | PM₂.₅ and PM₁₀ concentration-response functions (mortality) | Academic publication — CC-BY (journal-specific) |
| **WHO HRAPIE (2013) + updates** | O₃ and NO₂ concentration-response functions | WHO publications — citation required |
| **EU Water Framework Directive priority list** | Substance selection for Table 4 (water pollutants) | EU Institutional open data |
| **Costanza et al. (2014)** | Ecosystem service values used for biodiversity/land valuation | Academic publication |
| **Kuik (2008)** | Ecosystem valuation basis | Academic publication |
| **ExternE / NEEDS (2008)** | VOLY (Value of Life Year Lost) underpinning | Academic publication |

---

## 3. Table Mapping — Source to Pipeline

| `pipeline.py` variable | Handbook table | Chapter | Substances / rows | Unit |
|------------------------|----------------|---------|-------------------|------|
| `_AIR_DATA` | Table 3 | 2.3.1 | 20 substances (GHGs, PM, NOₓ, SO₂, NH₃, NMVOC, CH₄, heavy metals, organics) | EUR 2021/kg |
| `_WATER_DATA` | Table 4 | 2.3.2 | 22 substances × 2 media (freshwater + saltwater) = 44 rows | EUR 2021/kg |
| `_SOIL_DATA` | Table 5 | 2.3.3 | 21 substances (heavy metals, PAHs, nutrients) | EUR 2021/kg |
| `_LAND_DATA` | Table 6 | 2.3.4 | 1 row (land use occupation) | EUR 2021/m²/year |
| `_RECIPE_DATA` | Table 7 | 2.4.1 | 19 impact categories (cat. A/B/C), ReCiPe 2016 H | EUR 2021/unit |
| `_PEF_DATA` | Table 8 | 2.4.2 | 9 impact categories (CAT I and II), EU27 + NL | EUR 2021/unit |

### Substance details by table

**Table 3 — Air pollutants (20 substances)**

| Category | Substances |
|---|---|
| GHGs and common pollutants | CO₂, CFC-11, PM2.5, PM10, NOₓ, SO₂, NH₃, NMVOC, CH₄ |
| Heavy metals | As, Cd, Cr-VI, Pb, Hg, Ni |
| Organic compounds | 1,3-Butadiene, Benzene, Benzo(a)pyrene, Dioxins, Formaldehyde |

**Table 4 — Water pollutants (22 substances, 2 media)**

Arsenic, Barium, Benzo(a)anthracene, Benzo(a)pyrene, Cadmium, Carbendazim,
Cypermethrin, Deltamethrin, Esfenvalerate, Fluoranthene, Phosphate, Imidacloprid,
Irgarol/Cybutryne, Cobalt, Copper, Mercury, Lambda-cyhalothrin, Methylpirimiphos,
Nickel, Nitrate, Selenium, Thallium

**Table 5 — Soil pollutants (21 substances)**

Antimony, Anthracene, Arsenic, Barium, Benzo(a)anthracene, Benzo(a)pyrene, Cadmium,
Chromium III, Phenanthrene, Fluoranthene, Cobalt, Copper, Mercury, Lead, Molybdenum,
Naphthalene, Nickel, Selenium, Tin, Vanadium, Zinc

**Table 7 — ReCiPe 2016 midpoints (19 categories)**

Climate change, Ozone depletion, Ionising radiation, Oxidant formation (human health),
Oxidant formation (terrestrial ecosystems), Particulate matter formation, Acidification,
Freshwater eutrophication, Marine eutrophication, Terrestrial ecotoxicity, Freshwater
ecotoxicity, Marine ecotoxicity, Human toxicity (cancer), Human toxicity (non-cancer),
Land use, Mineral extraction, Fossil extraction, Water consumption, NO₂ mortality (addition)

**Table 8 — PEF midpoints (9 categories)**

Climate change, Ozone depletion, Ionising radiation, Oxidant formation (human health),
Particulate matter, Acidification, Freshwater eutrophication, Marine eutrophication,
Terrestrial eutrophication

---

## 4. Value Verification

All values in `pipeline.py` were verified against two independent locations in the handbook:

1. **Summary tables** in Chapter 1 (overview values, rounded)
2. **Detailed tables** in Chapter 2 (Tables 3–8, full precision)

Where the two locations differ (rounding), the Chapter 2 detailed value is used.
The one confirmed discrepancy (NOₓ: summary €31.8 vs Table 3 €31.1) is documented
in `VALIDATION_REPORT.md`.

---

## 5. Markdown Conversion Process

The PDF was converted to Markdown for reference and QA purposes using `pypdf`
(plain text extraction; no ML, no layout analysis). The resulting Markdown
preserves text content but loses table formatting. Numeric values in the Markdown
were used for cross-checking; the PDF remains the authoritative source.

---

## 6. What the Pipeline Does NOT Read at Runtime

- The PDF file
- The Markdown conversion
- Any external database or API

All data is embedded in `pipeline.py` as Python data structures, manually transcribed
and verified against the source tables.

---

## 7. License Model

### 7.1 Primary source — CE Delft Environmental Prices Handbook

| Attribute | Detail |
|---|---|
| **Copyright holder** | CE Delft, Delft, The Netherlands |
| **License type** | Proprietary — All Rights Reserved |
| **Free use** | Citation and short quotation with attribution permitted |
| **Commercial reproduction** | Requires written permission from CE Delft |
| **Redistribution of handbook** | Not permitted without permission |
| **Derived data pipelines** | Permitted for non-commercial research / policy use; always cite CE Delft |
| **License URL** | https://ce.nl/en/publications/environmental-prices-handbook/ |

**Attribution required:**
> De Vries, J., De Bruyn, S., Boerdijk, S., Juijn, D., Bijleveld, M., Van der Giesen, C.,
> Korteland, M., Odenhoven, N., Van Santen, W., Pápai, S. (2025).
> *Environmental Prices Handbook 2024: EU27 version* (Version 1.1, Reference 230107).
> CE Delft, Delft.

### 7.2 Methodology sources embedded in handbook derivation

| Source | License | Commercial use | Notes |
|---|---|---|---|
| ReCiPe 2016 H (Huijbregts et al.) | CC-BY 4.0 | Yes | Cite Huijbregts et al. 2017; https://doi.org/10.1007/s11367-016-1246-z |
| EC JRC PEF / EF 3.0 | EC legal notice | Non-commercial only | Attribution to EC-JRC required |
| EEA / IIASA GAINS model | EEA legal notice | Non-commercial only | https://www.eea.europa.eu/en/legal-notice |
| WHO concentration-response functions | WHO terms | Non-commercial | Citation required |

### 7.3 This pipeline's outputs

The coefficient matrices (CSV/Excel) produced by this pipeline are derived works
of the CE Delft handbook. They are made available under **CC BY-NC 4.0** (Attribution,
Non-Commercial) to reflect the CE Delft proprietary source license.

Users must:
1. Cite the CE Delft handbook (see §7.1 above)
2. Cite the pipeline: Euler, D. (2026). *CE Delft Environmental Prices Value Factor
   Pipeline* (vf_cedelft). Greenings.
3. Not use the outputs in commercial products without obtaining permission from CE Delft.

---

## 8. Updating Source Files

When a new edition of the handbook is published:

1. Replace the PDF in the project root.
2. Regenerate the Markdown conversion.
3. Update `pipeline.py` values — see `DATA_UPDATES.md` for the full procedure.
4. Update `VALIDATION_REPORT.md` with new known-good reference values.
5. Update the version and date in `config.py` metadata fields.

---

## 9. Source File Validation Checklist

Before a pipeline run, verify:

- [ ] PDF file is present in the project root
- [ ] Cover page reads "Environmental Prices Handbook 2024: EU27 version"
- [ ] Reference number 230107, Version 1.1, April 2025
- [ ] CO₂ air pollutant central value = €0.130/kg (Table 3, p. 32)
- [ ] PM2.5 air pollutant central value = €81.2/kg (Table 3)
- [ ] Cadmium central value = €155,294/kg (Table 3)
- [ ] Land use central value = €0.053/m²/year (Table 6)
- [ ] Climate change ReCiPe central = €0.13/kg CO₂-eq. (Table 7)

---

*Document Version 2.0 | Last Updated 2026-03-09 | Maintained by Greenings | dimitrij.euler@greenings.org*
*Value factors: CE Delft (De Vries et al. 2025) | Scripts: Dr Dimitrij Euler with support of Claude Code (Anthropic)*
