
while True:
    userContinue="y"
# ask user for input num1
    num1= float(input("Please input the first 1ºnumber:"))
# ask user for input num2 
    num2= float(input("Please input the 2ºnumber:"))
# ask user for input operator
    operator=input("please input an operator(+,-,* or /)")
# loop to confirm operator
    while operator !="+" and operator != "-" and operator !="*" and operator !="/":
        print("please choose the proper operator(+,-,*,/)")
        operator=input("please input and operator(+,*,- or /)")
#calculations
    if operator == "+":
        print (f"{num1}+{num2}={(num1 + num2)}")
#ask if they want to continue
        userContinue = input("Do you want to continue? (y or n)")
        while userContinue != "n" and userContinue !="y":
            print("please select y(yes) or n(no)")
            userContinue = input("Do you want to continue? (y or n)")
        if userContinue == "n":
            break
        else:
                continue
#calculations
    elif operator == "-":
        print (f"{num1}-{num2}={(num1 - num2)}")
#ask if they want to continue
        userContinue = input("Do you want to continue? (y or n)")
        while userContinue != "n" and userContinue !="y":
            print("please select y(yes) or n(no)")
            userContinue = input("Do you want to continue? (y or n)")
        if userContinue == "n":
            break
        else:
                continue
#calculations
    elif operator == "*":
        print (f"{num1}*{num2}={(num1 * num2)}") 
#ask if they want to continue
        userContinue = input("Do you want to continue? (y or n)")
        while userContinue != "n" and userContinue !="y":
            print("please select y(yes) or n(no)")
            userContinue = input("Do you want to continue? (y or n)")
        if userContinue == "n":
            break
        else:
                continue 
#calculations
    elif operator == "/":
        print (f"{num1}/{num2}={(num1 / num2)}")
#ask if they want to continue
        userContinue = input("Do you want to continue? (y or n)")
        while userContinue != "n" and userContinue !="y":
            print("please select y(yes) or n(no)")
            userContinue = input("Do you want to continue? (y or n)")
        if userContinue == "n":
            break
        else:
                continue
