# The Chai Point stall at Bengaluru airport estimates that each person visiting the store drinks an average of 1.7 small cups of tea.

# Assume a population standard deviation of 0.5 small cups. A sample of 30 customers collected over a few days averaged 1.85 small cups of tea per person.

# Test the claim using an appropriate test at an alpha = 0.05 significance value, with a critical z-score value of ±1.96.

# Note: Round off the z-score to two decimal places.

from scipy.stats import norm
import math
from statsmodels.stats.weightstats import _zstat_generic

Ho = "Average is equal to 1.7 small cups of tea"
Ha = "Average is not equal to 1.7 small cups of tea"

U = 1.7
sigma = 0.5
n = 30
xbar = 1.85
alpha = 0.05

z = (xbar-U)/(sigma/math.sqrt(n))

def predectionmethod1(z,alpha,Ho,Ha):
    print("From Prediction method 1")
    pvalue = 1-norm.cdf(z)
    print("The Zstat is", round(z, 2))
    print("The Pvalue is ", pvalue)
    if(pvalue<alpha):
        print("Reject Null Hypothesis")
        print(Ha)
    else:
        print("Failed to Reject Null Hypothesis")
        print(Ho)


def predectionmethod2(U,sigma,n,xbar,alpha,Ho,Ha):
    print("From Prediction method 2")
    standarerror = sigma/(math.sqrt(n))
    zstat, pvalue = _zstat_generic(xbar, U, standarerror, alternative='larger', diff=0)
    print("The Zstat is", round(zstat,2))
    print("The Pvalue is ", pvalue)
    if(pvalue<alpha):
        print("Reject Null Hypothesis")
        print(Ha)
    else:
        print("Failed to Reject Null Hypothesis")
        print(Ho)


predectionmethod1(z,alpha,Ho,Ha)
predectionmethod2(U,sigma,n,xbar,alpha,Ho,Ha)
