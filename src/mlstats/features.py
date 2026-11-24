"""Graduated feature engineering.

Rule (see CLAUDE.md): only features the user has already written by hand in a
notebook live here, copied as the user wrote them. Later notebooks call these
in setup and add new features on top.
"""
import numpy as np
import pandas as pd

ADDONS = ["OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies"]


def add_churn_features(df):
    """Notebook 13's features: addon_count, tenure_band, charge_drift. Returns a copy."""
    out = df.copy()
    # Addon Count
    out["addon_count"] = (out[ADDONS] == "Yes").sum(axis = 1)

    # tenure band
    out["tenure_band"] = pd.cut(out["tenure"], bins = [0,12,24,48,72], labels = ["0-12", "13-24", "25-48", "49-72"], include_lowest=True)

    # drift
    out["charge_drift"] = np.where(out["tenure"] > 0, (out["MonthlyCharges"] - (out["TotalCharges"]/out["tenure"])), 0)

    return out


def add_logit_features(df):
    """Notebook 14's features: log_tenure and six 0/1 add-on flags (<addon>_yes). Returns a copy."""
    out = df.copy()
    out["log_tenure"] = np.log1p(out["tenure"])
    # 0/1 "has it" flags, built the same way in train and test
    for c in ADDONS:
        out[c + "_yes"] = (out[c] == "Yes").astype(int)
    return out
