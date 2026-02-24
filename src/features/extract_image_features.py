import os
import cv2
import numpy as np
import pandas as pd
from tqdm import tqdm  # For progress bar visualization

IMAGE_DIR = "data/sample/sample_images"
OUTPUT_CSV = "data/processed/features.csv"


def extract_features(image_path):
    """
    Extract visual features from a single image.
    Returns a dictionary with numerical values.
    """
    img = cv2.imread(image_path)

    if img is None:
        return None

    # Convert to grayscale and calculate average brightness
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    brightness = gray.mean()

    # Sharpness using variance of the Laplacian
    sharpness = cv2.Laplacian(gray, cv2.CV_64F).var()

    # Colorfulness using color channel differences
    b, g, r = cv2.split(img)
    colorfulness = np.std(r - g) + np.std(r - b)

    return {
        "brightness": brightness,
        "sharpness": sharpness,
        "colorfulness": colorfulness
    }


def main():
    rows = []

    image_files = os.listdir(IMAGE_DIR)

    for image_name in tqdm(image_files):
        image_path = os.path.join(IMAGE_DIR, image_name)

        features = extract_features(image_path)

        if features is None:
            continue

        post_id = image_name.replace(".jpg", "")
        features["post_id"] = post_id
        rows.append(features)

    df = pd.DataFrame(rows)
    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
    df.to_csv(OUTPUT_CSV, index=False)

    print(f"Saved features to {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
