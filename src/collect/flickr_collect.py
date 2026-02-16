import os
import time
import random
import requests
import pandas as pd
from tqdm import tqdm
from PIL import Image
from io import BytesIO


SEARCH_TAGS = ["travel", "portrait", "food"]  # tags to query
IMAGES_TARGET = 300  # how many images to download locally (can increase later)
SAMPLE_SIZE = 30     # how many sample images to commit to GitHub
SLEEP_SECONDS = 1.0  # politeness delay between requests

RAW_CSV = "data/raw/flickr_posts_raw.csv"
SAMPLE_CSV = "data/sample/sample_posts.csv"
SAMPLE_IMG_DIR = "data/sample/sample_images"
FULL_IMG_DIR = "images/local_full"

os.makedirs(SAMPLE_IMG_DIR, exist_ok=True)
os.makedirs(FULL_IMG_DIR, exist_ok=True)

FEED_URL = "https://www.flickr.com/services/feeds/photos_public.gne"


def fetch_feed(tags):
    """Fetch Flickr public feed JSON (no API key needed)."""
    params = {
        "format": "json",
        "nojsoncallback": 1,
        "tags": ",".join(tags),
        "tagmode": "any"  # any of the tags
    }
    r = requests.get(FEED_URL, params=params, timeout=20)
    r.raise_for_status()
    return r.json()


def safe_download_image(url, out_path):
    """Download image from URL and save to out_path."""
    try:
        resp = requests.get(url, timeout=20)
        resp.raise_for_status()
        img = Image.open(BytesIO(resp.content)).convert("RGB")
        img.save(out_path, format="JPEG", quality=90)
        return True
    except Exception:
        return False


def make_id(item):
    """
    Create a stable-ish ID from the item's link.
    Example link: https://www.flickr.com/photos/{user}/{photo_id}/
    We'll extract the last numeric chunk if possible; otherwise hash-ish fallback.
    """
    link = item.get("link", "")
    parts = [p for p in link.split("/") if p]
    
    for p in reversed(parts):
        if p.isdigit():
            return p
    
    return str(abs(hash(link)))


def main():
    rows = []
    seen = set()

    print("Fetching public feed...")
    feed = fetch_feed(SEARCH_TAGS)
    items = feed.get("items", [])

    if not items:
        raise SystemExit("No items returned from feed. Try different tags.")

    print(f"Feed returned {len(items)} items. Downloading up to {IMAGES_TARGET}...")

    
    for item in tqdm(items[:IMAGES_TARGET]):
        post_id = make_id(item)
        if post_id in seen:
            continue
        seen.add(post_id)

        
        img_url = item.get("media", {}).get("m")
        if not img_url:
            continue

        title = item.get("title", "")
        tags = item.get("tags", "")
        published = item.get("published", "")
        date_taken = item.get("date_taken", "")
        author = item.get("author", "")
        link = item.get("link", "")

        
        full_path = os.path.join(FULL_IMG_DIR, f"{post_id}.jpg")
        if not os.path.exists(full_path):
            ok = safe_download_image(img_url, full_path)
            time.sleep(SLEEP_SECONDS)
            if not ok:
                continue

        rows.append({
            "post_id": post_id,
            "image_url": img_url,
            "page_url": link,
            "title": title,
            "tags": tags,
            "author": author,
            "published": published,
            "date_taken": date_taken,
            "source": "flickr_public_feed"
        })

    df = pd.DataFrame(rows).drop_duplicates(subset=["post_id"])
    if df.empty:
        raise SystemExit("No images downloaded. Try other tags.")

    os.makedirs(os.path.dirname(RAW_CSV), exist_ok=True)
    df.to_csv(RAW_CSV, index=False)
    print(f"Saved raw CSV: {RAW_CSV} ({len(df)} rows)")

    
    sample_df = df.sample(min(SAMPLE_SIZE, len(df)), random_state=42)
    os.makedirs(os.path.dirname(SAMPLE_CSV), exist_ok=True)
    sample_df.to_csv(SAMPLE_CSV, index=False)

    
    for pid in sample_df["post_id"]:
        src = os.path.join(FULL_IMG_DIR, f"{pid}.jpg")
        dst = os.path.join(SAMPLE_IMG_DIR, f"{pid}.jpg")
        if os.path.exists(src) and not os.path.exists(dst):
            Image.open(src).save(dst, format="JPEG", quality=90)

    print(f"Saved sample CSV: {SAMPLE_CSV} ({len(sample_df)} rows)")
    print(f"Saved sample images: {SAMPLE_IMG_DIR}")
    print("Done ✅")


if __name__ == "__main__":
    main()
