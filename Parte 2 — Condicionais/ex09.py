media = float(input("Digite a média do estudante: "))
if media >= 6:
    print("Aprovado")
elif media >= 4 and media < 6: 
    print("Recuperação")
else:
    print("Reprovado")