# There are 8 females and 12 males in a coaching class.

# After a practice test, the coach wants to know whether the average score of females is greater than the average score of males.

# Given data describes the scores of females and males in his class.

# female_scores=[25,30,45,49,47,35,32,42]

# male_scores=[45,47,25,22,29,32,27,28,40,49,50,33]
# Use an appropriate test to check whether the assumption of the coach is significant or not, at a 2% significance level?

import numpy as np
from scipy.stats import norm
import pandas as pd
from scipy.stats import ttest_ind
from scipy.stats import t as t_dist

female_scores=[25,30,45,49,47,35,32,42]
male_scores=[45,47,25,22,29,32,27,28,40,49,50,33]
alpha = 0.02
Ho ="The average scores of female is equal to average score of male"
Ha = "The average scores of females is greater than the average scores of males"

def method1(male,female,alpha,ha,ho):
    t_stat, pvalue = ttest_ind(female, male, alternative='greater')
    print("The Tstats of the test are ", t_stat)
    print("The Pvalue for the test is ", pvalue)
    if(pvalue<alpha):
        print("Reject the Null Hypothesis")
        print(ha)
    else:
        print("Failed to Reject the Null Hypothesis")
        print(ho)

method1(male_scores,female_scores,alpha,Ha,Ho)
