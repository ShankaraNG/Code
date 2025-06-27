import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols


data = {
    "Fertilizer": ['A', 'A', 'A', 'B', 'B', 'B',
                   'A', 'A', 'A', 'B', 'B', 'B',
                   'A', 'A', 'A', 'B', 'B', 'B'],
    "Watering_Frequency": ['Low', 'Medium', 'High', 'Low', 'Medium', 'High',
                           'Low', 'Medium', 'High', 'Low', 'Medium', 'High',
                           'Low', 'Medium', 'High', 'Low', 'Medium', 'High'],
    "Plant_Height": [15.2, 20.7, 24.3, 18.4, 23.1, 26.5,
                     32.7, 21.7, 27.3, 38.4, 33.1, 36.5,
                     12.2, 22.7, 35.3, 28.4, 22.1, 24.5]
}

df = pd.DataFrame(data)

def FertilizersandEffect(data):
    model = ols('Plant_Height ~ C(Watering_Frequency) * C(Fertilizer)', data=data).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    print(anova_table)
    pvalue = anova_table['PR(>F)'].iloc[2]
    if(pvalue < 0.05):
        print("Reject the Null Hypothesis")
    else:
        print("Failed to Reject the Null Hypothesis")

FertilizersandEffect(df)
