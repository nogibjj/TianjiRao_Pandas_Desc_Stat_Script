# import pandas as pd
import matplotlib.pyplot as plt

def desc_df(df):
    return df.describe()

def bar_plot(df):
    df.plot(kind="bar")
    plt.show()
    
    
def bar_plot_save(df):
    df.plot(kind="bar")
    plt.savefig("bar.png")
    
def save_to_md(df):
    tab1 = df.describe()
    bar_plot_save(df)
    with open("summary.md", "w", encoding="utf-8") as file:
        file.write("Statistical Describe:\n")
        file.write(tab1)
        file.write("\n\n") 
        file.write("![Bar Plot](bar.png)\n")
