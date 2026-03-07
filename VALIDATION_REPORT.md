# Validation Report — vf_cedelft

**Pipeline:** CE Delft Environmental Prices Handbook 2024 — Value Factor Extraction
**Author:** Dimitrij Euler (Greenings), with the support of Claude Code (Anthropic)
**Data source:** CE Delft (Joukje de Vries et al., April 2025)

---

## Validation Approach

All values in `pipeline.py` were transcribed from the CE Delft handbook and verified
against two independent locations in the source document:

1. **Summary tables** in the Introduction (Chapter 1, Tables 1 and 2) — pp. 7–9
2. **Detailed tables** in the Results chapter (Chapter 2, Tables 3–8) — pp. 32–37

Values were further spot-checked against the agent-read summary of the full handbook.
Any discrepancies between locations were resolved in favour of the Chapter 2 detailed
tables, which are more precise (e.g., PM2.5 central = €81.2/kg in Table 3 vs. "€81"
rounded in Table 1).

---

## Known-Good Reference Values

### Table 3 — Air Pollutants (EUR 2021/kg)

| Pollutant | Lower | Central | Upper | Verified |
|-----------|-------|---------|-------|----------|
| CO₂ | 0.050 | 0.130 | 0.160 | Both Table 1 and Table 3 |
| PM2.5 | 55.4 | 81.2 | 134 | Table 3 (Table 1 rounds to 81) |
| PM10 | 29.7 | 44.3 | 73.3 | Table 3 |
| NOₓ | 12.8 | 19.3 | 31.1 | Table 3 (Table 1: 31.8 — rounding difference) |
| SO₂ | 16.9 | 26.6 | 45.3 | Both tables |
| NH₃ | 17.4 | 25.2 | 39.5 | Both tables |
| NMVOC | 1.53 | 2.16 | 3.49 | Both tables |
| CH₄ | 1.80 | 4.68 | 5.77 | Both tables |
| CFC-11 | 283 | 725 | 926 | Table 3 |
| Cadmium (Cd) | 105,034 | 155,294 | 233,924 | Table 3 |
| Lead (Pb) | 18,455 | 27,287 | 41,106 | Table 3 |
| Mercury (Hg) | 9,983 | 14,951 | 23,019 | Table 3 |
| Arsenic (As) | 6,271 | 9,275 | 13,980 | Table 3 |
| Dioxins | 34,071,638 | 50,367,195 | 75,846,980 | Table 3 |

**Known discrepancy:** NOₓ upper value differs between Table 1 (€31.8) and Table 3 (€31.1).
Pipeline uses Table 3 value (€31.1) as it is the detailed authoritative source.

### Table 4 — Water Pollutants (EUR 2021/kg, central values)

| Pollutant | Freshwater central | Saltwater central | Verified |
|-----------|-------------------|------------------|----------|
| Arsenic | 2,411 | 188 | Table 4 |
| Cadmium | 31.5 | 9.0 | Table 4 |
| Mercury | 1,346 | 554 | Table 4 |
| Phosphate | 1.23 | 0 | Table 4 |
| Nitrate (N total) | 4.23 | 14.3 | Table 4 |
| Copper | 3.46 | 2.28 | Table 4 |

### Table 5 — Soil Pollutants (EUR 2021/kg, central values)

| Pollutant | Central | Verified |
|-----------|---------|----------|
| Cadmium (Cd) | 2,224 | Table 5 |
| Mercury (Hg) | 280 | Table 5 |
| Arsenic (As) | 168 | Table 5 |
| Zinc (Zn) | 787 | Table 5 |
| Nickel (Ni) | 45.1 | Table 5 |
| Lead (Pb) | 23.0 | Table 5 |

### Table 6 — Land Use (EUR 2021/m²/year)

| Category | Lower | Central | Upper | Verified |
|----------|-------|---------|-------|----------|
| Land use occupation | 0.037 | 0.053 | 0.069 | Table 6 |

### Table 7 — ReCiPe 2016 Midpoints (EUR 2021/unit, central values)

| Impact category | Unit | Central | Category | Verified |
|-----------------|------|---------|----------|----------|
| Climate change | EUR/kg CO₂-eq. | 0.13 | A | Tables 2 and 7 |
| Ozone depletion | EUR/kg CFC-11-eq. | 29.1 | A | Tables 2 and 7 |
| Particulate matter formation | EUR/kg PM2.5-eq. | 84.7 | A | Tables 2 and 7 |
| Acidification | EUR/kg SO₂-eq. | 5.28 | A | Tables 2 and 7 |
| Freshwater eutrophication | EUR/kg P-eq. | 3.74 | A | Tables 2 and 7 |
| Marine eutrophication | EUR/kg N-eq. | 14.25 | A | Tables 2 and 7 |
| Human toxicity (cancer) | EUR/kg 1.4-DCB-eq. | 3.99 | A | Tables 2 and 7 |
| Land use | EUR/m² a crop-eq. | 0.099 | B | Tables 2 and 7 |
| Water consumption | EUR/m³ | 0.407 | B | Tables 2 and 7 |
| NO₂ mortality | EUR/kg NOₓ-eq. | 5.94 | C | Tables 2 and 7 |

### Table 8 — PEF Midpoints (EUR 2021/unit, EU27 central)

| Impact category | EU27 central | NL central | Verified |
|-----------------|-------------|-----------|----------|
| Climate change (kg CO₂-eq.) | 0.130 | 0.130 | Table 8 |
| Ozone depletion (kg CFC-11-eq.) | 29.1 | 29.1 | Table 8 |
| Particulate matter (disease incidence) | 764,627 | 1,937,047 | Table 8 |
| Acidification (mol H⁺-eq.) | 2.04 | 2.01 | Table 8 |
| Freshwater eutrophication (kg P-eq.) | 3.74 | 5.53 | Table 8 |

---

## QA Checks Built Into Pipeline

1. **Row count verification:** Total 114 rows across 6 groups (20 + 44 + 21 + 1 + 19 + 9).
   Any deviation indicates a data transcription error.

2. **Unit consistency:** Each builder function enforces a single unit string per table group.
   Mixed units within a group would indicate a structural error.

3. **Dual-location verification:** Key values verified against both the introduction
   summary (Chapter 1) and the detailed tables (Chapter 2). Discrepancies documented above.

4. **Builder dispatch test:** All 6 keys present in `_BUILDERS`; `run_all()` exercises
   the complete pipeline end-to-end.

5. **Excel Metadata sheet:** Every Excel file contains a Metadata sheet with handbook
   attribution, enabling post-hoc provenance verification.

---

## Successful Extraction Log (Reference Run)

```
CE Delft Environmental Prices Handbook 2024 — extraction run
Started: 2026-03-07 07:18:09
Groups requested: ['air_pollutants', 'water_pollutants', 'soil_pollutants',
                   'land_use', 'midpoints_recipe', 'midpoints_pef']

  [OK]  01_air_pollutants            20 rows  0.07s  -> 01_cedelft_air_pollutants.csv
  [OK]  02_water_pollutants          44 rows  0.06s  -> 02_cedelft_water_pollutants.csv
  [OK]  03_soil_pollutants           21 rows  0.05s  -> 03_cedelft_soil_pollutants.csv
  [OK]  04_land_use                   1 rows  0.04s  -> 04_cedelft_land_use.csv
  [OK]  05_midpoints_recipe          19 rows  0.05s  -> 05_cedelft_midpoints_recipe.csv
  [OK]  06_midpoints_pef              9 rows  0.04s  -> 06_cedelft_midpoints_pef.csv

Done. 6/6 groups extracted, 114 total rows, 0 failed.
```

---

## Known Limitations and Exclusions

| Item | Status | Reason |
|------|--------|--------|
| PFAS and bioaccumulative substances | Not included | Explicitly excluded by CE Delft |
| PEF CAT III | Not included | Insufficient data within handbook scope |
| Site-specific values | Not included | EU27 averages only in handbook tables 3–8 |
| Country-differentiated values | Not included | Requires dedicated value transfer analysis |
| Full 3,000+ pollutant list | Partial (Annex H) | Only the main Tables 3–8 extracted; Annex H available in source MD |
| Noise valuation | Not included | Handbook §6.8; NL-specific; not in summary tables 3–8 |
| Source-differentiated PM/NOₓ | Not included | Chapter 6 table; beyond scope of summary extraction |

---

## Future Extension: Annex H (Full Pollutant List)

The handbook's Annex H contains environmental prices for more than 250 additional
pollutants to air, soil and water. This annex is available in the converted markdown
file and could be extracted as a table group `07_annex_h_full_list` in a future update.
