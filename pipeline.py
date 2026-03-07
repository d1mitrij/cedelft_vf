"""
CE Delft Environmental Prices Handbook 2024 — value factor extraction pipeline.

All 6 table groups are hard-coded from the verified handbook tables (Tables 3–8).
Produces CSV (UTF-8, tidy/long format) and formatted Excel (.xlsx) outputs.

Usage:
    from pipeline import run_table, run_all
    run_table("air_pollutants")   # one group
    run_all()                     # all six groups
"""

import csv
from pathlib import Path

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment

import config


# ---------------------------------------------------------------------------
# Hard-coded data — Table 3: Air pollutants (EUR 2021/kg)
# Columns: pollutant_id, pollutant_name, lower, central, upper, notes
# ---------------------------------------------------------------------------
_AIR_DATA = [
    ("CO2",          "Carbon dioxide",                            0.050,       0.130,       0.160,       ""),
    ("CFC-11",       "Chlorofluorocarbons",                       283,         725,         926,         ""),
    ("PM2.5",        "Particulate matter <2.5 um",                55.4,        81.2,        134,         "Use PM2.5 or PM10, not both"),
    ("PM10",         "Particulate matter <10 um",                 29.7,        44.3,        73.3,        "Use PM2.5 or PM10, not both"),
    ("NOx",          "Nitrogen oxides",                           12.8,        19.3,        31.1,        ""),
    ("SO2",          "Sulphur dioxide",                           16.9,        26.6,        45.3,        ""),
    ("NH3",          "Ammonia",                                   17.4,        25.2,        39.5,        ""),
    ("NMVOC",        "Volatile organic compounds (non-methane)",  1.53,        2.16,        3.49,        ""),
    ("CH4",          "Methane",                                   1.80,        4.68,        5.77,        ""),
    ("As",           "Arsenic",                                   6271,        9275,        13980,       "Heavy metal"),
    ("Cd",           "Cadmium",                                   105034,      155294,      233924,      "Heavy metal"),
    ("Cr-VI",        "Chromium VI",                               1815,        2703,        4121,        "Heavy metal"),
    ("Pb",           "Lead",                                      18455,       27287,       41106,       "Heavy metal"),
    ("Hg",           "Mercury",                                   9983,        14951,       23019,       "Heavy metal"),
    ("Ni",           "Nickel",                                    68,          126,         257,         "Heavy metal"),
    ("1.3-Butadiene","1,3-Butadiene",                             1.37,        1.91,        2.87,        "Organic compound"),
    ("Benzene",      "Benzene",                                   0.275,       0.394,       0.593,       "Organic compound"),
    ("BaP",          "Benzo(a)pyrene",                            3859,        5704,        8590,        "Organic compound / PAH"),
    ("Dioxins",      "Dioxins",                                   34071638,    50367195,    75846980,    "Organic compound; bioaccumulative"),
    ("Formaldehyde", "Formaldehyde",                              0.474,       0.642,       0.965,       "Organic compound"),
]

# ---------------------------------------------------------------------------
# Table 4: Water pollutants (EUR 2021/kg)
# Columns: pollutant_name, fw_lower, fw_central, fw_upper, sw_lower, sw_central, sw_upper
# ---------------------------------------------------------------------------
_WATER_DATA = [
    ("Arsenic",                171,      2411,     11361,    0.061,    188,      958),
    ("Barium",                 2.07,     6.02,     20,       0.0043,   0.161,    0.79),
    ("Benzo(a)anthracene",     0,        33.9,     43.9,     0,        5.44,     7.0),
    ("Benzo(a)pyrene",         100,      148,      223,      7.7,      11.4,     17.0),
    ("Cadmium",                3.06,     31.5,     144,      0.119,    9.0,      44.8),
    ("Carbendazim",            0.77,     1.10,     1.45,     0.0138,   0.0195,   0.0252),
    ("Cypermethrin",           957,      1360,     1770,     122,      174,      230),
    ("Deltamethrin",           98,       139,      180,      9.0,      12.7,     16.5),
    ("Esfenvalerate",          1241,     1760,     2280,     34,       48.0,     62.1),
    ("Fluoranthene",           10.3,     14.6,     19.2,     0.89,     1.27,     1.65),
    ("Phosphate",              0.845,    1.23,     3.34,     0,        0,        0),
    ("Imidacloprid",           0.267,    0.386,    0.541,    0.00325,  0.00461,  0.00598),
    ("Irgarol/Cybutryne",      0,        2141,     2772,     0,        58.1,     75),
    ("Cobalt",                 0.087,    0.225,    0.747,    0.0294,   0.176,    0.781),
    ("Copper",                 2.21,     3.46,     5.56,     0.79,     2.28,     6.60),
    ("Mercury",                9.1,      1346,     6802,     0.40,     554,      2819),
    ("Lambda-cyhalothrin",     734,      1045,     1364,     140,      202,      270),
    ("Methylpirimiphos",       21.0,     30.4,     42.2,     0.318,    0.453,    0.597),
    ("Nickel",                 9.9,      37.7,     140,      0.219,    4.70,     23),
    ("Nitrate (N total)",      2.27,     4.23,     8.19,     7.64,     14.3,     27.6),
    ("Selenium",               0.215,    0.513,    1.59,     0.073,    0.358,    1.53),
    ("Thallium",               7.3,      149,      733,      0.106,    25.0,     140),
]

# ---------------------------------------------------------------------------
# Table 5: Soil pollutants (EUR 2021/kg)
# Columns: pollutant_name, lower, central, upper
# ---------------------------------------------------------------------------
_SOIL_DATA = [
    ("Antimony (Sb)",          5.15,     19.1,     70.0),
    ("Anthracene",             0.119,    0.168,    0.218),
    ("Arsenic (As)",           19.5,     168,      884),
    ("Barium (Ba)",            15.4,     25.5,     48.1),
    ("Benzo(a)anthracene",     0,        0.219,    0.284),
    ("Benzo(a)pyrene",         1.57,     2.31,     3.49),
    ("Cadmium (Cd)",           9.3,      2224,     11320),
    ("Chromium (Cr) III",      0.00256,  0.0092,   0.0298),
    ("Phenanthrene",           0.028,    0.0403,   0.0520),
    ("Fluoranthene",           0.13,     0.18,     0.243),
    ("Cobalt (Co)",            0.000557, 0.094,    0.551),
    ("Copper (Cu)",            0.0166,   0.431,    2.15),
    ("Mercury (Hg)",           1.69,     280,      1425),
    ("Lead (Pb)",              0.97,     23.0,     118),
    ("Molybdenum (Mo)",        4.57,     28.0,     143),
    ("Naphthalene",            0.038,    3.11,     4.68),
    ("Nickel (Ni)",            5.80,     45.1,     287),
    ("Selenium (Se)",          0.00369,  0.201,    1.15),
    ("Tin (Sn)",               0.000143, 0.0708,   0.418),
    ("Vanadium (V)",           0.226,    1.60,     7.5),
    ("Zinc (Zn)",              0.0510,   787,      4003),
]

# ---------------------------------------------------------------------------
# Table 6: Land use (EUR 2021/m2/year)
# Columns: category, lower, central, upper
# ---------------------------------------------------------------------------
_LAND_DATA = [
    ("Land use occupation", 0.037, 0.053, 0.069),
]

# ---------------------------------------------------------------------------
# Table 7: ReCiPe 2016 midpoints (EUR 2021/unit)
# Columns: impact_category, unit, lower, central, upper, category
# category: A = certain, B = higher uncertainty, C = outside ReCiPe
# ---------------------------------------------------------------------------
_RECIPE_DATA = [
    ("Climate change",                          "EUR_2021/kg_CO2-eq.",          0.05,     0.13,     0.16,     "A"),
    ("Ozone depletion",                         "EUR_2021/kg_CFC-11-eq.",       15.2,     29.1,     69.6,     "A"),
    ("Ionising radiation",                      "EUR_2021/kBq_Co-60-eq.",       0.00275,  0.00422,  0.00594,  "A"),
    ("Oxidant formation, human health",         "EUR_2021/kg_NOx-eq.",          1.28,     1.86,     2.97,     "A"),
    ("Oxidant formation, terrestrial ecosystems","EUR_2021/kg_NOx-eq.",         0.416,    0.416,    0.526,    "A"),
    ("Particulate matter formation",            "EUR_2021/kg_PM2.5-eq.",        58.5,     84.7,     138.1,    "A"),
    ("Acidification",                           "EUR_2021/kg_SO2-eq.",          2.67,     5.28,     9.30,     "A"),
    ("Freshwater eutrophication",               "EUR_2021/kg_P-eq.",            2.56,     3.74,     10.13,    "A"),
    ("Marine eutrophication",                   "EUR_2021/kg_N-eq.",            7.64,     14.25,    27.60,    "A"),
    ("Terrestrial ecotoxicity",                 "EUR_2021/kg_1.4-DCB-eq.",      0.00045,  0.00064,  0.00083,  "A"),
    ("Freshwater ecotoxicity",                  "EUR_2021/kg_1.4-DCB-eq.",      0.0148,   0.0209,   0.0271,   "A"),
    ("Marine ecotoxicity",                      "EUR_2021/kg_1.4-DCB-eq.",      0.0022,   0.0032,   0.0041,   "A"),
    ("Human toxicity, cancer-related",          "EUR_2021/kg_1.4-DCB-eq.",      2.70,     3.99,     6.01,     "A"),
    ("Human toxicity, non-cancer-related",      "EUR_2021/kg_1.4-DCB-eq.",      0.048,    0.071,    0.106,    "A"),
    ("Land use",                                "EUR_2021/m2_a_crop-eq.",       0.070,    0.099,    0.128,    "B"),
    ("Mineral extraction",                      "EUR_2021/kg_Cu-eq.",           0.0,      0.0140,   0.0826,   "B"),
    ("Fossil extraction",                       "EUR_2021/kg_oil-eq.",          0.0,      0.028,    0.163,    "B"),
    ("Water consumption",                       "EUR_2021/m3",                  0.0,      0.407,    0.811,    "B"),
    ("NO2 mortality (addition)",                "EUR_2021/kg_NOx-eq.",          4.02,     5.94,     8.90,     "C"),
]

# ---------------------------------------------------------------------------
# Table 8: PEF midpoint prices, CAT I and II (EUR 2021/unit)
# Columns: impact_category, pef_unit, eu27_central, nl_central, pef_category
# ---------------------------------------------------------------------------
_PEF_DATA = [
    ("Climate change",                  "kg_CO2-eq.",           0.130,     0.130,     "CAT I"),
    ("Ozone depletion",                 "kg_CFC-11-eq.",        29.1,      29.1,      "CAT I"),
    ("Ionising radiation",              "kBq_U235-eq.",         0.00071,   0.00071,   "CAT I"),
    ("Oxidant formation, human health", "kg_NMVOC-eq.",         1.30,      1.40,      "CAT I"),
    ("Particulate matter formation",    "disease_incidence",    764627,    1937047,   "CAT I"),
    ("Acidification",                   "mol_H+-eq.",           2.04,      2.01,      "CAT II"),
    ("Freshwater eutrophication",       "kg_P-eq.",             3.74,      5.53,      "CAT II"),
    ("Marine eutrophication",           "kg_N-eq.",             14.25,     14.25,     "CAT II"),
    ("Terrestrial eutrophication",      "mol_N-eq.",            0.331,     0.344,     "CAT II"),
]


# ---------------------------------------------------------------------------
# Builder functions
# ---------------------------------------------------------------------------

def _build_air_pollutants_rows() -> list[dict]:
    rows = []
    for pid, name, lower, central, upper, notes in _AIR_DATA:
        rows.append({
            "source_table": "Table 3",
            "chapter": "2.3.1",
            "pollutant_id": pid,
            "pollutant_name": name,
            "lower": lower,
            "central": central,
            "upper": upper,
            "unit": "EUR_2021/kg",
            "notes": notes,
        })
    return rows


def _build_water_pollutants_rows() -> list[dict]:
    rows = []
    for (name, fw_lo, fw_ce, fw_up, sw_lo, sw_ce, sw_up) in _WATER_DATA:
        for medium, lo, ce, up in [
            ("freshwater", fw_lo, fw_ce, fw_up),
            ("saltwater",  sw_lo, sw_ce, sw_up),
        ]:
            rows.append({
                "source_table": "Table 4",
                "chapter": "2.3.2",
                "pollutant_name": name,
                "receiving_water": medium,
                "lower": lo,
                "central": ce,
                "upper": up,
                "unit": "EUR_2021/kg",
            })
    return rows


def _build_soil_pollutants_rows() -> list[dict]:
    rows = []
    for name, lower, central, upper in _SOIL_DATA:
        rows.append({
            "source_table": "Table 5",
            "chapter": "2.3.3",
            "pollutant_name": name,
            "lower": lower,
            "central": central,
            "upper": upper,
            "unit": "EUR_2021/kg",
        })
    return rows


def _build_land_use_rows() -> list[dict]:
    rows = []
    for category, lower, central, upper in _LAND_DATA:
        rows.append({
            "source_table": "Table 6",
            "chapter": "2.3.4",
            "category": category,
            "lower": lower,
            "central": central,
            "upper": upper,
            "unit": "EUR_2021/m2/year",
        })
    return rows


def _build_midpoints_recipe_rows() -> list[dict]:
    rows = []
    for category, unit, lower, central, upper, cat in _RECIPE_DATA:
        rows.append({
            "source_table": "Table 7",
            "chapter": "2.4.1",
            "impact_category": category,
            "unit": unit,
            "lower": lower,
            "central": central,
            "upper": upper,
            "reliability_category": cat,
            "category_description": {
                "A": "High certainty — recommended for all LCA applications",
                "B": "Higher uncertainty — use with caution",
                "C": "Outside ReCiPe; important for damage-cost completeness",
            }[cat],
        })
    return rows


def _build_midpoints_pef_rows() -> list[dict]:
    rows = []
    for category, unit, eu27, nl, pef_cat in _PEF_DATA:
        rows.append({
            "source_table": "Table 8",
            "chapter": "2.4.2",
            "impact_category": category,
            "pef_unit": unit,
            "eu27_central": eu27,
            "nl_central": nl,
            "unit_label": "EUR_2021/characterisation_unit",
            "pef_category": pef_cat,
        })
    return rows


# ---------------------------------------------------------------------------
# Dispatch table: key → (builder, fieldnames)
# ---------------------------------------------------------------------------
_BUILDERS = {
    "air_pollutants": (
        _build_air_pollutants_rows,
        ["source_table", "chapter", "pollutant_id", "pollutant_name",
         "lower", "central", "upper", "unit", "notes"],
    ),
    "water_pollutants": (
        _build_water_pollutants_rows,
        ["source_table", "chapter", "pollutant_name", "receiving_water",
         "lower", "central", "upper", "unit"],
    ),
    "soil_pollutants": (
        _build_soil_pollutants_rows,
        ["source_table", "chapter", "pollutant_name",
         "lower", "central", "upper", "unit"],
    ),
    "land_use": (
        _build_land_use_rows,
        ["source_table", "chapter", "category",
         "lower", "central", "upper", "unit"],
    ),
    "midpoints_recipe": (
        _build_midpoints_recipe_rows,
        ["source_table", "chapter", "impact_category", "unit",
         "lower", "central", "upper", "reliability_category", "category_description"],
    ),
    "midpoints_pef": (
        _build_midpoints_pef_rows,
        ["source_table", "chapter", "impact_category", "pef_unit",
         "eu27_central", "nl_central", "unit_label", "pef_category"],
    ),
}


# ---------------------------------------------------------------------------
# Excel writer
# ---------------------------------------------------------------------------
_HEADER_FILL = PatternFill(fill_type="solid", fgColor="1F4E79")
_HEADER_FONT = Font(bold=True, color="FFFFFF")
_HEADER_ALIGN = Alignment(horizontal="center", vertical="center", wrap_text=True)


def _write_excel(key: str, rows: list[dict], fieldnames: list[str], out_path: Path) -> None:
    cfg = config.get_table_config(key)
    wb = openpyxl.Workbook()

    # --- Sheet 1: Value Factors ---
    ws = wb.active
    ws.title = "Value Factors"
    ws.append(fieldnames)
    for cell in ws[1]:
        cell.fill = _HEADER_FILL
        cell.font = _HEADER_FONT
        cell.alignment = _HEADER_ALIGN
    ws.row_dimensions[1].height = 30
    ws.freeze_panes = "A2"
    for row in rows:
        ws.append([row.get(f, "") for f in fieldnames])

    # Auto-width
    for col in ws.columns:
        max_len = max((len(str(cell.value or "")) for cell in col), default=8)
        ws.column_dimensions[col[0].column_letter].width = min(max_len + 2, 50)

    # --- Sheet 2: Metadata ---
    ms = wb.create_sheet("Metadata")
    meta_rows = [
        ("Field", "Value"),
        ("Handbook title", cfg["title"]),
        ("Subtitle", cfg["subtitle"]),
        ("Authors", cfg["authors"]),
        ("Publisher", cfg["publisher"]),
        ("Publication date", cfg["publication_date"]),
        ("Version", cfg["version"]),
        ("Reference number", cfg["reference_number"]),
        ("Price level", cfg["price_level"]),
        ("Geographic scope", cfg["geographic_scope"]),
        ("Methodology", cfg["methodology"]),
        ("", ""),
        ("Table group", cfg["title"]),
        ("Source table", cfg["source_table"]),
        ("Chapter", cfg["chapter"]),
        ("Unit", cfg["unit"]),
        ("Description", cfg["description"]),
        ("Notes", cfg["notes"]),
    ]
    for r in meta_rows:
        ms.append(r)
    for cell in ms[1]:
        cell.fill = _HEADER_FILL
        cell.font = _HEADER_FONT
    ms.column_dimensions["A"].width = 22
    ms.column_dimensions["B"].width = 80

    wb.save(out_path)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def run_table(key: str) -> Path:
    """Extract one table group to CSV + Excel. Returns CSV path."""
    if key not in _BUILDERS:
        raise KeyError(f"Unknown table group '{key}'. Available: {list(_BUILDERS)}")

    builder, fieldnames = _BUILDERS[key]
    rows = builder()

    csv_path = config.get_output_path(key)
    excel_path = config.get_excel_path(key)

    # Write CSV
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # Write Excel
    _write_excel(key, rows, fieldnames, excel_path)

    return csv_path


def run_all() -> dict[str, Path]:
    """Run all table groups. Returns dict of key → CSV path."""
    results = {}
    for key in _BUILDERS:
        results[key] = run_table(key)
    return results
