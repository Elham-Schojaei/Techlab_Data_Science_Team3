import pandas as pd

meta = pd.read_csv("data/metadata.csv")
feats = pd.read_csv("data/features.csv")

final = meta.merge(feats, on="id", how="inner")
final.to_csv("data/final_dataset.csv", index=False)

print("Saved data/final_dataset.csv", final.shape)
