# A national survey was conducted to obtain information on the alcohol consumption patterns of U.S. adults by marital status.
# A random sample of 1772 residents, aged 18 and older, yielded the data displayed in Table below:
# Test whether Marital status and alcohol consumption are associated with a 5% significance level.

import numpy as np
import pandas as pd
from scipy.stats import chi2, chi2_contingency

#H0: Marital status and drinks are not related
#H1: Marital status and drinks are related

observed = [[67,213,74],
            [411,633,129],
            [85,51,7],
            [27,60,15]]

def expectedlist_df(observed):
    observed = np.array(observed)
    total = np.sum(observed, axis=1)
    total_col = np.sum(observed, axis=0)
    grand_total = np.sum(total)

    expected = np.zeros_like(observed, dtype=float)

    for i in range(observed.shape[0]):
        for j in range(observed.shape[1]):
            expected[i][j] = (total[i] * total_col[j]) / grand_total

    return expected

def chisquare(observed, expected):
    observed = np.array(observed)
    expected = np.array(expected)
    chisq = np.sum((observed - expected) ** 2 / expected)
    return chisq

def driver(observed):
    expected = expectedlist_df(observed)
    chisq = chisquare(observed, expected)
    dof = (len(observed) - 1) * (len(observed[0]) - 1)
    alpha = 0.05
    critical_value = chi2.ppf(1 - alpha, dof)
    pvalue = 1 - chi2.cdf(chisq, dof)

    print("Observed:\n", observed)
    print("Expected:\n", expected)
    print("Chi-square statistic:", chisq)
    print("Degrees of freedom:", dof)
    print("Critical value:", critical_value)
    print("P-value:", pvalue)

    if pvalue < alpha:
        print("Reject the null hypothesis: Marital status and alcohol consumption are associated.")
    else:
        print("Fail to reject the null hypothesis: No association between marital status and alcohol consumption.")
        
driver(observed)


def using_chi2_contingency(observed):
    chi2_stat, p, dof, expected = chi2_contingency(observed)
    alpha = 0.05
    critical_value = chi2.ppf(1 - alpha, dof)

    print("Chi-square statistic:", chi2_stat)
    print("Degrees of freedom:", dof)
    print("Critical value:", critical_value)
    print("P-value:", p)
    print("Expected frequencies:\n", expected)

    if p < alpha:
        print("Reject the null hypothesis: Marital status and alcohol consumption are associated.")
    else:
        print("Fail to reject the null hypothesis: No association between marital status and alcohol consumption.")
        
print("\nUsing chi2_contingency:")
using_chi2_contingency(observed)
