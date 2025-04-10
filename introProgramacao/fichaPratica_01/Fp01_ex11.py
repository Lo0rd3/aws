#pedir ao user o saldo 
saldo = float(input("introduzir saldo inicial:"))

#pedir ao user o valor a movimentar
movimento =float(input("Introduzir valor do movimento:"))
#calcular o saldo final
saldoFinal = saldo+movimento
#verificar se o user tem saldo suficiente 
if saldoFinal < 0:
    print("Operação Inválida. Saldo Insuficiente!só tem:", saldo,"Pobre!")
else :
    print("O Saldo Actual é de:", saldoFinal)
