import pandas as pd
import seaborn as sns 
import matplotlib as plt 
import numpy as np
import os

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


mainpath = '/Users/laar/Documents/Pyth_on/KAGGLE/Amazon_degradation/'
area  = pd.read_csv(os.path.join(mainpath, 'def_area_2004_2019.csv'), header = 0)
 
defor =  pd.read_excel(os.path.join(mainpath, 'deforestation_Brazil.xlsx'), header = 0)
fires = pd.read_csv(os.path.join(mainpath, 'inpe_brazilian_amazon_fires_1999_2019.csv'), header = 0)

defor.describe()

