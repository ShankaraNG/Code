# Out of a sample of 1,000 people residing in Maharashtra, 540 are rice eaters, while the rest consume wheat primarily.

# Can we assume that rice and wheat are equally popular in this state at a 5% significance level?


from statsmodels.stats.weightstats import ztest
from math import sqrt
from scipy.stats import norm

n=1000
pcap=540/1000
p=0.5
alpha=0.05
z=((pcap-p)/sqrt((pcap*(1-p))/n))

pvalue=1-norm.cdf(z)

print(pvalue)
if(pvalue<alpha):
    print("Reject the Null Hypothesis")
else:
    print("Failed to reject the Null Hypothesis")
