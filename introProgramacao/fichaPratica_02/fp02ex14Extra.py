#ask user to input a number to calculate
num=int(input("Please input the number to calculate: "))

#start variables to store result and counter
counter=1
result=1
#start varables to support multiplication without * operator

#calculate factorial with no multiplication
while counter <=num:
        multCounter=0
        multResult=0
        while multCounter<counter:
                multResult+=result
                multCounter +=1
        result=multResult
        counter +=1
print(f"the factorial value is: {result}")