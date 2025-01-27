import pandas as pd

df=pd.DataFrame([[1970, 'USA', 224.84, 71.3],[1972, 'Eng', 215.11, 72.7],[1985, 'Germany', 263.93, 75.8],
              [1988, 'France', 267.43, 77.2],[1999, 'USA', 890.77, 80.1],[2001, 'Germany', 1013.34, 80.6],
              [2012, 'Eng', 3114.683, 82.3]] , columns = ['Year', 'Country', 'Spending_USD', 'Life_Expectancy'])

def healthExp(df):
    bins = [1969, 1980, 1990, 2000, 2010, 2021]
    labels = ['(1969, 1980]', '(1980, 1990]', '(1990, 2000]', '(2000, 2010]', '(2010, 2021]']

    df['Year'] = pd.cut(df['Year'], bins=bins, labels=labels, right=False)
    grouped_df = df.groupby(by="Year")['Spending_USD'].mean().to_frame()
    grouped_df = grouped_df.rename(columns={ 'Spending_USD': 'avg_expenditure'})
    grouped_df['avg_expenditure'] = grouped_df['avg_expenditure'].round(3)   
    
    print(grouped_df)
    
healthExp(df)
