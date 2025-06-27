# It is known that the mean IQ of high school students is 100, and the standard deviation is 15.

# A coaching institute claims that candidates who study there have more IQ than an average high school student. When the IQ of 50 candidates was calculated, the average turned out to be 110

# Conduct an appropriate hypothesis test to test the institute’s claim, with a significance level of 5%


from scipy.stats import norm
import math
from statsmodels.stats.weightstats import _zstat_generic

Ho = "IQ of Students who study in that school is the same for all the average High School Students"
Ha = "IQ of the Students who study in that School is more than that IQ of all the average High School Students"

U = 100
sigma = 15
n = 50
xbar = 110
alpha = 0.05

z = (xbar-U)/(sigma/math.sqrt(n))

def predectionmethod1(z,alpha,Ho,Ha):
    print("From Prediction method 1")
    pvalue = 1-norm.cdf(z)
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
    print("The Pvalue is ", pvalue)
    if(pvalue<alpha):
        print("Reject Null Hypothesis")
        print(Ha)
    else:
        print("Failed to Reject Null Hypothesis")
        print(Ho)


predectionmethod1(z,alpha,Ho,Ha)
predectionmethod2(U,sigma,n,xbar,alpha,Ho,Ha)

