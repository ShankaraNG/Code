# The quality assurance department claims that on average the non-fat milk contains more than 190 mg of Calcium per 500 ml packet.

# To check this claim 45 packets of milk are collected and the content of calcium is recorded.

# Perform an appropriate test to check the claim with a 90% confidence level.

import gdown
import numpy as np
from scipy.stats import norm
import pandas as pd
from scipy.stats import ttest_1samp
from scipy.stats import t as t_dist


data = [193, 321, 222, 158, 176, 149, 154, 223, 233, 177, 280, 244, 138, 210, 167, 129, 254, 
        167, 194, 191, 128, 191, 144, 184, 330, 216, 212, 142, 216, 197, 231, 133, 205, 192, 195, 243, 224, 137, 234, 171, 176, 249, 222, 234, 191]

alpha = 0.1
n = 45
sd = np.std(data, ddof=1)
mean = np.mean(data)
xbar = 190
df = (sd**2 / n) ** 2 / (((sd**2 / n) ** 2) / (n - 1))
t = round((mean - xbar) / (sd / np.sqrt(n)),4)
print(f't={t}')
pvalue = 1 - t_dist.cdf(t, df)
print(f'pvalue={pvalue}')
if(pvalue < alpha):
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")
    
tvalue, pvalue = ttest_1samp(data, xbar, alternative='greater')
print(f'tvalue={round(tvalue,4)}')
print(f'pvalue={pvalue}')
if(pvalue < alpha):
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")
    
    
from scipy.stats import ttest_ind    
AL=[13.4, 10.9, 11.2, 11.8, 14, 15.3, 14.2, 12.6, 17, 16.2, 16.5, 15.7]
UREA=[12, 11.7, 10.7, 11.2, 14.8, 14.4, 13.9, 13.7, 16.9, 16, 15.6, 16]
t_stat, pvalue = ttest_ind(AL, UREA)
print(t_stat, pvalue ,pvalue/2)

alpha = 0.05 # 95% confidence
print('Apha',alpha)
if pvalue < alpha:
  print('Reject H0')
else:
  print ('Fail to Reject H0')
