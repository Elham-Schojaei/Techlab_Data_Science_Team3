import pandas as pd
import requests
from io import BytesIO
from PIL import Image
import numpy as np
import cv2

def compute_brightness(pil_img) -> float:
    gray = pil_img.convert("L")
    arr = np.array(gray, dtype=np.float32)
    return float(arr.mean())

def compute_sharpness(pil_img) -> float:
    gray = pil_img.convert("L")
    arr = np.array(gray, dtype=np.uint8)
    lap = cv2.Laplacian(arr, cv2.CV_64F)
    return float(lap.var())

def download_image(url: str) -> Image.Image:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return Image.open(BytesIO(r.content)).convert("RGB")

def main():
    meta = pd.read_csv("data/metadata.csv")
    rows = []

    for _, row in meta.iterrows():
        img_id = row["id"]
        url = row["image_url"]

        try:
            img = download_image(url)
            rows.append({
                "id": img_id,
                "brightness": compute_brightness(img),
                "sharpness": compute_sharpness(img),
            })
        except Exception as e:
            print("Skipped", img_id, "because", e)

    feats = pd.DataFrame(rows)
    feats.to_csv("data/features.csv", index=False)
    print("Saved data/features.csv", feats.shape)

if __name__ == "__main__":
    main()
