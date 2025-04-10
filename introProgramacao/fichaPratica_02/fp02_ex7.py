#pedir ao user um numero inteiro
num=int(input("introduzir um numero: "))

#determinar numero minimo e numero maximo
min= (num-5)
max= (num+5)

while num>min:
    num-=1
    print (num)
