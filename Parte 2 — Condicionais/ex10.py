#Proposta: 10. Peça a idade de uma pessoa e informe se ela já pode votar. A idade mínima é 16 anos.
idade_pessoa = int(input("Digite a sua idade: "))
if idade_pessoa >= 16:
    print("Já pode votar")
else:
    print("Ainda não pode votar")