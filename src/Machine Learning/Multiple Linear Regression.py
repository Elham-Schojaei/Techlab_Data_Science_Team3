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

# Multiple linear Regression Model for brightness and sharpness
print("\n \n \nMultiple Linear Regression Model for Brightness and Sharpness:")
from sklearn import linear_model
regr = linear_model.LinearRegression()

train_x = np.asanyarray(train[['brightness', 'sharpness']])
train_y = np.asanyarray(train[['likes']])

regr.fit(train_x, train_y)

print("\nCoefficients: ", regr.coef_)
print("\nIntercept: ", regr.intercept_)



# Prediction on test set

test_x = np.asanyarray(test[['brightness', 'sharpness']])
test_y = np.asanyarray(test[['likes']])

test_y_pred = regr.predict(test_x)


# Evaluation of the model
print("\n Evaluation of the model for Brightness and Sharpness:")
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

print("\nR2 Score: ", r2_score(test_y, test_y_pred))
print("\nMean Absolute Error: ", mean_absolute_error(test_y, test_y_pred))
print("\nMean Squared Error: ", mean_squared_error(test_y, test_y_pred))
print("\nRoot Mean Squared Error: ", np.sqrt(mean_squared_error(test_y, test_y_pred)))



# Multiple Linear Regression Model for Width and Sharpness
print("\n\n\nMultiple Linear Regression Model for Width and Sharpness:")
from sklearn import linear_model
regr = linear_model.LinearRegression()

train_x = np.asanyarray(train[['width', 'sharpness']])
train_y = np.asanyarray(train[['likes']])

regr.fit(train_x, train_y)

print("\nCoefficients: ", regr.coef_)
print("\nIntercept: ", regr.intercept_)

# Prediction on test set
test_x = np.asanyarray(test[['width', 'sharpness']])
test_y = np.asanyarray(test[['likes']])

test_y_pred = regr.predict(test_x)

# Evaluation of the model
print("\nEvaluation of the model for Width and Sharpness:")
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

print("\nR2 Score: ", r2_score(test_y, test_y_pred))
print("\nMean Absolute Error: ", mean_absolute_error(test_y, test_y_pred))
print("\nMean Squared Error: ", mean_squared_error(test_y, test_y_pred))
print("\nRoot Mean Squared Error: ", np.sqrt(mean_squared_error(test_y, test_y_pred)))


# Multiple Linear Regression Model for Width and Brightness
print("\n\n\nMultiple Linear Regression Model for Width and Brightness:")
from sklearn import linear_model
regr = linear_model.LinearRegression()

train_x = np.asanyarray(train[['width', 'brightness']])
train_y = np.asanyarray(train[['likes']])

regr.fit(train_x, train_y)

print("\nCoefficients: ", regr.coef_)
print("\nIntercept: ", regr.intercept_)

# Prediction on test set
test_x = np.asanyarray(test[['width', 'brightness']])
test_y = np.asanyarray(test[['likes']])

test_y_pred = regr.predict(test_x)

# Evaluation of the model
print("\nEvaluation of the model for Width and Brightness:")
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

print("\nR2 Score: ", r2_score(test_y, test_y_pred))
print("\nMean Absolute Error: ", mean_absolute_error(test_y, test_y_pred))
print("\nMean Squared Error: ", mean_squared_error(test_y, test_y_pred))
print("\nRoot Mean Squared Error: ", np.sqrt(mean_squared_error(test_y, test_y_pred)))


# Multiple Linear Regression Model for height and Sharpness
print("\n\n\nMultiple Linear Regression Model for Height and Sharpness:")
from sklearn import linear_model
regr = linear_model.LinearRegression()

train_x = np.asanyarray(train[['height', 'sharpness']])
train_y = np.asanyarray(train[['likes']])

regr.fit(train_x, train_y)

print("\nCoefficients: ", regr.coef_)
print("\nIntercept: ", regr.intercept_)

# Prediction on test set
test_x = np.asanyarray(test[['height', 'sharpness']])
test_y = np.asanyarray(test[['likes']])

test_y_pred = regr.predict(test_x)

# Evaluation of the model
print("\nEvaluation of the model for Height and Sharpness:")
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

print("\nR2 Score: ", r2_score(test_y, test_y_pred))
print("\nMean Absolute Error: ", mean_absolute_error(test_y, test_y_pred))
print("\nMean Squared Error: ", mean_squared_error(test_y, test_y_pred))
print("\nRoot Mean Squared Error: ", np.sqrt(mean_squared_error(test_y, test_y_pred)))


# Multiple Linear Regression Model for height and Brightness
print("\n\n\nMultiple Linear Regression Model for Height and Brightness:")
from sklearn import linear_model
regr = linear_model.LinearRegression()

train_x = np.asanyarray(train[['height', 'brightness']])
train_y = np.asanyarray(train[['likes']])

regr.fit(train_x, train_y)

print("\nCoefficients: ", regr.coef_)
print("\nIntercept: ", regr.intercept_)

# Prediction on test set
test_x = np.asanyarray(test[['height', 'brightness']])
test_y = np.asanyarray(test[['likes']])

test_y_pred = regr.predict(test_x)

# Evaluation of the model
print("\nEvaluation of the model for Height and Brightness:")
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

print("\nR2 Score: ", r2_score(test_y, test_y_pred))
print("\nMean Absolute Error: ", mean_absolute_error(test_y, test_y_pred))
print("\nMean Squared Error: ", mean_squared_error(test_y, test_y_pred))
print("\nRoot Mean Squared Error: ", np.sqrt(mean_squared_error(test_y, test_y_pred)))



# Multiple Linear Regression Model for Aspect Ratio and Sharpness
print("\n\n\nMultiple Linear Regression Model for Aspect Ratio and Sharpness:")
from sklearn import linear_model
regr = linear_model.LinearRegression()

train_x = np.asanyarray(train[['aspect_ratio', 'sharpness']])
train_y = np.asanyarray(train[['likes']])

regr.fit(train_x, train_y)

print("\nCoefficients: ", regr.coef_)
print("\nIntercept: ", regr.intercept_)

# Prediction on test set
test_x = np.asanyarray(test[['aspect_ratio', 'sharpness']])
test_y = np.asanyarray(test[['likes']])

test_y_pred = regr.predict(test_x)

# Evaluation of the model
print("\nEvaluation of the model for Aspect Ratio and Sharpness:")
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

print("\nR2 Score: ", r2_score(test_y, test_y_pred))
print("\nMean Absolute Error: ", mean_absolute_error(test_y, test_y_pred))
print("\nMean Squared Error: ", mean_squared_error(test_y, test_y_pred))
print("\nRoot Mean Squared Error: ", np.sqrt(mean_squared_error(test_y, test_y_pred)))



# Multiple Linear Regression Model for Aspect Ratio and Brightness
print("\n\n\nMultiple Linear Regression Model for Aspect Ratio and Brightness:")
from sklearn import linear_model
regr = linear_model.LinearRegression()

train_x = np.asanyarray(train[['aspect_ratio', 'brightness']])
train_y = np.asanyarray(train[['likes']])

regr.fit(train_x, train_y)

print("\nCoefficients: ", regr.coef_)
print("\nIntercept: ", regr.intercept_)

# Prediction on test set
test_x = np.asanyarray(test[['aspect_ratio', 'brightness']])
test_y = np.asanyarray(test[['likes']])

test_y_pred = regr.predict(test_x)

# Evaluation of the model
print("\nEvaluation of the model for Aspect Ratio and Brightness:")
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

print("\nR2 Score: ", r2_score(test_y, test_y_pred))
print("\nMean Absolute Error: ", mean_absolute_error(test_y, test_y_pred))
print("\nMean Squared Error: ", mean_squared_error(test_y, test_y_pred))
print("\nRoot Mean Squared Error: ", np.sqrt(mean_squared_error(test_y, test_y_pred)))




