import os
import pandas as pd
import requests

OUT_DIR = "data/images"
os.makedirs(OUT_DIR, exist_ok=True)

def main():
    meta = pd.read_csv("data/metadata.csv")

    for i, row in meta.iterrows():
        img_id = row["id"]
        url = row["image_url"]

        out_path = os.path.join(OUT_DIR, f"{img_id}.jpg")
        if os.path.exists(out_path):
            continue

        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            with open(out_path, "wb") as f:
                f.write(r.content)
            print("Saved", out_path)
        except Exception as e:
            print("Skipped", img_id, e)

if __name__ == "__main__":
    main()
