"""Download the IBM Telco churn dataset to data/churn/telco_churn.csv (raw, unchanged)."""
import datetime as dt
import io

import pandas as pd
import requests

from mlstats.paths import DATA_DIR

URL = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
OUT = DATA_DIR / "churn"


def main():
    source = URL
    try:
        resp = requests.get(URL, timeout=60)
        resp.raise_for_status()
        raw = resp.text
    except Exception as exc:  # fall back to OpenML
        print(f"IBM URL failed ({exc}); trying OpenML")
        from sklearn.datasets import fetch_openml

        bunch = fetch_openml(name="telco-customer-churn", as_frame=True)
        raw = bunch.frame.to_csv(index=False)
        source = "OpenML telco-customer-churn"
    df = pd.read_csv(io.StringIO(raw), dtype=str, keep_default_na=False)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "telco_churn.csv").write_text(raw, encoding="utf-8", newline="")

    assert df.shape == (7043, 21), df.shape
    n_churn = int((df["Churn"] == "Yes").sum())
    assert n_churn == 1869, n_churn
    blank = df["TotalCharges"].str.strip() == ""
    assert blank.sum() == 11, blank.sum()
    assert (df.loc[blank, "tenure"].astype(int) == 0).all()

    manifest = f"""# Churn data manifest

- Source: {source}
- Fetched: {dt.date.today()}
- File: `telco_churn.csv` (raw, unchanged)
- Shape: {df.shape[0]} rows x {df.shape[1]} columns
- `Churn == "Yes"`: {n_churn} ({n_churn / len(df):.1%})
- Blank `TotalCharges`: {int(blank.sum())}, all with `tenure == 0` (the loader sets them to 0.0)
"""
    (OUT / "MANIFEST.md").write_text(manifest, encoding="utf-8")
    print(manifest)
    print("All assertions passed.")


if __name__ == "__main__":
    main()
