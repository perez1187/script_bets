import pandas as pd
import numpy as np

df = pd.read_csv(r"data\active_03_05_22.csv")
df2 = pd.read_csv(r"data\oferta_20220503.csv")
df_main = pd.concat([df,df2])
df_main['is_ok']=df_main.duplicated(subset=['match','bet', 'outcome'])
#df_main.to_csv(r'data/my_data3.csv')
print (df_main)

# todo chuj chuj