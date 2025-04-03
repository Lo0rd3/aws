#pedir ao user 3 numeros inteiros
numero1 = int(input("inserir o 1º número: " ))
numero2 = int(input("inserir o 2º número: " ))
numero3 = int(input("inserir o 3º número: " ))

# calcular media aritemetica dos 3 numeros
mediaArit = (numero1 + numero2 + numero3)/ 3

# calcular media ponderada com os pesos de 20% , 30% e 50% respectivamente
mediaPond = ((numero1 * 0.2) + (numero2 * 0.3) + (numero3 * 0.5))


# print dos resultados
print("a média aritemetica dos 3 valores é: ", mediaArit)
print("a média ponderada dos 3 valores é: ", mediaPond)