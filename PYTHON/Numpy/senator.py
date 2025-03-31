# A state senator cannot decide how to vote on an environmental protection bill.

# The senator decides to request a survey and if the proportion of registered voters supporting the bill exceeds 0.60, she will vote for it.

# A random sample of 750 voters is selected and 495 are found to support the bill.

# Conduct an appropriate test at a 90% confidence interval.


from statsmodels.stats.weightstats import ztest
from math import sqrt
from scipy.stats import norm

pcap=498/750
p=0.60
alpha=0.90
z=((pcap-p)/sqrt((pcap*(1-p))/750))

pvalue=1-norm.cdf(z)

print(pvalue)
if(pvalue<alpha):
    print("Reject the Null Hypothesis")
else:
    print("Failed to reject the Null Hypothesis")
