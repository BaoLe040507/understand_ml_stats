"""Filesystem locations, resolved from this file so notebooks run from any folder."""
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]  # src/mlstats/paths.py -> repo root
BOOK_DIR = REPO_ROOT / "Textbooks" / "practical_stats_for_ds"
DATA_DIR = BOOK_DIR / "data"
