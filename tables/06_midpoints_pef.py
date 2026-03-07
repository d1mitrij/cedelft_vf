"""Table 8 — Midpoint prices for PEF impact categories CAT I and II (EUR 2021/unit)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pipeline

if __name__ == "__main__":
    csv_path = pipeline.run_table("midpoints_pef")
    print(f"Done: {csv_path}")
