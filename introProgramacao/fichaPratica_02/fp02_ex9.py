#pedir ao user para inserir um número inteiro maior que 2
num= int(input("Por favor insira um nº maior que 2:"))
if num<2:
    print("Erro! numero menor que 2")
prntNum=2
while prntNum != num:
    if prntNum%2 ==0:
        print(prntNum)
        prntNum +=1
    else:
        prntNum +=1
 