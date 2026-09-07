import pandas as pd
import os


def salvar_rejeitados(dados_rejeitados, caminho_arquivo):
    diretorio = os.path.dirname(caminho_arquivo)

    if diretorio and not os.path.exists(diretorio):
        os.makedirs(diretorio)

    dados_rejeitados.to_csv(caminho_arquivo, index=False)

    return caminho_arquivo
