# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:46:37 2024

@author: elisa
"""

import pandas as pd
import numpy as np
from scipy import stats
import random

# section3 topic: Bayes rules & random variables

# terminologies:
    # permutation, combination - useful for finding out total possible outcomes
    # factorial: 阶乘
    # Bayes' theorem: 
        # P(A|B) = P(B|A)*P(A) / P(B)
        # P(h) = P(h|1-A)*P(1-A) + P(h|A)*P(A)
    # decision tree
    # random variable: a random variable encompasses all possible values in a sample space, 
        # noted with a capital letter, such as X
    # expected value
    

# factorial with Python
print(np.math.factorial(5))

