# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:13:54 2024

@author: elisa
"""

import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
import sklearn
import statsmodels.api as sm


# section10 topic: multiple regression and ANOVA

# terminologies:
    # multicollinearity among predictors
    # R squared and adjusted R squared:
        # adjusted R squared takes into account the number of variables so it more true
        # R squared always increases as more variables are added
        # if adjusted r square is much lower than r square, indicates multicolinearity
        # adjusted R square = 1 - (1-R**2)*(n-1)/(n-p-1)
    # dummy variable
    # time-lagged variables
    # transformation of non-linear variables for linear reg:
        # example: y=(b0+b*x)**2, y=1/(b0+b*x), y=b0*x**b
    # ANOVA: analysis of variance, test for if there's difference between more than 2 groups

# tips dataset
df = sns.load_dataset('tips')

# inspect data
df.shape
df.info()
df.describe()

# inspect categorical variables
cat_cols = [col for col in df.columns if df[col].dtype.name == 'category']
for c in cat_cols:
    print('value distribution of {0}'.format(c))
    print(df[c].value_counts())
    print('\n')

# create dummy variables for sex, time
df_dummy = pd.get_dummies(df[['sex','time']])

df_use = pd.concat([df[['tip','total_bill','size']],df_dummy], axis=1)

# generate X and Y
x_col = [col for col in df_use.columns if col != 'tip']
# X = df_use[x_col]
X = df_use[['total_bill','size','sex_Male','time_Lunch']]
Y = df_use['tip']

## use sklearn
linear_model = LinearRegression().fit(X,Y)
y_pred = linear_model.predict(X)
rsqr = linear_model.score(X,Y)
sklearn.metrics.r2_score(Y,y_pred)

n=X.shape[0]
p=X.shape[1]
adj_rsqr = 1 - (1-rsqr**2)*(n-1)/(n-p-1)

# there is severe colinearity, therefore needs to remove highly correlated variables
corr_table = X.corr()

# to get statistics, need to use statsmodels package
linear_model2 = sm.OLS(Y,X).fit()
linear_model2.summary()
