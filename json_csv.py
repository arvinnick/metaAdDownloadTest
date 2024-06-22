#### JSON to CSV
import json
import os

import pandas as pd

output_folder = os.path.join(os.getcwd(), "output")
csv_output = os.path.join(output_folder, "ads_download.csv")
df = None
if not os.path.exists(csv_output):
    os.system("touch {}".format(csv_output))
for root, dirs, json_files in os.walk(output_folder, 2):
    for json_file in json_files:
        if json_file.endswith(".json"):
            json_data = json.load(open(os.path.join(root, json_file)))
            if df is None:
                df = pd.DataFrame.from_dict(json_data["data"])
            else:
                df = pd.concat([df, pd.DataFrame.from_dict(json_data["data"])])

df.to_csv(csv_output)