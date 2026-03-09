# Methodology — CE Delft Environmental Prices Handbook 2024

## Data Source

> **Environmental Prices Handbook 2024: EU27 version**
> CE Delft, April 2025 (Version 1.1, Reference: 230107)
>
> **Authors:** Joukje de Vries, Sander de Bruyn, Sjoerd Boerdijk, Daan Juijn,
> Marijn Bijleveld, Coen van der Giesen, Marisa Korteland, Nikki Odenhoven,
> Ward van Santen, Simon Pápai
>
> All methodology described below reflects the CE Delft approach as documented in
> the handbook. The extraction pipeline (scripts) was developed by **Dimitrij Euler
> (Greenings)** with the support of **Claude Code (Anthropic)**.

---

## 1. Purpose and Scope

The CE Delft Environmental Prices Handbook provides monetary values for the societal
cost of environmental pollution. These **environmental prices** quantify the welfare
loss per unit of emission (kg, m², kBq, etc.) and can be used in:

1. **Social Cost-Benefit Analyses (SCBA)** — valuing the environmental impact of
   policy measures and public investments (lower/upper variants recommended)
2. **Life Cycle Assessment (LCA)** — single-score weighting of environmental impacts
   (central values recommended; used as weighing ratios)
3. **Corporate Social Responsibility (CSR)** — environmental profit & loss accounts,
   natural capital accounting (central values recommended)

The 2024 EU27 edition covers **more than 3,000 environmentally hazardous pollutants**
at EUR 2021 price levels, representing a major update from the 2018 EU version.

---

## 2. Three-Level Framework

Environmental prices are derived through a three-level impact pathway structure:

```
LEVEL 1 — INTERVENTIONS
    Emissions to air, water, soil
    Nuisances/extraction (noise, ionising radiation, land use, water use)

        |
        | (environmental fate and dispersion models)
        v

LEVEL 2 — MIDPOINTS (Environmental themes)
    Climate change, ozone depletion, particulate matter formation,
    photochemical oxidant formation, eutrophication, acidification,
    human toxicity (cancer / non-cancer), ecotoxicity (terrestrial /
    freshwater / marine), ionising radiation, land use, mineral/fossil
    resource extraction, water consumption, noise pollution

        |
        | (dose-response relationships + monetary valuation)
        v

LEVEL 3 — ENDPOINTS (Welfare impacts)
    Human health (mortality, morbidity, genetic effects)
    Ecosystem services (biodiversity, agricultural/forestry yields)
    Buildings and materials (repair, cleaning, cultural heritage)
    Resource availability (raw material scarcity)
    Well-being (noise nuisance, visual impacts)
```

---

## 3. Four-Step Derivation Approach

### Step 1 — Establish Endpoint Valuations

Damage values are defined for each endpoint based on welfare economics literature:

| Endpoint | Valuation method | Key value |
|----------|-----------------|-----------|
| Human health (mortality) | VOLY — stated preferences (WTP) | € 85,000/VOLY (central, 2021) |
| Human health (morbidity) | WTP + cost-of-illness studies | Varies by effect (see handbook Table 11) |
| Ecosystem services (biodiversity) | Stated preferences + ecosystem service studies | PDF-based (€/species-fraction lost) |
| Buildings and materials | Revealed preferences (actual maintenance spending) | Repair + cleaning cost estimates |
| Resource availability | Replacement/strategic stock costs | Scarcity rent approach |

**VOLY (Value of Life Year Lost) variants:**

| Variant | 2021 Value | Income elasticity |
|---------|-----------|-------------------|
| Lower | € 57,500 | 0.3 |
| Central | € 85,000 | 0.65 |
| Upper | € 128,000 | 1.0 |

### Step 2 — Calculate Primary Pollutant Prices (~40 pollutants)

Using the **Impact Pathway Approach (IPA)**:

```
Price[s] = Σ_pathways (Emission[s] → Dispersion → Concentration → Dose-response → Endpoint damage × Monetary value)
```

**Dispersion models used:**
- Air: EEA 2021 GAINS/SHERPA model (22×33 km grid, finer resolution than 2018 edition)
- Specific NO₂ dispersion: 1×1 km resolution
- Water: fate and transport models per water body type

**Dose-response functions (Concentration-Response Functions, CRFs):**
- PM₂.₅/PM₁₀ mortality: Chen & Hoek (2020) relative risk approach with updated WHO data
- NO₂ mortality: WHO (2013) + recent epidemiological literature
- O₃: HRAPIE (2013) + WHO updates
- Ecosystem effects: EUNIS/ReCiPe 2016 characterisation factors

### Step 3 — Allocate to Midpoint Prices

Using **ReCiPe 2016 characterisation factors** (hierarchical/average perspective):

```
MidpointPrice[theme] = Σ_substances (PrimaryPrice[s] × CharacterisationFactor[s, theme] × EmissionShare[s])
```

Emission-weighted averaging across all EU27 emission sources ensures that the
midpoint price reflects actual emission composition in the EU.

### Step 4 — Derive Secondary Pollutant Prices (3,000+ substances)

For substances without direct IPA modelling, prices are derived by applying
ReCiPe characterisation factors to the midpoint prices:

```
Price[secondary] = Σ_themes (MidpointPrice[theme] × CharacterisationFactor[secondary, theme])
```

This allows coverage of the full Ecoinvent/ReCiPe substance database.

---

## 4. Key Updates in 2024 vs. 2018 Edition

| Aspect | 2018 EU version | 2024 EU version |
|--------|----------------|-----------------|
| Price level | EUR 2015 | EUR 2021 |
| Income elasticity (VOLY) | 0% | 0.3–1.0 (by variant) |
| Social discount rate | 3% | 2.25% |
| IPA dispersion model | NEEDS (2008) | EEA/GAINS (2021) |
| Spatial resolution | 50×50 km | 22×33 km (NO₂: 1×1 km) |
| Characterisation model | ReCiPe 2008 | ReCiPe 2016 H + PEF |
| Health model | NEEDS CRFs | Relative Risk approach |
| Black carbon | Not included | Added with separate valuation |
| Secondary organic aerosols | Not included | Added to PM formation |
| Ecosystem valuation | Kuik et al. 2008 | Kuik 2008 + Costanza et al. 2014 |
| Raw materials valuation | Not included | New comprehensive approach |
| PEF midpoints | Not included | CAT I and II included |

---

## 5. Table Groups Extracted by This Pipeline

### Table 3 — Air Pollutants (EUR 2021/kg)

**Coverage:** 20 substances across three categories:

1. **Greenhouse gases and common air pollutants:**
   CO₂, CFC-11, PM2.5, PM10, NOₓ, SO₂, NH₃, NMVOC, CH₄

2. **Heavy metals:**
   As, Cd, Cr-VI, Pb, Hg, Ni

3. **Organic compounds:**
   1,3-Butadiene, Benzene, Benzo(a)pyrene, Dioxins, Formaldehyde

**Note on PM:** PM2.5 and PM10 should not be used simultaneously as they represent
overlapping size fractions of the same emissions. The handbook provides more
differentiated values by emission source type (stationary/traffic) in Chapter 6.

### Table 4 — Water Pollutants (EUR 2021/kg)

**Coverage:** 22 substances × 2 receiving water bodies (freshwater, saltwater) = 44 rows.

Substances selected based on the EU Water Framework Directive priority pollutant list.
Prices cover eutrophication (N, P), ecotoxicity and human toxicity pathways.
Wide uncertainty ranges reflect different characterisation model perspectives in ReCiPe 2016.

### Table 5 — Soil Pollutants (EUR 2021/kg)

**Coverage:** 21 substances including heavy metals, PAHs, and nutrients.

Based on an exploratory analysis of environmental damage from waste (CE Delft, 2022a).
Covers human health (excluding IQ effects) and ecosystem impacts only.

### Table 6 — Land Use (EUR 2021/m²/year)

**Coverage:** Land-use occupation relative to a natural baseline.

Quantifies biodiversity loss due to average EU27 land use over a 50-year time horizon.
Valued via stated preferences and ecosystem service studies. Suitable for natural capital
accounting. Not suitable for land-use change analysis without additional modelling.

**Central value:** € 0.053 per m² per year

### Table 7 — ReCiPe 2016 Midpoints (EUR 2021/unit)

**Coverage:** 19 impact categories with reliability classification:

- **Category A (14):** High certainty — Climate change, ozone depletion, ionising radiation,
  oxidant formation (×2), particulate matter, acidification, eutrophication (×2), ecotoxicity (×3),
  human toxicity (×2)
- **Category B (4):** Higher uncertainty — Land use, mineral extraction, fossil extraction,
  water consumption
- **Category C (1):** Outside ReCiPe but required for completeness — NO₂ mortality
  (additional step beyond standard ReCiPe characterisation)

**Usage with LCA:** Midpoint prices must be combined with the corresponding ReCiPe 2016
characterisation factors computed from an LCA. The midpoint price represents the
emission-weighted average damage per unit of the ReCiPe characterisation score.

### Table 8 — PEF Midpoints (EUR 2021/unit)

**Coverage:** 9 impact categories rated CAT I or CAT II by the European Commission JRC.

- **CAT I (5):** Climate change, ozone depletion, ionising radiation, oxidant formation,
  particulate matter formation
- **CAT II (4):** Acidification, freshwater eutrophication, marine eutrophication,
  terrestrial eutrophication

Prices provided for both EU27 average and Netherlands-specific conditions (central
values only). Applicable to EN15804-A2 and other PEF-based LCA standards.

---

## 6. Uncertainty Framework

### Three-Variant Approach

All pollutant and midpoint prices are reported with three variants:

| Variant | Recommended use | Represents |
|---------|----------------|------------|
| **Lower** | SCBA (lower sensitivity bound) | Conservative dose-response; lower VOLY; Individualist ReCiPe perspective for toxics |
| **Central** | LCA, CSR, general applications | Most likely estimate; balanced assumptions |
| **Upper** | SCBA (upper sensitivity bound) | Higher dose-response estimates; higher VOLY; Egalitarian ReCiPe perspective for toxics |

### Sources of Uncertainty

1. **Dose-response uncertainty** — CRF shape and slope at low concentrations
2. **Valuation uncertainty** — VOLY estimates, ecosystem service values
3. **Model uncertainty** — dispersion model assumptions, spatial averaging
4. **Characterisation uncertainty** — ReCiPe 2016 perspective (I/H/E) for toxic substances
5. **Data uncertainty** — emission statistics, population exposure data

Toxic substances (heavy metals, organic compounds) typically have the widest
lower-upper ranges due to fundamentally different characterisation model assumptions
between the Individualist and Egalitarian perspectives of ReCiPe 2016.

---

## 7. Geographic Scope and Applicability

**Default scope:** EU27 average values (emission-weighted across all member states).

**Limitations:**
- Not suitable for site-specific studies (local population density, meteorology)
- Not applicable to non-EU countries without value transfer
- PM₂.₅ and NOₓ vary significantly by emission source type (point source height, urban density)
- Water N/P prices depend on limiting nutrient (freshwater vs. saltwater differs)
- Dutch-specific values provided for PEF particulate matter and some eutrophication figures

---

## 8. Value Transfer

**No value transfer is applied in the CE Delft Environmental Prices Handbook.**

Environmental prices are derived using the **Impact Pathway Approach (IPA)** directly
calibrated to EU27 conditions — population exposure, emission sources, dispersion
meteorology, and receptor densities are all EU27-specific. The result is a single
set of EU27 average values at EUR 2021 price levels.

### Value transfer guidance for non-EU use

If these values are applied outside the EU27, a value transfer procedure is required.
CE Delft documents the following guidance:

| Transfer type | Approach | Key parameter |
|---|---|---|
| **Temporal** | Inflate using country-specific CPI or GDP deflator | Eurostat HICP (EU); national CPI |
| **Geographic (income)** | Scale by income elasticity: `VF_country = VF_EU27 × (GNI_country / GNI_EU27)^ε` | ε = 0.3–1.0 (per VOLY variant) |
| **Geographic (exposure)** | Adjust population exposure and emission density | Country-specific dispersion model required |

The three uncertainty variants (lower / central / upper) embed different income
elasticity assumptions (0.3, 0.65, 1.0) that indirectly capture some geographic
income variation.

---

### External Sources Used in IPA Derivation — License Detail

The Impact Pathway Approach used to derive the EU27 environmental prices draws on
the following external sources. Each source is documented with its precise license
terms, as their licenses govern the downstream use of the derived coefficient matrices.

#### 8.1 EEA / GAINS Dispersion Model (2021) — SHERPA

| Attribute | Detail |
|---|---|
| **Used for** | Air pollutant concentration mapping on 22×33 km grid (IPA Step 2); NO₂ at 1×1 km resolution |
| **Full citation** | European Environment Agency / IIASA (2021). GAINS emission scenarios and SHERPA air quality dispersion modelling. EEA, Copenhagen. |
| **License** | **CC BY** (EEA Data Policy: all EEA materials free for commercial and non-commercial reuse with source acknowledgement) |
| **Commercial use** | ✓ Yes |
| **Attribution required** | Yes — "Source: European Environment Agency" |
| **License URL** | https://www.eea.europa.eu/en/datahub/eea-data-policy |

---

#### 8.2 IIASA GAINS Model — Emission Inventories

| Attribute | Detail |
|---|---|
| **Used for** | Emission inventories and source-receptor matrices for PM/NOₓ/SO₂/NH₃ (IPA Step 1 and Step 3) |
| **Full citation** | Klimont, Z. et al. GAINS (Greenhouse Gas and Air Pollution Interactions and Synergies) model. IIASA, Laxenburg, Austria. https://gains.iiasa.ac.at |
| **License** | **CC BY-NC 4.0** (IIASA Terms of Use) |
| **Commercial use** | ✗ Non-commercial only |
| **Attribution required** | Yes — cite IIASA and GAINS model |
| **Redistribution** | Restricted — no extraction of substantial database portions |
| **License URL** | https://iiasa.ac.at/terms-of-use |

---

#### 8.3 WHO / Chen & Hoek (2020) — PM Concentration-Response Functions

| Attribute | Detail |
|---|---|
| **Used for** | PM₂.₅ and PM₁₀ mortality concentration-response functions (IPA Step 3); replaces older HRAPIE PM functions in 2024 edition |
| **Full citation** | Chen, J. and Hoek, G. (2020). Long-term exposure to PM and all-cause and cause-specific mortality: A systematic review and meta-analysis. *Environment International*, 143, 105974. |
| **License** | **CC BY 4.0** (Elsevier open access article) |
| **Commercial use** | ✓ Yes |
| **Attribution required** | Yes — cite Chen & Hoek 2020 |
| **License URL** | https://doi.org/10.1016/j.envint.2020.105974 |

---

#### 8.4 WHO HRAPIE (2013) — O₃ and NO₂ Concentration-Response Functions

| Attribute | Detail |
|---|---|
| **Used for** | O₃ and NO₂ concentration-response functions (IPA Step 3); NOₓ/SO₂ non-primary impacts in 2024 edition |
| **Full citation** | WHO Regional Office for Europe (2013). *Health Risks of Air Pollution in Europe — HRAPIE Project*. WHO Regional Office for Europe, Copenhagen. |
| **License** | **© WHO 2013 — All rights reserved** (published before WHO's November 2016 open-access policy) |
| **Commercial use** | ✗ Permission required from WHO |
| **Attribution required** | Yes — cite WHO HRAPIE 2013 |
| **Redistribution** | Restricted; short quotation with attribution permitted |
| **License URL** | https://www.who.int/about/policies/publishing/open-access |

---

#### 8.5 Costanza et al. (2014) — Global Ecosystem Service Values

| Attribute | Detail |
|---|---|
| **Used for** | Unit ecosystem service values (USD/ha/yr) used in biodiversity and land use valuation (Table 6; ecosystem damage pathway) |
| **Full citation** | Costanza, R., de Groot, R., Sutton, P., van der Ploeg, S., Anderson, S.J., Kubiszewski, I., Farber, S., Turner, R.K. (2014). Changes in the global value of ecosystem services. *Global Environmental Change*, 26, 152–158. |
| **License** | **All rights reserved — Elsevier B.V.** (paywalled journal article; standard academic copyright) |
| **Commercial use** | ✗ Reproduction requires Elsevier permission |
| **Attribution required** | Yes — cite Costanza et al. 2014 with DOI |
| **Redistribution** | ✗ Not permitted without publisher permission |
| **License URL** | https://doi.org/10.1016/j.gloenvcha.2014.04.002 |

---

#### 8.6 Brander, Kuik et al. (2008) — Ecosystem Value Transfer

| Attribute | Detail |
|---|---|
| **Used for** | Meta-analytic value transfer methodology for scaling ecosystem service unit values to EU27 context |
| **Full citation** | Brander, L.M., Ghermandi, A., Kuik, O., Markandya, A., Nunes, P.A.L.D., Schaafsma, M., Wagtendonk, A. (2012). Scaling up ecosystem services values: methodology, applicability, and a case study. *AMBIO*, 41, 780–793. (Earlier version: EEA working paper 2008.) |
| **License** | EEA working paper version: **CC BY** (EEA Data Policy). Journal version: Springer/AMBIO academic copyright. |
| **Commercial use** | EEA version: ✓ Yes. Journal version: requires permission |
| **Attribution required** | Yes — cite Brander, Kuik et al. |
| **License URL** | https://www.eea.europa.eu |

---

#### 8.7 ReCiPe 2016 H — Midpoint Characterisation Factors

| Attribute | Detail |
|---|---|
| **Used for** | Midpoint characterisation factors (IPA Step 3 → Tables 7–8); secondary pollutant derivation (IPA Step 4) |
| **Full citation** | Huijbregts, M.A.J. et al. (2017). ReCiPe2016: a harmonised life cycle impact assessment method at midpoint and endpoint level. *International Journal of Life Cycle Assessment*, 22(2), 138–147. RIVM Report 2016-0104. |
| **License** | **CC BY 4.0** (open-access journal article; RIVM repository open access) |
| **Commercial use** | ✓ Yes |
| **Attribution required** | Yes — cite Huijbregts et al. 2017 |
| **License URL** | https://doi.org/10.1007/s11367-016-1246-y |

---

#### 8.8 EC JRC EF 3.0 — PEF Characterisation Factors

| Attribute | Detail |
|---|---|
| **Used for** | CAT I/II classification for Table 8; EF 3.0 characterisation factors for 9 PEF midpoint categories |
| **Full citation** | Saouter, E. et al. (2018). *Supporting information to the characterisation factors of recommended EF Life Cycle Impact Assessment methods*. JRC Technical Report JRC114822. European Commission Joint Research Centre. |
| **License** | **CC BY 4.0** (EU institutional content under EC Decision 2011/833/EU) |
| **Commercial use** | ✓ Yes — reuse authorised with source acknowledgement |
| **Attribution required** | Yes — "Source: European Commission, Joint Research Centre" |
| **License URL** | https://commission.europa.eu/legal-notice_en; https://publications.jrc.ec.europa.eu/repository/handle/JRC114822 |

---

#### 8.9 ExternE / NEEDS (2008) — VOLY Foundation

| Attribute | Detail |
|---|---|
| **Used for** | Value of Life Year Lost (VOLY) underpinning — the EUR 85,000/VOLY central value originates from this EU-funded research programme |
| **Full citation** | European Commission FP6 (2008). *NEEDS — New Energy Externalities Developments for Sustainability* (Project ID: 502687). Final report. EC Research DG, Brussels. |
| **License** | **EU Publication copyright** — EU-funded project; reports freely available from Publications Office of the EU; non-commercial academic reuse permitted with attribution |
| **Commercial use** | Non-commercial academic/policy use: permitted with attribution |
| **Attribution required** | Yes — cite NEEDS project / ExternE and European Commission |
| **License URL** | https://op.europa.eu/en/publication-detail/-/publication/b2b86b52-4f18-4b4e-a134-b1c81ad8a1b2/language-en |

---

#### 8.10 EU Water Framework Directive — Priority Substance List

| Attribute | Detail |
|---|---|
| **Used for** | Substance selection for Table 4 (water pollutants): the 22 substances are drawn from the EU WFD priority pollutants list |
| **Full citation** | European Commission (2013). Directive 2013/39/EU amending Directives 2000/60/EC and 2008/105/EC as regards priority substances in water policy. *OJ L 226*, 1–17. |
| **License** | **CC BY 4.0** (EU legal acts — freely reusable under EC Decision 2011/833/EU; EUR-Lex open access) |
| **Commercial use** | ✓ Yes |
| **Attribution required** | Yes — cite Directive 2013/39/EU with OJ reference |
| **License URL** | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32013L0039 |

---

#### 8.11 Eurostat — HICP for Temporal Value Transfer Guidance

| Attribute | Detail |
|---|---|
| **Used for** | Recommended source for temporal value transfer of EU27 prices to other years: `VF(t) = VF(2021) × HICP(t) / HICP(2021)` |
| **Full citation** | Eurostat (annual). *Harmonised Index of Consumer Prices (HICP)*. European Commission, Luxembourg. https://ec.europa.eu/eurostat/web/hicp |
| **License** | **CC BY 4.0** (Eurostat / EC data under Decision 2011/833/EU) |
| **Commercial use** | ✓ Yes — free reuse, adaptation, and redistribution including commercial |
| **Attribution required** | Yes — "Source: Eurostat" |
| **License URL** | https://ec.europa.eu/eurostat/help/copyright-notice |

---

## 9. Relation to Other Value Factor Systems

| System | Organisation | Geographic scope | Currency | Year |
|--------|-------------|-----------------|----------|------|
| CE Delft Handbook 2024 | CE Delft (NL) | EU27 | EUR 2021 | 2025 |
| UBA Methodological Convention 4.0 | German EPA | Germany | EUR 2025 | 2025 |
| EPS 2015d.1 | Swedish Life Cycle Centre | Global (uniform) | EUR 2015 | 2016 |
| eQALY | Valuing Impact | Global (188 countries) | USD 2023 | 2024 |

The CE Delft prices are also cited in the eQALY framework (Valuing Impact, 2025)
as the source for natural capital pollution valuation factors.

---

## 10. Pipeline Extraction Approach

### Data Transcription

All values in `pipeline.py` are manually transcribed from the following handbook tables
and verified against the source markdown (converted from the official PDF):

| Script data variable | Handbook source | Verification |
|---------------------|-----------------|--------------|
| `_AIR_DATA` | Table 3 (p. 32) | Verified against Table 1 (p. 8) summary |
| `_WATER_DATA` | Table 4 (p. 33) | Verified against handbook text §2.3.2 |
| `_SOIL_DATA` | Table 5 (p. 34) | Verified against handbook text §2.3.3 |
| `_LAND_DATA` | Table 6 (p. 35) | Verified against handbook text §2.3.4 |
| `_RECIPE_DATA` | Table 7 (p. 35-36) | Verified against Table 2 (p. 9) summary |
| `_PEF_DATA` | Table 8 (p. 37) | Verified against handbook text §2.4.2 |

### Output Format

Tidy (long) CSV format — one row per unique pollutant/medium/category combination.
Each file includes: source table reference, chapter, lower/central/upper values, unit string.

Excel output includes a formatted "Value Factors" sheet and a "Metadata" sheet with
full publication attribution.

---

## 11. Citation

When using these value factors in research or policy analysis, cite the original source:

> De Vries, J., De Bruyn, S., Boerdijk, S., Juijn, D., Bijleveld, M., Van der Giesen, C.,
> Korteland, M., Odenhoven, N., Van Santen, W., Pápai, S. (2025).
> *Environmental Prices Handbook 2024: EU27 version* (Version 1.1, Reference 230107).
> CE Delft, Delft.

For the extraction pipeline:

> Euler, D. (2026). *CE Delft Environmental Prices Value Factor Pipeline* (vf_cedelft).
> Developed with the support of Claude Code (Anthropic). Greenings.
