# %%

lista = [2, 132, "teo", ["ds", "de", "da"], True]

lista [2]
# %%

# dicionares são pares de chave e valor

dados_teo = {"sobrenome":"calvo",
             "nome":"teo", 
             "filhos":True,
             "formacao":["estatistica", "bigdata datascience"],
             "cargos":[
                 {"nome": "ds jr", "empresa": "tapps"},
                 {"nome": "ds pl", "empresa": "sas"},
                 {"nome": "ds sr", "empresa": "boticario"},
                 {"nome": "ds espec.", "empresa": "via varejo"},
                 ]
             }

print(dados_teo)

#%%

print(dados_teo["formacao"][-1])
print(dados_teo["cargos"][-1]["empresa"])

# %%
dados_teo["estado civil"] = "casado"

print(dados_teo)
# %%
print("chaves:", dados_teo.keys())
print("valores", dados_teo.values())
print("itens:", dados_teo.items())

# %%
for i in [10,20,45,38,"Teo"]:
    print(i)

# %%
for i in dados_teo:
    print(i, "->", dados_teo[i])
# %%

for chave, valor in dados_teo.items():
    print(chave, "->", valor)