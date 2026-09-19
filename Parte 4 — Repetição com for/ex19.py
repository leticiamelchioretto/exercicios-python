n = int(input("Digite um número para o fatorial: "))
fatorial = 1
for i in range(2, n + 1):
    fatorial *= i
print(n,"! = ", fatorial )