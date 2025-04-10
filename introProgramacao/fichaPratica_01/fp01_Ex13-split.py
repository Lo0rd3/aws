#pedir ao user horas e minutos no formato HH:MM
horaMin = input("Por favor insira as horas e minutos no formato HH:MM:")

#separar horas e minutos
hora = int(horaMin.split(":")[0])
min = int(horaMin.split(":")[1])
 
# verificar se é AM ou PM
if hora > 12:
    amPm = "PM"
else:
    amPm = "AM"

#trasformar as horas no formato 12H
if hora >= 12:
    horaConvert = (hora - 12)
else:
    horaConvert =hora
#transformar no formato final
print (f"{horaConvert:02d}:{min:02d} {amPm}")