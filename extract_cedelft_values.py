"""
Orchestrator for CE Delft Environmental Prices Handbook 2024 value factor extraction.

Extracts all 6 table groups to CSV and Excel files in the output/ directory.

Usage:
    python extract_cedelft_values.py                         # all table groups
    python extract_cedelft_values.py --only air water soil   # selective
    python extract_cedelft_values.py --list                  # list available groups
"""

import argparse
import sys
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import pipeline
import config


def _list_groups():
    print("Available table groups:")
    for key, cfg in config.TABLE_GROUPS.items():
        print(f"  {cfg['id']}  {key:<22}  {cfg['source_table']}  —  {cfg['title']}")


def main():
    parser = argparse.ArgumentParser(
        description="Extract CE Delft Environmental Prices Handbook 2024 value factors"
    )
    parser.add_argument(
        "--only", nargs="+", metavar="KEY",
        help="Extract only the specified table group(s)",
    )
    parser.add_argument(
        "--list", action="store_true",
        help="List available table groups and exit",
    )
    args = parser.parse_args()

    if args.list:
        _list_groups()
        return

    keys = args.only if args.only else list(config.TABLE_GROUPS)

    # Validate keys
    unknown = [k for k in keys if k not in config.TABLE_GROUPS]
    if unknown:
        print(f"Error: unknown table group(s): {unknown}")
        _list_groups()
        sys.exit(1)

    log_path = Path(__file__).parent / f"execution_log_{datetime.now():%Y%m%d_%H%M%S}.txt"
    log_lines = [
        f"CE Delft Environmental Prices Handbook 2024 — extraction run",
        f"Started: {datetime.now():%Y-%m-%d %H:%M:%S}",
        f"Groups requested: {keys}",
        "",
    ]

    print(f"Extracting {len(keys)} table group(s)...\n")
    total_rows = 0
    success = 0
    failed = 0

    for key in keys:
        cfg = config.TABLE_GROUPS[key]
        t0 = time.time()
        try:
            csv_path = pipeline.run_table(key)
            elapsed = time.time() - t0

            # Count rows
            with open(csv_path, encoding="utf-8") as f:
                rows = sum(1 for _ in f) - 1  # exclude header

            total_rows += rows
            success += 1
            msg = f"  [OK]  {cfg['id']}_{key:<22}  {rows:>4} rows  {elapsed:.2f}s  -> {csv_path.name}"
            print(msg)
            log_lines.append(msg)
        except Exception as e:
            elapsed = time.time() - t0
            failed += 1
            msg = f"  [FAIL] {cfg['id']}_{key:<22}  {elapsed:.2f}s  ERROR: {e}"
            print(msg)
            log_lines.append(msg)

    summary = (
        f"\nDone. {success}/{len(keys)} groups extracted, "
        f"{total_rows} total rows, {failed} failed."
    )
    print(summary)
    log_lines += ["", summary, f"Finished: {datetime.now():%Y-%m-%d %H:%M:%S}"]

    log_path.write_text("\n".join(log_lines), encoding="utf-8")
    print(f"Log written to: {log_path.name}")


if __name__ == "__main__":
    main()
