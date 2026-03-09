# WHAT MAKES AN IMAGE POPULAR?


## Project Overview

### Why this project exists:  

Brands spend a lot of time and money creating images for social media, ads, and e-commerce — but choosing “the right” visuals is often based on gut feeling.

We wanted to change that.


### What we built: 

A data-driven framework that turns images into measurable data:

✅ Collects large-scale image content
✅ Extracts visual features 
✅ Connects those features to engagement signals 

In short: we help teams understand what makes an image perform better — and why.


### What you get (business value)

This project helps companies and creators:

✅Create stronger content
Choose visual styles that consistently drive engagement.

✅Boost marketing results
Improve reach, interaction, and campaign performance.

✅Reduce trial-and-error
Spend less budget on “guessing” what works.

✅Scale decisions with confidence
Apply insights across platforms, audiences, and campaigns.


## Who it’s for

✅Social Media Teams
Decide which images to post (and learn what your audience reacts to).

✅Marketing & Advertising Agencies
Test visual strategies before launching big campaigns.

✅E-commerce Platforms
Improve product imagery to increase interaction and interest.

✅Brands & Content Creators
Learn which visual elements attract attention — and repeat success.

---

This project builds a complete data-science pipeline to explore how visual properties of images can be turned into measurable data for analysis.


## Data source

We use the Unsplash API to collect:

- image metadata (IDs, descriptions, tags, etc.)
- image URLs for downloading the photos


## What the pipeline does

Our workflow runs in clear steps:

- Collect metadata from Unsplash
Fetches image metadata using the API and saves it as a structured CSV.

- Download the images
Uses the image URLs to download and store the photos locally.

- Extract visual features from images
Computes simple but meaningful features such as:

brightness (how light/dark an image is)

sharpness (how detailed/clear an image is)

- Merge everything into one dataset
Combines metadata + extracted features into one clean final table.



## 📁 Project Structure

### `src/`
Python source code for the pipeline:

- data collection (Unsplash metadata)

- image downloading

- feature extraction (e.g., brightness, sharpness)

- merging / dataset creation

---

### `notebooks/`
Jupyter notebooks for exploration, visualization, and experiments (EDA, prototyping, model testing).

---

### `data/raw/`
- Raw data collected from Unsplash (untouched):

metadata.csv (image IDs + URLs + basic metadata)
---

### `data/processed/`
Cleaned and merged datasets ready for analysis and modeling (features, final dataset).

---

### `data/sample/`
Small sample of data and images used for quick testing and demonstration

---

### `reports/figures/`
Generated plots, charts, and visual outputs used in reports and presentations.

---

### `docs/`
Project documentation (data dictionary, methodology notes, ethics statement, etc.).
