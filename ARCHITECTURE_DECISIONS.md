# Architecture Decisions — vf_cedelft

**Pipeline:** CE Delft Environmental Prices Handbook 2024 — Value Factor Extraction
**Author:** Dimitrij Euler (Greenings), with the support of Claude Code (Anthropic)
**Data source:** CE Delft (Joukje de Vries et al., April 2025)

---

## ADR-001 — Hard-code all data in pipeline.py

**Decision:** Transcribe all handbook values directly into Python data structures in
`pipeline.py`. No PDF parsing or Excel parsing at runtime.

**Rationale:**
- PDF-extracted text (pypdf) has formatting issues; runtime parsing would be fragile
- Hard-coding ensures exact, verifiable values with full audit trail
- Consistent pattern (config + pipeline + tables/) for structural clarity
- All values verified against two independent locations in the handbook (summary
  tables in Chapter 1 and detailed tables in Chapter 2)

**Trade-off:** Manual update required when a new handbook version is published.

---

## ADR-002 — Flat tidy CSV as primary output format

**Decision:** Produce long/tidy CSV files (one row per unique combination of dimensions)
rather than wide pivot tables or HDF5 matrices.

**Rationale:**
- CE Delft data is not a country × sector matrix (unlike EPS/eQALY) — it is a flat
  list of substance prices, making HDF5 unnecessary overhead
- Tidy format is directly importable into pandas, R, Excel, and database systems
- Appropriate for non-country-differentiated flat substance price data
- Human-readable without tooling

---

## ADR-003 — Separate freshwater and saltwater as rows (not columns)

**Decision:** In Table 4 (water pollutants), represent freshwater and saltwater values
as separate rows with a `receiving_water` column, rather than as separate column pairs.

**Rationale:**
- Maintains tidy format — one measurement per row
- Allows easy filtering by receiving water body
- Avoids column explosion (6 value columns instead of 3)
- Enables easy filtering by receiving water body

---

## ADR-004 — Reliability category retained for ReCiPe midpoints

**Decision:** Include the `reliability_category` field (A/B/C) and a human-readable
`category_description` in the midpoints_recipe output.

**Rationale:**
- Category A/B/C classification is a core methodological distinction in the handbook
  that affects how values should be used
- Without this flag, downstream users cannot determine which midpoints are suitable
  for standard LCA vs. which require caution
- Category C (NO₂ mortality) is outside ReCiPe characterisation and must be flagged

---

## ADR-005 — PEF output includes both EU27 and NL columns

**Decision:** Table 8 (PEF midpoints) retains separate `eu27_central` and `nl_central`
columns rather than stacking them as two rows per category.

**Rationale:**
- Only central values exist for PEF (no lower/upper); the two geographies are the
  primary differentiating dimension
- Keeping both in a single row enables direct EU27 vs. NL comparison
- Pivoting to rows would require adding a `geography` column with only two values,
  which adds complexity without benefit given the small table size (9 rows)

---

## ADR-006 — Excel output with Metadata sheet and formatted header

**Decision:** Produce formatted Excel files with a dark-blue header row, frozen pane,
and a separate "Metadata" sheet containing full handbook attribution.

**Rationale:**
- Excel is the primary delivery format for non-technical stakeholders
- CE Delft handbook attribution must be prominently visible in every output file
- Formatted headers improve readability for direct use in SCBA/LCA spreadsheets
- CE Delft attribution is prominently visible in every output file

---

## ADR-007 — Single orchestrator with --only and --list flags

**Decision:** Implement `extract_cedelft_values.py` as a unified CLI orchestrator
supporting selective extraction (`--only`) and group listing (`--list`).

**Rationale:**
- Consistent CLI interface for selective extraction and listing
- `--only` enables fast partial updates when a single table needs refreshing
- Timestamped execution log provides audit trail of extraction runs
- Individual table scripts (`tables/NN_*.py`) allow independent testing

---

## ADR-008 — Sequential processing (no parallelism)

**Decision:** Run all 6 table groups sequentially rather than using ThreadPoolExecutor.

**Rationale:**
- Total extraction time is under 0.5 seconds — parallelism provides no benefit
- Sequential execution simplifies debugging and log output
- All 6 table groups complete in under 0.5 s — parallelism provides no benefit

---

## ADR-009 — Units encoded as explicit strings (not a separate lookup table)

**Decision:** Include the `unit` field directly in every CSV row as a plain string
(e.g. `EUR_2021/kg`, `EUR_2021/m2/year`, `EUR_2021/kg_CO2-eq.`).

**Rationale:**
- Prevents unit confusion when files are opened independently
- No need to join a separate units table for interpretation
- Units vary meaningfully across table groups and within midpoints_recipe
- Self-documenting format reduces integration errors

---

## ADR-010 — No value transfer or country differentiation

**Decision:** Publish EU27 average values only, without applying income-based
value transfer to other countries.

**Rationale:**
- CE Delft explicitly states these values are EU27 averages and are unsuitable
  for application to other countries without dedicated value transfer analysis
- Adding speculative country-differentiated values would misrepresent the source
- Country differentiation is the responsibility of downstream applications
  (e.g. the eQALY framework already uses CE Delft as one of several inputs)
- If value transfer is needed, VALUE_TRANSFER.md (future document) should guide it

---

## ADR-011 — Markdown source document retained as reference

**Decision:** Keep `Environmental_Prices_Handbook_2024_EU27_version.md` (the
pypdf-converted handbook) in the repository as a human-readable reference and
QA source, even though it is not parsed at runtime.

**Rationale:**
- Provides a searchable reference for verifying pipeline values without opening PDF
- Used during initial transcription QA to confirm table data
- pypdf conversion captures all numerical values correctly even if formatting is imperfect
- Retained in .gitignore scope for large file management if repository is published

---

## ADR-012 — Attribution in every output file, not just README

**Decision:** Every Excel output file contains a Metadata sheet with the full CE Delft
handbook citation and the Greenings/Euler/Claude pipeline authorship.

**Rationale:**
- Output files are often shared independently of the repository
- CE Delft's intellectual property must be attributed at the point of use
- Users encountering a standalone `.xlsx` file must be able to trace the source
- Standalone files remain fully traceable to their source
