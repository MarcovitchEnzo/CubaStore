#Função para verificar nulos:
def verificar_nulos(df, nome):
    val = df.isnull().sum().sum()
    print(f"NULOS EM {nome}:")
    return val

#Função para verificar duplicados:
def verificar_duplicados(df,coluna, nome):
    val = df[coluna].duplicated().sum()
    print(f"DUPLICADOS EM {nome}:")
    return val

#Função para verificar se os dados estão alinhados em tabelas diferentes:
def verificar_td(df1, coluna1, nome1, df2, coluna2, nome2):
    val = (~df1[coluna1].isin(df2[coluna2])).sum()
    print(f"REFERÊNCIAS INVÁLIDAS EM {nome1} → {nome2}:")
    return val

#REGRAS DE NEGÓCIO

#Função para verificar se os valores são iguais ou menores que 0:
def verificar_val_minimo(df, coluna,valor_minimo, igual_permitido):
    if igual_permitido:
        val = df[coluna] < valor_minimo
    else:
        val = df[coluna] <= valor_minimo

    dados_invalidos = df[val]
    return dados_invalidos