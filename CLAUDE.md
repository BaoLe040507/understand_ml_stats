# understand_ml_stats

Purpose: build intuition for the ML/stats fundamentals covered in *Practical
Statistics for Data Scientists* by applying each concept to a real dataset
(Ames Housing) instead of just reading. The user is a working data scientist
who already knows the syntax — the goal is conceptual intuition, not a
tutorial.

## Learner profile and goal

The user is currently an **associate (entry-level) data scientist**. The
point of this repo is to build the depth of intuition expected of a **senior
data scientist, a decision-science / causal-inference role, or a machine-
learning role** — they are not committed to one track, and anything learned
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

## Role: guided instructor, not implementer

Claude scaffolds exercises. Claude does not solve them.

- The user reads a chunk of the textbook first (usually ~5-6 concepts, in
  book order, not necessarily related to each other) and brings Claude the
  main ideas they just read.
- For each concept / concept cluster, Claude creates or extends a Jupyter
  notebook under `Textbooks/practical_stats_for_ds/notebooks/` with:
  - A markdown cell posing a question or scenario grounded in the Ames
    Housing data that requires applying the concept to answer.
  - An empty code cell (or a few) for the user to implement their answer in.
  - No solution code, no pre-filled analysis, no answer key.
- If a textbook example is written around the book's own datasets (King
  County housing, `lc_loans`, `state.csv`, etc.), translate it onto Ames
  Housing rather than using the book's dataset.
- Group notebooks by overarching concept/topic, not strictly by the order
  concepts were mentioned — a batch of 5-6 loosely related concepts from the
  book may span multiple notebooks, and a later batch may extend an existing
  notebook if it revisits the same topic.

## Explanation style

Default to concrete, worked-numeric-example explanations over abstract/
formal ones when introducing a new concept — walk through actual numbers
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
  function/approach — without writing the solution code or stating the
  final numeric/interpretive answer.
- Only after that (roughly 3 hints without it clicking) give the fuller
  walkthrough or solution.
- This resets per question — a fresh question always starts back at hints,
  even if the previous one needed a full walkthrough.
- This is separate from the post-hoc review protocol below: hints are
  real-time scaffolding while the user is actively working a question;
  review happens after they've committed to an answer.

## Notebook conventions

- Location: `Textbooks/practical_stats_for_ds/notebooks/`
- Naming: `NN_topic-slug.ipynb`, where `NN` is a zero-padded running sequence
  number reflecting encounter order (e.g. `01_estimates-of-location.ipynb`,
  `02_estimates-of-variability.ipynb`). Extend an existing file (new cells)
  rather than creating a duplicate if the topic already has a notebook.
- Each concept gets its own markdown question cell + empty code cell(s), so
  the notebook reads as a sequence of self-contained mini-exercises.
- Any exercise question that needs a library function the user may not have
  memorized ends with a short `*Tools for this question:*` bullet list: the
  call signature with its main parameters, what it returns, and any gotcha
  (e.g., "`cooks_distance` returns a tuple, take `[0]`"). The goal is that
  the user never has to leave the notebook to read documentation. Verify the
  signatures against the installed versions. Exam questions don't need this
  (they involve little or no code).
- Notebook JSON is nbformat 4.5: every cell needs a unique `id`; copy the
  kernelspec metadata from an existing notebook; write files as UTF-8; run
  `nbformat.validate` on anything generated.
- Before writing question text, check the actual column names/levels in
  `ames_housing.csv`. Quirks: quality ratings are *words* (`Overall_Qual` is
  `Very_Poor`...`Very_Excellent`, not 1-10); "none" is an explicit level
  (`No_Garage`, `No_Basement`, `No_Fireplace`), not NaN; `Lot_Frontage` uses 0
  where other versions have NA; rows are ordered roughly by neighborhood, not
  by date; `Gr_Liv_Area == First_Flr_SF + Second_Flr_SF + Low_Qual_Fin_SF`
  exactly; `Year_Remod_Add` is floored at 1950 (older homes show 1950 whether
  or not they were remodeled), so "was remodeled" flags need `Year_Built >= 1950`.

## Time budget (from notebook 09 onward)

Each notebook, exam included, should take the user **one hour at most**. They
found 60-90+ minute notebooks too slow to get through the book, so 09-12 were
condensed to this format and every new notebook follows it:

- At most **4 exercise sections**, each with at most **3 sub-parts** (about 10
  minutes per section). Drop a sub-part if an earlier one already settles its
  answer; move overflow topics into the exam instead of adding sections.
- At most **one heavy pipeline sub-part per notebook** (a CV loop, a bootstrap,
  a train/test comparison of several models). When a later section needs the
  same machinery, tell the user to reuse their earlier function or split.
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

## Exams (from Ch 4 onward)

Starting with Chapter 4, every notebook ends with an **Exam** section (do not
retrofit notebooks 04-07). Purpose: test intuition and interview readiness,
not coding.

- 5 questions per notebook (08 has 7; it predates the time budget). Mostly *no code*: the model outputs are
  printed into the question (as fenced ```text blocks, never as code cells,
  so they don't read as pre-filled analysis) and the user reads, predicts,
  or explains. Three question types, mixed: **read an output**, **predict
  what happens if X changes**, **interview-style** ("how would you explain /
  what could go wrong / what would you do").
- Each question has a title, a role-lean tag (DS / Causal / ML), the stem
  with real numbers, then two cells: **Your answer** (user fills in) and
  **Review** (placeholder `_pending_`; Claude fills in after the user
  answers).
- Exam output must come from model specs/subsets that differ from the
  notebook's exercises, so the exam is not an answer key for the exercises.
  Every number in a stem must be computed from the real data (a throwaway
  script that builds the notebook and prints the exam outputs is the
  reliable way); never invent output.
- No hidden answer key in the notebook. Review cells stay empty until the
  user has answered.
- Reviewing exam answers follows the Review protocol below: confirm briefly
  when right (being right is a fully acceptable outcome), correct only real
  flaws. The "stuck" hint ladder is for exercises, not exams; if the user
  asks for help on an exam question, give a hint first, then fill in the
  review only after they have committed an answer.

## Tooling

- pandas and numpy are the primary implementation tools for the user's
  answers. scipy / statsmodels / matplotlib are fine as supporting tools for
  statistical tests and plots.
- Python 3.12 environment already has: pandas, numpy, scipy, statsmodels,
  matplotlib, scikit-learn, ipykernel. No seaborn or jupyter/jupyterlab CLI
  installed — notebooks are expected to be run via an IDE's Jupyter
  integration (e.g. VS Code), not `jupyter notebook`/`lab`.
- Not installed: `pygam`, seaborn. For splines/GAMs use patsy `bs()`/`cr()`
  inside `smf.ols` formulas and `statsmodels.gam.api.GLMGam` + `BSplines`.
  Python has no built-in AIC stepwise; point the user at a hand-written loop
  on `.aic` or `sklearn.feature_selection.SequentialFeatureSelector` (which
  ranks by CV score instead). patsy `bs()` cannot predict outside the range
  it was fit on unless `lower_bound`/`upper_bound` are passed.

## Syllabus / progress tracker

`Textbooks/practical_stats_for_ds/syllabus.md` is a chapter-by-chapter,
section-by-section checklist of the book's contents (reconstructed from the
book's official code repo, not verbatim — correct it as discrepancies show
up), plus a list of what the book deliberately doesn't cover (Bayesian
inference, time series, deep learning, NLP, causal inference, survival
analysis, MLOps, etc.).

- Before scaffolding a new notebook, check this file to see what's already
  covered and avoid duplicating exercises.
- After a notebook is created/extended for a concept, check off the
  relevant section(s) and note the notebook filename next to it.
- This is also the answer to "what have I learned so far" and "what's the
  book missing" — read it rather than re-deriving book structure each time.

## Dataset

`Textbooks/practical_stats_for_ds/data/ames_housing.csv` — the full De Cock
Ames Housing dataset (2,930 rows x 81 columns, zero missing values),
fetched from OpenML (`sklearn.datasets.fetch_openml(data_id=43926)`).
Target column: `Sale_Price`. Also includes `Latitude`/`Longitude`. This is
the cleaned, full version (not the 1,460-row Kaggle train.csv subset), so
concepts like distributions, outliers, and missing-data handling should be
introduced deliberately if needed rather than relying on this file to have
gaps.

## Review protocol

After the user completes a notebook exercise, Claude reviews:

1. Whether the code and result are correct.
2. The user's markdown bullet-point explanation of what the result means.

If the explanation is sound, confirm briefly and move on — do not manufacture
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
