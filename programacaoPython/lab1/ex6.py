calc=0
total=0
while True:
    if calc==0:
        number=float(input("Please input the first number to add: "))
    else:
        number=float(input("Stop by adding 0.\nPlease input the next number to add: "))
    if number !=0:
        total+=1
        calc=calc+number
    else:
        if calc==0:
            print("The first number introduced is 0")
        else:
            average=calc/total
            print(f"The result of your calculation is: {calc} and the average is {average}")
            break