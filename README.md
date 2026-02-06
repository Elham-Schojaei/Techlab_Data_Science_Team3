# Techlab_Data_Science_Team3
Research topic: WHAT MAKES AN IMAGE POPULAR?
Project Overview

Business Problem
Companies invest heavily in visual content for:
- social media
- advertising
- e-commerce

However, content performance is often driven by intuition rather than data.

Our Solution
We built a data-driven framework that:
- analyzes large-scale image data
- extracts measurable visual features
- links image characteristics to user engagement

The result is a decision-support tool that helps companies understand what makes images perform better.

Concrete Business Value
Our approach allows clients to:
- Optimize content creation
→ choose image styles that increase engagement
- Improve marketing performance
→ higher likes, comments, and reach
- Reduce trial-and-error costs
→ fewer campaigns based only on guesswork
- Scale content decisions
→ apply insights across platforms and campaigns

Example Use Cases
Social Media Teams
→ decide which images to post and when
Marketing & Advertising Agencies
→ test visual strategies before launching campaigns
E-commerce Platforms
→ optimize product images to increase interaction
Content Creators & Brands
→ understand which visual elements attract audiences

---

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
