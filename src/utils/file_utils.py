import pandas as pd

def ler_csv(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo)
    return df

clientes = ler_csv("../../data/raw/customers.csv")
print(clientes)