import os
import pandas as pd

path = os.path.join(os.path.curdir, "output", "test2", "ads_data", "test2_processed_data.xlsx")
df = pd.read_excel(path)
df = df.drop(df.loc[df["languages"].isna()].index)
df = df.loc[df["languages"].str.contains("en")]
df = df.drop(df.loc[df["target_locations"].isna()].index)
df = df.loc[df["target_locations"].str.contains("Germany")]
df["ad_delivery_start_time"] = pd.to_datetime(df["ad_delivery_start_time"])
df = df.sort_values(by="ad_delivery_start_time", ascending=False)
df = df.loc[df["ad_delivery_start_time"] >= pd.to_datetime('2024-06-01')]
df.to_excel(os.path.join(os.path.curdir, "output", "test2", "ads_data", "filtered_data.xlsx"))




