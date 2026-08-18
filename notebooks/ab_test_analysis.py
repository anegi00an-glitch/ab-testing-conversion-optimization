"""Independent A/B-test analysis for a simulated portfolio experiment."""

from pathlib import Path

import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "conversion_experiment_simulated.csv"


def main() -> None:
    df = pd.read_csv(DATA_PATH)

    required = {"user_id", "experiment_group", "country", "device", "channel", "converted"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    if not df["user_id"].is_unique:
        raise ValueError("Expected one row per user.")

    summary = df.groupby("experiment_group")["converted"].agg(users="count", converters="sum")
    summary["conversion_rate"] = summary["converters"] / summary["users"]

    control = summary.loc["control"]
    treatment = summary.loc["treatment"]

    z_stat, p_value = proportions_ztest(
        [treatment["converters"], control["converters"]],
        [treatment["users"], control["users"]],
    )

    absolute_lift = treatment["conversion_rate"] - control["conversion_rate"]
    relative_lift = absolute_lift / control["conversion_rate"]

    print("\nConversion summary")
    print(summary.to_string(float_format=lambda x: f"{x:.4f}"))
    print(f"\nAbsolute lift: {absolute_lift:.4%}")
    print(f"Relative lift: {relative_lift:.2%}")
    print(f"Z-statistic: {z_stat:.3f}")
    print(f"P-value: {p_value:.4f}")
    print("Decision:", "significant at 5%" if p_value < 0.05 else "insufficient evidence at 5%")


if __name__ == "__main__":
    main()
