numero = int(input("digite o número inteiro:  "))
primo = True 

#corpo do calculo

for x in range (2, numero):
    if numero % x == 0:
        primo = False
        break
#resultado em tela
if primo and numero > 1:
    print ("é primo")
else:
    print ("não é primo")
