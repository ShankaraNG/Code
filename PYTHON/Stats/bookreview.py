# There is a website, "www.goodreads.com" where people can leave their reviews about a book and rate them on a scale of 1 to 5 stars.
# The following table gives the number of pages of a random sample of books with different ratings, as listed on the site:


# one_star = [382, 391, 335, 368, 400, 372]
# two_star = [560, 343, 512, 329, 391, 367]
# three_star = [384, 458, 409, 309, 374, 459]
# four_star = [325, 390, 304, 240, 306, 169]
# five_star = [360, 298, 272, 368, 320, 326]

# At a 1% significance level, does the data provide sufficient evidence to conclude that there is a difference in the mean number of pages among books in these five rating groups?

from scipy.stats import f_oneway

one_star = [382, 391, 335, 368, 400, 372]
two_star = [560, 343, 512, 329, 391, 367]
three_star = [384, 458, 409, 309, 374, 459]
four_star = [325, 390, 304, 240, 306, 169]
five_star = [360, 298, 272, 368, 320, 326]

fstat, pvalue = f_oneway(one_star, two_star, three_star, four_star, five_star)
print(f"F-statistic: {fstat:.4f}")
print(f"P-value: {pvalue:.4f}")
alpha = 0.01
if pvalue < alpha:
    print("Reject the null hypothesis: There is a difference in the mean number of pages among books in these five rating groups.")
else:
    print("Fail to reject the null hypothesis: No difference in the mean number of pages among books in these five rating groups.")

