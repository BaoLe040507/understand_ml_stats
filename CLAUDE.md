# understand_ml_stats

Purpose: build intuition for the ML/stats fundamentals covered in *Practical
Statistics for Data Scientists* (Bruce, Bruce & Gedeck, O'Reilly) by applying
each concept to real data instead of just reading. The user is a working data
scientist who already knows the syntax. The goal is conceptual intuition, not
a tutorial.

**Project mode (from notebook 11 onward):** each chapter is a small project
with one guiding question and one dataset. Notebooks are still ~1-hour
section-sized units, but they build on each other inside the chapter, and
Claude writes the plumbing so the user's hour goes into the concepts. See
*Chapter projects* below.

## Learner profile and goal

The user is currently an **associate (entry-level) data scientist**. The
point of this repo is to build the depth of intuition expected of a **senior
data scientist, a decision-science / causal-inference role, or a machine-
learning role**. They are not committed to one track, and anything learned
here should transfer across all three. So:

- Favor "why does this happen / what breaks / what would you do about it"
  over "how do I call this function."
- Whenever a concept has a common interview angle (assumptions and what each
  one protects, bias vs. variance, leakage, confounding vs. mediators,
  extrapolation, interpretation of coefficients, metric choice, etc.), build
  that angle into the exercises and the exam, even if the book doesn't stress
  it. Content beyond the book is fine when flagged as **supplementary**.
- Tag content that leans toward one role (DS / Causal / ML) where it helps,
  but don't treat the tags as exclusive.

## Process: Opus advisor reviews the plan first

Before implementing any new notebook (or batch of notebooks) and its exam,
Claude drafts a short plan (notebook split, exercise list, exam question
topics/roles) and has the **Opus advisor** (the `advisor` tool) review it
**before writing files**. Fold the advisor's corrections into the build. Call
the advisor again before declaring the work done. Skipping this step is not
allowed even when the request looks routine.

## Role: Claude builds the plumbing, the user writes the concept

Claude scaffolds exercises and writes everything that is *not* the concept
being taught. Claude does not solve the concept parts.

- **The user writes:** any code that *is* the statistical idea of the
  section, such as fitting and specifying the model, computing VIF / Cook's
  distance / a bootstrap / a permutation test the first time, choosing a
  threshold, and all interpretation (prediction and reflection cells).
- **Claude pre-fills:** the setup cell (imports, data loading via
  `mlstats`, any filtering, merging, or feature prep that isn't the concept),
  and plotting or printing cells that *consume* the user's result.
- **Stub cells:** a user code cell may contain a one-line stub naming the
  variable that later pre-filled cells expect (e.g. `model = ...  # fit
  excess return on the market factor`). It must not contain any part of the
  answer beyond the variable name and a one-line comment.
- **Graduated helpers:** once the user has implemented a concept by hand in
  a notebook, Claude may add a library version of it to `src/mlstats/`
  (e.g. `walk_forward_splits`, `bootstrap_stat`) and later notebooks can call
  it in setup cells. Never put an ungraduated concept in `src/`.
- **Reading:** the user reads the relevant book sections before a notebook.
  Separate notes are optional, since the prediction and reflection cells act
  as the notes. The user doesn't have to bring a summary first; "start
  notebook NN" is enough. Each section's text opens with which book section
  it covers.
- If a textbook example is written around the book's own datasets (King
  County housing, `lc_loans`, `state.csv`, `sp500_data`, etc.), translate it
  onto **that chapter's project dataset** (see *Chapter projects*), not the
  book's dataset.

## Explanation style

Default to concrete, worked-numeric-example explanations over abstract/
formal ones when introducing a new concept: walk through actual numbers
(e.g. "draw these 3 values, square them, add them up") before reaching for
formal terminology like "degrees of freedom." If a term is unavoidable,
define it in plain language grounded in the example, not as a standalone
definition up front. This applies to scaffolding text written into
notebooks, not just chat replies.

## When the user is stuck

If the user says they're stuck, asks for help mid-question, or their
attempt is heading somewhere wrong, don't hand over the answer immediately.

- For the first 2-3 exchanges on a given question, respond with a hint: name
  the relevant concept, ask a guiding question, or point at the right
  function/approach, without writing the solution code or stating the final
  numeric/interpretive answer.
- Only after that (roughly 3 hints without it clicking) give the fuller
  walkthrough or solution.
- This resets per question. A fresh question always starts back at hints,
  even if the previous one needed a full walkthrough.
- If the user is stuck on *plumbing* (pandas errors, import paths, data
  shape), not the concept, just fix it. The hint ladder is for concepts only.
- This is separate from the post-hoc review protocol below: hints are
  real-time scaffolding while the user is actively working a question;
  review happens after they've committed to an answer.

## Repo layout

```
understand_ml_stats/
├── CLAUDE.md
├── README.md
├── pyproject.toml                 # src/ installed editable: pip install -e .
├── src/mlstats/
│   ├── paths.py                   # DATA_DIR etc., resolved from the package location
│   ├── data.py                    # load_ames, load_returns, load_factors, load_universe,
│   │                              # load_churn, load_churn_split
│   └── plots.py                   # plumbing-only plot helpers + graduated helpers
├── scripts/
│   ├── fetch_markets.py           # yfinance + Ken French download -> data/markets/
│   └── fetch_churn.py             # IBM Telco churn download -> data/churn/
└── Textbooks/practical_stats_for_ds/
    ├── syllabus.md                # tracker: Status block + checklist + dataset per section
    ├── data/
    │   ├── ames/ames_housing.csv  # committed
    │   ├── markets/               # gitignored; rebuilt by scripts/fetch_markets.py
    │   └── churn/                 # gitignored; rebuilt by scripts/fetch_churn.py
    ├── notebooks/
    │   ├── ch01_eda/              # 01–03 when imported
    │   ├── ch02_sampling/         # 04
    │   ├── ch03_significance/     # 05–07
    │   ├── ch04_regression/       # 08–12
    │   ├── ch05_classification/   # 13–15
    │   ├── ch06_statistical_ml/   # 16–19
    │   └── ch07_unsupervised/     # 20–22
    └── reviews/                   # R01_..., R02_... weekly exam notebooks
```

New datasets are gitignored because the repo is public: Yahoo data shouldn't
be redistributed. The fetch scripts are the source of truth. They use frozen
date windows and ticker lists, so a fresh clone reproduces the same data.
Each `data/<dataset>/MANIFEST.md` records source, window, shape, and sanity
numbers.

## Notebook conventions

- Location: `Textbooks/practical_stats_for_ds/notebooks/chNN_<slug>/`.
- Naming: `NN_topic-slug.ipynb`, where `NN` is a zero-padded running sequence
  number across the whole book (it does not restart per chapter). Extend an
  existing file rather than creating a duplicate if the topic already has a
  notebook.
- Data loading is always `from mlstats.data import load_<x>`, never a
  relative CSV path, so notebooks run from any folder.
- The first notebook of each chapter opens with the **project question** and
  a ~100-word brief of the dataset. Later notebooks in the chapter open with
  one line on what the previous notebook established.
- If a notebook needs a model or frame built in an earlier notebook, rebuild
  it in the pre-filled setup cell (via an `mlstats` helper if it's reused);
  never ask the user to retype earlier work.
- Each concept gets its own markdown question cell + code cell(s), so the
  notebook reads as a sequence of self-contained mini-exercises.
- Any exercise question that needs a library function the user may not have
  memorized ends with a short `*Tools for this question:*` bullet list: the
  call signature with its main parameters, what it returns, and any gotcha
  (e.g., "`cooks_distance` returns a tuple, take `[0]`"). The goal is that
  the user never has to leave the notebook to read documentation. Verify the
  signatures against the installed versions.
- Notebook JSON is nbformat 4.5: every cell needs a unique `id`; copy the
  kernelspec metadata from an existing notebook; write files as UTF-8; run
  `nbformat.validate` on anything generated.
- Never re-execute or rewrite cells the user has already filled in.

## Time budget

Each notebook should take the user **one hour at most** (exams are no longer
inside notebooks; see *Exams*). Don't spend the freed time on more content.

- At most **4 exercise sections**, each with at most **3 sub-parts** (about 10
  minutes per section). Drop a sub-part if an earlier one already settles its
  answer; move overflow topics into the exam instead of adding sections.
- At most **one heavy pipeline sub-part per notebook** (a CV loop, a bootstrap,
  a train/test comparison of several models). When a later section needs the
  same machinery, reuse the user's earlier function or a graduated helper.
- "Compute it by hand" **once per concept**, then use the library.
- Each section has a checkable **Predict first** line (it asks for a sign,
  a direction, a rough size, or a choice between buckets, never just "predict
  what happens"), followed by a `_Prediction:_` markdown cell before the code
  cells and a `_What matched, what surprised you, and why (2-3 bullets):_`
  cell after them.
- Keep the intro to about 100 words and each section's text to about 150-250
  words. Trim prose and boilerplate, never the worked numeric picture.
- Put known plumbing gotchas (unseen category levels, predicting outside a
  spline's range, tuple returns) in the Tools list, so the user's time goes
  into the concept and not into debugging pandas.

## Exams: weekly review notebooks

Purpose: test intuition and interview readiness, not coding. Exams are still
**written at build time**, 5 questions per notebook, but from notebook 11
onward they go into the **current review notebook** in
`Textbooks/practical_stats_for_ds/reviews/` instead of the end of the
exercise notebook. The user works through the review notebook in one weekly
session (~30-45 min).

- Notebooks 08, 09, 10, and 12 keep their existing in-notebook exams. Don't
  move them. Notebooks 04-07 have no exams; don't retrofit.
- Review notebooks are named `RNN_<topics>.ipynb` (`R01_regression-
  diagnostics.ipynb`, ...). Append each new notebook's exam to the open
  review notebook under a `## From notebook NN — <title>` heading. Once the
  user has answered and Claude has reviewed it, the review is closed and the
  next notebook's exam starts `RNN+1`. A review notebook shouldn't exceed
  ~10 questions; start a new one if it would.
- Questions are mostly *no code*: the model outputs are printed into the
  question (as fenced ```text blocks, never as code cells, so they don't read
  as pre-filled analysis) and the user reads, predicts, or explains. Three
  question types, mixed: **read an output**, **predict what happens if X
  changes**, **interview-style** ("how would you explain / what could go
  wrong / what would you do").
- Each question has a title, a role-lean tag (DS / Causal / ML), the stem
  with real numbers, then two cells: **Your answer** (user fills in) and
  **Review** (placeholder `_pending_`; Claude fills in after the user
  answers).
- Exam output must come from model specs/subsets that differ from the
  notebook's exercises, so the exam is not an answer key for the exercises.
  Every number in a stem must be computed from the real data (a throwaway
  script that builds the notebook and prints the exam outputs is the
  reliable way); never invent output.
- No hidden answer key. Review cells stay empty until the user has answered.
- Reviewing exam answers follows the Review protocol below. If the user asks
  for help on an exam question, give a hint first, then fill in the review
  only after they have committed an answer.

## Chapter projects

| Ch | Project question | Dataset | Notebooks |
|---|---|---|---|
| 1–3 | (done in the old format) | Ames | 01–07 |
| 4 | What drives price / how far can I trust a coefficient? | Ames (10, 12), markets (11) | 08–12 |
| 5 | Who will churn, and who should a limited retention budget target? | churn | 13–15 |
| 6 | Can more flexible models honestly beat the Ch5 logistic baseline? | churn | 16–19 |
| 7 | What hidden structure is there in the market, and in customers? | markets (20–21), churn (22) | 20–22 |

Planned notebook split (adjust with the advisor when building; keep the
time budget):

- **10** Interpreting the regression equation: Ames, in progress, unchanged.
- **11** Regression diagnostics: **markets**. "How much should I trust a
  stock's beta?" Outliers/influence (earnings days, March 2020); heteroskedasticity
  (volatility clustering, robust HC standard errors); correlated errors
  (daily residuals look uncorrelated but squared residuals aren't;
  overlapping multi-day returns → autocorrelation → Newey-West HAC);
  partial residual plot of a stock on the Fama-French factors (does the
  market slope bend in down markets?).
- **12** Polynomial, spline, GAM: Ames, already built, unchanged.
- **13** Naive Bayes + discriminant analysis (churn baselines).
- **14** Logistic regression: logit, GLM, odds ratios, interpreting
  coefficients (the `No internet service` dummy-trap quirk), assessing the
  model.
- **15** Evaluating classifiers + imbalanced data: confusion matrix,
  precision/recall/specificity, ROC/AUC, lift; under/oversampling and
  weighting; cost-based threshold from a retention-offer cost vs. customer
  value. *Supplementary (Causal):* churn risk ≠ responsiveness to the offer
  (uplift). SMOTE is conceptual/exam-only unless `imbalanced-learn` gets
  installed.
- **16** KNN: standardization, KNN as a feature engine.
- **17** Trees: recursive partitioning, impurity, stopping/pruning.
- **18** Bagging and random forest: variable importance, hyperparameters.
- **19** Boosting: algorithm, XGBoost (install `xgboost` when building),
  regularization, hyperparameters with CV.
- **20** PCA on universe returns: is PC1 the market? Loadings by sector;
  scree. Correspondence analysis is exam-only (on churn categoricals).
- **21** K-means + hierarchical clustering of stocks: clusters vs. GICS
  sectors, choosing k, correlation-based dissimilarity, dendrogram.
  *Supplementary:* survivorship bias of a "today's large caps" universe.
- **22** Model-based clustering (`GaussianMixture`) + scaling and mixed
  data on churn customers: dominant variables, Gower's distance by hand
  once.

Ch5 and Ch6 all use **one fixed stratified train/test split** from
`load_churn_split()` and the same headline metric, so every model comparison
across notebooks 13-19 is honest.

## Datasets and quirks

Before writing question text, check actual column names/levels in the data.

### Ames — `data/ames/ames_housing.csv`, `load_ames()`
The full De Cock Ames Housing dataset (2,930 rows x 81 columns, zero missing
values), fetched from OpenML (`sklearn.datasets.fetch_openml(data_id=43926)`).
Target `Sale_Price`; includes `Latitude`/`Longitude`. Cleaned full version,
so distributions, outliers, and missing-data handling must be introduced
deliberately. Quirks: quality ratings are *words* (`Overall_Qual` is
`Very_Poor`...`Very_Excellent`, not 1-10); "none" is an explicit level
(`No_Garage`, `No_Basement`, `No_Fireplace`), not NaN; `Lot_Frontage` uses 0
where other versions have NA; rows are ordered roughly by neighborhood, not
by date; `Gr_Liv_Area == First_Flr_SF + Second_Flr_SF + Low_Qual_Fin_SF`
exactly; `Year_Remod_Add` is floored at 1950, so "was remodeled" flags need
`Year_Built >= 1950`.

### Markets — `data/markets/`, `load_returns()`, `load_factors()`, `load_universe()`
Daily data for a frozen universe of ~66 large-cap US stocks (6 per GICS
sector) plus SPY, **2016-01-01 to 2025-12-31**, from yfinance (adjusted
close), and Fama-French 3 factors (daily) from the Ken French Data Library.
Files: `prices.csv` (date x ticker, adjusted close), `returns.csv` (daily
simple returns), `ff_factors_daily.csv` (`Mkt_RF, SMB, HML, RF`, already
converted from percent to decimals), `universe.csv` (`ticker, name,
sector`). Quirks and teaching angles:
- Factor regressions use **excess returns** (stock return − `RF`).
- It's a **time series**: never shuffled K-fold; use time-based /
  walk-forward splits. Independence is violated in ways the book barely
  covers. Point it out as supplementary.
- Fat tails and volatility clustering: normal-theory intervals and constant
  variance are often wrong. That's a feature of the curriculum here.
- Dates are inner-joined between yfinance and French (holiday mismatches).
- Sector labels are **current** GICS (Alphabet/Meta moved to Communication
  Services in 2018); the universe is chosen with hindsight, so it has
  **survivorship bias**.
- Big single-day moves cluster on earnings dates and March 2020.
- Daily-return prediction mostly fails. Treat that as an honest-evaluation
  lesson, never a reason to tune until something looks good.

### Churn — `data/churn/telco_churn.csv`, `load_churn()`, `load_churn_split()`
IBM Telco Customer Churn: 7,043 customers x 21 columns, `Churn` = Yes for
1,869 (~26.5%). The loader adds `churned` (0/1), drops `customerID` from
modeling frames, and converts `TotalCharges` to float. Quirks:
- `TotalCharges` is text in the raw file with **11 blank values**, all
  customers with `tenure == 0`; the loader sets them to 0 and the
  MANIFEST documents it.
- `SeniorCitizen` is 0/1 while other binary columns are `"Yes"/"No"`.
- `"No internet service"` / `"No phone service"` levels in the add-on
  columns duplicate `InternetService == "No"` / `PhoneService == "No"`, so
  naive dummies are perfectly collinear (the dummy trap, for real).
- `TotalCharges ≈ tenure × MonthlyCharges`, so expect multicollinearity.
- Cross-sectional snapshot with no dates: random stratified splits are fine
  here, unlike markets.

## Tooling

- pandas and numpy are the primary implementation tools for the user's
  answers. scipy / statsmodels / matplotlib / scikit-learn are fine as
  supporting tools.
- Python 3.12 `.venv` has: pandas, numpy, scipy, statsmodels, matplotlib,
  scikit-learn, ipykernel, yfinance, requests, and `mlstats` (editable).
  No seaborn, no jupyter CLI: notebooks run via VS Code's Jupyter
  integration. Install new packages only when a notebook needs them (e.g.
  `xgboost` for 19), and add them to `pyproject.toml`.
- Not installed: `pygam`, seaborn, `pandas-datareader` (broken on 3.12;
  French data is parsed from the zip directly). For splines/GAMs use patsy
  `bs()`/`cr()` inside `smf.ols` formulas and `statsmodels.gam.api.GLMGam` +
  `BSplines`. Python has no built-in AIC stepwise; point the user at a
  hand-written loop on `.aic` or
  `sklearn.feature_selection.SequentialFeatureSelector`. patsy `bs()` cannot
  predict outside the range it was fit on unless `lower_bound`/`upper_bound`
  are passed.
- Robust SEs: `.fit(cov_type="HC3")` and `.fit(cov_type="HAC",
  cov_kwds={"maxlags": k})` in statsmodels.

## Syllabus / progress tracker

`Textbooks/practical_stats_for_ds/syllabus.md` is the chapter-by-chapter,
section-by-section checklist of the book's contents (reconstructed, not
verbatim; correct it as discrepancies show up), plus the list of what the
book deliberately doesn't cover.

- It opens with a **Status** block: current notebook and section, next step,
  open review notebook, and a dated one-line log of recent sessions. **Read
  it at the start of every session** and state where things left off in one
  or two lines. **Update it at the end of every session.**
- Each checked item notes its notebook path and dataset.
- Before scaffolding a new notebook, check it to avoid duplicating
  exercises; after building, check off the section(s).
- This is the answer to "what have I learned so far" and "what's the book
  missing". Read it rather than re-deriving book structure.

## Review protocol

After the user completes a notebook exercise, Claude reviews:

1. Whether the code and result are correct.
2. The user's markdown bullet-point explanation of what the result means.

If the explanation is sound, confirm briefly and move on. Don't manufacture
follow-up questions or push back just to be thorough. Only go deeper when
something is actually incorrect or incomplete, and explain the specific
flaw. The goal is one clean pass per concept, not a dragged-out Socratic
dialogue.

### Review format: easy to scan (applies to exam Review cells and chat reviews)

The user wants reviews they can read in seconds, so:

- Open with **one line** of overall verdict.
- Then **one bullet per sub-part**, starting with a bold verdict
  (**Right**, **Mostly right**, **Right call, wrong reason**, **Off**).
- Only flawed parts get a fix, and the fix is **one or two sentences**, with
  the key number or the sentence they should say instead (in italics).
- Bold the one term or number that matters. No paragraphs, no re-teaching the
  whole concept, no more than about 120 words per question.
- Anything right gets a verdict and nothing else.
