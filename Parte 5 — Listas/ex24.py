#Proposta: 24. Dada a lista [5, 12, 8, 20, 3, 15], informe quantos itens são maiores que 10.
lista = [5, 12, 8, 20, 3, 15]
contagem = 0
for n in lista:
    if n > 10:
        contagem += 1
print("Numeros maiores que 10:", contagem)