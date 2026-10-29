# Markets data manifest

- Sources: yfinance adjusted close (auto_adjust=True); Ken French Data Library daily 3 factors (https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip)
- Window: 2016-01-01 to 2025-12-31 (yfinance end exclusive); run date 2026-10-29
- Tickers: 66 stocks (6 per GICS sector, current classification) + SPY
- Files: prices.csv (2513, 67), returns.csv (2513, 67), ff_factors_daily.csv (2513, 4), universe.csv (67, 3)
- Dates inner-joined between yfinance and French; factors converted from percent to decimals
- SPY total return over window: 300.3%
- Mean daily RF: 0.000087
- Corr(SPY excess return, Mkt_RF): 0.9948
- 5 largest absolute daily SPY moves:
  - 2020-03-16: -10.94%
  - 2025-04-09: +10.50%
  - 2020-03-12: -9.57%
  - 2020-03-24: +9.06%
  - 2020-03-13: +8.55%
