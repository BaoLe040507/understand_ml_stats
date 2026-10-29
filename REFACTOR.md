# One-time refactor: switch the repo to project mode

**For the VS Code Claude session.** This is a one-time task list. `CLAUDE.md`
has already been updated to describe the end state, so read it in full first.
Then do the steps below in order, verify each one, and delete this file in
the final commit.

Ground rules:
- Work on a branch: `git checkout -b refactor/project-mode`. Commit after each
  numbered step. Don't push; the user will review and merge.
- **Never change the user's work.** Notebooks 04–10 contain the user's
  answers, and **notebook 10 is in progress** (section 1 done, sections 2–4
  and the exam blank). Apart from the single data-loading line in step 5,
  don't touch their cells, outputs, or metadata. Don't re-execute them.
- Use `git mv` for every move so history follows the files.
- The `.venv` is at the repo root (Windows: `.venv\Scripts\python.exe`).
- Step 6 builds a new notebook, so the **advisor process** in CLAUDE.md
  applies to it.

---

## 1. Move existing files into the new layout

```
Textbooks/practical_stats_for_ds/data/ames_housing.csv
  -> Textbooks/practical_stats_for_ds/data/ames/ames_housing.csv

notebooks/04_binomial-and-reference-distributions.ipynb       -> notebooks/ch02_sampling/
notebooks/05_ab-testing-and-t-tests.ipynb                     -> notebooks/ch03_significance/
notebooks/06_multiple-testing-dof-and-anova.ipynb             -> notebooks/ch03_significance/
notebooks/07_chi-square-bandits-and-power.ipynb               -> notebooks/ch03_significance/
notebooks/08_simple-and-multiple-regression.ipynb             -> notebooks/ch04_regression/
notebooks/09_factor-variables-in-regression.ipynb             -> notebooks/ch04_regression/
notebooks/10_interpreting-the-regression-equation.ipynb       -> notebooks/ch04_regression/
notebooks/11_regression-diagnostics.ipynb                     -> notebooks/ch04_regression/
notebooks/12_polynomial-spline-and-gam.ipynb                  -> notebooks/ch04_regression/
```

Create empty folders (with a `.gitkeep`): `notebooks/ch01_eda/` (Ch1–2
notebooks 01–03 are "pending import" per the syllabus; they'll go here),
`notebooks/ch05_classification/`, `notebooks/ch06_statistical_ml/`,
`notebooks/ch07_unsupervised/`, `reviews/`, `data/markets/`, `data/churn/`
(all under `Textbooks/practical_stats_for_ds/`).

## 2. Package, dependencies, .gitignore

- `pyproject.toml` at the repo root: setuptools, src layout, package
  `mlstats`, `requires-python = ">=3.12"`, dependencies: pandas, numpy,
  scipy, statsmodels, matplotlib, scikit-learn, ipykernel, yfinance,
  requests. Don't pin tightly; use the versions already installed as lower
  bounds.
- `src/mlstats/__init__.py`, `paths.py`, `data.py`, `plots.py`.
- Install: `.venv\Scripts\python -m pip install -e .` (this also pulls in
  yfinance and requests).
- Root `.gitignore`: `.venv/`, `__pycache__/`, `.ipynb_checkpoints/`,
  `*.egg-info/`, `Textbooks/practical_stats_for_ds/data/markets/*` and
  `.../data/churn/*` **except** each folder's `MANIFEST.md` and `.gitkeep`.
  Ames stays committed.

## 3. Loaders (`src/mlstats/paths.py`, `data.py`)

- `paths.py`: `REPO_ROOT` from `Path(__file__).resolve()` (src/mlstats →
  up two levels), `BOOK_DIR`, `DATA_DIR = BOOK_DIR / "data"`.
- `load_ames()`: reads `data/ames/ames_housing.csv`, returns it unchanged
  (the existing notebooks depend on the raw columns).
- `load_universe()`, `load_prices()`, `load_returns()`, `load_factors()`:
  read the market CSVs with a `DatetimeIndex`. `load_returns(tickers=None,
  excess=False)`: when `excess=True`, subtract `RF` after an inner date join
  with the factors.
- `load_churn()`: full frame with `churned` (0/1) added and `TotalCharges` as
  float (11 blanks → 0.0, all have `tenure == 0`; assert that).
  `load_churn_split(test_size=0.3, seed=42)`: stratified on `churned`,
  returns `(train, test)` DataFrames without `customerID`. This exact split
  is reused by every Ch5–6 notebook, so the seed is fixed and must never
  change.
- If a data file is missing, raise a clear error naming the fetch script to
  run.
- `plots.py`: start empty apart from a docstring explaining the "plumbing or
  graduated helpers only" rule from CLAUDE.md.

## 4. Fetch scripts + manifests

**`scripts/fetch_markets.py`**
- Frozen window: `START = "2016-01-01"`, `END = "2026-01-01"` (yfinance's
  `end` is exclusive, so this ends 2025-12-31).
- Frozen universe (6 per GICS sector, current classifications) plus `SPY`
  as a benchmark (sector `"Benchmark"`):

  | Sector | Tickers |
  |---|---|
  | Information Technology | AAPL MSFT NVDA ORCL CSCO ADBE |
  | Communication Services | GOOGL META NFLX DIS VZ T |
  | Consumer Discretionary | AMZN HD MCD NKE SBUX LOW |
  | Consumer Staples | PG KO PEP WMT COST CL |
  | Health Care | JNJ UNH PFE MRK ABT AMGN |
  | Financials | JPM BAC WFC GS MS AXP |
  | Industrials | CAT HON UNP DE MMM LMT |
  | Energy | XOM CVX COP SLB EOG OXY |
  | Utilities | NEE DUK SO D AEP SRE |
  | Real Estate | PLD AMT SPG O EQIX PSA |
  | Materials | SHW APD NEM FCX ECL NUE |

  If any ticker lacks full-window history from yfinance, report it to the
  user and swap in another large cap from the same sector. Don't drop
  dates to make it fit.
- One batched `yf.download(..., auto_adjust=True, progress=False)` call. The
  result has MultiIndex columns; take `"Close"` (which is adjusted when
  `auto_adjust=True`). Save `prices.csv` (date x ticker) and `returns.csv`
  (`pct_change()`, first row dropped). Fill no gaps silently: after the
  first row, assert there are no NaNs.
- Fama-French 3 factors, daily: download
  `https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip`
  with `requests`, read the single CSV inside with `zipfile`, skip the text
  header lines until the row starting with `,Mkt-RF`, stop at the first
  non-date row (copyright footer), parse dates `%Y%m%d`, rename to
  `Mkt_RF, SMB, HML, RF`, **divide by 100** (the source is in percent), clip
  to the window. Save `ff_factors_daily.csv`. Don't use `pandas-datareader`;
  it's broken on Python 3.12.
- `universe.csv`: `ticker, name, sector` (names from yfinance `.info` are
  fine, or hard-code them).
- Sanity checks (print them and write them to `data/markets/MANIFEST.md`
  along with source URLs, window, run date, and shapes): rows ≈ 2,500
  trading days; SPY total return over the window; mean `RF`; correlation of
  SPY excess return with `Mkt_RF` (should be > 0.98); the 5 largest
  absolute daily SPY moves with dates (should include March 2020).

**`scripts/fetch_churn.py`**
- Source: `https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv`.
  If that URL fails, try `sklearn.datasets.fetch_openml` by searching
  OpenML for the Telco Customer Churn dataset, and tell the user which
  source was used.
- Save the raw file unchanged as `data/churn/telco_churn.csv`.
- Assert: 7,043 rows x 21 columns; `Churn == "Yes"` count 1,869; exactly 11
  blank `TotalCharges`, all with `tenure == 0`. Write these, the source, and
  the run date to `data/churn/MANIFEST.md`.

Run both scripts and confirm every assertion passes.

## 5. Repoint existing notebooks at the loader

In notebooks 04–12, replace the line `ames = pd.read_csv('../data/ames_housing.csv')`
(check for variants and different variable names first by grepping
`read_csv`) with:

```python
from mlstats.data import load_ames
ames = load_ames()
```

Edit only that line, in the source of that one cell, and leave outputs and
execution counts alone. Do it with a small Python script using `nbformat`
(load → edit the one cell's source → `nbformat.validate` → write UTF-8), not
by hand-editing JSON. Then confirm the loader works by running
`python -c "from mlstats.data import load_ames; print(load_ames().shape)"`
→ `(2930, 81)`. Don't execute the notebooks.

## 6. Rebuild notebook 11 on market data

`notebooks/ch04_regression/11_regression-diagnostics.ipynb` is currently an
unstarted Ames notebook (only the imports cell is filled). Replace it with
the markets version described in CLAUDE.md → *Chapter projects* (the old
version stays in git history). Follow every CLAUDE.md convention: advisor
review of the plan first and again before finishing, time budget, Predict
first / Prediction / reflection cells, Tools lists checked against the
installed statsmodels, stub cells, pre-filled setup and plotting cells,
nbformat validation.

- The intro states the Ch4 thread continuing ("can I trust this
  coefficient?") and gives a ~100-word brief of the market dataset. The
  project question is: **how much should I trust a stock's beta?**
- Suggested sections (refine with the advisor):
  1. **Outliers and influential values.** One stock's daily excess return on
     `Mkt_RF`; studentized residuals, leverage, Cook's distance; which dates
     dominate (earnings days, March 2020); beta with vs. without them.
  2. **Heteroskedasticity.** Residuals over time (volatility clustering);
     Breusch-Pagan; classical vs. HC3 standard errors (what changes and what
     doesn't).
  3. **Correlated errors.** Daily residuals look nearly uncorrelated but
     their squares aren't (uncorrelated ≠ independent); then overlapping
     20-day returns → strong autocorrelation → Durbin-Watson and Newey-West
     HAC standard errors.
  4. **Partial residual plot and nonlinearity.** Three-factor model; partial
     residual plot for `Mkt_RF`; does the slope bend in down markets? (This
     sets up notebook 12.)
- Pick concrete tickers by checking the data. Choose ones where each effect
  is clearly visible, and say why in the build notes to the user, not in
  the notebook.
- **Exam:** write its 5 questions (computed from real data, using different
  tickers or specs from the exercises) into a new
  `reviews/R01_regression-diagnostics.ipynb`, under `## From notebook 11 —
  Regression diagnostics`, using the exact question / Your answer / Review
  cell format from CLAUDE.md. The review notebook gets a short intro (how
  the weekly review works, ~60 words). Don't put an exam section in
  notebook 11.

## 7. Update syllabus.md and add a README

**`syllabus.md`**
- Add a **Status** block at the top:
  - Current: notebook 10, section 1 done (reflection bullets still blank);
    sections 2–4 next.
  - Then: 11 (markets, rebuilt), 12 (Ames), then Ch5 on churn.
  - Open review notebook: `reviews/R01_regression-diagnostics.ipynb` (11's
    exam). Exams for 10 and 12 remain inside those notebooks.
  - Log: `2026-10-29: repo refactored to project mode (see CLAUDE.md)`.
- Update every notebook path to the new `chNN_*/` folders, and add the
  dataset to each checked line (e.g. `— notebooks/ch04_regression/11_... ·
  markets`).
- Change the 11 entries' notes to reflect the markets rebuild.
- Add the planned notebook number next to each unchecked Ch5–7 section,
  following the split in CLAUDE.md.
- Update the "How this gets used" section to mention the Status block.

**`README.md`** (the repo is public): 10–15 lines covering what this repo
is, the folder layout, setup (`python -m venv .venv`, `pip install -e .`,
run both fetch scripts), and a note that market and churn data are fetched,
not committed. No personal details beyond what's already in CLAUDE.md.

## 8. Final verification, then hand back

- `nbformat.validate` passes on every `.ipynb` under `Textbooks/`.
- All loaders run and return the expected shapes.
- `git status` shows no data files under `markets/` or `churn/` other than
  the manifests.
- Grep for any remaining `../data/` or `read_csv(` paths in notebooks.
- Delete this `REFACTOR.md` in the final commit.
- Report back to the user in under 10 bullets: what moved, any ticker swaps
  or source fallbacks, the tickers chosen for notebook 11 and why, anything
  that needs their decision. Then tell them they can pick up notebook 10,
  section 1's reflection bullets.
