#pedir ao user 2 numeros e o simbolo da operação aritemetica
num1 = float(input("inserir o 1º número:"))
operator = input ("Inserir operador aritmético:")
num2 = float(input("inserir o 2º número:"))


# verificar operador aritemetico
if operator == "+" :
    print ( num1,"+",num2,"=", (num1+num2))
elif operator == "-":
    print ( num1,"-",num2,"=", (num1-num2))
elif operator ==("*"):
    print ( num1,"*",num2,"=", (num1*num2))
elif operator== ("/"):
    print ( num1,"/",num2,"=", (num1*num2))
else:
    print ("Erro! O operador está errado! Por favor utilise os operadoes +, -, * ou /") 
