# As a product manager, you want to evaluate the user satisfaction for two different seasons of Naruto Shippuden (Season 1 and Season 2).

# You collected feedback from 250 viewers who watched Season 1 of Naruto Shippuden, and 120 expressed satisfaction. Similarly, for Season 2, you gathered data from 300 viewers, and 150 of them expressed satisfaction.

# Conduct an appropriate test at a 95% confidence interval to determine if there's a higher user satisfaction for Season 2 than for Season 1.



import numpy as np
import pandas as pd
import math
from scipy.stats import norm
import sys
from statsmodels.stats.proportion import proportions_ztest

x1 = 120
n1 = 250
x2 = 150
n2 = 300
p1 = x1/n1
p2 = x2/n2
pcap = (x1+x2)/(n1+n2)

Ho = "There is no Significant difference betweeen the satisfaction expressed by season 2 and seaon 1 for the viewers"
Ha = "there is significant difference betweeen the satisfaction expressed by season 2 and seaon 1 for the viewers"
tailedtest = "larger"
confidence = 0.95
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



from statsmodels.stats.proportion import proportions_ztest

# Sample values
count = 495       # number of successes
nobs = 750        # sample size
value = 0.60      # null hypothesis proportion
alpha = 0.10      # 90% confidence level

# One-tailed test: alternative is 'larger' since we want to see if p > 0.60
z_stat, p_value = proportions_ztest(count=count, nobs=nobs, value=value, alternative='larger')

# Output
print(f"Z-statistic: {z_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Hypothesis decision
if p_value < alpha:
    print("✅ Reject the null hypothesis: Support exceeds 60%.")
else:
    print("❌ Fail to reject the null hypothesis: Not enough evidence to say support exceeds 60%.")
