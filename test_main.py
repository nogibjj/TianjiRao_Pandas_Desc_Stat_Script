from main import desc_df
import pandas as pd

# 
df = pd.read_csv()


def test_main():
    desc = desc_df(df)
    assert desc.loc['count'][0] == 5.0
    assert desc.loc['mean'][0] == 27600.0
    assert desc.loc['min'][0] == 22000.0




