import pandas as pd

wine_df = pd.read_csv("data/winemag-data-130k-v2.csv")
wine_df_copy = wine_df

wine_df_copy["count"] = 1

country_stats = (
    wine_df_copy.groupby("country")
    .agg({"count": "sum", "points": "mean"})
    .reset_index()
)
country_stats["points"] = country_stats["points"].round(1)
country_stats = country_stats.sort_values(by="count", ascending=False)

country_stats.to_csv("data/reviews-per-country.csv", index=False)
