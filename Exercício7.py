#Dados de entrada
divida = float(input("Insira o valor da dívida: "))

#cabeçalho solicitado
print(" | Dívida | Juros | Quantidade de Parcelas | Valor da Parcela|")

#lista de parcelas e taxas:
parcelas_juros = [(1, 0), (3, 0.10), (6, 0.15), (9, 0.20), (12, 0.25)]

#calculo
for parcelas, juros in parcelas_juros:
    valor_juros = divida * juros
    valor_total = divida + valor_juros
    valor_parcela = valor_total / parcelas

#resultado
    print(f"| {valor_total:.2f} | {valor_juros:.2f} | {parcelas} | {valor_parcela:.2f} |")
