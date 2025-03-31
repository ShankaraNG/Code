

# The Head of Data Analyst Department is conducting a comparative analysis of the complexity of SQL queries written by two analysts, namely Analyst X and Analyst Y.

# He has gathered data on the number of lines of code for each SQL query.

# Analyst X's SQL lines of code: [15, 18, 20, 17, 16, 19, 22, 16, 18, 21, 23, 18, 17, 19, 20, 24, 25, 26, 27, 28, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# Analyst Y's SQL lines of code: [14, 17, 19, 16, 15, 18, 21, 15, 17, 20, 22, 17, 16, 18, 19, 23, 24, 25, 26, 27, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# The analyst hypothesizes that Analyst Y writes less complex code compared to Analyst X. To investigate this hypothesis, conduct an appropriate test with a 90% confidence interval.


from statsmodels.stats.weightstats import ztest

a= [15, 18, 20, 17, 16, 19, 22, 16, 18, 21, 23, 18, 17, 19, 20, 24, 25, 26, 27, 28, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
b= [14, 17, 19, 16, 15, 18, 21, 15, 17, 20, 22, 17, 16, 18, 19, 23, 24, 25, 26, 27, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]


zscore , pvalue = ztest(x1=a,x2=b,alternative="larger")
print(pvalue)
alpha=0.01
if(pvalue<alpha):
    print("Reject the Null Hypothesis")
else:
    print("Failed to reject the Null Hypothesis")
    
