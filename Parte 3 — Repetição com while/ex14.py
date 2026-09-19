#Proposta: 14. Peça um número e exiba sua tabuada de 1 a 10.
t = int(input("Digite um número: "))
i = 1
while i <= 10:
    print(t, " X ", i, " = ", t * i)
    i += 1