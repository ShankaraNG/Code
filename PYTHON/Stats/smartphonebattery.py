# Consumer Reports publishes reviews and comparisons of products based on results from its laboratory.
# Data from their website gave the following table for battery lives in hours, for samples of smartphones made by four different mobile companies.

# Brand_A = [19.60, 18.82, 19.00, 18.45, 19.79, 19.03, 17.89, 19.42]
# Brand_B = [21.10, 20.00, 20.43, 19.67, 18.99, 19.98, 20.14, 19.78]
# Brand_C = [10.31, 10.02, 9.41, 9.89, 10.05, 10.52, 11.02, 10.42]
# Brand_D = [17.02, 16.71, 17.78, 18.65, 15.98, 17.63, 17.00, 16.78, 16.92, 17.14]
# At a 2% significance level, does the data provide sufficient evidence to conclude that there is a significant difference in the mean battery life, among the four brands?

# And, if significant, then perform pairwise T-tests to identify which pairs of smartphone brands offer a different mean battery life.

from scipy.stats import f_oneway, ttest_ind
from itertools import combinations
import numpy as np
import pandas as pd

Brand_A = [19.60, 18.82, 19.00, 18.45, 19.79, 19.03, 17.89, 19.42]
Brand_B = [21.10, 20.00, 20.43, 19.67, 18.99, 19.98, 20.14, 19.78]
Brand_C = [10.31, 10.02, 9.41, 9.89, 10.05, 10.52, 11.02, 10.42]
Brand_D = [17.02, 16.71, 17.78, 18.65, 15.98, 17.63, 17.00, 16.78, 16.92, 17.14]

fpath, pvalue = f_oneway(Brand_A, Brand_B, Brand_C, Brand_D)
print(f"F-statistic: {fpath:.4f}")
print(f"P-value: {pvalue:.4f}")
alpha = 0.02
if pvalue < alpha:
    print("Reject the null hypothesis: There is a significant difference in the mean battery life among the four brands.")
    brand_data = {
    'A': Brand_A,
    'B': Brand_B,
    'C': Brand_C,
    'D': Brand_D
    }

    # Run pairwise t-tests
    results = []
    p_values = []

    for (brand1, brand2) in combinations(brand_data.keys(), 2):
        t_stat, p_val = ttest_ind(brand_data[brand1], brand_data[brand2])
        results.append((brand1, brand2, t_stat, p_val))
        p_values.append(p_val)
        
    for i, (brand1, brand2, t_stat, raw_p) in enumerate(results):
        p_val1 = p_values[i]
        print(f"{brand1} vs {brand2} → t-stat = {t_stat:.4f}, raw p = {raw_p:.4f}, adjusted p = {p_val1:.4f}")
        if p_val1 < 0.02:
            print(" Significant differennce", p_val1)
        else:
            print("No significant difference")
else:         
    print("Fail to reject the null hypothesis: No significant difference in the mean battery life among the four brands.")
