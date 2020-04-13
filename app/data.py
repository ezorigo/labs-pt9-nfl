import pandas as pd 

data = pd.read_csv('data/players_full1.csv')

week1 = pd.read_csv('data/predictions-week1.csv')
week1 = week1.set_index('player')