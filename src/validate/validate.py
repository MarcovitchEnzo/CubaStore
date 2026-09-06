from src.utils.file_utils import ler_csv
print()
print("-" * 20)

#Validação dos dados em .csv

#Leitura dos Dados
cm = ler_csv("../../data/raw/customers.csv")
oi = ler_csv("../../data/raw/order_items.csv")
os = ler_csv("../../data/raw/orders.csv")
pt = ler_csv("../../data/raw/products.csv")

#1 (Customers)
print("NULOS EM CUSTOMERS:")
print(cm.isnull().sum())
print()
print("DUPLICADOS EM CUSTOMERS:")
print("ID:",cm["customer_id"].duplicated().sum())
print("E-MAIL:",cm["email"].duplicated().sum())
print("-" * 20)

#2 (Order_Items)
print("NULOS EM ORDER_ITEMS:")
print(oi.isnull().sum())
print()
print("DUPLICADOS EM ORDER_ITEMS:")
print("ID:",oi["order_item_id"].duplicated().sum())
#Verificação se todos os order_items.order_id estão em orders.order_id. (REF1)
#Verificação se todos os order_items.product_id estão em products.product_id. (REF2)
print("REFERÊNCIAS INVÁLIDAS:")
print("REF1:",(~oi["order_id"].isin(os["order_id"])).sum())
print("REF2:",(~oi["product_id"].isin(pt["product_id"])).sum())
print("-" * 20)

#3 (Orders)
print("NULOS EM ORDERS:")
print(os.isnull().sum())
print()
print("DUPLICADOS EM ORDERS:")
print("ID:",os["order_id"].duplicated().sum())
#Verificação se todos os orders.customer_id estão em customers.customer_id.
print("REFERÊNCIAS INVÁLIDAS:")
print("REF:",(~os["customer_id"].isin(cm["customer_id"])).sum())
print("-" * 20)

#4
print("NULOS EM PRODUCTS:")
print(pt.isnull().sum())
print()
print("DUPLICADOS EM PRODUCTS:")
print("ID:",pt["product_id"].duplicated().sum())
print("-" * 20)
