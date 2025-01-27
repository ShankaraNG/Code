import pandas as pd

df = pd.DataFrame([['Canada', 70.6, 78.3, 80.2, 82.3, 81.4, 80.3], ['France', 71.8, 74.7, 79.32, 77.2, 80.0, 81.2], 
              ['Germany', 74.8, 74.7, 77.32, 77.2, 80.0, 81.2], ['Japan', 74.9, 74.7, 77.32, 77.8, 82.0, 81.2], 
              ['Korea', 74.1, 74.7, 77.32, 77.2, 80.0, 83.2]], columns = ['Country', 2000, 2001, 2002, 2003, 2004, 2005])



def lifeExp(df):
    melted=pd.melt(df,id_vars=['Country'],var_name='Year', value_name='Life_Expectancy')
    melted=melted.groupby('Year')['Life_Expectancy'].aggregate('mean').sort_values(ascending=False).head(5).reset_index().set_index('Year')
    print(melted)

lifeExp(df)
