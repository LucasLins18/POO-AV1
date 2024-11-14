#gabarito da prova:
gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

notas = []

while True:
    acertos = 0

#Entrada de respostas:
    for x in range(10):
        resposta = input(f"digite a resposta da questão {x+1}: "). upper()
        if resposta == gabarito[x]:
            acertos += 1
    
    print ("Total de acertos", acertos)
    notas.append(acertos)
    
    continuar = input ("outro aluno vai utilizar o sistema? (s/n):  ").lower()
    if continuar != "s":
        break
     

if notas:
    print ("maior acerto", max(notas))
    print ("menor acerto", min(notas))
    print ("Total de alunos", len(notas))
    print ("media de notas", sum(notas) / len(notas))