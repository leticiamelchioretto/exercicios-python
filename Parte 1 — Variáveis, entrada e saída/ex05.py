#Proposta: 5. Peça o preço de um produto e a quantidade comprada. Exiba o valor total, com duas casas decimais.
preco_produto = float(input("Digite o preço do produto: "))
quantidade_produto = int(input("E a quantidade: "))
print(f"Total: {preco_produto * quantidade_produto:.2f} reais")