# Faça um programa que vende uma garrafa de água:
# Se o clinete escolher água natural, será cobrado R$1,50
# Se o cliente escolher água com gás, será cobrado R$2,50

texto = """
Escolha a sua água para comprar
(1) Água natural
(2) Água com gás
"""
opcao = input(texto)

conta = 0
if opcao == "1":
    conta = 1.5
elif opcao == "2":
    conta = 2.5

if conta == 0:
    print("Entre com a opção correta, por favor.")
else:
    print("Sua conta é: R$", conta)