"""Table 7 — Environmental prices for LCA: ReCiPe 2016 midpoints (EUR 2021/unit)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pipeline

if __name__ == "__main__":
    csv_path = pipeline.run_table("midpoints_recipe")
    print(f"Done: {csv_path}")
