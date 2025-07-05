# An experiment was performed to compare the effectiveness of Ammonium Chloride and urea on the grain yield (in quintal per hectare) and the results are given in the arrays below:

# Ammonium_chloride = [13.4, 10.9, 11.2, 11.8, 14, 15.3, 14.2, 12.6, 17, 16.2, 16.5, 15.7]
# Urea = [12, 11.7, 10.7, 11.2, 14.8, 14.4, 13.9, 13.7, 16.9, 16, 15.6, 16]
# Conduct an appropriate test to compare the same with a 95% confidence level and choose the appropriate option below.

import numpy as np
from statsmodels.stats.weightstats import ttest_ind
from scipy.stats import norm
import math
import sys



ac = [13.4, 10.9, 11.2, 11.8, 14, 15.3, 14.2, 12.6, 17, 16.2, 16.5, 15.7]
urea = [12, 11.7, 10.7, 11.2, 14.8, 14.4, 13.9, 13.7, 16.9, 16, 15.6, 16]
alpha = 1-0.95
Ho = "The effects of both ammonium chloride and Urea are the same"
Ha = "The Effects are different"
tail = "twosided"

def method1(ac,urea,alpha,ho,ha,tail):
    n1 = len(ac)
    n2 = len(urea)
    ac = np.array(ac)
    urea = np.array(urea)
    acmean = np.mean(ac)
    acstd = np.std(ac)
    ureamean = np.mean(urea)
    ureastd = np.std(urea)
    tstats = (acmean-ureamean)/math.sqrt((acstd**2/n1)+(ureastd**2/n2))
    print("The T Statistics is ", tstats)
    if(tail.upper()== "LARGER"):
        pvalue = 1-norm.cdf(tstats)
    elif(tail.upper()== "SMALLER"):
        pvalue = norm.cdf(tstats)
    elif(tail.upper() == "TWOSIDED"):
        pvalue = 2*(1-norm.cdf(tstats))
    else:
        print("Wrong Input for the Tail test")
        sys.exit(1)
    
    print("The pvalue for the Tstats is ", pvalue)
    if(pvalue<alpha):
        print("Rejecting Null Hypothesis")
        print(ha)
    else:
        print("Failed to Reject Null Hypothesis")
        print(ho)

def method2(ac,urea,alpha,ho,ha,tail): 
    if(tail.upper()== "LARGER"):
        tstats, pvalue, df = ttest_ind(ac,urea,alternative="larger")
    elif(tail.upper()== "SMALLER"):
        tstats, pvalue, df = ttest_ind(ac,urea, alternative="smaller")
    elif(tail.upper() == "TWOSIDED"):
        tstats, pvalue, df = ttest_ind(ac,urea, alternative="two-sided")
    else:
        print("Wrong Input for the Tail test")
        sys.exit(1)
        
    print("The T Statistics is ", tstats)    
    print("The pvalue for the Tstats is ", pvalue)
    if(pvalue<alpha):
        print("Rejecting Null Hypothesis")
        print(ha)
    else:
        print("Failed to Reject Null Hypothesis")
        print(ho)
        
        
method1(ac,urea,alpha,Ho,Ha,tail)
method2(ac,urea,alpha,Ho,Ha,tail)
