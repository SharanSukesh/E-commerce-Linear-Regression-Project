
# E-commerce Linear Regression Project

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Libraries used](#libraries-used)
* [Dataset used](#dataset-used)
* [Built on](#built-on)
* [Questions answered](#questions-answered)
* [Model Training and Testing Steps](#model-training-and-testing-steps)
* [Live Demo](#live-demo)
* [Ackowledgements](#ackowledgements)
* [Author](#author)


## About the Project 
Exploratory Data Analysis of a small e-commerce dataset to answer the problem statement given.</br></br>
The python notebook __"02-Linear Regression Project"__ contains an initial EDA of data from the hypothetical e-commerce platform and analyzes how different features impact the company's sales. 

It also suggests actionable insights as well as the features to concentrate on in order to increase their sales. We also offer different ways to answer the problem statement and train a linear regression model to be able to predict __"Yearly Amount Spent"__ as well as to analyze the coefficients of our model. 

## Libraries used 
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

## Dataset used 
* __Perian Data__ - Ecommerce Customers

## Built with
* Jupyter Notebook

## Questions answered 
1. How does the amount a customer spends per year correlate to the time they spend on the website?
2. How does the amount a customer spends per year correlate to the time they spend on the mobile app?
3. How does the average amount of time a customer spends on the mobile application correlate to the length of their membership?
4. How does the average amount of time a customer spends on the website correlate to the length of their membership?
5. How does the average session length of a customer correlate to the amount that they spend in a year?
6. How does the length of membership influence the amount spent per year?

## Model Training and Testing Steps
1. Training the Model
2. Predicting the Test Data
3. Evaluating the Model
4. Examinnig the Residuals
5. Analyzing our Coefficients

## Live Demo
Below is a link that will direct you to the live project which contains input fields for each independant variable and a predict button which, when clicked, will use the model we have trained to output a value of estimated yearly expenditure of a customer.

<a href='https://e-commerce-linear-regression.herokuapp.com/'>Live Demo</a> - Demo

## Ackowledgements
* <a href='http://www.pieriandata.com'>Perian Data</a> - Dataset

## Author - Sharan Sukesh



