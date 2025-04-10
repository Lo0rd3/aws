num = int(input("Por favor insira um numero: "))
soma =0
cont=0
while num != -1:
    soma=soma+num
    cont += 1
    num = int(input("Por favor insira um numero: "))

#calcular a media dos numeros inseridos antes do -1
media=soma/cont
#print
print(f"media: {media}")
