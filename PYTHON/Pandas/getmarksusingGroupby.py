import pandas as pd

data = {
    'roll_no': [1, 2, 1, 3, 1, 3, 3, 3, 2, 2, 1, 2],
    'subject': ['NN', 'DL', 'ML', 'Prob', 'DL', 'ML', 'DL', 'NN', 'NN', 'Prob', 'Prob', 'ML'],
    'marks': [97, 63, 63, 71, 64, 90, 66, 46, 74, 62, 94, 67]
}

df = pd.DataFrame(data)

def get_marks(df):
    
    max_marks = df.groupby('subject')['marks'].aggregate('max')
    max_marks = max_marks.reset_index()
    result = pd.merge(df, max_marks, on=['subject', 'marks'], how='inner')
    print(result)
    
get_marks(df)
