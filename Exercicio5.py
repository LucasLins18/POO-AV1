print ("Lojas Quase Dois - Tabela de preços")

#Entrada de quantidade
produtos = int(input("Insira a quantiade de itens: "))

#valor total
valor=produtos * 1.99

print("Valor total desta compra é: R$", valor)

#Geração tabela de preços
for quantidade in range (1,51):
    preco = quantidade * 1.99
    print (quantidade, "/", "R$", preco)
