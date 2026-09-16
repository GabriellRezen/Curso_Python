#Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra

palavra = "amanda"
count = 0

for letra in palavra:
    if letra == "a":
        count += 1

print("A letra 'a' aparece", count, "vezes.")
