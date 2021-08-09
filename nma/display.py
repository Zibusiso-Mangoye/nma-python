import numpy as np
import pandas as pd


def display(data, col=[]):
    """
    Displays results as a table
    INPUT : data to be displayed; columns to used in the table
    OUTPUT : displays a pandas dataframe
    """
    # Creating a dataframe
    df = pd.DataFrame(data, columns=col)

    # print dataframe.
    print(df)
