# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 10:47:10 2024

@author: elisa
"""

import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns

# section4 topic: normal distribution, z score

# terminologies:
    # normal distribution:
        # mean
        # std: 68% within +-1std, 95% within +-2std, almost 99.7% within 3
    # z score: 
        # def: the # of std a value is from the mean

# scenario: a gorup of penguins, height normally distributed
# mean of 40 inches, std of 5 inches

mean = 40
std = 5

############ create a normal distribution
height_dist = norm(loc=mean, scale=std)

# random sampling from above distribution with rvs()
# an array
sample = height_dist.rvs(size=20)

# plot random samples with larger sample size
sample = height_dist.rvs(size=5000)
# Use seaborn style and increase font size 
sns.set_theme(style='ticks', font_scale=1.5)
# set figure dimensions 
plt.figure(figsize=(12, 6))
# Plot histogram 
# Use larger bin count (100) to get smoother shape
plt.hist(sample, bins=40)
 
plt.title("Emperor Penguin Heights - Histogram")
plt.xlabel("Height (inches)")
plt.ylabel("Frequency")

############ Probability of a given value using pdf()
# pdf: probability density function
# what's the probability of a penguin's height is 40?
prob_40 = height_dist.pdf(x = 40)
print(round(prob_40,4))

############ Density Curve using pdf()

# get 1000 evenly spaced heights between 20 and 60
height_values = np.linspace(20,60,num=1000)
height_values.size
height_values[:10].round(2)
height_values[-10:].round(2)

# get probabilities for each value using pdf()
probs = height_dist.pdf(x = height_values)

# plot density curve 
plt.figure(figsize=(12, 6))
# heights on x-axis and their probabilities on y-axis 
plt.plot(height_values, probs)
# shade the area under the density curve
plt.fill_between(height_values, probs, alpha=0.2)
plt.title("Emperor Penguin Heights - Density Curve", pad=20)
plt.xlabel("Height (inches)", labelpad=10)
plt.ylabel("Probability", labelpad=10)

########### find Percent Below a Value using cdf()
# cdf: cumulative density function
below_44 = height_dist.cdf(44)
below_44.round(4)

# plot density curve 
plt.figure(figsize=(12, 6))
plt.plot(height_values, probs)
# Shade the region where height <= 44 inches
shaded_region =  (height_values <= 44)
plt.fill_between(height_values, probs, 
                 where=shaded_region)
 
plt.title("Emperor Penguin Heights - Under 44 Inches", pad=20)
plt.xlabel("Height (inches)", labelpad=10)
plt.ylabel("Probability", labelpad=10)

########### Calculate the value given Percentile using ppf()
# ppf: percent point function
percentile_90th = height_dist.ppf(0.9) # return the value within dist


# we can also do calculations directly using one line code without setting up the norm dist
norm.pdf(x=8, loc=10,scale=2)
norm.cdf(x=10, loc=10,scale=2)
norm.ppf(0.84) # return z value










