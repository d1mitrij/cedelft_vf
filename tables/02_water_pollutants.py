"""Table 4 — Environmental prices for emissions to water (EUR 2021/kg)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import pipeline

if __name__ == "__main__":
    csv_path = pipeline.run_table("water_pollutants")
    print(f"Done: {csv_path}")
