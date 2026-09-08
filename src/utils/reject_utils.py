import os


def salvar_rejeitados(dados_rejeitados, caminho_arquivo):
    diretorio = os.path.dirname(caminho_arquivo)

    if diretorio and not os.path.exists(diretorio):
        os.makedirs(diretorio)

    if os.path.exists(caminho_arquivo):
        dados_rejeitados.to_csv(caminho_arquivo, mode="a", header=False, index=False)
    else:
        dados_rejeitados.to_csv(caminho_arquivo, index=False)

    return caminho_arquivo

def reject_reason(dados_rejeitados, motivo):
    dados_rejeitados["rejection_reason"] = motivo
    return dados_rejeitados