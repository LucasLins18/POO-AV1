pares = impares = 0
#solicitar 10 números
for _ in range(10):
    numero = int(input("Digite o número inteiro: "))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
#resultados
print("pares", pares, "/ impares:", impares)
