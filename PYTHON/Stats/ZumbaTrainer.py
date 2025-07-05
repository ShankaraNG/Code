# The Zumba trainer claims to the customers, that their new dance routine helps to reduce more weight.

# Weight of 8 people were recorded before and after following the new Zumba training for a month:

# wt_before = [85, 74, 63.5, 69.4, 71.6, 65,90,78]

# wt_after = [82, 71, 64, 65.2, 67.8, 64.7,95,77]

# Test the trainer's claim with 90% confidence. Further, what would be the pvalue?

import numpy as np
from scipy.stats import norm
import pandas as pd
from scipy.stats import ttest_ind
from scipy.stats import t as t_dist

wt_before = [85, 74, 63.5, 69.4, 71.6, 65,90,78]
wt_after = [82, 71, 64, 65.2, 67.8, 64.7,95,77]
alpha = 1-0.9
Ho ="There is no difference between the weights before and after the change of the routine"
Ha = "The weight is reduced more after the new routine"

def method1(wt_before,wt_after,alpha,ha,ho):
    t_stat, pvalue = ttest_ind(wt_before, wt_after, alternative='greater')
    print("The Tstats of the test are ", t_stat)
    print("The Pvalue for the test is ", pvalue)
    if(pvalue<alpha):
        print("Reject the Null Hypothesis")
        print(ha)
    else:
        print("Failed to Reject the Null Hypothesis")
        print(ho)

method1(wt_before,wt_after,alpha,Ha,Ho)
