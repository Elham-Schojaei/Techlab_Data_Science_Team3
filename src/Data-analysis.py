
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


## Data Visualisation
sns.set_theme(style="whitegrid")


## Load Dataset
data = pd.read_csv("data/processed/final_dataset.csv")


##  First Inspection
print(data.head())
print("\nShape:", data.shape)
print("\nColumns:")
print(data.columns)
print("\nInfo:")
print(data.info())
print("\nMissing values:")
print(data.isna().sum())


## First Engagement Analysis (likes)
print("\nSummary statistics for likes:")
print(data["likes"].describe())

# Engagement Distribution Visualization
plt.figure(figsize=(8,5))
sns.histplot(data["likes"], bins=40, kde=True)
plt.title("Distribution of Likes")
plt.xlabel("Likes")
plt.ylabel("Frequency")
plt.show()


# Adjustment to the log transformation
data["log_likes"] = np.log1p(data["likes"])

# Adjust Distribution Visualization
plt.figure(figsize=(8,5))
sns.histplot(data["log_likes"], bins=40, kde=True)
plt.title("Distribution of Log(Likes)")
plt.xlabel("Log Likes")
plt.ylabel("Frequency")
plt.show()



## Features Analysis
features = ["brightness", "sharpness", "width", "height"]
print(data[features].describe())


# Brightness Distribution
plt.figure(figsize=(8,5))
sns.histplot(data["brightness"], bins=40, kde=True)

plt.title("Brightness Distribution")
plt.xlabel("Brightness")
plt.ylabel("Frequency")

plt.show()

# Sharpness Distribution
plt.figure(figsize=(8,5))
sns.histplot(data["sharpness"], bins=40, kde=True)

plt.title("Sharpness Distribution")
plt.xlabel("Sharpness")
plt.ylabel("Frequency")

plt.show()

# Dimensions Distribution
fig, axes = plt.subplots(1,2, figsize=(12,5))

sns.histplot(data["width"], bins=40, ax=axes[0])
axes[0].set_title("Image Width Distribution")

sns.histplot(data["height"], bins=40, ax=axes[1])
axes[1].set_title("Image Height Distribution")

plt.show()


# Aspect Ratio Analysis
data["aspect_ratio"] = data["width"] / data["height"]


# New Variable (Orientation)
data["orientation"] = np.where(
    data["height"] > data["width"],
    "portrait",
    np.where(data["width"] > data["height"], "landscape", "square")
)

# Orientation Distribution
print(data["orientation"].value_counts())