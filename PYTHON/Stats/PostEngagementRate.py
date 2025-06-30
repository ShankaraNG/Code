
# As a social media analyst, you want to compare the engagement rates of posts from two different accounts (Account X and Account Y).

# You collected data on 180 posts from Account X, where 40 received high engagement. Similarly, you collect data on 200 posts from Account Y, where 60 received high engagement.

# Conduct an appropriate test at a 95% confidence interval to determine if there's a significant difference in high engagement proportions between the two accounts.



import numpy as np
import statsmodels.api as sm

# Account X data
success_X = 40
sample_size_X = 180

# Account Y data
success_Y = 60
sample_size_Y = 200

# Perform the two-proportion Z-test
z_stat, p_value = sm.stats.proportions_ztest([success_X, success_Y], [sample_size_X, sample_size_Y], alternative='two-sided')

# Significance level
alpha = 0.05

# Print the results
print(f"Z-statistic: {z_stat}")
print(f"P-value: {p_value}")

# Interpret the results
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference in high engagement proportions between the two accounts.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in high engagement proportions between the two accounts.")
