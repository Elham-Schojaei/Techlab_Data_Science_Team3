# METHODOLOGY

## Dataset Overview

The dataset contains a collection of images along with:
- image metadata
- engagement metrics
- visual features extracted directly from the images

Main variables used in the analysis:

Variable:	    Description
likes:	        Number of likes received by the image (engagement proxy)
brightness:     Average brightness level of the image
sharpness:      Measure of image clarity/detail
width:	        Image width in pixels
height:	        Image height in pixels
aspect_ratio:   Ratio between width and height
orientation:	Image format: portrait, landscape, or square


## Data Preparation

Before starting the analysis, several preprocessing steps were performed.

#### Initial Data Inspection

The dataset was inspected to verify:
- dataset size
- variable types
- missing values
- general data consistency

Basic descriptive statistics were computed to understand the structure of the data.

#### Engagement Distribution Analysis

The distribution of the engagement variable (likes) was analyzed.

Results showed a highly right-skewed distribution, meaning:
- most images receive relatively few likes
- a small number of images receive very high engagement

This pattern is common in social media datasets and reflects a long-tail distribution of attention.

#### Log Transformation of Engagement

To reduce the influence of extreme values and make the data more suitable for statistical analysis, a log transformation was applied:

log_likes = log(1 + likes)

This transformation helps:
- reduce skewness
- stabilize variance
- improve interpretability in later analyses.

All subsequent analyses use log_likes instead of raw likes.

## Visual Feature Exploration

After preparing the engagement variable, we explored the visual characteristics of the images.

Feature distributions analyzed:
- brightness
- sharpness
- image width
- image height

These analyses helped understand the range and variability of the visual properties present in the dataset.

#### Derived Features

Two additional features were created to better describe image structure.

1. Aspect Ratio: aspect_ratio = width / height

This variable captures the shape of the image.

2. Image Orientation
Images were categorized into three formats:
- portrait → height > width
- landscape → width > height
- square → width = height

This classification helps analyze whether certain image formats perform better in terms of engagement.

## Relationship Between Visual Features and Engagement

To investigate how visual characteristics relate to engagement, several analyses were performed.

1. Brightness vs Engagement

A scatter plot was used to explore the relationship between brightness and engagement.

Findings:
- No strong relationship was observed.
- Images with different brightness levels show similar engagement patterns.
- Correlation with log_likes is relatively weak (≈ 0.19).

This suggests that brightness alone is not a strong driver of engagement.

2. Sharpness vs Engagement

A similar analysis was conducted for image sharpness.

Findings:
- No clear relationship between sharpness and engagement.
- Correlation with engagement is close to zero.
- This indicates that image clarity alone does not significantly influence engagement levels.

3. Image Orientation and Engagement

Engagement distributions were compared across image formats using boxplots.

Findings:
- Portrait images show slightly higher median engagement.
- Landscape images have slightly lower engagement on average.
- Square images are underrepresented in the dataset.

This result suggests that vertical image formats may attract slightly more user attention, possibly because they occupy more screen space in social media feeds.

#### Correlation Analysis

A correlation matrix was computed to examine relationships between all numerical variables.

Key observations:
- Weak correlation between brightness and engagement
- No meaningful correlation between sharpness and engagement
- Expected correlations between width, height, and aspect ratio due to their mathematical relationships
- Overall, the visual features analyzed so far explain only a limited portion of engagement variability.

