#Proposta: 13. Peça uma senha ao usuário e continue pedindo até que ele digite senai123. Ao acertar, exiba "Acesso liberado".
senha = input("Digite a senha: ")
while senha != "senai123":
    senha = input("A senha está incorreta. Tente novamente: ")
print("Acesso liberado")