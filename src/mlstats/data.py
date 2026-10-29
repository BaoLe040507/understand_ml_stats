"""Dataset loaders. Notebooks always load data through these, never a CSV path."""
import pandas as pd

from .paths import DATA_DIR


def _require(path, script):
    if not path.exists():
        raise FileNotFoundError(f"{path} is missing. Run `python scripts/{script}` from the repo root to build it.")
    return path


def load_ames() -> pd.DataFrame:
    """Ames Housing (2,930 x 81), unchanged from the committed CSV."""
    return pd.read_csv(_require(DATA_DIR / "ames" / "ames_housing.csv", "(committed file; check git)"))


def _read_dated(name, script="fetch_markets.py"):
    return pd.read_csv(_require(DATA_DIR / "markets" / name, script), index_col=0, parse_dates=True)


def load_universe() -> pd.DataFrame:
    """ticker, name, sector for the frozen universe (plus SPY as 'Benchmark')."""
    return pd.read_csv(_require(DATA_DIR / "markets" / "universe.csv", "fetch_markets.py"))


def load_prices() -> pd.DataFrame:
    """Adjusted close, date x ticker."""
    return _read_dated("prices.csv")


def load_factors() -> pd.DataFrame:
    """Fama-French 3 factors, daily, as decimals: Mkt_RF, SMB, HML, RF."""
    return _read_dated("ff_factors_daily.csv")


def load_returns(tickers=None, excess=False) -> pd.DataFrame:
    """Daily simple returns. With excess=True, subtract RF after an inner date join with the factors."""
    r = _read_dated("returns.csv")
    if tickers is not None:
        r = r[[tickers] if isinstance(tickers, str) else list(tickers)]
    if excess:
        f = load_factors()
        r, rf = r.align(f["RF"], join="inner", axis=0)
        r = r.sub(rf, axis=0)
    return r


def load_churn() -> pd.DataFrame:
    """IBM Telco churn (7,043 x 21) plus `churned` (0/1); TotalCharges as float."""
    df = pd.read_csv(_require(DATA_DIR / "churn" / "telco_churn.csv", "fetch_churn.py"))
    tc = df["TotalCharges"].astype(str).str.strip().replace("", pd.NA)
    blank = tc.isna()
    assert (df.loc[blank, "tenure"] == 0).all(), "blank TotalCharges should only occur at tenure == 0"
    df["TotalCharges"] = pd.to_numeric(tc).fillna(0.0)
    df["churned"] = (df["Churn"] == "Yes").astype(int)
    return df


def load_churn_split(test_size=0.3, seed=42):
    """Fixed stratified (train, test) split on `churned`, customerID dropped.

    Every Ch5-6 notebook uses this exact split; never change the defaults.
    """
    from sklearn.model_selection import train_test_split

    df = load_churn().drop(columns="customerID")
    return tuple(train_test_split(df, test_size=test_size, random_state=seed, stratify=df["churned"]))
