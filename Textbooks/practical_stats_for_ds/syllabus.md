# Practical Statistics for Data Scientists — syllabus & progress tracker

Reconstructed from the book's official code repository
([gedeck/practical-statistics-for-data-scientists](https://github.com/gedeck/practical-statistics-for-data-scientists))
plus general knowledge of the 2nd edition's structure — this is **not** a
verbatim table of contents (some purely conceptual subsections with no
accompanying code may be missing or slightly mis-titled). Correct it against
the actual book as discrepancies show up; treat it as a living document.

Check off a section when a notebook exists that exercises it, and add the
notebook filename next to the checked item so this doubles as an index.

## How this gets used

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
- [x] Binomial Distribution — `notebooks/04_binomial-and-reference-distributions.ipynb` (complete)
- [x] Chi-Square Distribution (as a reference distribution) — `notebooks/04_binomial-and-reference-distributions.ipynb` (in progress)
- [ ] F-Distribution (as a reference distribution) — *skipped by user judgment, not important to their goals*
- [x] Poisson and Related Distributions — `notebooks/04_binomial-and-reference-distributions.ipynb` (complete; last section of this notebook)
  - [x] Poisson Distribution — `notebooks/04_binomial-and-reference-distributions.ipynb` (complete)
  - [ ] Exponential Distribution — *skipped by user judgment, not important to their goals*
  - [ ] Weibull Distribution — *skipped by user judgment, not important to their goals*

## Ch 3 — Statistical Experiments and Significance Testing
- [x] A/B Testing and Hypothesis Tests (null/alternative hypothesis, one-way vs. two-way tests) — `notebooks/05_ab-testing-and-t-tests.ipynb` (scaffolded, not yet answered)
- [x] Resampling (permutation test, exhaustive vs. bootstrap permutation test) — `notebooks/05_ab-testing-and-t-tests.ipynb` (scaffolded, not yet answered)
- [x] Statistical Significance and P-Values — `notebooks/05_ab-testing-and-t-tests.ipynb` (scaffolded, not yet answered)
  - [x] Alpha, Type 1 and Type 2 Errors — `notebooks/05_ab-testing-and-t-tests.ipynb` (scaffolded, not yet answered)
- [x] t-Tests — `notebooks/05_ab-testing-and-t-tests.ipynb` (scaffolded, not yet answered)
- [ ] Multiple Testing
- [ ] Degrees of Freedom
- [ ] ANOVA
  - [ ] F-Statistic
  - [ ] Two-Way ANOVA
- [ ] Chi-Square Test
  - [ ] Chi-Square Test: A Resampling Approach
  - [ ] Fisher's Exact Test
  - [ ] Relevance for Data Science
- [ ] Multi-Arm Bandit Algorithm
- [ ] Power and Sample Size

## Ch 4 — Regression and Prediction
- [ ] Simple Linear Regression (regression equation, fitted values, residuals)
- [ ] Multiple Linear Regression
  - [ ] Assessing the Model (RMSE, R², adjusted R²)
  - [ ] Model Selection and Stepwise Regression
  - [ ] Weighted Regression
- [ ] Factor (Categorical) Variables in Regression
  - [ ] Dummy Variable Representation
  - [ ] Factor Variables with Many Levels
  - [ ] Ordered Factor Variables
- [ ] Interpreting the Regression Equation
  - [ ] Correlated Predictors
  - [ ] Multicollinearity
  - [ ] Confounding Variables
  - [ ] Interactions and Main Effects
- [ ] Testing the Assumptions: Regression Diagnostics
  - [ ] Outliers
  - [ ] Influential Values
  - [ ] Heteroskedasticity, Non-Normality, and Correlated Errors
  - [ ] Partial Residual Plots and Nonlinearity
- [ ] Polynomial and Spline Regression
  - [ ] Generalized Additive Models (GAM)

## Ch 5 — Classification
- [ ] Naive Bayes
- [ ] Discriminant Analysis (LDA)
- [ ] Logistic Regression
  - [ ] Logistic Response Function and Logit
  - [ ] Logistic Regression and the GLM
  - [ ] Predicted Values, Interpreting Coefficients, Odds Ratios
  - [ ] Assessing the Model
- [ ] Evaluating Classification Models
  - [ ] Confusion Matrix
  - [ ] Precision, Recall, Specificity
  - [ ] ROC Curve, AUC
  - [ ] Lift
- [ ] Strategies for Imbalanced Data
  - [ ] Undersampling / Oversampling / Up-Down Weighting
  - [ ] Data Generation (e.g. SMOTE)
  - [ ] Cost-Based Classification
  - [ ] Exploring the Predictions

## Ch 6 — Statistical Machine Learning
- [ ] K-Nearest Neighbors
  - [ ] Standardization (Z-Scores)
  - [ ] KNN as a Feature Engine
- [ ] Tree Models
  - [ ] Recursive Partitioning Algorithm
  - [ ] Measuring Homogeneity or Impurity
  - [ ] Stopping the Tree from Growing
- [ ] Bagging and the Random Forest
  - [ ] Variable Importance
  - [ ] Hyperparameters
- [ ] Boosting
  - [ ] The Boosting Algorithm
  - [ ] XGBoost
  - [ ] Regularization: Avoiding Overfitting
  - [ ] Hyperparameters and Cross-Validation

## Ch 7 — Unsupervised Learning
- [ ] Principal Components Analysis (PCA)
  - [ ] Interpreting Principal Components
  - [ ] Correspondence Analysis
- [ ] K-Means Clustering
  - [ ] K-Means Algorithm
  - [ ] Interpreting the Clusters
  - [ ] Selecting the Number of Clusters
- [ ] Hierarchical Clustering
  - [ ] The Dendrogram
  - [ ] Measures of Dissimilarity
- [ ] Model-Based Clustering
  - [ ] Multivariate Normal Distribution
  - [ ] Mixtures of Normals
  - [ ] Selecting the Number of Clusters
- [ ] Scaling and Categorical Variables
  - [ ] Scaling the Variables
  - [ ] Dominant Variables
  - [ ] Categorical Data and Gower's Distance
  - [ ] Problems with Clustering Mixed Data

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
