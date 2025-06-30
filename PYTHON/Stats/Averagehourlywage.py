# The average hourly wage of a sample of 150 workers in plant 'A' was Rs.2·87 with a standard deviation of Rs. 1·08.

# The average wage of a sample of 200 workers in plant 'B' was Rs. 2·56 with a standard deviation of Rs. 1·28.

# (i) Calculate the Z-score for this scenario.

# (ii) Can an applicant safely assume that the hourly wages paid by plant 'A' are higher than those paid by plant 'B' at a 1% significance level?

import numpy as np
from statsmodels.stats.weightstats import ztest
import pandas as pd
import math
from scipy.stats import norm
import sys

n1 = 150
sd1 = 1.08
x1 = 2.87
n2= 200
sd2 = 1.28
x2 =2.56
tail = 'larger'
alpha = 0.01

ho = "The hourly wages of Plant A is Equal to Plant B"
ha = "The hourly wages of Plant A > that of Plant B"


def method1(x1,n1,sd1,n2,sd2,x2,alpha,ho,ha,tail):
    se = math.sqrt((sd1**2/n1)+(sd2**2/n2))
    z = (x1-x2)/se
    print("The Z stats vlaue is", z)
    if(tail.upper() == "LARGER"):
        pvalue = 1 - norm.cdf(z)
    elif(tail.upper() == "SMALLER"):
        pvalue = norm.cdf(z)
    elif(tail.upper() == "TWOSIDED"):
        pvalue = 2 * (1 - norm.cdf(abs(z)))
    else:
        print("Invalid test specified please check the tail value")
        sys.exit(1)
    
    print("The Pvalue for the given Z stat is", pvalue)
    if(pvalue < alpha):
        print("Rejecting the Null Hypothesis")
        print(ha)
    else:
        print("Failed to reject the Null Hypothesis")
        print(ho)
        
    
def method2(x1,n1,sd1,n2,sd2,x2,alpha,ho,ha,tail):
    np.random.seed(42)
    sample1 = np.random.normal(loc=x1, scale=sd1, size=n1)
    sample2 = np.random.normal(loc=x2, scale=sd2, size=n2)
    if(tail.upper() == "LARGER"):
        z_stat, p_value = ztest(sample1, sample2, alternative='larger')
    elif(tail.upper() == "SMALLER"):
        z_stat, p_value = ztest(sample1, sample2, alternative='smaller')
    elif(tail.upper() == "TWOSIDED"):
        z_stat, p_value = ztest(sample1, sample2, alternative='two-sided')
    else:
        print("Invalid test specified please check the tail value")
        sys.exit(1)
    
    print("The Z stats vlaue is", z_stat)
    print("The Pvalue for the given Z stat is", p_value)
    if(p_value < alpha):
        print("Rejecting the Null Hypothesis")
        print(ha)
    else:
        print("Failed to reject the Null Hypothesis")
        print(ho)
    
method1(x1,n1,sd1,n2,sd2,x2,alpha,ho,ha,tail)
method2(x1,n1,sd1,n2,sd2,x2,alpha,ho,ha,tail)

        
    
        
    
    
    
