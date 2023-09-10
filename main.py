# import pandas as pd
import matplotlib.pyplot as plt

def desc_df(df):
    return df.describe()

def bar_plot(df):
    df.plot(kind="bar")
    plt.show()