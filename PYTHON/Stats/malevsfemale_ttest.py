import gdown
import numpy as np
from scipy.stats import norm
import pandas as pd
from scipy.stats import ttest_ind
from scipy.stats import t as t_dist

men = [13.3, 6.0, 20.0, 8.0, 14.0, 19.0, 18.0, 25.0, 16.0, 24.0, 15.0, 1.0, 15.0]
women = [22.0, 16.0, 21.7, 21.0, 30.0, 26.0, 12.0, 23.2, 28.0, 23.0]

meanofmen = np.mean(men)
meanofwomen= np.mean(women)
sdofmen = np.std(men, ddof=1)
sdofwomen = np.std(women, ddof=1)


t = (meanofmen-meanofwomen)/np.sqrt((sdofmen**2/len(men))+(sdofwomen**2/len(women)))
df = ((sdofmen**2 / len(men) + sdofwomen**2 / len(women)) ** 2) / \
     (((sdofmen**2 / len(men)) ** 2) / (len(men) - 1) + ((sdofwomen**2 / len(women)) ** 2) / (len(women) - 1))
print(f't={t}')
pvalue = 2 * (1 - t_dist.cdf(abs(t), df))
print(f'pvalue={pvalue}')
alpha = 0.05
if(pvalue < 0.05):
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")
    
tvalue , pvalue = ttest_ind(men, women, alternative='two-sided')
print(f'tvalue={tvalue}')
print(f'pvalue={pvalue}')
alpha = 0.05
if(pvalue < 0.05):
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")    
