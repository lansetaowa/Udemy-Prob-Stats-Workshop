# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 13:53:16 2024

@author: elisa
"""

import numpy as np
import pandas as pd
from scipy.stats import norm
from sklearn.linear_model import LinearRegression
from scipy import stats

# section9 topic: simple linear regression

# terminologies:
    # X: independent variable (predictor)
    # Y: dependent variable
    # intercept, slope, error
        # Y = intercept + slope*X + error
    # intercept and slope are determined by minimizing the sum of square of residuals
    # R squared: the proportion of variation of Y predicted by X
        # R is the correlation between X and Y
    # outputs of slope and intercept:
        # coefficient
        # standard error
        # t statistic
        # p value
        # confidence interval
        # degree of freedom
        # standardized coefficients: has var of 1
            # gives the number of std of Y will change given the number of std in X
        # the F statistic & significance F (part of ANOVA)
    # Regression Assumptions:
        # Linearity
        # independence of erros
        # Homoscedasticity: meaning random residuals，不会随着x变化
        # normality of error distribution
    # standard error of prediction
        # single point pred: Se * sqrt(1 + 1/n + (x_new - x_mean)**2/((n-1)*(std_x**2)))
        # mean pred: Se * sqrt(1/n + (x_new - x_mean)**2/((n-1)*(std_x**2)))

np.random.seed(42)
n = 20

x = np.random.normal(0, 1, n)

# Formula: y = 0.6 * x + random_noise
noise = np.random.normal(0, 1, n)
y = 0.6 * x + 0.5* noise

# Create DataFrame
df = pd.DataFrame({'X': x, 'Y': y})
df.corr()

X = df[['X']]
Y = df['Y']

# fit simple linear model
linear_model = LinearRegression().fit(X,Y)

# equivalent to:
linear_model = LinearRegression()
linear_model.fit(X,Y)

# R square
rsq = linear_model.score(X,Y)

intercept = linear_model.intercept_ # intercept
slope = linear_model.coef_[0] # slope

# making prediction
y_pred = linear_model.predict(X)

## compute standard error, t stat and p value for above model
residuals = y - y_pred

# dof
p = 1 # number of predictors, only 1 in this case
dof = n - p - 1

# Residual sum of squares, total sum of squares
rss = np.sum(residuals**2)
tss = np.sum((y-np.mean(y))**2)

# variance of the residuals
sigma_squared = rss / dof

# calculate standard error
x_mean = np.mean(df['X'])
se_slope = np.sqrt(sigma_squared / np.sum((x-x_mean)**2))
se_intercept = np.sqrt(sigma_squared*(1/n + x_mean**2/np.sum((x-x_mean)**2)))

# calculate t stat
t_slope = slope/se_slope
t_intercept = intercept / se_intercept

# compute p-value
p_slope = 2 * (1 - stats.t.cdf(np.abs(t_slope), df = dof))
p_intercept = 2 * (1 - stats.t.cdf(np.abs(t_intercept), df=dof))







