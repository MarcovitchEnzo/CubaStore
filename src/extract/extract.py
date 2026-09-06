import pandas as pd

#Leitura dos Dados
cm = pd.read_csv("../../data/raw/customers.csv")
oi = pd.read_csv("../../data/raw/order_items.csv")
os = pd.read_csv("../../data/raw/orders.csv")
pt = pd.read_csv("../../data/raw/products.csv")

#Exibição
print(cm.head(2))
print(oi.head(2))
print(os.head(2))
print(pt.head(2))

