#pedir ao user para inserir 3 número
num1 = int(input("inserir 1º número:"))
num2 = int(input("inserir 2º número:"))
num3 = int(input("inserir 3º número:"))

#pedir ao user se quer ordem crescente ou decrescente

ordem = input("Escolha a ordem:\n(>)-Crescente \n(<)-Decrescente\n")


#verificar qual dos numeros e o maior
if num1 > num2 and num1>num3:
    maior = num1
    if num2>num3:
        medio = num2
        menor = num3
    else :
        medio=num3
        menor =num2
if num2 > num1 and num2>num3:
    maior = num2
    if num1>num3:
        medio = num1
        menor = num3
    else :
        medio=num3
        menor=num1
if num3 > num2 and num3>num1:
    maior = num3
    if num2>num1:
        medio = num2
        menor = num1
    else :
        medio=num1
        menor =num2

#verificar de o user colocou ordem de acordo com o pedido
#if ordem != ("<") or (">"):
  #  print("Erro! formato da ordem errado!")

#print dos resultados 
if ordem == ">":
    print(f"{maior}>{medio}>{menor}")
elif ordem =="<":
    print(f"{menor}<{medio}<{maior}")
else:
    print("Erro! formato da ordem errado!")
