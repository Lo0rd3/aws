bigPair=None
oddCounter=0
while oddCounter<5:
    number=int(input("Please input a number:"))
    if number%2==0:
        if bigPair is None or number>bigPair:
            bigPair=number
    else:
        oddCounter+=1
if bigPair==0:
    print("You didn't input a pair! start again!")
else:
    print(f"The biggest pair you entered was:{bigPair}")