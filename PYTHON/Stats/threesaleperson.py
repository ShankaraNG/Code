# A Company wishes to test whether three sales persons Saurav, Naveen, and Radha make the same sales or they differ in their selling ability by comparing the average number of sales made by them last week.

# Out of 14 sales 'Saurav' made 5, 'Naveen' made 4 and 'Radha' made 5. The following arrays describes the records of the sales persons in rupees.


# Saurav = [300, 400, 300, 500, 50]
# Naveen = [600, 300, 300, 400]
# Radha = [700, 300, 400, 600, 500]

# Test whether the average sales of the Saurav, Naveen, and Radha differ in size at a 95% confidence level.

import numpy as np
import pandas as pd
from scipy.stats import f_oneway

Saurav = [300, 400, 300, 500, 50]
Naveen = [600, 300, 300, 400]
Radha = [700, 300, 400, 600, 500]

fstat, pvalue = f_oneway(Saurav, Naveen, Radha)
print(f"F-statistic: {fstat:.4f}")
print(f"P-value: {pvalue:.4f}")
alpha = 1-0.95
if pvalue < alpha:
    print("Reject the null hypothesis: There is a difference in the average sales of Saurav, Naveen, and Radha.")
else:
    print("Fail to reject the null hypothesis: No difference in the average sales of Saurav, Naveen, and Radha.")
