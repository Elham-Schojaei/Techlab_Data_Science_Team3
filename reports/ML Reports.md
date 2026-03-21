# Machine Learning Findings

## Goal

The goal of the machine learning analysis was to investigate whether the number of `likes` can be explained or predicted using image-related features such as:

- brightness
- sharpness
- width
- height
- aspect ratio

We tested several regression-based models to explore both linear and non-linear relationships between these features and the number of likes.

---

## Exploratory Data Analysis (EDA)

The dataset contains **1006 images** and the following relevant columns:

- `width`
- `height`
- `likes`
- `brightness`
- `sharpness`

An additional feature, **aspect ratio**, was created as:

```python
aspect_ratio = width / height

## Summary Statistics

- **Mean width:** 4482.39  
- **Mean height:** 3919.87  
- **Mean likes:** 2498.76  
- **Mean brightness:** 108.80  
- **Mean sharpness:** 876.36  

The number of likes had a wide spread:

- **Minimum likes:** 0  
- **Maximum likes:** 19493  

This large range already suggested that predicting likes from only a few low-level image features might be difficult.

Scatter plots of the variables against `likes` did not show strong or clear trends. The points were highly scattered, which suggested weak linear relationships and possible non-linear behavior, although no strong pattern was visually obvious.

---

## Models Tested

The following models were tested:

### 1. Simple Linear Regression
- brightness → likes  
- sharpness → likes  
- width → likes  
- height → likes  
- aspect ratio → likes  

### 2. Multiple Linear Regression
- brightness + sharpness → likes  
- width + sharpness → likes  
- width + brightness → likes  
- height + sharpness → likes  
- height + brightness → likes  
- aspect ratio + sharpness → likes  
- aspect ratio + brightness → likes  

### 3. Polynomial Regression (Single Feature)
- brightness  
- sharpness  
- width  
- height  
- aspect ratio  

### 4. Polynomial Regression (Two Features)
- brightness + sharpness  
- height + brightness  
- width + brightness  
- height + sharpness  
- width + sharpness  
- width + height  
- aspect ratio + brightness  
- aspect ratio + sharpness  

---

## Evaluation Metrics

The models were evaluated using:

- **R² Score**
- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**

R² was the main metric used to compare how much variation in likes could be explained by each model.

---

## Results

### 1. Simple Linear Regression

| Model | R² | MAE | RMSE |
|---|---:|---:|---:|
| Brightness → Likes | 0.0111 | 1809.66 | 2756.91 |
| Sharpness → Likes | -0.0021 | 1818.79 | 2775.22 |
| Width → Likes | 0.0006 | 1801.73 | 2771.52 |
| Height → Likes | 0.0064 | 1829.17 | 2763.48 |
| Aspect Ratio → Likes | 0.0176 | 1819.69 | 2747.90 |

#### Interpretation

All simple linear regression models performed poorly. The best simple linear model was **Aspect Ratio → Likes**, but its **R² = 0.0176**, which means it explained only about **1.76%** of the variation in likes.

This suggests that none of the individual features had a strong linear relationship with likes.

---

### 2. Multiple Linear Regression

| Model | R² | MAE | RMSE |
|---|---:|---:|---:|
| Brightness + Sharpness | -0.0231 | 1608.43 | 2197.83 |
| Width + Sharpness | -0.0385 | 1604.06 | 2214.30 |
| Width + Brightness | -0.0523 | 1630.64 | 2229.02 |
| Height + Sharpness | -0.0009 | 1574.85 | 2173.83 |
| Height + Brightness | -0.0078 | 1582.11 | 2181.38 |
| Aspect Ratio + Sharpness | -0.0266 | 1592.17 | 2201.55 |
| Aspect Ratio + Brightness | -0.0380 | 1606.47 | 2213.75 |

#### Interpretation

The multiple linear regression models did not improve the predictive power in terms of R². Most of them produced negative R² values, which means they performed worse than simply predicting the average number of likes.

Although some combinations produced slightly lower MAE and RMSE, the explanatory power remained extremely weak.

---

### 3. Polynomial Regression (Single Feature)

| Model | R² | MAE | RMSE |
|---|---:|---:|---:|
| Brightness | 0.0092 | 1941.76 | 2852.47 |
| Sharpness | -0.0157 | 1969.49 | 2888.07 |
| Width | 0.0034 | 1939.85 | 2860.78 |
| Height | 0.0004 | 1933.83 | 2865.10 |
| Aspect Ratio | -0.0058 | 1960.47 | 2873.91 |

#### Interpretation

Single-feature polynomial regression also did not provide meaningful improvement. Adding quadratic terms to one feature at a time was not enough to explain likes.

---

### 4. Polynomial Regression (Two Features)

| Model | R² | MAE | RMSE |
|---|---:|---:|---:|
| Brightness + Sharpness | 0.0117 | 1661.02 | 2244.90 |
| Height + Brightness | -0.0144 | 1677.97 | 2274.38 |
| Width + Brightness | -0.0080 | 1669.48 | 2267.16 |
| Height + Sharpness | 0.0521 | 1607.95 | 2198.58 |
| Width + Sharpness | 0.0590 | 1620.18 | 2190.51 |
| Width + Height | 0.0200 | 1651.89 | 2235.47 |
| Aspect Ratio + Brightness | 0.0185 | 1651.91 | 2237.21 |
| Aspect Ratio + Sharpness | 0.0778 | 1606.09 | 2168.56 |

#### Interpretation

Among all tested models, the best result was obtained from the two-feature polynomial regression using **Aspect Ratio and Sharpness**, with:

- **R² = 0.0778**
- **MAE = 1606.09**
- **RMSE = 2168.56**

This means the model explained about **7.78%** of the variation in likes.

Although this was the best model in the experiment, the result is still weak overall. Even the best model captured only a small part of the variation in likes.

---

## Best Model

The best-performing model in this analysis was:

### Polynomial Regression using Aspect Ratio and Sharpness

**Performance:**

- **R² = 0.0778**
- **MAE = 1606.09**
- **MSE = 4702654.12**
- **RMSE = 2168.56**

This model performed better than all simple linear, multiple linear, and single-feature polynomial models, but the performance is still limited.

---

## Overall Conclusion

The machine learning analysis did **not** find strong predictive relationships between likes and the tested image features.

### Main Findings
- None of the simple linear regression models showed meaningful predictive power.
- Most multiple linear regression models performed poorly and often had negative R² values.
- Single-feature polynomial regression did not improve the results.
- Two-feature polynomial regression performed slightly better, especially for **aspect ratio + sharpness**, but the improvement was still limited.

### Final Interpretation

The data shows no strong or clear trends between the tested low-level image properties and the number of likes.

This suggests that:

- likes are likely influenced by many other factors not included in the dataset
- low-level visual features such as brightness, sharpness, width, height, and aspect ratio alone are not sufficient to predict popularity well

Possible missing factors may include:

- image content
- subject matter
- composition
- color semantics
- posting context
- user popularity
- captions or metadata not included in the model

---

## Summary

In summary, several regression models were tested to predict likes from image features. While the best result came from a two-feature polynomial regression model using **aspect ratio and sharpness**, overall performance remained weak. Therefore, the current dataset does not provide strong evidence that these visual features alone can explain or predict the number of likes effectively.