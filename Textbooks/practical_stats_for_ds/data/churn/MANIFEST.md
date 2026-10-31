# Churn data manifest

- Source: https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv
- Fetched: 2026-10-29
- File: `telco_churn.csv` (raw, unchanged)
- Shape: 7043 rows x 21 columns
- `Churn == "Yes"`: 1869 (26.5%)
- Blank `TotalCharges`: 11, all with `tenure == 0` (the loader sets them to 0.0)
