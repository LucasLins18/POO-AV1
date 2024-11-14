#Entrada do número inteiro
numero =int(input("Insira um número entre 1 e 10: "))

#Corpo da questão
if 1 <= numero <=10:
    print("Tabuada de", numero)

#loop para geração e visualização  da tabuada
    for x in range(1,11):
        resultado = numero * x
        print(numero,"x", x, "=" ,resultado)