# The Highway Administration conducts an annual survey on motor vehicles travelling on the highway. They publish their findings in Highway Statistics, based on different types of vehicles.
# Independent simple random samples of cars, buses, and trucks yielded the data on a number of thousand miles driven last year.

# cars = [19.9, 15.3, 2.2, 6.8, 34.2, 8.3, 12.0, 7.0, 9.5, 1.1]
# buses = [1.8, 24.6, 7.2, 37.0, 7.2, 21.2, 6.5, 23.6]
# trucks = [13.3, 23.0, 25.4, 15.3, 57.1, 14.5, 26.0]
# We want to decide if there is a difference in last year’s mean number of miles driven among cars, buses, and trucks.

# At a 93% confidence level, does the data provide sufficient evidence to conclude that there is a difference in last year’s mean number of miles driven by cars, buses, and trucks?

from scipy.stats import f_oneway
from itertools import combinations
import numpy as np
import pandas as pd

cars = [19.9, 15.3, 2.2, 6.8, 34.2, 8.3, 12.0, 7.0, 9.5, 1.1]
buses = [1.8, 24.6, 7.2, 37.0, 7.2, 21.2, 6.5, 23.6]
trucks = [13.3, 23.0, 25.4, 15.3, 57.1, 14.5, 26.0]

fstat, pvalue = f_oneway(cars, buses, trucks)
print(f"F-statistic: {fstat:.4f}")
print(f"P-value: {pvalue:.4f}")
alpha = 0.07
if pvalue < alpha:
    print("Reject the null hypothesis: There is a difference in last year's mean number of miles driven by cars, buses, and trucks.")
else:
    print("Fail to reject the null hypothesis: No difference in last year's mean number of miles driven by cars, buses, and trucks.")
    
