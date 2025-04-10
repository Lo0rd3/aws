#pedir ao user para inserir 3 número
num1 = int(input("inserir 1º número:"))
num2 = int(input("inserir 2º número:"))
num3 = int(input("inserir 3º número:"))

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


#print dos resultados 
print(f"{maior}>{medio}>{menor}")