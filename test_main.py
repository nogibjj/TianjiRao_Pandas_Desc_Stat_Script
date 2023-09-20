from main import desc_df, bar_plot
import pandas as pd

# Elextrix Vehicle Population Data
# df = pd.read_csv("Electric_Vehicle_Population_Data.csv")


def test_desc_df():
    df = pd.read_csv("Electric_Vehicle_Population_Data.csv")
    # mean
    assert desc_df(df).loc["mean", "Electric Range"] == 70.49573804284242
    # median
    assert desc_df(df).loc["50%", "Model Year"] == 2021.0
    # standard deviation
    assert desc_df(df).loc["std", "Electric Range"] == 97.12873497790751


def test_bar_plot():
    df = pd.read_csv("Electric_Vehicle_Population_Data.csv")
    # Here we can focus on the visualization of Electric Range using a bar plot
    # Since the data set is too large to run in codespace, 
    # here we only use the first 100 observation as an example
    bar_plot(df["Electric Range"][:100])


if __name__ == "__main__":
    test_bar_plot()
    # test_desc_df()