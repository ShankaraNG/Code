import pandas as pd
def location_divide(df):
    '''
    input:
    df -> the dataframe provided to the function
    
    output:
    df_new -> the new preprocessed dataframe
    '''
    
    ### STEP 1: Split the values into 2 columns
    
    df_new = df['City\tState'].str.split("\t", expand = True)
    
    ### STEP 2: Split the column name into 2
    df_new.columns = df.columns.str.split("\t", expand = True)
    
    return df_new

df = pd.DataFrame({'City\tState': ["Kolkata\tWest Bengal", "Chennai\tTamil Nadu", "Hyderabad\tTelengana", "Bangalore\tKarnataka"]})
location_divide(df)
