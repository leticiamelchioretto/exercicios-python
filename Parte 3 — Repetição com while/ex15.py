positivos = 0
valor = float(input("Digite um número: "))
while valor != 0:
    if valor > 0:
        positivos += 1
    valor = float(input("Digite um número ou 0 para parar: "))
print("Quantidade de positivos:", positivos)