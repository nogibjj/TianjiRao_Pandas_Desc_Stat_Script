import pandas as pd

def desc_df():
    data = {'price': [22000, 27000, 25000, 29000, 35000]
        }
    df = pd.DataFrame(data)
    return df.describe()