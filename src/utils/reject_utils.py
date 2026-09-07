import pandas as pd
import os


def salvar_rejeitados(dados_rejeitados, caminho_arquivo, motivo):
    diretorio = os.path.dirname(caminho_arquivo)

    if diretorio and not os.path.exists(diretorio):
        os.makedirs(diretorio)

    dados_rejeitados["rejection_reason"] = motivo

    if os.path.exists(caminho_arquivo):
        dados_rejeitados.to_csv(caminho_arquivo, mode="a", header=False, index=False)
    else:
        dados_rejeitados.to_csv(caminho_arquivo, index=False)

    return caminho_arquivo
