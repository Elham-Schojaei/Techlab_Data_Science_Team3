# %%
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

# %%
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

# %%
# Adjustment to the log transformation
data["log_likes"] = np.log1p(data["likes"])

# Adjust Distribution Visualization
plt.figure(figsize=(8,5))
sns.histplot(data["log_likes"], bins=40, kde=True)
plt.title("Distribution of Log(Likes)")
plt.xlabel("Log Likes")
plt.ylabel("Frequency")
plt.show()

# %%
