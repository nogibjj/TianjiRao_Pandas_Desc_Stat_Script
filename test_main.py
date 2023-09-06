from main import desc_df
import pandas as pd

data = {'price': [22000, 27000, 25000, 29000, 35000]
        }

df = pd.DataFrame(data)

def test_main(df):
    desc = desc_df(df)
    assert desc.loc['count'][0] == 5.0
    assert desc.loc['mean'][0] == 27600.0
    assert desc.loc['min'][0] == 22000.0