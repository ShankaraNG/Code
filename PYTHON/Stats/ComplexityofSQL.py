# The Head of Data Analyst Department is conducting a comparative analysis of the complexity of SQL queries written by two analysts, namely Analyst X and Analyst Y.

# He has gathered data on the number of lines of code for each SQL query.

# Analyst X's SQL lines of code: [15, 18, 20, 17, 16, 19, 22, 16, 18, 21, 23, 18, 17, 19, 20, 24, 25, 26, 27, 28, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# Analyst Y's SQL lines of code: [14, 17, 19, 16, 15, 18, 21, 15, 17, 20, 22, 17, 16, 18, 19, 23, 24, 25, 26, 27, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# The analyst hypothesizes that Analyst Y writes less complex code compared to Analyst X. To investigate this hypothesis, conduct an appropriate test with a 90% confidence interval.


import numpy as np
import pandas as pd
import math
from scipy.stats import norm
import sys
from statsmodels.stats.weightstats import ztest


x= [15, 18, 20, 17, 16, 19, 22, 16, 18, 21, 23, 18, 17, 19, 20, 24, 25, 26, 27, 28, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [14, 17, 19, 16, 15, 18, 21, 15, 17, 20, 22, 17, 16, 18, 19, 23, 24, 25, 26, 27, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
alpha = 1-0.9
ho = "Both analyst x and analyst y writes the same complex code"
ha = "Analyst Y writes less complex code compared to Analyst x"
tailedtest = "larger"

def method(x,y,alpha,ho,ha,tail):

    if(tail.upper() == "LARGER"):
        zstat, pvalue = ztest(x,y,alternative='larger')
    elif(tail.upper() == "SMALLER"):
        zstat, pvalue = ztest(x,y,alternative='smaller')
    elif(tail.upper() == "TWOSIDED"):
        zstat, pvalue = ztest(x,y,alternative='two-sided')
    else:
        print("Invalid test specified please check the tail value")
        sys.exit(1)
        
    print("The Zstat value is ", zstat)
    print("The Pvalue for the given Z stat is", pvalue)
    if(pvalue < alpha):
        print("Rejecting the Null Hypothesis")
        print(ha)
    else:
        print("Failed to reject the Null Hypothesis")
        print(ho)

method(x,y,alpha,ho,ha,tailedtest)
