soma = 0
valor = float(input("Digite um número: "))
while valor != 0:
    soma += valor
    valor = float(input("Digite outro número ou digite 0 para parar: "))
print("Soma:", soma)