#ask user to input a number to calculate
num=int(input("Please input the number to calculate: "))

#start variables to store result and counter
counter=1
result=1

#calculate factorial 
while counter <=num:
        result=result*counter
        counter +=1
print(f"the factorial value is: {result}")