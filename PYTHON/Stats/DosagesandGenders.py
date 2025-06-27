# import numpy as np
# from scipy.stats import ks_2samp
# import pandas as pd
# import statsmodels.api as sm
# from statsmodels.formula.api import ols


# data_df = pd.read_csv('E:\\Scalar\\Python\\dosages.txt', delimiter=',')


# def dosagesandgender(data):
#     model = ols('Test_values ~ C(Supplement_Dosage) * C(Dietary)', data=data).fit()
#     anova_table = sm.stats.anova_lm(model, typ=2)
#     print(anova_table)
#     pvalue = anova_table['PR(>F)'].iloc[2]
#     if(pvalue < 0.01):
#         print("Reject the Null Hypothesis")
#     else:
#         print("Failed to Reject the Null Hypothesis")

# dosagesandgender(data_df)

from scipy.stats import norm
import math

x=64.5
u=65
sigma = 2.5
n = 20
z = (x-u)/(sigma/math.sqrt(n))

p_value = norm.cdf(z)
print(p_value)


