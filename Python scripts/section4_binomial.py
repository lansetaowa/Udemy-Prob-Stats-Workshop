# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 15:43:25 2024

@author: elisa
"""

import pandas as pd
import numpy as np
from scipy.stats import binom
import random

# section3 topic: probability distributions, binomial distribution

# terminologies:
    # Binomial Distribution:
        # 2 possible outcomes
        # # of trials: n; # of success: k; prob of success: p
        # probability of k successes: (n!/(k!*(n-k)!)) * p**k * (1-p)**(n-k)
        # expected value: n*p
        # variance: n*p*(1-p)
        # std: sqrt(n*p*(1-p))
    # random variable: a random variable encompasses all possible values in a sample space, 
        # noted with a capital letter, such as X
    # uniform distribution: all outcomes are equally likely

######### below are codes of using scipy.stats.binom #############
n = 10
k = 4
p = 0.3

# pmf: probability mass function
binom.pmf(k, n, p)

binom.pmf(k=10, n=20, p=0.6)

# cdf: cumulative distribution function 
# CDF(x) = P(X ≤ x)
binom.cdf(k,n,p)

# sf: survival function, the opposite of cdf, i.e. sf = 1-cdf
binom.sf(k,n,p)

# find stats for the distribution
mean, var = binom.stats(n,p)

# ppf: the inverse calculation of cdf
prob = binom.cdf(k,n,p)
print(binom.ppf(prob, n,p))
print(binom.ppf(prob+0.01, n,p))

# others
binom.mean(n,p)
binom.median(n,p)
binom.interval(confidence = 0.9, n=n,p=p)

# generate random numbers in array
r = binom.rvs(n,p, size = 100)


# example of expected value with binomial
# From past experience, the manager of a car rental company knows that 20% of the customers who make a reservation for a car will never appear to claim their cars. Because of this, though the company has only 22 cars to rent, the manager always takes advance reservations from 25 customers per day.
# Every claimed car results in $60 of income for the company. While harder to quantify, the manager estimates that every customer who has a reservation but is turned away due to overbooking results in a loss of $200 to the company due to bad word of mouth. Based on this information, should the manager continue taking 25 reservations per day or would it make more economic sense to take just 24?
n = 25
p = 0.8

total = 0
for k in range(1,n+1):
    p_come = binom.pmf(k, n=n, p=0.8)
    #print(n_come)
    
    if k<=22:
        expected = p_come*60*k
    elif k>=23:
        expected = p_come*(60*k - (k-22)*200)
    #print(expected)
    
    total = total + expected


