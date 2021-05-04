# --------------
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# path- variable storing file path

#Code starts here

#Load dataset & Display the first five columns
df= pd.read_csv(path)
df.head(5)

#Store all the features in X and target variable in y
X = df.loc[:, df.columns != 'Price']
y = df['Price']

#Split the dataframe into train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.3, random_state = 6)

#Find the correlation between the independent features and print
corr = X_train.corr()
print("The correlation between the features:", corr)


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Code starts here

#Instantiate a linear regression model
regressor = LinearRegression()

#Fit the model on the training data
regressor.fit(X_train,y_train)

#Make predictions on the X_test features
y_pred = regressor.predict(X_test)

#Find the r^2 score
r2 = r2_score(y_test, y_pred)
print("The r2 score is:", r2)


# --------------
from sklearn.linear_model import Lasso

# Code starts here

#Instantiate a lasso model
lasso = Lasso()

#Fit the model on the training data
lasso.fit(X_train,y_train)

#Make predictions on the X_test features
lasso_pred = lasso.predict(X_test)

#Find the r^2 score
r2_lasso = r2_score(y_test, lasso_pred)
print("r2 score using Lasso Regressor is:", r2_lasso)


# --------------
from sklearn.linear_model import Ridge

# Code starts here

# Instantiate a lasso model
ridge = Ridge()

# Fit the model on the training data
ridge.fit(X_train,y_train)

# Make predictions on the X_test features
ridge_pred = ridge.predict(X_test)

# Find the r^2 score
r2_ridge = r2_score(y_test, ridge_pred)
print('The r2 score using Ridge regression is:', r2_ridge)

# Code ends here


# --------------
from sklearn.model_selection import cross_val_score

#Code starts here

#Initiate a LinearRegression()
regressor = LinearRegression()

# Calculate cross_val_score
score = cross_val_score(regressor, X_train, y_train, cv=10)

# Calculate the mean of 'score'
mean_score = np.mean(score)
print('The mean score is:', mean_score)


# --------------
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

#Code starts here

# make pipeline for second degree polynomialfeatures
model = make_pipeline(PolynomialFeatures(2), LinearRegression())

# Fit the model on training set
model.fit(X_train, y_train)

# predict the model performance
y_pred = model.predict(X_test)

# calculate r2 score
r2_poly = r2_score(y_test, y_pred)

# print r2 score
print(r2)



