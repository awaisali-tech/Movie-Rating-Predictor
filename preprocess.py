import json
import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "movies.json")

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# If data is a list:
if isinstance(data, list):
    df = pd.DataFrame(data)
elif isinstance(data, dict) and "results" in data:
    df = pd.DataFrame(data["results"])
else:
    raise ValueError("Unexpected JSON structure")

# ✅ Clean columns:
# Convert lists (genres, posters, etc.) into comma-separated strings
for col in df.columns:
    if df[col].apply(lambda x: isinstance(x, list)).any():
        df[col] = df[col].apply(
            lambda x: x[0] if isinstance(x, list) and len(x) == 1 
            else ", ".join(map(str, x)) if isinstance(x, list) 
            else x
        )
output_path = os.path.join(BASE_DIR, "movies_clean.csv")
df.to_csv(output_path, index=False, encoding="utf-8")
print(f"✅ Clean CSV saved to {output_path}")





