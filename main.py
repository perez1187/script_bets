import pandas as pd
import numpy as np

def find_duplicates():
    df = pd.read_csv(r"data\active15.csv")
    df2 = pd.read_csv(r"data\candidates15.csv")
    df_main = pd.concat([df,df2])
    df_main['is_ok']=df_main.duplicated(subset=['match','bet', 'outcome'])
    df_main.to_csv(r'data/my_data150522.csv')
    print (df_main)

def __main__():
    find_duplicates()

if __name__ == "__main__":
    __main__()

