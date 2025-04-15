#ask user to how many nº he want to input
numQuantity= int(input("Please state how many number you want to input: "))

#start numCounter, numbStorage & state
numCounter=0
numStorage=0
state =0

#loop 
while numCounter <numQuantity:
    num=int(input("Please enter a number: "))
    if num >numStorage:
        numCounter +=1
        numStorage = num
    else:
        numCounter+=1
        numStorage=num
        state +=1
#check if 
if state ==0:
    print("The number is increasing!")
else:
    print("The number is not increasing!")