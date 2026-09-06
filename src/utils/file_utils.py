import pandas as pd
import os


def ler_csv(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError("Arquivo não encontrado: " + caminho_arquivo)

    try:
        df = pd.read_csv(caminho_arquivo)
        return df
    except Exception:
        raise Exception("Erro ao ler o arquivo: " + caminho_arquivo)


clientes = ler_csv("../../data/raw/customers.csv")
print(clientes)