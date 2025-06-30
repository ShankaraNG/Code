# The Quidditch teams at Hogwarts conducted tryouts for two positions: Chasers and Seekers.

# In Group Chasers, out of 90 students who tried out, 57 were selected. In Group Seekers, out of 120 students who tried out, 98 were selected.

# Is there a significant difference in the proportion of students selected for Chasers and Seekers positions?

# Conduct a test at 90% confidence level.

import numpy as np
import pandas as pd
import math
from scipy.stats import norm
import sys
from statsmodels.stats.proportion import proportions_ztest

x1 = 57
n1 = 90
x2 = 98
n2 = 120
p1 = x1/n1
p2 = x2/n2
pcap = (x1+x2)/(n1+n2)

Ho = "There is no Significant difference between the Chasers and Seekers position"
Ha = "there is significant difference between the chasers and Seekers position"
tailedtest = "twosided"
confidence = 0.9
alpha = 1-confidence

def method1(p1,p2,pcap,n1,n2,alpha,ho,ha,tail):
    z = (p1-p2)/math.sqrt((1-pcap)*pcap*((1/n1)+(1/n2)))
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
        
        
def method2(x1,x2,n1,n2,alpha,ho,ha,tail):
    total = [n1,n2]
    success = [x1,x2]
    if(tail.upper() == "LARGER"):
        zstat , pvalue = proportions_ztest(count=success, nobs=total, alternative='larger')
    elif(tail.upper() == "SMALLER"):
        zstat , pvalue = proportions_ztest(count=success, nobs=total, alternative='smaller')
    elif(tail.upper() == "TWOSIDED"):
        zstat , pvalue = proportions_ztest(count=success, nobs=total, alternative='two-sided')
    else:
        print("Invalid test specified please check the tail value")
        sys.exit(1)
        
    print("The Z stats vlaue is", zstat)
    print("The Pvalue for the given Z stat is", pvalue)
    if(pvalue < alpha):
        print("Rejecting the Null Hypothesis")
        print(ha)
    else:
        print("Failed to reject the Null Hypothesis")
        print(ho)

method1(p1,p2,pcap,n1,n2,alpha,Ho,Ha,tailedtest)
method2(x1,x2,n1,n2,alpha,Ho,Ha,tailedtest)
