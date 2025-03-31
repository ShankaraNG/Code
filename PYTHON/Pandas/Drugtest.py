# You are testing two drugs as a remedy. Drug A is effective in 41 out of a sample of 195. Drug B works on 351 out of 605 people.

# Are the two drugs comparable in terms of effectiveness? Use a 5% significance level for testing.


# Perform an appropriate test.

from statsmodels.stats.proportion import proportions_ztest
from math import sqrt
from scipy.stats import norm
import numpy as np

# Given data
x1 = 41
n1 = 195 
x2 = 351 
n2 = 605 
pofa = x1 / n1 
pofb = x2 / n2 
pcap = (x1 + x2) / (n1 + n2)
se = sqrt(pcap * (1 - pcap) * (1 / n1 + 1 / n2))
z = (pofa - pofb) / se
print("The Z score for the test is", z)
alpha = 0.05
p = 2 * (1 - norm.cdf(abs(z)))
print("The p-value is", p)
if p < alpha:
    print("Reject the Null Hypothesis")
else:
    print("Fail to Reject the Null Hypothesis")
    
x1=41
n1=195
x2=351
n2=605
z_stat, p_value = proportions_ztest(count=[x2, x1], nobs=[n2, n1])

print(p_value)

if(p_value<alpha):
    print("Reject the Null Hypothesis")
else:
    print("Failed to Reject the Null Hypothesis")
    
    


#############Difference between the manual method and the library method is for the following reason#####

# The reason you are seeing different Z-values and p-values between the manual calculation and the proportions_ztest from statsmodels can be attributed to the way the test is performed internally in the proportions_ztest function versus the manual method.
# Let me explain the differences in more detail:
# 1. Z-Value Calculation:
# Both approaches should theoretically use the same formula for calculating the Z-value:
# Z=p^A−p^BStandard ErrorZ = \frac{{\hat{p}_A - \hat{p}_B}}{{\text{{Standard Error}}}}Z=Standard Errorp^A−p^B 
# Where:
# •	p^A\hat{p}_Ap^A and p^B\hat{p}_Bp^B are the sample proportions.
# •	The standard error (SE) is calculated using the pooled proportion, which combines the proportions of both groups.
# The formula for the standard error in the two-proportion Z-test is:
# SE=p^pool(1−p^pool)(1n1+1n2)SE = \sqrt{{\hat{p}_{\text{pool}} \left( 1 - \hat{p}_{\text{pool}} \right) \left( \frac{1}{n_1} + \frac{1}{n_2} \right)}}SE=p^pool(1−p^pool)(n11+n21) 
# Where:
# •	p^pool\hat{p}_{\text{pool}}p^pool is the pooled proportion, calculated as x1+x2n1+n2\frac{{x_1 + x_2}}{{n_1 + n_2}}n1+n2x1+x2.
# The differences in Z-values typically arise from slightly different ways of calculating the pooled proportion, standard error, or from small rounding differences in floating-point operations.
# 2. p-Value Calculation:
# The p-value is computed based on the Z-value using the cumulative distribution function (CDF) of the standard normal distribution:
# p=2(1−Φ(∣Z∣))p = 2 \left( 1 - \Phi(|Z|) \right)p=2(1−Φ(∣Z∣)) 
# Where:
# •	Φ(∣Z∣)\Phi(|Z|)Φ(∣Z∣) is the CDF of the standard normal distribution evaluated at the absolute value of the Z-score.
# In both cases, the p-value calculation should be essentially the same, but small differences in precision between the manual calculation and proportions_ztest could lead to slight differences in the final p-value.
# Why the Differences in Results?
# 1.	Precision and Internal Handling: The proportions_ztest function internally may use higher precision or different numerical methods (such as more accurate approximations of the CDF or adjustments to improve numerical stability). For example, it may use internal checks to adjust for small values or improve the precision of the calculations.
# o	The Z-value from the proportions_ztest could differ slightly from your manual calculation due to such internal adjustments.
# o	p-value differences arise because the proportions_ztest may use more precision or handle edge cases differently (like very small p-values).
# 2.	Z-value Magnitude: The manual calculation results in a Z-score of -8.99, which is highly negative and suggests a very significant difference between the two sample proportions. The Z-value is large in magnitude, so the p-value is extremely small, leading to a rejection of the null hypothesis.
# The p-value is calculated as 000 in the manual approach because the computed Z-value is so extreme. This means the difference between the two proportions is so large that the p-value is effectively 000. This is a typical behavior when the observed difference is very large.
# In the proportions_ztest, the computed p-value is extremely small (2.566230446480293e-19), which is essentially 0, leading to the same conclusion: reject the null hypothesis.
# 3.	Rounding Errors: The very small differences you are seeing in the p-values (0.0 vs 2.566230446480293e-19) are likely due to rounding errors or floating-point precision. The proportions_ztest might not round the result to the nearest zero in the same way your manual approach does.
# In Summary:
# •	The Z-values may differ slightly due to internal optimizations or precision handling in proportions_ztest.
# •	The p-values can differ because of the method used in calculating them or how the result is rounded.
# •	Both methods essentially conclude the same thing, which is that the difference between the two proportions is statistically significant (p-value close to 0, rejecting the null hypothesis).
# If you'd like to get the same Z-value and p-value as proportions_ztest, it’s best to rely on the function itself, as it takes care of many nuances in the calculation and is optimized for accuracy.
# In practice, the small differences in results are not significant, and both methods lead to the same conclusion about rejecting the null hypothesis.
