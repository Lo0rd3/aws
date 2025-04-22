#ask user to input a number
num=int(input("Please input a number to check if it is a prime number:"))

if num<=1:
    print("The number not a prime number")

else:
    numDiv=0
    for i in range(1, num+1):
        if num%i ==0:
            numDiv +=1
    if numDiv ==2:
        print("The number is a prime number")
    else:
        print("The number not a prime number")
    