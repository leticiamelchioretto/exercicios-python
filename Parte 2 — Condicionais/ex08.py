#proposta: 8. Peça um número e informe se ele é positivo, negativo ou igual a zero.
num = float(input("Digite um número: "))
if num > 0:
    print("Ele é positivo")
elif num < 0:
    print("Ele é negativo")
else:
    print("Ele é igual a zero")