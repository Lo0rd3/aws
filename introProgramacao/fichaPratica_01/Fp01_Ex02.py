#pedir ao user para inserir o salário
salario = float(input("Por favor insira o salário:"))

#calcular imposto 
if salario < 15000:
    print("Taxa a pagar(20%):",salario * 0.2)
else:
    print("taxa a pagar(30%):", salario*0.3)