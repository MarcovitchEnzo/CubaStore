from src.utils.file_utils import ler_csv
from src.validate.functions import verificar_nulos, verificar_duplicados, verificar_td

print()
print("-" * 20)

#Validação dos dados em .csv

#Leitura dos Dados
cm = ler_csv("../../data/raw/customers.csv")
oi = ler_csv("../../data/raw/order_items.csv")
os = ler_csv("../../data/raw/orders.csv")
pt = ler_csv("../../data/raw/products.csv")

#1 (Customers)
print(verificar_nulos(cm, "CUSTOMERS"))
print()
print(verificar_duplicados(cm,"customer_id", "CUSTOMERS"))
print("-" * 20)

#2 (Order_Items)
print(verificar_nulos(oi, "ORDER ITEMS"))
print()
print(verificar_duplicados(oi,"order_item_id", "ORDER ITEMS"))
print()
#Verificação se todos os order_items.order_id estão em orders.order_id. (REF1)
#Verificação se todos os order_items.product_id estão em products.product_id. (REF2)
print(verificar_td(oi, "order_id", "ORDER ITEMS", os, "order_id", "ORDERS"))
print(verificar_td(oi, "product_id", "ORDER ITEMS", pt, "product_id", "PRODUCTS"))
print("-" * 20)

#3 (Orders)
print(verificar_nulos(os, "ORDERS"))
print()
print(verificar_duplicados(os,"order_id", "ORDERS"))
print()
#Verificação se todos os orders.customer_id estão em customers.customer_id.
print(verificar_td(os, "customer_id", "ORDERS", cm, "customer_id", "CUSTOMERS"))
print("-" * 20)

#4
print(verificar_nulos(pt, "PRODUCTS"))
print()
print(verificar_duplicados(pt,"product_id", "PRODUCTS"))
print("-" * 20)
