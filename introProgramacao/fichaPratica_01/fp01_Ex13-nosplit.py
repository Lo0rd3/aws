#pedir entrada das horas e minutos 
horas = int(input("Insira as horas:"))
min = int(input("insira os minutos:"))

#verificar se e AM ou PM
if horas>12:
    amPm= "PM"
else:
    amPm = "AM"

#trasformar as horas no formato 12H
if horas >= 12:
    horaConvert = (horas - 12)
else:
    horaConvert =horas

#print
print(horaConvert,":", min, amPm)