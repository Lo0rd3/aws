calc=0
while True:
    if calc==0:
        number=float(input("Please input the first number to add: "))
    else:
        number=float(input("Stop by adding 0.\nPlease input the next number to add: "))
    if number !=0:
        calc=calc+number
    else:
        print(f"The result of your calculation is: {calc}")
        break