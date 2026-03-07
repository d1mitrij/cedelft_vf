"""Table 6 — Environmental prices for land use occupation (EUR 2021/m2/year)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pipeline

if __name__ == "__main__":
    csv_path = pipeline.run_table("land_use")
    print(f"Done: {csv_path}")
