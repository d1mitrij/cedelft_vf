"""
Configuration for CE Delft Environmental Prices Handbook 2024 value factors.

Source:  Environmental Prices Handbook 2024: EU27 version
Authors: CE Delft (Joukje de Vries, Sander de Bruyn, Sjoerd Boerdijk, Daan Juijn,
         Marijn Bijleveld, Coen van der Giesen, Marisa Korteland, Nikki Odenhoven,
         Ward van Santen, Simon Pápai)
Version: 1.1 (April 2025)
Price level: EUR 2021
"""

from pathlib import Path

_ROOT = Path(__file__).parent
_OUTPUT_DIR = _ROOT / "output"

TABLE_GROUPS = {
    "air_pollutants": {
        "id": "01",
        "title": "Environmental prices for emissions of air pollutants",
        "source_table": "Table 3",
        "chapter": "2.3.1",
        "description": (
            "Environmental prices for emissions of key air pollutants in the EU27, "
            "in EUR 2021 per kg. Covers greenhouse gases, classic air pollutants, "
            "heavy metals and organic compounds. Lower/upper recommended for SCBA; "
            "central value recommended for LCA and CSR applications."
        ),
        "unit": "EUR_2021/kg",
        "notes": (
            "PM2.5 and PM10 should not be included simultaneously. "
            "EU27 average values; not suitable for site-specific studies. "
            "Source types (stationary, traffic) can further differentiate PM and NOx."
        ),
    },
    "water_pollutants": {
        "id": "02",
        "title": "Environmental prices for emissions to water",
        "source_table": "Table 4",
        "chapter": "2.3.2",
        "description": (
            "Environmental prices for emissions of priority pollutants to freshwater "
            "and saltwater in the EU27, in EUR 2021 per kg. Based on Water Framework "
            "Directive monitoring priority substances. Wide lower-upper ranges reflect "
            "uncertainty in toxicity characterisation models (ReCiPe 2016 perspectives)."
        ),
        "unit": "EUR_2021/kg",
        "notes": (
            "Freshwater and saltwater values reported separately. "
            "Central value is most plausible; lower/upper for SCBA uncertainty bands."
        ),
    },
    "soil_pollutants": {
        "id": "03",
        "title": "Environmental prices for emissions to soil",
        "source_table": "Table 5",
        "chapter": "2.3.3",
        "description": (
            "Environmental prices for emissions of key pollutants to soil in the EU27, "
            "in EUR 2021 per kg. Covers impacts on human health and ecosystems. "
            "IQ effects on human health are excluded. Selection guided by CE Delft (2022a) "
            "exploratory analysis of environmental damage from waste."
        ),
        "unit": "EUR_2021/kg",
        "notes": (
            "Does not include IQ effects. Wide ranges reflect uncertainty in "
            "toxicity characterisation and dose-response relationships."
        ),
    },
    "land_use": {
        "id": "04",
        "title": "Environmental prices for land use occupation",
        "source_table": "Table 6",
        "chapter": "2.3.4",
        "description": (
            "Environmental prices for land-use occupation in the EU27 for effects on "
            "biodiversity relative to a 'natural state', in EUR 2021 per m2 per year. "
            "Based on biodiversity loss over a 50-year time horizon. Suitable for "
            "natural capital accounting by companies."
        ),
        "unit": "EUR_2021/m2/year",
        "notes": (
            "Recommended for use with caution. Preferable to measure precise biodiversity "
            "loss directly. Not suitable for land-use change valuations without "
            "additional analysis on the baseline and alternative scenarios."
        ),
    },
    "midpoints_recipe": {
        "id": "05",
        "title": "Environmental prices for LCA: ReCiPe 2016 midpoints",
        "source_table": "Table 7",
        "chapter": "2.4.1",
        "description": (
            "Midpoint-level environmental prices for use in life cycle assessments (LCA), "
            "based on the ReCiPe 2016 characterisation model for EU27 average conditions. "
            "Enables single-score weighting of LCA results. Prices in EUR 2021 per "
            "ReCiPe characterisation unit."
        ),
        "unit": "EUR_2021/characterisation_unit",
        "notes": (
            "Cat A: high certainty (recommended for all LCA applications). "
            "Cat B: higher uncertainty (use with caution). "
            "Cat C: outside ReCiPe but important for damage-cost estimates. "
            "Must be used with ReCiPe 2016 characterisation factors. "
            "Central values for LCA/CSR; lower/upper for SCBA sensitivity analysis."
        ),
    },
    "midpoints_pef": {
        "id": "06",
        "title": "Midpoint prices for PEF impact categories (CAT I and II)",
        "source_table": "Table 8",
        "chapter": "2.4.2",
        "description": (
            "Central midpoint environmental prices for EU27 and Netherlands for Product "
            "Environmental Footprint (PEF) impact categories rated CAT I and CAT II. "
            "CAT I: recommended and satisfactory. CAT II: recommended but needs improvement. "
            "Applicable to EN15804-A2 and related European LCA methods."
        ),
        "unit": "EUR_2021/characterisation_unit",
        "notes": (
            "CAT III not included (insufficient data within handbook scope). "
            "Central values only. EU27 and Netherlands-specific values provided. "
            "Must be used with corresponding PEF characterisation factors."
        ),
    },
}

PUBLICATION = {
    "title": "Environmental Prices Handbook 2024",
    "subtitle": (
        "EU27 version – Methodical justification of key indicators used for "
        "the valuation of emissions and environmental impact"
    ),
    "authors": (
        "Joukje de Vries, Sander de Bruyn, Sjoerd Boerdijk, Daan Juijn, "
        "Marijn Bijleveld, Coen van der Giesen, Marisa Korteland, "
        "Nikki Odenhoven, Ward van Santen, Simon Pápai"
    ),
    "publisher": "CE Delft",
    "publication_date": "April 2025",
    "version": "1.1",
    "reference_number": "230107",
    "price_level": "EUR_2021",
    "geographic_scope": "EU27",
    "methodology": "Impact Pathway Approach (IPA) with ReCiPe 2016 and PEF characterisation",
}


def get_output_path(key: str) -> Path:
    _OUTPUT_DIR.mkdir(exist_ok=True)
    cfg = TABLE_GROUPS[key]
    return _OUTPUT_DIR / f"{cfg['id']}_cedelft_{key}.csv"


def get_excel_path(key: str) -> Path:
    _OUTPUT_DIR.mkdir(exist_ok=True)
    cfg = TABLE_GROUPS[key]
    return _OUTPUT_DIR / f"{cfg['id']}_cedelft_{key}.xlsx"


def get_table_config(key: str) -> dict:
    if key not in TABLE_GROUPS:
        raise KeyError(f"Unknown table group '{key}'. Available: {list(TABLE_GROUPS)}")
    return {**TABLE_GROUPS[key], "key": key, **PUBLICATION}
