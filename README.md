# E-commerce-Linear-Regression-Project
Exploratory Data Analysis of a small e-commerce dataset to answer the problem statement given.</br></br>
The python notebook __"02-Linear Regression Project"__ contains an initial EDA of data from the hypothetical e-commerce platform and analyzes how different features impact the company's sales. 

It also suggests actionable insights as well as the features to concentrate on in order to increase their sales. We also offer different ways to answer the problem statement and train a linear regression model to be able to predict __"Yearly Amount Spent"__ as well as to analyze the coefficients of our model. 

## Libraries used:
* Numpy
* Pandas
* Matplotlib
* Seaborn
* sklearn

```bash
import numpy as np                                                
import pandas as pd                                               
import pandas_profiling
import matplotlib.pyplot as plt
import seaborn as sns            
%matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn import metrics 
```

## Dataset used :
* __Perian Data__ - Ecommerce Customers

## Built on:
* Jupyter Notebook

## Questions answered :
1. How does the amount a customer spends per year correlate to the time they spend on the website?
2. How does the amount a customer spends per year correlate to the time they spend on the mobile app?
3. How does the average amount of time a customer spends on the mobile application correlate to the length of their membership?
4. How does the average amount of time a customer spends on the website correlate to the length of their membership?
5. How does the average session length of a customer correlate to the amount that they spend in a year?
6. How does the length of membership influence the amount spent per year?

## Model Training and Testing Steps:
1. Training the Model
2. Predicting the Test Data
3. Evaluating the Model
4. Examinnig the Residuals
5. Analyzing our Coefficients

## Models used:
1. Linear Regression

## Hypotheses tested
1. Engine efficiency has played a role in car sale trends over the last 5 years
2. Engine efficiency to price plays an important role in car sale trends with respect to engine drive and car body
  * With respect to engine drive
  * With respect to the car body

## Ackowledgements
* Perian Data - dataset

## Author - Sharan Sukesh

