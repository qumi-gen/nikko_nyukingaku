import pandas as pd

df = pd.read_csv('nikko.csv')

df['預り（入金）'] = df['預り（入金）'].str.replace(',', '')

nyukin = df[df['摘要'].isin(['ATM 三菱UFJ'])].copy()

nyukin['預り（入金）'].astype(int).sum()
