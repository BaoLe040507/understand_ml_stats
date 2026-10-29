# Practical Statistics for Data Scientists — syllabus & progress tracker

Reconstructed from the book's official code repository
([gedeck/practical-statistics-for-data-scientists](https://github.com/gedeck/practical-statistics-for-data-scientists))
plus general knowledge of the 2nd edition's structure — this is **not** a
verbatim table of contents (some purely conceptual subsections with no
accompanying code may be missing or slightly mis-titled). Correct it against
the actual book as discrepancies show up; treat it as a living document.

Check off a section when a notebook exists that exercises it, and add the
notebook filename next to the checked item so this doubles as an index.

## Status

- **Current:** notebook 10 (`ch04_regression/10_interpreting-the-regression-equation.ipynb`), section 1 done (reflection bullets still blank); sections 2-4 next.
- **Then:** 11 (markets, rebuilt), 12 (Ames), then Ch 5 on churn.
- **Open review notebook:** `reviews/R01_regression-diagnostics.ipynb` (11's exam). Exams for 10 and 12 remain inside those notebooks.
- **Log:**
  - 2026-10-29: repo refactored to project mode (see CLAUDE.md)

## How this gets used

- **Start of every session:** read the Status block above, state where things left off in a line or two, and update it (and the log) at the end of the session.
- Before scaffolding a new notebook, Claude should skim this file to see
  what's already covered and avoid duplicating exercises.
- After a notebook is created/extended for a concept, mark the relevant
  section(s) `[x]` here and note the notebook filename.
- If the user's description of a concept doesn't match a listed section
  (because this outline is imperfect), add/fix the entry rather than forcing
  it into the wrong bucket.

---

## Ch 1 — Exploratory Data Analysis
- [x] Estimates of Location (mean, trimmed mean, median, weighted mean) — *(pending import: user-completed, notebook to be added to repo)*
- [x] Estimates of Variability (std dev, variance, MAD, range, IQR, percentiles) — *(pending import)*
- [x] Percentiles and Boxplots — *(pending import)*
- [x] Frequency Tables and Histograms — *(pending import)*
- [x] Density Estimates — *(pending import)*
- [x] Exploring Binary and Categorical Data (mode, expected value, bar charts) — *(pending import)*
- [x] Correlation (Pearson's r, correlation matrix, scatterplots) — *(pending import)*
- [x] Exploring Two or More Variables — *(pending import)*
  - [x] Hexagonal Binning and Contours (numeric vs numeric, large n) — *(pending import)*
  - [x] Two Categorical Variables (contingency tables) — *(pending import)*
  - [x] Categorical and Numeric Data (grouped boxplots/violin plots) — *(pending import)*
  - [x] Visualizing Multiple Variables (faceting/trellis) — *(pending import)*

## Ch 2 — Data and Sampling Distributions
- [x] Random Sampling and Sample Bias — *(pending import)*
- [x] Selection Bias — *(pending import)*
- [x] Sampling Distribution of a Statistic — *(pending import)*
- [x] The Bootstrap — *(pending import)*
- [x] Confidence Intervals — *(pending import)*
- [x] Normal Distribution — *(pending import)*
  - [x] Standard Normal and QQ-Plots — *(pending import)*
- [x] Long-Tailed Distributions — *(pending import)*
- [x] Student's t-Distribution — *(pending import)*
- [x] Binomial Distribution — `notebooks/ch02_sampling/04_binomial-and-reference-distributions.ipynb` · Ames (complete)
- [x] Chi-Square Distribution (as a reference distribution) — `notebooks/ch02_sampling/04_binomial-and-reference-distributions.ipynb` · Ames (in progress)
- [ ] F-Distribution (as a reference distribution) — *skipped by user judgment, not important to their goals*
- [x] Poisson and Related Distributions — `notebooks/ch02_sampling/04_binomial-and-reference-distributions.ipynb` · Ames (complete; last section of this notebook)
  - [x] Poisson Distribution — `notebooks/ch02_sampling/04_binomial-and-reference-distributions.ipynb` · Ames (complete)
  - [ ] Exponential Distribution — *skipped by user judgment, not important to their goals*
  - [ ] Weibull Distribution — *skipped by user judgment, not important to their goals*

## Ch 3 — Statistical Experiments and Significance Testing
- [x] A/B Testing and Hypothesis Tests (null/alternative hypothesis, one-way vs. two-way tests) — `notebooks/ch03_significance/05_ab-testing-and-t-tests.ipynb` · Ames (complete)
- [x] Resampling (permutation test, exhaustive vs. bootstrap permutation test) — `notebooks/ch03_significance/05_ab-testing-and-t-tests.ipynb` · Ames (complete)
- [x] Statistical Significance and P-Values — `notebooks/ch03_significance/05_ab-testing-and-t-tests.ipynb` · Ames (complete)
  - [x] Alpha, Type 1 and Type 2 Errors — `notebooks/ch03_significance/05_ab-testing-and-t-tests.ipynb` · Ames (complete)
- [x] t-Tests — `notebooks/ch03_significance/05_ab-testing-and-t-tests.ipynb` · Ames (complete)
- [x] Multiple Testing — `notebooks/ch03_significance/06_multiple-testing-dof-and-anova.ipynb` · Ames (scaffolded, not yet answered)
- [x] Degrees of Freedom — `notebooks/ch03_significance/06_multiple-testing-dof-and-anova.ipynb` · Ames (scaffolded, not yet answered)
- [x] ANOVA — `notebooks/ch03_significance/06_multiple-testing-dof-and-anova.ipynb` · Ames (scaffolded, not yet answered)
  - [x] F-Statistic — `notebooks/ch03_significance/06_multiple-testing-dof-and-anova.ipynb` · Ames (scaffolded, not yet answered)
  - [x] Two-Way ANOVA — `notebooks/ch03_significance/06_multiple-testing-dof-and-anova.ipynb` · Ames (scaffolded, not yet answered)
- [x] Chi-Square Test — `notebooks/ch03_significance/07_chi-square-bandits-and-power.ipynb` · Ames (scaffolded, not yet answered)
  - [x] Chi-Square Test: A Resampling Approach — `notebooks/ch03_significance/07_chi-square-bandits-and-power.ipynb` · Ames (scaffolded, not yet answered)
  - [x] Fisher's Exact Test — `notebooks/ch03_significance/07_chi-square-bandits-and-power.ipynb` · Ames (scaffolded, not yet answered)
  - [x] Relevance for Data Science — `notebooks/ch03_significance/07_chi-square-bandits-and-power.ipynb` · Ames (scaffolded, not yet answered)
- [x] Multi-Arm Bandit Algorithm — `notebooks/ch03_significance/07_chi-square-bandits-and-power.ipynb` · Ames (scaffolded, not yet answered)
- [x] Power and Sample Size — `notebooks/ch03_significance/07_chi-square-bandits-and-power.ipynb` · Ames (scaffolded, not yet answered)

## Ch 4 — Regression and Prediction
*(Sections below came from the reconstructed outline; flag any that don't match the book.)*
- [x] Simple Linear Regression (regression equation, fitted values, residuals) — `notebooks/ch04_regression/08_simple-and-multiple-regression.ipynb` · Ames (scaffolded, not yet answered; exam included)
- [x] Multiple Linear Regression — `notebooks/ch04_regression/08_simple-and-multiple-regression.ipynb` · Ames (scaffolded, not yet answered; exam included)
  - [x] Assessing the Model (RMSE, R², adjusted R²) — `notebooks/ch04_regression/08_simple-and-multiple-regression.ipynb` · Ames (scaffolded, not yet answered; exam included)
  - [x] Model Selection and Stepwise Regression — `notebooks/ch04_regression/08_simple-and-multiple-regression.ipynb` · Ames (scaffolded, not yet answered; exam included)
  - [x] Weighted Regression — `notebooks/ch04_regression/08_simple-and-multiple-regression.ipynb` · Ames (scaffolded, not yet answered; exam included)
- [x] Factor (Categorical) Variables in Regression — `notebooks/ch04_regression/09_factor-variables-in-regression.ipynb` · Ames (scaffolded, not yet answered; exam included)
  - [x] Dummy Variable Representation — `notebooks/ch04_regression/09_factor-variables-in-regression.ipynb` · Ames (scaffolded, not yet answered; exam included)
  - [x] Factor Variables with Many Levels — `notebooks/ch04_regression/09_factor-variables-in-regression.ipynb` · Ames (scaffolded, not yet answered; exam included)
  - [x] Ordered Factor Variables — `notebooks/ch04_regression/09_factor-variables-in-regression.ipynb` · Ames (scaffolded, not yet answered; exam included)
- [x] Interpreting the Regression Equation — `notebooks/ch04_regression/10_interpreting-the-regression-equation.ipynb` · Ames (scaffolded, not yet answered; exam included)
  - [x] Correlated Predictors — `notebooks/ch04_regression/10_interpreting-the-regression-equation.ipynb` · Ames (scaffolded, not yet answered; exam included)
  - [x] Multicollinearity — `notebooks/ch04_regression/10_interpreting-the-regression-equation.ipynb` · Ames (scaffolded, not yet answered; exam included)
  - [x] Confounding Variables — `notebooks/ch04_regression/10_interpreting-the-regression-equation.ipynb` · Ames (scaffolded, not yet answered; exam included)
  - [x] Interactions and Main Effects — `notebooks/ch04_regression/10_interpreting-the-regression-equation.ipynb` · Ames (scaffolded, not yet answered; exam included)
- [x] Testing the Assumptions: Regression Diagnostics — `notebooks/ch04_regression/11_regression-diagnostics.ipynb` · markets (built; markets rebuild: how much to trust a stock's beta; exam in `reviews/R01_regression-diagnostics.ipynb`)
  - [x] Outliers — `notebooks/ch04_regression/11_regression-diagnostics.ipynb` · markets (built; LOW influence by Cook's distance, March 2020)
  - [x] Influential Values — `notebooks/ch04_regression/11_regression-diagnostics.ipynb` · markets (built; leverage x residual, beta with vs. without influential days)
  - [x] Heteroskedasticity, Non-Normality, and Correlated Errors — `notebooks/ch04_regression/11_regression-diagnostics.ipynb` · markets (built; Breusch-Pagan, HC3; non-normality / fat tails are not exercised; exam in R01)
  - [x] Partial Residual Plots and Nonlinearity — `notebooks/ch04_regression/11_regression-diagnostics.ipynb` · markets (built; SPG three-factor model, down-market kink; exam in R01)
- [x] Polynomial and Spline Regression — `notebooks/ch04_regression/12_polynomial-spline-and-gam.ipynb` · Ames (scaffolded, not yet answered; exam included)
  - [x] Generalized Additive Models (GAM) — `notebooks/ch04_regression/12_polynomial-spline-and-gam.ipynb` · Ames (scaffolded, not yet answered; exam included)

Supplementary (not in the book, flagged in the notebooks): omitted-variable-bias identity and mediators / bad controls (`10`), uncorrelated vs. independent errors and overlapping-return autocorrelation / HAC (`11`), survivorship in the stock universe (R01 exam), target-encoding leakage (`09`).

## Ch 5 — Classification
- [ ] Naive Bayes — *planned: notebook 13 · churn*
- [ ] Discriminant Analysis (LDA) — *planned: notebook 13 · churn*
- [ ] Logistic Regression — *planned: notebook 14 · churn*
  - [ ] Logistic Response Function and Logit — *planned: notebook 14 · churn*
  - [ ] Logistic Regression and the GLM — *planned: notebook 14 · churn*
  - [ ] Predicted Values, Interpreting Coefficients, Odds Ratios — *planned: notebook 14 · churn*
  - [ ] Assessing the Model — *planned: notebook 14 · churn*
- [ ] Evaluating Classification Models — *planned: notebook 15 · churn*
  - [ ] Confusion Matrix — *planned: notebook 15 · churn*
  - [ ] Precision, Recall, Specificity — *planned: notebook 15 · churn*
  - [ ] ROC Curve, AUC — *planned: notebook 15 · churn*
  - [ ] Lift — *planned: notebook 15 · churn*
- [ ] Strategies for Imbalanced Data — *planned: notebook 15 · churn*
  - [ ] Undersampling / Oversampling / Up-Down Weighting — *planned: notebook 15 · churn*
  - [ ] Data Generation (e.g. SMOTE) — *planned: notebook 15, conceptual / exam-only · churn*
  - [ ] Cost-Based Classification — *planned: notebook 15 · churn*
  - [ ] Exploring the Predictions — *planned: notebook 15 · churn*

## Ch 6 — Statistical Machine Learning
- [ ] K-Nearest Neighbors — *planned: notebook 16 · churn*
  - [ ] Standardization (Z-Scores) — *planned: notebook 16 · churn*
  - [ ] KNN as a Feature Engine — *planned: notebook 16 · churn*
- [ ] Tree Models — *planned: notebook 17 · churn*
  - [ ] Recursive Partitioning Algorithm — *planned: notebook 17 · churn*
  - [ ] Measuring Homogeneity or Impurity — *planned: notebook 17 · churn*
  - [ ] Stopping the Tree from Growing — *planned: notebook 17 · churn*
- [ ] Bagging and the Random Forest — *planned: notebook 18 · churn*
  - [ ] Variable Importance — *planned: notebook 18 · churn*
  - [ ] Hyperparameters — *planned: notebook 18 · churn*
- [ ] Boosting — *planned: notebook 19 · churn*
  - [ ] The Boosting Algorithm — *planned: notebook 19 · churn*
  - [ ] XGBoost — *planned: notebook 19 · churn*
  - [ ] Regularization: Avoiding Overfitting — *planned: notebook 19 · churn*
  - [ ] Hyperparameters and Cross-Validation — *planned: notebook 19 · churn*

## Ch 7 — Unsupervised Learning
- [ ] Principal Components Analysis (PCA) — *planned: notebook 20 · markets*
  - [ ] Interpreting Principal Components — *planned: notebook 20 · markets*
  - [ ] Correspondence Analysis — *planned: exam-only (churn categoricals)*
- [ ] K-Means Clustering — *planned: notebook 21 · markets*
  - [ ] K-Means Algorithm — *planned: notebook 21 · markets*
  - [ ] Interpreting the Clusters — *planned: notebook 21 · markets*
  - [ ] Selecting the Number of Clusters — *planned: notebook 21 · markets*
- [ ] Hierarchical Clustering — *planned: notebook 21 · markets*
  - [ ] The Dendrogram — *planned: notebook 21 · markets*
  - [ ] Measures of Dissimilarity — *planned: notebook 21 · markets*
- [ ] Model-Based Clustering — *planned: notebook 22 · churn*
  - [ ] Multivariate Normal Distribution — *planned: notebook 22 · churn*
  - [ ] Mixtures of Normals — *planned: notebook 22 · churn*
  - [ ] Selecting the Number of Clusters — *planned: notebook 22 · churn*
- [ ] Scaling and Categorical Variables — *planned: notebook 22 · churn*
  - [ ] Scaling the Variables — *planned: notebook 22 · churn*
  - [ ] Dominant Variables — *planned: notebook 22 · churn*
  - [ ] Categorical Data and Gower's Distance — *planned: notebook 22 · churn*
  - [ ] Problems with Clustering Mixed Data — *planned: notebook 22 · churn*

---

## What this book does *not* cover (known scope gaps)

Worth knowing so gaps don't get mistaken for something missed in this repo —
these are just outside the book's scope, not unfinished checklist items:

- **Bayesian inference** beyond Naive Bayes as a classifier — no priors/
  posteriors, MCMC, or Bayesian A/B testing.
- **Time series** — no forecasting, ARIMA, seasonality/trend decomposition.
- **Deep learning / neural networks** — not covered at all.
- **NLP / text and embeddings.**
- **Causal inference** beyond a brief mention of confounding — no
  propensity scores, DAGs, instrumental variables, diff-in-diff.
- **Survival analysis.**
- **Missing data / imputation** — treated lightly; the book mostly works
  with clean data.
- **Probability theory foundations** — the book is applied; it names
  distributions and uses them, but doesn't build up measure-theoretic or
  axiomatic probability.
- **Model deployment / MLOps.**

If a concept from outside this list comes up, it's fair game to still build
an Ames exercise for it — just flag that it's supplementary, not from the
book.
