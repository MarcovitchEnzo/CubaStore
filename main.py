import pandas as pd

df=pd.read_csv("data/raw/customers.csv")
print(df)
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.head(2))
print(df.tail(2))
print(df[["name","city"]])
