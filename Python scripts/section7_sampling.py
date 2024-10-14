# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:44:58 2024

@author: elisa
"""

import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy.stats import t

import matplotlib.pyplot as plt
import seaborn as sns

# section6 topic: sampling

# terminologies:
    # population, sample, sample must be representative
        # std of sample mean is: std of pop / sqrt(N), N is sample size
        # inference from a sample is much more powerful than one individual from pop
        # randomization
    # Central Limit Theorem: 
        # the mean of the sample will be a normal dist around the population mean
        # the expected value of sample mean equals pop mean
    # Proportion Sampling or dealing with a percentage in test:
        # pop mean perc = p, the hypothesis p we are testing against
        # std of sample perc = sqrt(p*(1-p)/N), N is sample size
    # Margin of Error: a term for sampling, Z*sample_std
    # T distribution: a more flat, spread-out curve than normal
        # a more conservative estimate of a standard normal dist
        # T-curve is a series of curves that depends on DOF
        # DOF: n-1
        # confidence interval
        # alpha: total uncertainty
        # used when information is limited, such as pop std is unknown
            # therefor had to use sample std
            # if pop std is known, should still use z score
        # exception: when dealing with proportions, almost always use z table
    
# using stats.scipy.t for t distribution calculations
# df, loc, scale

t.stats(df=5, moments='mvsk')

t.pdf(0.9, df=10) # probability density function
t.ppf(0.1, df=20, loc=2, scale=1) # percent point function
t.cdf(2, df=25, loc=2, scale=1) # cumulative density

t.rvs(df=20, size=100) # generate random numbers














    