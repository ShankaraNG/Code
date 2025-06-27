import numpy as np
from scipy.stats import kstest
import pandas as pd




delivery_method_A = [2.5, 3.2, 2.8, 3.5, 3.0, 2.7, 2.9, 3.1, 2.6, 3.3]

delivery_method_B = [3.8, 3.2, 3.5, 3.1, 3.9, 3.0, 3.3, 3.6, 3.4, 3.7]

t_stats, pvalue = kstest(delivery_method_A,delivery_method_B)
print(pvalue)

if(pvalue < 0.05):
    print("Reject the Null Hypothesis")
else:
    print("Failed to Reject the Null Hypothesis")
