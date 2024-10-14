# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:02:40 2024

@author: elisa
"""

import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns

# section5 topic: joint random variables

# terminologies:
    # confidence interval: associated with a percentage, in the form of a range of values
        # confidence level =  1-alpha (each side will only have alpha/2)
        # confidence interval is very important in sampling
    # joint random variables
        # joint random variables: X, Y, P(X=x & Y=y), probability associated with a combination of X and Y
        # covariance: 
            # form1: Expected[X*Y] - mean(X)*mean(Y)
                # mean(x*y) - mean(X)*mean(Y)
            # or form2: cov(X,Y) = sum((x-mean_X)*(y-mean_Y)) / (n-1)
        # correlation: standardized
            # correlation = cov(X,Y) / std_X*std_Y
        # expected value of a*X + b*Y: a*mean(X) + b*mean(Y)
        # variance of X+Y: std_X**2 + std_Y**2 + 2*cov(X,Y)
        # variance of a*X+b*Y: a**2*std_X**2 + b**2*std_Y**2 + 2*a*b*cov(X,Y)
            # or: a**2*std_X**2 + b**2*std_Y**2 + 2*a*b*corr(X,Y)*std_X*std_Y

# example table
# Setting a seed so the example is reproducible
np.random.seed(4272018)

df = pd.DataFrame(np.random.randint(low= 0, high= 20, size= (5, 2)),
                  columns= ['X', 'Y'])

# variance
df.var()
df['X'].var() # returns sample var, which is over N-1
np.var(df['X']) # returns population var, which is over N, not N-1

# covariance
# form1
df['xy'] = df['X']*df['Y']
np.mean(df['xy']) - np.mean(df['X'])*np.mean(df['Y']) # 2.6

# form2: cov(X,Y), used to calculate correlation
df['x2'] = df['X'] - np.mean(df['X'])
df['y2'] = df['Y'] - np.mean(df['Y'])
df['xy2'] = df['x2']*df['y2']
np.sum(df['xy2'])/4 # 3.25, will get 2.6 if divided by 5

df.cov() # will give 3.25 for X and Y
np.cov(df['X'],df['Y'])

# correlation
# correlation = cov(X,Y) / std_X*std_Y
std_x = df['X'].std()
std_Y = df['Y'].std()

corr = 3.25 / (std_Y*std_x) # 0.11

df.corr()
np.corrcoef(df['X'],df['Y'])












