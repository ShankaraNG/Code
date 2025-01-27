#given the code separate it to morning evening and afternoon and night and take the count of each


import pandas as pd

df = pd.DataFrame([['2019-03-23 20:21:09', '2019-03-23 20:27:24', 1, 1.6], ['2019-03-04 16:11:55', '2019-03-04 16:19:00', 1, 0.79], 
              ['2019-03-27 17:53:01', '2019-03-27 18:00:25', 1, 1.37], ['2019-03-10 01:23:59', '2019-03-10 01:49:51', 1, 7.70], 
              ['2019-03-30 13:27:42', '2019-03-30 13:37:14', 3, 2.16]], columns = ['pickup', 'dropoff', 'passengers', 'distance'])


def timeOfDay(df):
    # Your Code Goes Here
    df['pickup'] = pd.to_datetime(df['pickup']).dt.hour
    bin=[-1,6,12,18,24]
    labels= ['morning', 'day', 'afternoon', 'night']
    df['time_of_day'] = pd.cut(df['pickup'], bins = bin, labels = labels)
    df = df.groupby('time_of_day')['pickup'].aggregate('count').sort_values(ascending=False)
    print(df)


timeOfDay(df)
