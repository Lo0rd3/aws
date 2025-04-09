#pedir ao user para inserir o salário
salario = float(input("Por favor insira o salário:"))

#calcular imposto 
if salario > 25000:
    print("paga de imposto 40%:",salario *0.4)
elif salario > 20000:
    print("paga de imposto 35%:",salario *0.35)
elif salario > 15000:
    print("paga de imposto 30%:", salario*0.3)
else :
    print("paga de imposto 20%:", salario* 0.2)