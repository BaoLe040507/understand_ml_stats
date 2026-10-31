# understand_ml_stats

Notebooks for building intuition for the ML/stats fundamentals in *Practical Statistics for Data Scientists* (Bruce, Bruce & Gedeck) by applying each concept to real data. Each chapter is a small project with one guiding question and one dataset (Ames housing, daily stock returns, telecom churn). `CLAUDE.md` describes the working method; `Textbooks/practical_stats_for_ds/syllabus.md` tracks progress.

## Layout

- `src/mlstats/`: installable package with data loaders (`data.py`), paths, and plot helpers.
- `scripts/`: `fetch_markets.py` and `fetch_churn.py` download the datasets.
- `Textbooks/practical_stats_for_ds/notebooks/chNN_<topic>/`: exercise notebooks, numbered across the book.
- `Textbooks/practical_stats_for_ds/reviews/`: weekly review (exam) notebooks.
- `Textbooks/practical_stats_for_ds/data/`: Ames is committed; market and churn data are fetched.

## Setup

```
python -m venv .venv
.venv\Scripts\activate          # macOS/Linux: source .venv/bin/activate
pip install -e .
python scripts/fetch_markets.py
python scripts/fetch_churn.py
```

Market data (Yahoo Finance, Ken French Data Library) and churn data are downloaded by the scripts above and are not committed to the repo; each `data/<dataset>/MANIFEST.md` records the source, window, and sanity checks. Notebooks run in VS Code's Jupyter integration with the `.venv` kernel.
