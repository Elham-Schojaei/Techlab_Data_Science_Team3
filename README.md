# Techlab_Data_Science_Team3
Research topic: WHAT MAKES AN IMAGE POPULAR?
Project Overview

This project builds a complete data science pipeline to understand how images affect user engagement, such as likes and comments.
We use two data sources:
- Flickr, which provides a large number of images and is used as the main dataset
- Instagram, using a small dataset shared voluntarily by users, used only for validation

The project works by:
- collecting images and their engagement data
- turning visual aspects of images into numerical features
- analyzing how these features relate to engagement levels

At the end of the project, we deliver:
- a reproducible pipeline that can be run from start to finish
- a clean and structured dataset
- machine learning models that help explain engagement patterns
- clear and practical insights on what makes images more engaging
  



## 📁 Project Structure

### `src/`
Python source code for the project (data collection, feature extraction, modeling, utilities).

---

### `notebooks/`
Jupyter notebooks for exploration, visualization, and experiments (EDA, prototyping, model testing).

---

### `data/raw/`
Original, untouched data collected from sources (Flickr metadata CSV, Instagram opt-in CSV, etc.).  
⚠️ Do not modify files here.

---

### `data/processed/`
Cleaned and merged datasets ready for analysis and modeling (features, final dataset).

---

### `data/sample/`
Small sample of data and images used for quick testing and demonstration (safe to commit to GitHub).

---

### `reports/figures/`
Generated plots, charts, and visual outputs used in reports and presentations.

---

### `docs/`
Project documentation (data dictionary, methodology notes, ethics statement, etc.).
