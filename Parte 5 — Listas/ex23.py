#Proposta: 23. Usando a mesma lista, encontre e exiba o maior valor.
numeros = [3, 9, 6, 15, 12]
maior_numero = numeros[0]
for n in numeros:
    if n > maior_numero:
        maior_numero = n
print("O maior número é:", maior_numero)