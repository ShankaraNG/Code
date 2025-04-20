from scipy.stats import f_oneway, ttest_ind
from itertools import combinations
import numpy as np
import pandas as pd
from scipy.stats import kruskal


algorithm_A = np.array([23, 25, 22, 27, 28, 24, 26, 29, 21, 30, 25, 43, 26, 28, 24, 22, 27, 46, 25, 29]) 
algorithm_B = np.array([31, 28, 29, 32, 30, 33, 27, 28, 32, 30, 31, 29, 30, 48, 33, 31, 29, 30, 32, 31]) 
algorithm_C = np.array([45, 43, 23, 49, 49, 8, 21, 20, 42, 40, 28, 46, 44, 37, 44, 38, 42, 34, 42, 40])

stat, p_value = kruskal(algorithm_A, algorithm_B, algorithm_C)
print("test statistic:",stat)
print("p_value:",p_value)
'''
H0:execution times are the same for all three algorithms.
H1: At least one of the execution times is different among the three algorithms

'''

if p_value < 0.05:
    print("Reject H0")
    print(" At least one of the execution times is different among the three algorithms ")
else:
    print("Fail to reject H0")
    print("execution times are the same for all three algorithms")
