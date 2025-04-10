#pedir ao user um numero inteiro
num=int(input("introduzir um numero: "))

#determinar numero minimo e numero maximo & print
min= (num-5)
max= (num+5)
numAtual=min
#print dos números
while numAtual<=max:
    if numAtual != num:
        print (numAtual)
    numAtual += 1