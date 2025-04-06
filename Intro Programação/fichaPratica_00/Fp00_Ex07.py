#pedir ao user 3 preços

preco1 = float(input("digite o primeiro preço:"))
preco2 = float(input("digite o segundo preço:"))
preco3 = float(input("digite o terceiro preço:"))

#calcula o a soma dos preços

precoBruto = preco1 + preco2 + preco3

#aplica o desconto de 10%
precoFinal = precoBruto - (precoBruto * 0.10)
#mostra o preço final com o desconto aplicado
print ("Preço sem desconto: ", precoBruto)
print ("Preço final com 10% de desconto:",precoFinal)