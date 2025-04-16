from scipy.stats import norm
from scipy.stats import poisson
from scipy.stats import binom
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.weightstats import ttest_ind
from scipy.stats import ttest_1samp


sample = np.random.randint(1, 201, 30)
print(sample)
mean = np.mean(sample)
standard_deviation = np.std(sample)
xbar=100

z=(xbar-mean)/(standard_deviation/np.sqrt(30))
print(f'z={z}')

tvalue , pvalue = ttest_1samp(sample, xbar)
print(f'tvalue={tvalue}')
print(f'pvalue={pvalue}')
alpha = 0.05
if pvalue < alpha:
    print("Reject the null hypothesis. The sample mean is significantly different from the population mean.")
else:
    print("Fail to reject the null hypothesis. The sample mean is not significantly different from the population mean.")
