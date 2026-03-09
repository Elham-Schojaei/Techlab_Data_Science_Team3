import requests
import pandas as pd

ACCESS_KEY = "BQHGi0xwpnlY3ngNqV19JtqQrdi99t44YFm1rterq0M"

def main():
    url = "https://api.unsplash.com/search/photos"
    headers = {"Authorization": f"Client-ID {ACCESS_KEY}"}

    all_rows = []
    page = 1
    per_page = 30
    total_wanted = 2000  # start small (50). Later you can increase to 200, 500...

    while len(all_rows) < total_wanted:
        params = {"query": "nature", "page": page, "per_page": per_page}
        r = requests.get(url, headers=headers, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()

        for p in data["results"]:
            all_rows.append({
                "id": p["id"],
                "created_at": p["created_at"],
                "width": p["width"],
                "height": p["height"],
                "likes": p["likes"],
                "color": p.get("color"),
                "alt_description": p.get("alt_description"),
                "username": p["user"]["username"],
                "image_url": p["urls"]["regular"],
            })
            if len(all_rows) >= total_wanted:
                break

        page += 1

    df = pd.DataFrame(all_rows)
    df.to_csv("data/metadata.csv", index=False)
    print("Saved data/metadata.csv", df.shape)

if __name__ == "__main__":
    main()
