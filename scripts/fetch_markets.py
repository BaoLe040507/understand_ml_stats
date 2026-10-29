"""Download prices (yfinance) and Fama-French 3 factors to data/markets/ over a frozen window."""
import datetime as dt
import io
import zipfile

import numpy as np
import pandas as pd
import requests
import yfinance as yf

from mlstats.paths import DATA_DIR

START, END = "2016-01-01", "2026-01-01"  # yfinance end is exclusive -> last day 2025-12-31
OUT = DATA_DIR / "markets"
FF_URL = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip"

UNIVERSE = {
    "Information Technology": "AAPL MSFT NVDA ORCL CSCO ADBE",
    "Communication Services": "GOOGL META NFLX DIS VZ T",
    "Consumer Discretionary": "AMZN HD MCD NKE SBUX LOW",
    "Consumer Staples": "PG KO PEP WMT COST CL",
    "Health Care": "JNJ UNH PFE MRK ABT AMGN",
    "Financials": "JPM BAC WFC GS MS AXP",
    "Industrials": "CAT HON UNP DE MMM LMT",
    "Energy": "XOM CVX COP SLB EOG OXY",
    "Utilities": "NEE DUK SO D AEP SRE",
    "Real Estate": "PLD AMT SPG O EQIX PSA",
    "Materials": "SHW APD NEM FCX ECL NUE",
}
NAMES = {
    "AAPL": "Apple", "MSFT": "Microsoft", "NVDA": "NVIDIA", "ORCL": "Oracle", "CSCO": "Cisco", "ADBE": "Adobe",
    "GOOGL": "Alphabet", "META": "Meta Platforms", "NFLX": "Netflix", "DIS": "Walt Disney", "VZ": "Verizon", "T": "AT&T",
    "AMZN": "Amazon", "HD": "Home Depot", "MCD": "McDonald's", "NKE": "Nike", "SBUX": "Starbucks", "LOW": "Lowe's",
    "PG": "Procter & Gamble", "KO": "Coca-Cola", "PEP": "PepsiCo", "WMT": "Walmart", "COST": "Costco", "CL": "Colgate-Palmolive",
    "JNJ": "Johnson & Johnson", "UNH": "UnitedHealth", "PFE": "Pfizer", "MRK": "Merck", "ABT": "Abbott", "AMGN": "Amgen",
    "JPM": "JPMorgan Chase", "BAC": "Bank of America", "WFC": "Wells Fargo", "GS": "Goldman Sachs", "MS": "Morgan Stanley", "AXP": "American Express",
    "CAT": "Caterpillar", "HON": "Honeywell", "UNP": "Union Pacific", "DE": "Deere", "MMM": "3M", "LMT": "Lockheed Martin",
    "XOM": "Exxon Mobil", "CVX": "Chevron", "COP": "ConocoPhillips", "SLB": "Schlumberger", "EOG": "EOG Resources", "OXY": "Occidental Petroleum",
    "NEE": "NextEra Energy", "DUK": "Duke Energy", "SO": "Southern Company", "D": "Dominion Energy", "AEP": "American Electric Power", "SRE": "Sempra",
    "PLD": "Prologis", "AMT": "American Tower", "SPG": "Simon Property", "O": "Realty Income", "EQIX": "Equinix", "PSA": "Public Storage",
    "SHW": "Sherwin-Williams", "APD": "Air Products", "NEM": "Newmont", "FCX": "Freeport-McMoRan", "ECL": "Ecolab", "NUE": "Nucor",
    "SPY": "SPDR S&P 500 ETF",
}


def fetch_factors():
    z = zipfile.ZipFile(io.BytesIO(requests.get(FF_URL, timeout=60).content))
    lines = z.read(z.namelist()[0]).decode("latin-1").splitlines()
    start = next(i for i, ln in enumerate(lines) if ln.strip().startswith(",Mkt-RF"))
    rows = []
    for ln in lines[start + 1:]:
        parts = [p.strip() for p in ln.split(",")]
        if not (parts[0].isdigit() and len(parts[0]) == 8):
            break  # copyright footer
        rows.append(parts)
    f = pd.DataFrame(rows, columns=["date", "Mkt_RF", "SMB", "HML", "RF"])
    f["date"] = pd.to_datetime(f["date"], format="%Y%m%d")
    f = f.set_index("date").astype(float) / 100  # source is in percent
    print("factor file covers", f.index.min().date(), "to", f.index.max().date())
    assert f.index.max() >= pd.Timestamp("2025-12-31"), "factor file does not cover the window"
    return f.loc[START:"2025-12-31"]


def main():
    tickers = [t for s in UNIVERSE.values() for t in s.split()] + ["SPY"]
    raw = yf.download(tickers, start=START, end=END, auto_adjust=True, progress=False)
    prices = raw["Close"][tickers]
    print(pd.DataFrame({"first": prices.apply(lambda c: c.first_valid_index()),
                        "last": prices.apply(lambda c: c.last_valid_index()),
                        "n_nan": prices.isna().sum()}).to_string())
    returns = prices.pct_change().iloc[1:]
    assert not returns.isna().any().any(), returns.isna().sum()[lambda s: s > 0]

    factors = fetch_factors()
    common = returns.index.intersection(factors.index)
    print(f"dates: returns {len(returns)}, factors {len(factors)}, shared {len(common)}")
    returns, prices, factors = returns.loc[common], prices.loc[common], factors.loc[common]

    sector = {t: s for s, ts in UNIVERSE.items() for t in ts.split()} | {"SPY": "Benchmark"}
    universe = pd.DataFrame({"ticker": tickers, "name": [NAMES[t] for t in tickers], "sector": [sector[t] for t in tickers]})

    OUT.mkdir(parents=True, exist_ok=True)
    prices.to_csv(OUT / "prices.csv")
    returns.to_csv(OUT / "returns.csv")
    factors.to_csv(OUT / "ff_factors_daily.csv")
    universe.to_csv(OUT / "universe.csv", index=False)

    spy_total = (1 + returns["SPY"]).prod() - 1
    corr = (returns["SPY"] - factors["RF"]).corr(factors["Mkt_RF"])
    big = returns["SPY"].abs().nlargest(5)
    big_txt = "\n".join(f"  - {d.date()}: {returns['SPY'][d]:+.2%}" for d in big.index)
    assert 2400 <= len(returns) <= 2600, len(returns)
    assert corr > 0.98, corr
    assert any(d.year == 2020 and d.month == 3 for d in big.index)
    manifest = f"""# Markets data manifest

- Sources: yfinance adjusted close (auto_adjust=True); Ken French Data Library daily 3 factors ({FF_URL})
- Window: {START} to 2025-12-31 (yfinance end exclusive); run date {dt.date.today()}
- Tickers: {len(tickers) - 1} stocks (6 per GICS sector, current classification) + SPY
- Files: prices.csv {prices.shape}, returns.csv {returns.shape}, ff_factors_daily.csv {factors.shape}, universe.csv {universe.shape}
- Dates inner-joined between yfinance and French; factors converted from percent to decimals
- SPY total return over window: {spy_total:.1%}
- Mean daily RF: {factors['RF'].mean():.6f}
- Corr(SPY excess return, Mkt_RF): {corr:.4f}
- 5 largest absolute daily SPY moves:
{big_txt}
"""
    (OUT / "MANIFEST.md").write_text(manifest, encoding="utf-8")
    print(manifest)
    print("All assertions passed.")


if __name__ == "__main__":
    main()
