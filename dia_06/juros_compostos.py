# %%

def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    """ juros_copmpostos serve para calcular o retorno financeiro apartir de um
    aporte, deve considera o valor de aporte, a taxa de juros atual e o tempo (em anos)
    para cálculo do valor a ser retornado.

    aporte: 
        um número que represente o valor em R$

    taxa:
        um número em float entre 0 e 1 que represente o valor taxa de juros
    
    anos:
        um número inteiro >= 1 que representa o tempo que o investimento terá liquidez
    """
    return aporte * (1 + taxa) ** anos

#%%

juros_compostos(aporte=1000, taxa=0.13, anos=4)
# %%
