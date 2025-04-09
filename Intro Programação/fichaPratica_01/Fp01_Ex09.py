#pedir ao user input de 3 nuumeros inteiros
num1 = int(input("inserir 1º número:"))
num2 = int(input("inserir 2º número:"))
num3 = int(input("inserir 3º número:"))

#verificar qual dos números é maior & print

if num1 > num2 and num1>num3 :
    print("o número maior é:", num1)
if num2 > num1 and num2>num3:
    print("o número maior é:", num2)
if num3 > num2 and num3>num1:
    print("o número maior é:", num3)
    