import pandas as pd
from src.utils.file_utils import ler_csv
from src.validate.functions import verificar_nulos, verificar_duplicados, verificar_td, verificar_val_minimo
from src.utils.reject_utils import salvar_rejeitados, reject_reason

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

#4 (Products)
print(verificar_nulos(pt, "PRODUCTS"))
print()
print(verificar_duplicados(pt,"product_id", "PRODUCTS"))
print("-" * 20)

#Criar DataFrame para acumular os registros rejeitados:
rejeitados_order_items = pd.DataFrame()

#Validar coluna quantity:
reject_quant = verificar_val_minimo(oi, "quantity", 0, False)
reject_quant = reject_reason(reject_quant, "quantity menor ou igual a zero")

#Validar coluna unit_price:
reject_unit_price = verificar_val_minimo(oi, "unit_price", 0, True)
reject_unit_price = reject_reason(reject_unit_price, "unit_price menor que 0")

#Concatenar registros rejeitados:
rejeitados_order_items = pd.concat([reject_quant, reject_unit_price])

#Agrupar os motivos de rejeição na mesma linha:
motivos = rejeitados_order_items.groupby("order_item_id")["rejection_reason"].agg("; ".join)
motivos_df = motivos.reset_index()

#Remover a coluna de motivo anterior:
dados_rejeitados = rejeitados_order_items.drop(columns=["rejection_reason"])

#Unir os dados rejeitados aos motivos consolidados:
dados_rejeitados = dados_rejeitados.merge(motivos_df, on="order_item_id")

#Remover registros duplicados por order_item_id
dados_rejeitados.drop_duplicates(subset=["order_item_id"], inplace=True)

#Enviar dados rejeitados para um csv:
salvar_rejeitados(dados_rejeitados, "../../data/rejected/rejected_data.csv")
