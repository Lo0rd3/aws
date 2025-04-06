#pedir ao user para inserir 2 números
num1 = int (input("Digite o primeiro número:"))
num2 = int (input("Digite o segundo número:"))

#ver qual o maior numero
if num1 == num2 :
    print("Os números sao iguais") 
    
elif num1 >= num2 :
    print("O número maior é o primeiro:", num1) 
    
else :
    print("O número maior é o segundo:", num2)
