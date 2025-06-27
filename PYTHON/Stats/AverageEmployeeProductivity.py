import numpy as np
from scipy.stats import kstest
import pandas as pd
import pingouin as pg


Work_Condition = ['Office', 'Office', 'Office', 'Office', 'Office', 'Office', 'Office', 'Office', 'Office', 'Office', 'Office', 'Office','Remote', 'Remote', 'Remote', 'Remote', 'Remote', 'Remote','Remote', 'Remote', 'Remote', 'Remote', 'Remote', 'Remote']

Management_Style = ['Directive', 'Autonomous', 'Collaborative', 'Collaborative', 'Directive', 'Directive', 'Autonomous', 'Autonomous', 'Directive', 'Autonomous', 'Autonomous', 'Autonomous', 'Collaborative','Collaborative', 'Collaborative', 'Autonomous', 'Collaborative','Collaborative', 'Directive', 'Autonomous', 'Directive','Directive', 'Directive', 'Collaborative']

Productivity_Score = [79, 75, 93, 68, 77, 71, 91, 83, 86, 92, 66, 74, 77, 94, 89, 85, 70, 92, 92, 76, 76, 84, 94, 94]

data = {
    'Work_Condition': Work_Condition,
    'Management_Style': Management_Style,
    'Productivity_Score' : Productivity_Score
    }

data_df = pd.DataFrame(data)


def prediction(data_df):
    model =pg.anova(data=data_df, dv='Productivity_Score', between=['Work_Condition', 'Management_Style'],ss_type=2)
    print(model)
    pvalue = model['p-unc'][2]
    print(pvalue)
    alpha = 0.05
    if(pvalue<alpha):
        print("Reject Null Hypothesis")
    else:
        print("Failed to Reject Null Hypothesis")

prediction(data_df)
