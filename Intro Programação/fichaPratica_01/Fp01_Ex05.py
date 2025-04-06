#pedir ao user dois numeros 
num1 = int(input("digite o primeiro número:"))
num2 = int(input("digite o segundo número:"))

if num1==num2:
    print("Os Números sao iguais")
elif num1 >= num2 :
    print("Número maior:",num1)
    print("Número menor:",num2)
else :
    print("Número maior:",num2)
    print("Número menor:",num1)
    

      