# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 09:34:12 2024

@author: elisa
"""

import pandas as pd
import numpy as np
from scipy import stats
import random

# basic terminologies

## 1. events, complements, sample space
## 2. population, sample
## 3. measure of central tendency: mean, median, mode
## 4. variance & standard deviation
## 5. expected value
## 6. probability = outcomes you are looking for / total possible outcomes

def calc_mean(input_list):
    
    # calculate the mean of a list of numbers
    result = sum(input_list) / len(input_list)
    return result

def calc_median(input_list):
    
    # calculate the median of a list of numbers
    sorted_list = sorted(input_list)
    
    if len(input_list) % 2 == 1:
        
        target = (len(input_list) + 1)/2
        result = sorted_list[target-1]
        
    elif len(input_list) % 2 == 0:
        
        target = int(len(input_list) / 2)
        result = (sorted_list[target-1] + sorted_list[target])/2
    
    return result

def calc_mode(input_list):
    
    # calculate the mode of a list of numbers if there's only one
    result_dict = {}
    
    for x in input_list:
        if x not in result_dict.keys():
            result_dict[x] = 1
        elif x in result_dict.keys():
            result_dict[x] = result_dict[x] + 1
    
    max_key = input_list[0]
    for k,v in result_dict.items():
        if v > result_dict[max_key]:
            max_key = k
    
    return max_key

def calc_var(input_list):
    
    # calculate the variance of a list of numbers
    mean = sum(input_list) / len(input_list)
    
    square_sum = 0
    for x in input_list:
        square_sum = square_sum + (x - mean)**2
    
    result = square_sum/len(input_list)
    
    return result

def calc_std(input_list):
    
    # calculate the standard deviation of a list of numbers
    mean = sum(input_list) / len(input_list)
    
    square_sum = 0
    for x in input_list:
        square_sum = square_sum + (x - mean)**2
    
    result = np.sqrt(square_sum/len(input_list))
    
    return result
    


if __name__ == '__main__':
    #Generate random numbers between 10 and 30
    rlist = random.sample(range(10, 30), 10)
    mode_list = [2,2,2,5,5,10,11,14,2,5,2,10]
    
    r_mean = calc_mean(rlist)
    print("calculated mean is: ", r_mean)
    # np.mean()
    
    r_median = calc_median(rlist)
    print("calculated median is: ",r_median)
    # np.median()
    
    r_mode = calc_mode(mode_list)
    print("calculated mode is: ",)
    # np.mode()
    
    r_var = calc_var(rlist)
    print("calculated variance is: ",r_var)
    # np.var()
    
    r_std = calc_std(rlist)
    print("calculated standard deviation is: ",r_std)
    # np.std()

