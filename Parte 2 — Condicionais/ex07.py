#Proposta: 7. Peça dois números e exiba qual é o maior. Se forem iguais, informe isso.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2:
    print("O maior é", num1)
elif num2 > num1:
    print("O maior é", num2)
else:
    print("Os números são iguais")