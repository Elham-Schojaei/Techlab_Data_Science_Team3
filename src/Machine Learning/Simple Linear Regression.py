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

plt.scatter(df["brightness"], df["likes"], color="purple")
plt.xlabel("brightness")
plt.ylabel("likes")
plt.show()

plt.scatter(df["sharpness"], df["likes"], color="green")
plt.xlabel("sharpness")
plt.ylabel("likes")
plt.show()
 
plt.scatter(df["width"], df["likes"], color="red")
plt.xlabel("width") 
plt.ylabel("likes")
plt.show()  

plt.scatter(df["height"], df["likes"], color="orange")
plt.xlabel("height")        
plt.ylabel("likes")
plt.show()


plt.scatter(df["aspect_ratio"], df["likes"])
plt.xlabel("Aspect Ratio")
plt.ylabel("Likes")
plt.title("Aspect Ratio vs Likes")
plt.show()



#linear regression modelS:

from sklearn import linear_model

# Keep needed columns
cdf = df[['likes', 'brightness', 'sharpness', 'width', 'height', 'aspect_ratio']]

# Train-test split
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


# simple linear regression for brightness and likes

regr = linear_model.LinearRegression()

train_x = np.asanyarray(train[['brightness']])
train_y = np.asanyarray(train[['likes']])

test_x = np.asanyarray(test[['brightness']])
test_y = np.asanyarray(test[['likes']])

regr.fit(train_x, train_y)
test_y_pred = regr.predict(test_x)

print("\n \n \n Simple Linear Regression Model for Brightness and Likes:")
print("\nCoefficient:", regr.coef_)
print("\nIntercept:", regr.intercept_)

#evaluate the model using mean absolute error, mean squared error, and r2 score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
print("\nEvaluation of the linear regression model for Brightness and Likes:")
print("\nR2 Score: ", r2_score(test_y, test_y_pred))
print("\nMean Absolute Error: ", mean_absolute_error(test_y, test_y_pred))
print("\nMean Squared Error: ", mean_squared_error(test_y, test_y_pred))
print("\nRoot Mean Squared Error: ", np.sqrt(mean_squared_error(test_y, test_y_pred)))




# simple linear regression for sharpness and likes

regr = linear_model.LinearRegression()

train_x = np.asanyarray(train[['sharpness']])
train_y = np.asanyarray(train[['likes']])

test_x = np.asanyarray(test[['sharpness']])
test_y = np.asanyarray(test[['likes']])

regr.fit(train_x, train_y)
test_y_pred = regr.predict(test_x)

print("\n \n Simple Linear Regression Model for Sharpness and Likes:")
print("\nCoefficient:", regr.coef_)
print("\nIntercept:", regr.intercept_)

#evaluate the model using mean absolute error, mean squared error, and r2 score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
print("\n \nEvaluation of the linear regression model for Sharpness and Likes:")
print("\nR2 Score: ", r2_score(test_y, test_y_pred))
print("\nMean Absolute Error: ", mean_absolute_error(test_y, test_y_pred))
print("\nMean Squared Error: ", mean_squared_error(test_y, test_y_pred))
print("\nRoot Mean Squared Error: ", np.sqrt(mean_squared_error(test_y, test_y_pred)))




# simple linear regression for width and likes
regr = linear_model.LinearRegression()

train_x = np.asanyarray(train[['width']])
train_y = np.asanyarray(train[['likes']])

test_x = np.asanyarray(test[['width']])
test_y = np.asanyarray(test[['likes']])

regr.fit(train_x, train_y)
test_y_pred = regr.predict(test_x)

print("\n \n SimpleLinear Regression Model for Width and Likes:")
print("\nCoefficient:", regr.coef_)
print("\nIntercept:", regr.intercept_)

#evaluate the model using mean absolute error, mean squared error, and r2 score

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
print("\nEvaluation of the linear regression model for Width and Likes:")
print("\nR2 Score: ", r2_score(test_y, test_y_pred))
print("\nMean Absolute Error: ", mean_absolute_error(test_y, test_y_pred))
print("\nMean Squared Error: ", mean_squared_error(test_y, test_y_pred))
print("\nRoot Mean Squared Error: ", np.sqrt(mean_squared_error(test_y, test_y_pred)))




# simple linear regression for height and likes

regr = linear_model.LinearRegression()

train_x = np.asanyarray(train[['height']])
train_y = np.asanyarray(train[['likes']])

test_x = np.asanyarray(test[['height']])
test_y = np.asanyarray(test[['likes']])

regr.fit(train_x, train_y)
test_y_pred = regr.predict(test_x)

print("\n \n Simple Linear Regression Model for Height and Likes:")
print("\nCoefficient:", regr.coef_)
print("\nIntercept:", regr.intercept_)

#evaluate the model using mean absolute error, mean squared error, and r2 score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
print("\nEvaluation of the linear regression model for Height and Likes:")
print("\nR2 Score: ", r2_score(test_y, test_y_pred))
print("\nMean Absolute Error: ", mean_absolute_error(test_y, test_y_pred))
print("\nMean Squared Error: ", mean_squared_error(test_y, test_y_pred))
print("\nRoot Mean Squared Error: ", np.sqrt(mean_squared_error(test_y, test_y_pred)))




# simple linear regression for aspect ratio and likes
print("\n \n Simple Linear Regression Model for Aspect Ratio and Likes:")   
regr = linear_model.LinearRegression()

train_x = np.asanyarray(train[["aspect_ratio"]])
train_y = np.asanyarray(train[["likes"]])

regr.fit(train_x, train_y)

test_x = np.asanyarray(test[["aspect_ratio"]])
test_y = np.asanyarray(test[["likes"]])
test_y_pred = regr.predict(test_x)

print("\n Coefficient:", regr.coef_)
print("\n Intercept:", regr.intercept_)

#evaluate the model using mean absolute error, mean squared error, and r2 score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
print("\nEvaluation of the linear regression model for Aspect Ratio and Likes:")
print("\nR2 Score: ", r2_score(test_y, test_y_pred))
print("\nMean Absolute Error: ", mean_absolute_error(test_y, test_y_pred))
print("\nMean Squared Error: ", mean_squared_error(test_y, test_y_pred))
print("\nRoot Mean Squared Error: ", np.sqrt(mean_squared_error(test_y, test_y_pred)))

