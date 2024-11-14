#entrada de dados
popA = 80000
popB = 200000

taxaA = 0.03 
taxaB = 0.015

anos = 0

#corpo do cálculo

while popA <= popB:
    popA = popA + (popA * taxaA)
    popB = popB + (popB * taxaB)
    anos = anos +1

#Resultado:
print ("É necessário", anos, "anos para a população do país A ultrapassar ou igualar a população do país B")