"""
Template for a single table group entry-point script.
Copy this file, rename it, and replace KEY with the table group name.

Usage:
    python tables/NN_KEY.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import pipeline

if __name__ == "__main__":
    csv_path = pipeline.run_table("KEY")
    print(f"Done: {csv_path}")
