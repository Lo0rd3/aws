#pedir as notas ao user
nota1 = float(input("Introduzir 1ª nota:"))
nota2 = float(input("Introduzir 2ª nota:"))
nota3 = float(input("Introduzir 3ª nota:"))

#calcular media ponderada com os pesos nota1:20% nota2:35% nota3:40%

media = (nota1*0.25) + (nota2*0.35) + (nota3*.40)

#verificar se é nota postiva 

if media >=9.5 :
    print("O aluno está aprovado")
else:
    print("O aluno está reprovado")
print (media ,"Valores")
