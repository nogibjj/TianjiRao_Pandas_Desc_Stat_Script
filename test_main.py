from main import desc_df, bar_plot
import pandas as pd
import matplotlib as plt

# Elextrix Vehicle Population Data
df = pd.read_csv('Electric_Vehicle_Population_Data.csv')


def test_desc_df():
    # mean
    assert desc_df(df).loc['mean', 'Electric Range'] == 70.49573804284242
    # median
    assert desc_df(df).loc['50%', 'Model Year'] == 2021.0
    # standard deviation
    assert desc_df(df).loc['std', 'Electric Range'] == 97.1287349778698

    
    
def test_bar_plot():    
    # Here we can focus on the visualization of Electric Range using a bar plot
    bar_plot(df['Electric Range'])


