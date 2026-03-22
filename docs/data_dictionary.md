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

#### Color Analysis

To extend the analysis beyond basic technical image properties, we also examined the role of dominant color.

The dataset includes a color variable representing the main color associated with each image. To make this feature easier to interpret, dominant colors were grouped into broader categories such as:

blue
white
gray
red
black
green
other

This allowed us to compare engagement levels across different color groups.

Dominant Color and Engagement

The analysis suggests that dominant color is associated with differences in engagement.

Key findings:

- Blue and white dominant images show the highest average engagement.
- Gray and red images show intermediate performance.
- Green dominant images display the lowest engagement values on average.

This result suggests that color may be more informative than some basic technical features such as brightness or sharpness.

From a business perspective, this is relevant because color is directly linked to:

- visual attention
- emotional response
- perceived aesthetic quality
- brand communication

These findings indicate that color palette may play an important role in visual performance, and that certain dominant tones may be more effective in attracting user interaction.

However, this relationship should be interpreted as associative rather than causal, since engagement is likely influenced by several additional factors, including image content and context.

#### Time Analysis

A time-based analysis was also conducted to explore whether engagement changes over time and whether there are temporal patterns that may help explain performance differences.

The created_at variable was converted into a datetime format, allowing the extraction of temporal features such as:

- year
- month
- posting period
- Engagement Over Time

Monthly average engagement was analyzed to identify possible trends.

The initial results suggested that engagement tends to decline over time, with earlier years showing higher and more stable average values, and more recent years displaying lower and more volatile engagement.

However, a second analysis on the number of images per month showed that the dataset becomes much smaller in later periods. In particular:

- the years between 2016 and 2018 contain the largest concentration of images
- later years include far fewer monthly observations
- months with very few images produce unstable average engagement values

Because of this, the temporal analysis was refined by focusing on the period 2016–2018, which provides the most reliable and representative sample for time-based exploration.

Main Insights from Time Analysis
- Engagement is not constant over time
- Earlier periods show more stable performance
- Later periods appear more volatile, but this is partly due to the lower number of available images
- Temporal context may influence engagement, but recent fluctuations should be interpreted with caution because of limited sample size

This suggests that image performance should not be evaluated only through visual features, but also in relation to its temporal context, since broader platform dynamics, audience behavior, and dataset composition may affect results.

## Updated Key Takeaways

The exploratory analysis suggests that:

Engagement follows a long-tail distribution, common in social media datasets
- Basic visual properties such as brightness and sharpness show weak relationships with engagement
- Image orientation may have a small effect, with portrait images performing slightly better
- Dominant color appears to be more informative, with blue and white images showing higher average engagement
- Time also matters, although temporal patterns must be interpreted carefully because of uneven sample size across years

Overall, the results indicate that engagement is influenced by a combination of factors, and that simple technical image features alone are not enough to fully explain performance.

