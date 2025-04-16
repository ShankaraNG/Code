from scipy.stats import norm
from scipy.stats import poisson
from scipy.stats import binom
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest



x1=50
n1=1000
x2=30
n2=500
p1_hat=x1/n1
p2_hat=x2/n2
p_hat= (x1+x2)/(n1+n2)

z= (p1_hat-p2_hat)/((1-p_hat)*p_hat*(1/n1+1/n2))**.5
print(f'z={z}')
#we need two tailed test, so multiply by 2 for comparison sake
p = 2*(1-norm.cdf(np.abs(z)))
print(p)


n_season1, x_season1 = 1000, 50

n_season2, x_season2 = 500, 30


z_stat, p_value = proportions_ztest(count=[x_season2, x_season1], nobs=[n_season2, n_season1], alternative='two-sided')


print(f"Z-statistic: {z_stat:.4f}")

print(f"P-value: {p_value:.4f}")


alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis. There is evidence of higher user satisfaction for Season 2 than Season 1.")
else:
    print("Fail to reject the null hypothesis. There is no significant evidence of higher user satisfaction for Season 2.")
