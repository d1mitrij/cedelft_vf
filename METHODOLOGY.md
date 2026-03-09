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

### Value transfer for non-EU use

If these values are applied outside the EU27, a value transfer procedure is required.
CE Delft documents the following guidance:

| Transfer type | Approach | Key parameter |
|---|---|---|
| **Temporal** | Inflate using country-specific CPI or GDP deflator | Eurostat HICP (EU) |
| **Geographic (income)** | Scale by income elasticity: `VF_country = VF_EU27 × (GNI_country / GNI_EU27)^ε` | Income elasticity ε = 0.3–1.0 (per VOLY variant) |
| **Geographic (exposure)** | Adjust population exposure and emission density | Country-specific dispersion model required |

The three uncertainty variants (lower / central / upper) embed different income
elasticity assumptions (0.3, 0.65, 1.0) that indirectly capture some geographic
income variation.

### External sources used in derivation

| Stage | External source | Role |
|---|---|---|
| Dispersion modelling | EEA/GAINS model (2021), SHERPA | Concentration mapping for air pollutants |
| Dose-response | Chen & Hoek (2020); WHO HRAPIE (2013); IARC | CRFs for PM, NO₂, O₃, carcinogens |
| Ecosystem valuation | Costanza et al. (2014); Kuik (2008) | Biodiversity / ecosystem service values |
| Characterisation factors | ReCiPe 2016 H (Huijbregts et al. 2017) | Midpoint → endpoint; secondary pollutant prices |
| PEF categorisation | EC JRC EF 3.0 (2018); EN 15804-A2 | CAT I/II assignment for Table 8 |
| EU mortality valuation | VOLY — ExternE / NEEDS project (2008) | Value of Life Year Lost |
| Water framework | EU WFD priority substances list | Table 4 substance selection |

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
