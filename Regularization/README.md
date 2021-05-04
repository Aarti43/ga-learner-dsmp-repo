<h1>This project is to predict the house prices in Melbourne</h1>
<p>In this dataset, each observation is a different house attribute with various features, like the number of properties that exist in the suburb, land size, building size, governing council for the area, real estate agent, price of the house, etc.</p>

<p>Some of the features of Type, Method, SellerG, CouncilArea, and Regionname in the data are textual in nature. Done behind-the-scenes data preprocessing and modified the data</p>
<p></p>

<p>The dataset has details of 6830 house entries with the 15 features</p>

<p>After completing this project, I have the better understanding of how to build a regularized regression model. In this project, I have applied the following concepts.</p>

<ul>
	<li>Train-test split</li>

<li>
Correlation between the features</li><li>

Linear Regression</li><li>

Polynomial Regressor</li><li>

Lasso Regressor</li><li>

Ridge Regressor</li><li>

R2 Evaluation Metrics</li></ul>

<h2>Process followed:</h2>
<p>I first check for the multicolinearity and found none of the features in the dataset are collinear. Then used LinearRegression model and predicted the target veriable for test dataset and found that the R2 score is: 0.610875922874348.</p>

<p>Then went for the Lasso and Ridge and cross validation model to check if the R2 score is increasing and found that the score is almost same. Lastly used polynomial regressor and found r2 is increased by 10%. Hence saved the predictions in csv file.</p>
