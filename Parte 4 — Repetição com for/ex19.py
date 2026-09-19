#Proposta: 19. Peça um número e calcule seu fatorial. O fatorial de 5 é 5 × 4 × 3 × 2 × 1 = 120.
n = int(input("Digite um número para o fatorial: "))
fatorial = 1
for i in range(2, n + 1):
    fatorial *= i
print(n,"! = ", fatorial )