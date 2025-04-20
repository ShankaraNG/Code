# The United States is divided into four regions: Northeast, Midwest, South and West regions.

# Independent random samples of households in these regions yielded the data on last year’s energy consumptions.

# a = [13, 8, 11, 12, 11]
# b = [15, 10, 16, 11, 13, 10]
# c = [5, 11, 9, 5]
# d = [8, 10, 6, 5, 7]


# At a 5% significance level, does the data provide sufficient evidence to conclude that there is a difference in last year’s mean energy consumption
# by households among the four regions?

from scipy.stats import f_oneway

a = [13, 8, 11, 12, 11]
b = [15, 10, 16, 11, 13, 10]
c = [5, 11, 9, 5]
d = [8, 10, 6, 5, 7]

fstat, pvalue = f_oneway(a, b, c, d)
print("F-statistic:", fstat)
print("P-value:", pvalue)
alpha = 0.05
if pvalue < alpha:
    print("Reject the null hypothesis: There is a difference in last year's mean energy consumption by households among the four regions.")
else:
    print("Fail to reject the null hypothesis: No difference in last year's mean energy consumption by households among the four regions.")

