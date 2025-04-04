# pedir 2 valores int ao user
valor1 = int(input("digite o primeiro valor:"))
valor2 = int(input("digite o segundo valor:"))

#trocar dos valores
valor1 = valor1 + valor2
valor2 = valor1 - valor2
valor1 = valor1 - valor2

# mostrar a troca de valores

print ("o primeiro valor 1 depois da troca é : ", valor1)
print ("o segundo valor 2 depois da troca é : ", valor2)