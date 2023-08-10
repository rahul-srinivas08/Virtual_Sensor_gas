import pandas as pd
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np # linear algebra
import matplotlib 
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns
def proc(df):
    print(df.shape,"shape of dataframe")
    print(df.dtypes)
    print("checking for null values")
    print(df.isnull().sum())
    print("visuall of null values, ok no null values")
    sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
    



    