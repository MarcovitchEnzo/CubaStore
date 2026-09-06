from src.utils.file_utils import ler_csv

#Validação dos dados em .csv

#1 (Customers)
cm = ler_csv("../../data/raw/customers.csv")
print("NULOS EM CUSTOMERS:")
print(cm.isnull().sum())
print("-" * 20)

#2 (Order_Items)
oi = ler_csv("../../data/raw/order_items.csv")
print("NULOS EM ORDER_ITEMS:")
print(oi.isnull().sum())
print("-" * 20)

#3 (Orders)
os = ler_csv("../../data/raw/orders.csv")
print("NULOS EM PEDIDOS:")
print(os.isnull().sum())
print("-" * 20)

#4
pt = ler_csv("../../data/raw/products.csv")
print("NULOS EM PRODUCTOS:")
print(pt.isnull().sum())
print("-" * 20)
