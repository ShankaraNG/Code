# According to a survey conducted on car owners, it was determined that

# 60% of owners have only one car,
# 28% have two cars, and
# 12% have three or more cars.
# Suppose Ram conducted his own survey within his residential society, and found that

# 73 owners have only one car,
# 38 owners have two cars, and
# 18 owners have three or more cars.
# Determine whether Ram's survey supports the original one, with a significance level of 0.05.

import numpy as np
import pandas as pd
from scipy.stats import chi2, chi2_contingency, chisquare

excepted = [77.4,36.12,15.48]
observed = [73,38,18]

alpha = 0.05
dof = len(observed) - 1

chisquare_stat, p_value = chisquare(observed, excepted)
print("Chi-square statistic:", chisquare_stat)
print("P value:", p_value)
if(p_value < alpha):
    print("Reject the null hypothesis: Ram's survey does not support the original one.")
else:       
    print("Fail to reject the null hypothesis: Ram's survey supports the original one.")

