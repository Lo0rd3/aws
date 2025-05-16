#aks user to input the starting salary
salary=float(input("Please input the starting salary: "))
#ask user to input  the code for the position
position=int(input("101-Manager\n102-Engineer\n103-Technician\n000-Other\nPlease insert te correct code for the position: "))
#calculations
if position==101:
    increase=salary*0.25
    finalSalary= salary+increase
    print (f"Starting salary:{salary}€\nRaise:{increase}\nUpdated salary:{finalSalary}")
elif position==102:
    increase=salary*0.2
    finalSalary= salary+increase
    print (f"Starting salary:{salary}€\nRaise:{increase}\nUpdated salary:{finalSalary}")
elif position==103:
    increase=salary*0.15
    finalSalary= salary+increase
    print (f"Starting salary:{salary}€\nRaise:{increase}\nUpdated salary:{finalSalary}")
else:
    increase=salary*0.10
    finalSalary= salary+increase
    print (f"Starting salary:{salary}€\nRaise:{increase}\nUpdated salary:{finalSalary}")