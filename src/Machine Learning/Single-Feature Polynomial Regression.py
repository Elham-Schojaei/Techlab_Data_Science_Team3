import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

# Load the dataset
import requests
url = "https://raw.githubusercontent.com/Elham-Schojaei/Techlab_Data_Science_Team3/d349ebcddfa64b667b9113a5348ce1771ab33bc9/data/processed/final_dataset.csv"

response = requests.get(url)
response.raise_for_status()

with open("final_dataset.csv", "wb") as f:
    f.write(response.content)

# Load the dataset into a DataFrame and perform basic exploratory data analysis
print("\nBasic Exploratory Data Analysis: \n")
df = pd.read_csv("final_dataset.csv")

print(df.head())
print(df.columns)
print(df.describe())

df["aspect_ratio"] = df["width"] / df["height"]

viz = df[['likes', 'brightness', 'sharpness', 'width', 'height', 'aspect_ratio']]
viz.hist()
plt.show()

plt.scatter(df["brightness"], df["likes"], color="blue")
plt.xlabel("brightness")
plt.ylabel("likes")
plt.show()

plt.scatter(df["sharpness"], df["likes"], color="blue")
plt.xlabel("sharpness")
plt.ylabel("likes")
plt.show()

plt.scatter(df["width"], df["likes"], color="blue")
plt.xlabel("width") 
plt.ylabel("likes")
plt.show()  

plt.scatter(df["height"], df["likes"], color="blue")
plt.xlabel("height")        
plt.ylabel("likes")
plt.show()


plt.scatter(df["aspect_ratio"], df["likes"])
plt.xlabel("Aspect Ratio")
plt.ylabel("Likes")
plt.title("Aspect Ratio vs Likes")
plt.show()


# Creating a train and test dataset
cdf = df[['likes', 'brightness', 'sharpness', 'width', 'height', 'aspect_ratio']]

msk = np.random.rand(len(cdf)) < 0.8
train = cdf[msk]
test = cdf[~msk]


# scatter plot for train and test data on brightness and likes
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(train.brightness, train.likes, color='blue', label="Train")

ax1.scatter(test.brightness, test.likes, color='red', label="Test")

plt.xlabel("brightness")
plt.ylabel("likes")
plt.legend()
plt.show()

# scatter plot for train and test data on sharpness and likes
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(train.sharpness, train.likes, color='blue', label="Train")

ax1.scatter(test.sharpness, test.likes, color='red', label="Test")

plt.xlabel("sharpness")
plt.ylabel("likes")
plt.legend()
plt.show()


# Single-feature polynomial regression:

from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Polynomial regression model for brightness and likes
# Polynomial Regression Model for Brightness
print("\n \n \nPolynomial Regression Model for Brightness:")

train_x = np.asanyarray(train[['brightness']])
train_y = np.asanyarray(train[['likes']])

test_x = np.asanyarray(test[['brightness']])
test_y = np.asanyarray(test[['likes']])

poly = PolynomialFeatures(degree=2)
train_x_poly = poly.fit_transform(train_x)
test_x_poly = poly.transform(test_x)

clf = linear_model.LinearRegression()
clf.fit(train_x_poly, train_y)

test_y_pred = clf.predict(test_x_poly)

print("\nEvaluation of the model for Brightness:")
print("\nR2 Score: ", r2_score(test_y, test_y_pred))
print("\nMean Absolute Error: ", mean_absolute_error(test_y, test_y_pred))
print("\nMean Squared Error: ", mean_squared_error(test_y, test_y_pred))
print("\nRoot Mean Squared Error: ", np.sqrt(mean_squared_error(test_y, test_y_pred)))



# Polynomial Regression Model for Sharpness
print("\n\n \n Polynomial Regression Model for Sharpness:")

train_x = np.asanyarray(train[['sharpness']])
train_y = np.asanyarray(train[['likes']])

test_x = np.asanyarray(test[['sharpness']])
test_y = np.asanyarray(test[['likes']])

poly = PolynomialFeatures(degree=2)
train_x_poly = poly.fit_transform(train_x)
test_x_poly = poly.transform(test_x)

clf = linear_model.LinearRegression()
clf.fit(train_x_poly, train_y)

test_y_pred = clf.predict(test_x_poly)

print("\nEvaluation of the model for Sharpness:")
print("\nR2 Score: ", r2_score(test_y, test_y_pred))
print("\nMean Absolute Error: ", mean_absolute_error(test_y, test_y_pred))
print("\nMean Squared Error: ", mean_squared_error(test_y, test_y_pred))
print("\nRoot Mean Squared Error: ", np.sqrt(mean_squared_error(test_y, test_y_pred)))



# Polynomial Regression Model for Width
print("\n\n \n Polynomial Regression Model for Width:")

train_x = np.asanyarray(train[['width']])
train_y = np.asanyarray(train[['likes']])

test_x = np.asanyarray(test[['width']])
test_y = np.asanyarray(test[['likes']])

poly = PolynomialFeatures(degree=2)
train_x_poly = poly.fit_transform(train_x)
test_x_poly = poly.transform(test_x)

clf = linear_model.LinearRegression()
clf.fit(train_x_poly, train_y)

test_y_pred = clf.predict(test_x_poly)

print("\nEvaluation of the model for Width:")
print("\nR2 Score: ", r2_score(test_y, test_y_pred))
print("\nMean Absolute Error: ", mean_absolute_error(test_y, test_y_pred))
print("\nMean Squared Error: ", mean_squared_error(test_y, test_y_pred))
print("\nRoot Mean Squared Error: ", np.sqrt(mean_squared_error(test_y, test_y_pred)))



# Polynomial Regression Model for Height
print("\n\n \n Polynomial Regression Model for Height:")

train_x = np.asanyarray(train[['height']])
train_y = np.asanyarray(train[['likes']])

test_x = np.asanyarray(test[['height']])
test_y = np.asanyarray(test[['likes']])

poly = PolynomialFeatures(degree=2)
train_x_poly = poly.fit_transform(train_x)
test_x_poly = poly.transform(test_x)

clf = linear_model.LinearRegression()
clf.fit(train_x_poly, train_y)

test_y_pred = clf.predict(test_x_poly)

print("\nEvaluation of the model for Height:")
print("\nR2 Score: ", r2_score(test_y, test_y_pred))
print("\nMean Absolute Error: ", mean_absolute_error(test_y, test_y_pred))
print("\nMean Squared Error: ", mean_squared_error(test_y, test_y_pred))
print("\nRoot Mean Squared Error: ", np.sqrt(mean_squared_error(test_y, test_y_pred)))


# Polynomial Regression Model for Aspect Ratio
print("\n\n \n Polynomial Regression Model for Aspect Ratio:")

train_x = np.asanyarray(train[['aspect_ratio']])
train_y = np.asanyarray(train[['likes']])

test_x = np.asanyarray(test[['aspect_ratio']])
test_y = np.asanyarray(test[['likes']])

poly = PolynomialFeatures(degree=2)
train_x_poly = poly.fit_transform(train_x)
test_x_poly = poly.transform(test_x)

clf = linear_model.LinearRegression()
clf.fit(train_x_poly, train_y)

test_y_pred = clf.predict(test_x_poly)

print("\nEvaluation of the model for Aspect Ratio:")
print("\nR2 Score: ", r2_score(test_y, test_y_pred))
print("\nMean Absolute Error: ", mean_absolute_error(test_y, test_y_pred))
print("\nMean Squared Error: ", mean_squared_error(test_y, test_y_pred))
print("\nRoot Mean Squared Error: ", np.sqrt(mean_squared_error(test_y, test_y_pred)))