# %%

#lista em python não são arrays
idades = [28,42,43,35,39,28,38]
print(idades)

# %%

teo = ["teo","calvo",32,True,"casado", 2342.98]
print(teo)

# %%

type(teo)

# %%
#idade
print(teo[2])
#renda
print(teo[5])
#nome
print(teo[0])

# %%

idades = [28,42,43,35,39,28,38,42,34]

print("soma idades:", sum(idades)) 

print("qtde idade:", len(idades))

print("media idades:", sum(idades)/len(idades))

print("menor idades:", min(idades))

# %%

teo = ["Teo Calvo",32,True,"Casado",["estagiario","ds jr","ds pl","ds sr","head"],[1500, 4000, 4550, 6500, 10000],["Ana","Maria","Claudia"]]

print("Tamanho de teo:", len(teo))

print(teo[6][0])

exs = teo[6]
primeira_ex = exs[0]
print(primeira_ex)
# %%

tamanho = len(teo)
pos = tamanho - 1

exs = teo[pos]

teo[pos][len(exs) - 1]
# %%

teo[-1][-1]
teo[-1][-2]
# %%

#primeiros 4 elementos
teo[0:4]

# %%

teo[4][3:5]

# %%

teo[4][-2:]

# %%

salarios = teo[5]
salarios[::-1]
# %%
