# WHAT MAKES AN IMAGE POPULAR?

## Project Overview

### Why this project exists

Brands invest a lot of time and money in creating images for social media, advertising, and e-commerce. However, choosing “the right” visuals is often based on gut feeling.

This project aims to make that process more data-driven.


### What we built

We developed a data-science pipeline that transforms images into measurable data by:

- collecting large-scale image content
- extracting visual features
- connecting those features to engagement signals

In short, the project helps explore what makes an image perform better and why.


### Business value

This project can help companies and creators:

- **Create stronger content**  
  Identify visual styles that are more likely to drive engagement.

- **Improve marketing performance**  
  Support better reach, interaction, and campaign results.

- **Reduce trial-and-error**  
  Make fewer decisions based only on guesswork.

- **Scale decisions with confidence**  
  Apply insights across platforms, audiences, and campaigns.

---

## Who it’s for

- **Social Media Teams**  
  To decide which images to post and better understand audience preferences.

- **Marketing and Advertising Agencies**  
  To test visual strategies before launching larger campaigns.

- **E-commerce Platforms**  
  To improve product imagery and increase interaction.

- **Brands and Content Creators**  
  To identify visual elements that attract attention and repeat successful patterns.

---

## Project Goal

This project builds a complete data-science pipeline to investigate how visual properties of images can be transformed into measurable features and analyzed in relation to engagement.

The main question is:

**Can low-level visual features such as brightness, sharpness, width, height, and aspect ratio help explain image popularity?**

---

## Data Source

We use the **Unsplash API** to collect:

- image metadata
- image URLs
- descriptive information associated with each image

---

## What the Pipeline Does

The workflow is organized into several steps:

### 1. Collect metadata from Unsplash
Fetches image metadata using the API and saves it in a structured CSV file.

### 2. Download images
Uses the image URLs to download and store the photos locally.

### 3. Extract visual features
Computes simple but meaningful image features such as:

- **brightness** — how light or dark an image is
- **sharpness** — how clear or detailed an image is

### 4. Merge everything into one dataset
Combines metadata and extracted features into one final dataset for analysis and modeling.

---

## Machine Learning Summary

To investigate whether visual properties can predict popularity, we tested several regression-based machine learning models using the number of `likes` as the target variable.

### Features used

The main features tested were:

- brightness
- sharpness
- width
- height
- aspect ratio

### Models tested

We explored:

- **Simple Linear Regression**
- **Multiple Linear Regression**
- **Polynomial Regression (single feature)**
- **Polynomial Regression (two features)**

### Main finding

Overall, the machine learning results showed that the tested visual features had **weak predictive power**.

The best-performing model was:

- **Polynomial Regression using aspect ratio and sharpness**
- **R² = 0.0778**
- **MAE = 1606.09**
- **RMSE = 2168.56**

Although this was the strongest result among the tested models, it still explained only a small portion of the variation in likes.

### Interpretation

This suggests that low-level image properties alone are **not enough** to explain or predict image popularity well.

Image engagement is likely influenced much more strongly by other factors, such as:

- Image content
- Subject matter
- Composition
- Posting context
- User popularity
- Captions or metadata not included in the model

### Conclusion of the ML part

The project shows that simple visual features can be measured and modeled, but they do not appear to be strong standalone predictors of popularity in this dataset.

---

## Key Insight

This project is valuable not because it “solved” popularity prediction, but because it built a full end-to-end pipeline and showed the limits of using only basic image features for engagement prediction.

That insight is important: to better understand popularity, future work should combine low-level image features with richer semantic and contextual information.

---

## Project Structure

### `src/`
Python source code for the pipeline, including:

- Data collection from Unsplash
- Image downloading
- Feature extraction
- Dataset creation and merging
- Machine learning scripts
- Exploratory data analysis

### `data/raw/`
Raw collected data from Unsplash.

### `data/processed/`
Cleaned and merged datasets ready for analysis and modeling.

### `data/sample/`
Example images

### `reports/`
Ml reports

### `reports/figures/`
visual outputs used in reports.

### `docs/`
METHODOLOGY for Exploratory data analysis

### `notebooks/`
Exploratory data analysis notebook

---
## How to use our codes: 

You can start by generating the dataset yourself using `01_get_metadata.py` in `src/collect/`.  
After that, extract the visual features and merge the data using `02_extract_features.py` and `03_merge.py` in `src/features/`.

For the analysis part, you can run the EDA code in `src/Exploratory Data Analysis/`.  
For the machine learning part, you can run the regression models in `src/Machine Learning/`.

---
## Future Improvements

Possible next steps for improving the project include:

- Adding semantic image features
- Using image content classification
- Including text-based metadata
- Exploring deep learning approaches
- Analyzing user- and platform-level context

---

## Final Note

This project demonstrates a complete data-science workflow from data collection to feature engineering, exploratory analysis, and machine learning.

It provides a solid foundation for future work on understanding what makes an image popular.