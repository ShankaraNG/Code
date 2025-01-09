# Given a dataframe below about customer review & ratings.



# Return a subset of the dataframe with records having rating >= 6, containing the columns "profession", "gender" and "age" only.

# Input Format:

# A DataFrame
# Output Format:

# Subset Dataframe
# Sample Input:

# {'name':["Sam","Roma","Mark"], "profession":['dev','mle','Data scientist'],"gender":['male','female','male'], "age":[21,20,25],"review":['No comments','hardworker','need improvement'],"rating":[10,5,7]}
# Sample Output:



# Sample Explanation:

# The first and third rows with names 'Sam' and 'Mark' have ratings greater than or equal to 6.



import pandas as pd
def filtered_customers(df):
    ''' df is a dataframe with columns ['name', 'profession', 'gender', 'age', 'review', 'rating']
        Output -> A dataframe with required rows is expected to be returned'''

    # YOUR CODE GOES HERE
    # Filter the dataframe having ratings>=6 and choose the required columns
    x=df['rating'] >= 6
    new_df=df[x]
    print(new_df[['profession','gender','age']])
    


a={'name':["Sam","Roma","Mark"], "profession":['dev','mle','Data scientist'],
   "gender":['male','female','male'], "age":[21,20,25],"review":['No comments','hardworker','need improvement'],"rating":[10,5,7]}

filtered_customers(pd.DataFrame(a))
