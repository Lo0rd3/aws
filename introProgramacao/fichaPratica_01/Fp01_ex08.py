#pedir as notas ao user
nota1 = float(input("Introduzir 1ª nota:"))
nota2 = float(input("Introduzir 2ª nota:"))
nota3 = float(input("Introduzir 3ª nota:"))

#calcular media ponderada com os pesos nota1:20% nota2:35% nota3:40%

media = (nota1*0.25) + (nota2*0.35) + (nota3*.40)

#verificar se notas estao nos valoes pedidos
if nota1 <=float(0) or nota1>=float(20) or nota2 <=float(0) or nota2>=float(20) or nota3 <=float(0) or nota3>=float(20):
    print ("Erro verifique as notas. Minimo 0, maximo 20")
elif media >9.5 :
    print("O aluno está aprovado")
    print (media, "Valores")
else:
    print("O aluno está reprovado")
    print (media ,"Valores")
