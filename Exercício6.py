#valores de entrada
salario = 1000.00

# aumento 1996
salario += salario * 0.015 

#aumentos a partir de 1997
aumento = 0.03

#calculo salarial
for ano in range (1997,2026):
    salario += salario * aumento
    aumento *= 2

print (f"Salário atualizado em 2025 , será de: R$ {salario}")