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

**License:** Proprietary — CE Delft, All Rights Reserved
**License URL:** https://ce.nl/en/publications/environmental-prices-handbook/

**Required attribution:**
> De Vries, J., De Bruyn, S., Boerdijk, S., Juijn, D., Bijleveld, M., Van der Giesen, C.,
> Korteland, M., Odenhoven, N., Van Santen, W., Pápai, S. (2025).
> *Environmental Prices Handbook 2024: EU27 version* (Version 1.1, Reference 230107).
> CE Delft, Delft.

---

## 2. External Methodology Sources

The CE Delft handbook draws on nine external methodological sources to derive
its environmental prices. These are secondary inputs to the handbook authors,
not direct inputs to this pipeline, but they govern the downstream license of
the coefficient matrices this pipeline produces.

### 2.1 ReCiPe 2016 H — Midpoint Characterisation Factors

| Attribute | Detail |
|---|---|
| **Used for** | Midpoint characterisation factors (Tables 7–8); secondary pollutant derivation (Step 4) |
| **Full citation** | Huijbregts, M.A.J., Steinmann, Z.J.N., Elshout, P.M.F., Stam, G., Verones, F., Vieira, M., Zijp, M., Hollander, A., van Zelm, R. (2017). ReCiPe2016: a harmonised life cycle impact assessment method at midpoint and endpoint level. *International Journal of Life Cycle Assessment*, 22(2), 138–147. |
| **Report** | RIVM Report 2016-0104, Bilthoven, The Netherlands |
| **License** | **CC BY 4.0** (Open Access journal article; RIVM Report open access) |
| **Commercial use** | ✓ Yes |
| **Attribution required** | Yes — cite Huijbregts et al. 2017 |
| **Redistribution** | ✓ Allowed; adaptations permitted with attribution |
| **License URL** | https://doi.org/10.1007/s11367-016-1246-y (article); https://www.rivm.nl/en/life-cycle-assessment-lca/downloads (factors) |

---

### 2.2 EC JRC Environmental Footprint 3.0 (EF 3.0) — PEF Characterisation Factors

| Attribute | Detail |
|---|---|
| **Used for** | CAT I/II classification for Table 8; EF 3.0 characterisation factors for 16 impact categories |
| **Full citation** | Saouter, E., Biganzoli, F., Ceriani, L., Versteeg, D., Crenna, E., Zampori, L., Sala, S., Pant, R. (2018). *Supporting information to the characterisation factors of recommended EF Life Cycle Impact Assessment methods*. JRC Technical Report JRC114822. European Commission Joint Research Centre, Ispra. |
| **Governing decision** | EC Commission Decision 2011/833/EU (OJ L 330, 14.12.2011, p. 39) — reuse of Commission documents |
| **License** | **CC BY 4.0** (EU institutional content under Decision 2011/833/EU) |
| **Commercial use** | ✓ Yes — reuse authorised with source acknowledgement |
| **Attribution required** | Yes — "Source: European Commission, Joint Research Centre" |
| **Redistribution** | ✓ Allowed |
| **License URL** | https://commission.europa.eu/legal-notice_en; https://eplca.jrc.ec.europa.eu/EnvironmentalFootprint.html |

---

### 2.3 EEA / GAINS Dispersion Model (2021) — Air Pollutant Concentration Mapping

| Attribute | Detail |
|---|---|
| **Used for** | Air pollutant concentration mapping on 22×33 km grid (IPA Step 2 — impact pathway analysis for PM, NOₓ, SO₂, NH₃) |
| **Full citation** | European Environment Agency / IIASA (2021). GAINS emission scenarios and air quality dispersion modelling. EEA, Copenhagen. |
| **License** | **CC BY** (EEA Data Policy: free reuse with acknowledgement) |
| **Commercial use** | ✓ Yes |
| **Attribution required** | Yes — "Source: European Environment Agency" |
| **Redistribution** | ✓ Allowed; content may not be altered without EEA permission |
| **License URL** | https://www.eea.europa.eu/en/datahub/eea-data-policy |

---

### 2.4 IIASA GAINS Model — Emission Inventories and Source-Receptor Relationships

| Attribute | Detail |
|---|---|
| **Used for** | Emission inventories and source-receptor relationships for PM/NOₓ/SO₂/NH₃ (IPA Step 1 and Step 3) |
| **Full citation** | Klimont, Z. et al. IIASA GAINS (Greenhouse Gas and Air Pollution Interactions and Synergies) model. International Institute for Applied Systems Analysis (IIASA), Laxenburg, Austria. https://gains.iiasa.ac.at |
| **License** | **CC BY-NC 4.0** (IIASA Terms of Use) |
| **Commercial use** | ✗ Non-commercial only |
| **Attribution required** | Yes — cite IIASA and GAINS model |
| **Redistribution** | Restricted — users may not extract or reuse substantial portions of IIASA databases; limited non-exclusive non-transferable licence for personal non-commercial use |
| **Registration** | One-time registration required before access |
| **License URL** | https://iiasa.ac.at/terms-of-use; https://gains.docs.iiasa.ac.at/start/rights.html |

---

### 2.5 WHO / Chen & Hoek (2020) — PM Concentration-Response Functions (CRFs)

| Attribute | Detail |
|---|---|
| **Used for** | PM₂.₅ and PM₁₀ concentration-response functions for mortality (IPA Step 3 — dose-response) |
| **Full citation** | Chen, J. and Hoek, G. (2020). Long-term exposure to PM and all-cause and cause-specific mortality: A systematic review and meta-analysis. *Environment International*, 143, 105974. |
| **License** | **CC BY 4.0** (Elsevier open access article) |
| **Commercial use** | ✓ Yes |
| **Attribution required** | Yes — cite Chen & Hoek 2020 |
| **Redistribution** | ✓ Allowed |
| **License URL** | https://doi.org/10.1016/j.envint.2020.105974 |

---

### 2.6 WHO HRAPIE (2013) — O₃ and NO₂ Concentration-Response Functions

| Attribute | Detail |
|---|---|
| **Used for** | O₃ and NO₂ concentration-response functions (IPA Step 3 — dose-response for ozone and nitrogen dioxide) |
| **Full citation** | WHO Regional Office for Europe (2013). *Health Risks of Air Pollution in Europe — HRAPIE Project: New emerging risks to health from air pollution*. WHO Regional Office for Europe, Copenhagen. |
| **License** | **© WHO 2013 — All rights reserved** (published before WHO's 2016 open-access policy) |
| **Commercial use** | ✗ Permission required from WHO |
| **Attribution required** | Yes — cite WHO HRAPIE 2013 |
| **Redistribution** | Restricted — short quotations with attribution permitted; reproduction of tables requires WHO permission |
| **Note** | WHO publications from November 2016 onward carry CC BY-NC-SA 3.0 IGO; the 2013 report predates this policy |
| **License URL** | https://www.who.int/about/policies/publishing/open-access |

---

### 2.7 EU Water Framework Directive — Substance Priority List

| Attribute | Detail |
|---|---|
| **Used for** | Substance selection for Table 4 (water pollutants) — EU priority substances list |
| **Full citation** | European Commission (2013). Directive 2013/39/EU amending Directives 2000/60/EC and 2008/105/EC as regards priority substances in the field of water policy. *Official Journal of the European Union*, L 226, 1–17. |
| **License** | **CC BY 4.0** (EU legal acts — EC Decision 2011/833/EU governs reuse of Commission documents; EUR-Lex content freely reusable) |
| **Commercial use** | ✓ Yes |
| **Attribution required** | Yes — cite the Directive with OJ reference |
| **Redistribution** | ✓ Allowed |
| **License URL** | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32013L0039 |

---

### 2.8 Costanza et al. (2014) — Global Ecosystem Service Values

| Attribute | Detail |
|---|---|
| **Used for** | Unit ecosystem service values (USD/ha/yr) used in biodiversity/land valuation derivation |
| **Full citation** | Costanza, R., de Groot, R., Sutton, P., van der Ploeg, S., Anderson, S.J., Kubiszewski, I., Farber, S., Turner, R.K. (2014). Changes in the global value of ecosystem services. *Global Environmental Change*, 26, 152–158. |
| **License** | **All rights reserved — Elsevier B.V.** (journal article, standard copyright; not open access) |
| **Commercial use** | ✗ Reproduction requires Elsevier permission |
| **Attribution required** | Yes — cite Costanza et al. 2014 with DOI |
| **Redistribution** | ✗ Not permitted without publisher permission |
| **Note** | The methodology and unit values are widely cited in academic literature; the underlying data sources (biome areas etc.) are largely open. The paper itself is paywalled. |
| **License URL** | https://doi.org/10.1016/j.gloenvcha.2014.04.002 |

---

### 2.9 Brander, Kuik et al. (2008) — Ecosystem Services Value Transfer

| Attribute | Detail |
|---|---|
| **Used for** | Meta-analytic value transfer methodology for scaling ecosystem service unit values |
| **Full citation** | Brander, L.M., Ghermandi, A., Kuik, O., Markandya, A., Nunes, P.A.L.D., Schaafsma, M., Wagtendonk, A. (2012). Scaling up ecosystem services values: methodology, applicability, and a case study. *AMBIO*, 41, 780–793. (Earlier working paper version 2008, Report to EEA.) |
| **License** | **CC BY** (EEA working paper, 2008); journal version Springer/AMBIO academic copyright |
| **Commercial use** | EEA version: ✓ Yes; journal version: requires permission |
| **Attribution required** | Yes — cite Brander, Kuik et al. |
| **Redistribution** | EEA version: ✓ Allowed |
| **License URL** | https://www.eea.europa.eu |

---

### 2.10 ExternE / NEEDS (2008) — VOLY and Exposure-Response Functions

| Attribute | Detail |
|---|---|
| **Used for** | Value of Life Year Lost (VOLY) underpinning the mortality cost calculations; exposure-response functions for chronic mortality |
| **Full citation** | European Commission FP6 (2008). *NEEDS — New Energy Externalities Developments for Sustainability*. Final report. EC Research DG, Brussels. CORDIS Project ID: 502687. |
| **License** | **EU Publication copyright** — EU-funded research publications freely available from Publications Office of the EU; reuse permitted for non-commercial academic purposes with attribution |
| **Commercial use** | Permitted for academic/policy use with attribution; commercial redistribution of verbatim content restricted |
| **Attribution required** | Yes — cite NEEDS project / ExternE and European Commission |
| **Redistribution** | Non-commercial academic use permitted |
| **Note** | ExternE website archived (not maintained since 2012). EU Publications Office Terms apply. |
| **License URL** | https://op.europa.eu/en/publication-detail/-/publication/b2b86b52-4f18-4b4e-a134-b1c81ad8a1b2/language-en |

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

### 7.2 License summary — external methodology sources

| Source | License | Commercial use | Notes |
|---|---|---|---|
| ReCiPe 2016 H (Huijbregts et al. 2017) | CC BY 4.0 | ✓ Yes | Cite DOI 10.1007/s11367-016-1246-y |
| EC JRC EF 3.0 / PEF | CC BY 4.0 (EC Decision 2011/833/EU) | ✓ Yes | Source: EC-JRC required |
| EEA / GAINS dispersion data | CC BY | ✓ Yes | Source: EEA required |
| IIASA GAINS model | CC BY-NC 4.0 | ✗ Non-commercial only | Registration required; no database extraction |
| WHO / Chen & Hoek 2020 CRFs | CC BY 4.0 | ✓ Yes | Elsevier open access article |
| WHO HRAPIE 2013 | © WHO 2013 All Rights Reserved | ✗ Permission required | Pre-2016 policy; short citations permitted |
| EU WFD priority list | CC BY 4.0 (EC Decision 2011/833/EU) | ✓ Yes | EUR-Lex open data |
| Costanza et al. 2014 | All Rights Reserved (Elsevier) | ✗ Permission required | Paywalled journal article |
| Brander, Kuik et al. 2008 | CC BY (EEA report version) | ✓ Yes | EEA working paper version |
| ExternE / NEEDS 2008 | EU Publication copyright | Non-commercial academic | EU-funded; archived |

### 7.3 Governing license for this pipeline's outputs

The coefficient matrices produced by this pipeline are derived works of the CE Delft
handbook and embed methodology from IIASA GAINS (CC BY-NC 4.0) and the pre-2016 WHO
HRAPIE report (all rights reserved). The most restrictive applicable upstream constraint
is the CE Delft proprietary license, which prohibits commercial redistribution.

Pipeline outputs are made available under **CC BY-NC 4.0** (Attribution, Non-Commercial)
consistent with the CE Delft source license. Users must:

1. Cite the CE Delft handbook (§1 above)
2. Cite the pipeline: Euler, D. (2026). *CE Delft Environmental Prices Value Factor
   Pipeline* (vf_cedelft). Greenings. https://github.com/Greenings/transitionvaluation
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

*Document Version 3.0 | Last Updated 2026-03-09 | Maintained by Greenings | dimitrij.euler@greenings.org*
*Value factors: CE Delft (De Vries et al. 2025) | Scripts: Dr Dimitrij Euler with support of Claude Code (Anthropic)*
