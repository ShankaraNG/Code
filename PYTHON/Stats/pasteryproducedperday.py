# A French cafe has historically maintained that their average daily pastry production is at most 500.

# With the installation of a new machine, they assert that the average daily pastry production has increased. The average number of pastries produced per day over a 70-day period was found to be 530.

# Assume that the population standard deviation for the pastries produced per day is 125.

# Perform a z-test with the critical z-value = 1.64 at the alpha (significance level) = 0.05 to evaluate if there's sufficient evidence to support their claim of the new machine producing more than 500 pastries daily.

# Note: Round off the z-score to two decimal places.


from scipy.stats import norm
import math
from statsmodels.stats.weightstats import _zstat_generic

Ho = "Pastery Produced per day is equal to 500"
Ha = "Pastery produced per day is more than 500"

U = 500
sigma = 125
n = 70
xbar = 530
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
