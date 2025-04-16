from scipy.stats import norm
from scipy.stats import poisson
from scipy.stats import binom
import numpy as np
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest


print(2 * (1 - norm.cdf(2.5331)))

a= [15, 18, 20, 17, 16, 19, 22, 16, 18, 21, 23, 18, 17, 19, 20, 24, 25, 26, 27, 28, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
b= [14, 17, 19, 16, 15, 18, 21, 15, 17, 20, 22, 17, 16, 18, 19, 23, 24, 25, 26, 27, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]


zscore , pvalue = ztest(x1=a,x2=b,alternative="two-sided")
alpha=0.01
if(pvalue<alpha):
    print("Reject the Null Hypothesis")
else:
    print("Failed to reject the Null Hypothesis")
