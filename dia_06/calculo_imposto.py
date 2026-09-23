# %%

def calc_impost(preco:float, tx_base:float, **kwargs):
    imposto = preco * tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]

    return imposto

#%%

calc_impost(100, 0.03, municipio=0.01, estadual=0.005, nacional=0.001)
# %%
