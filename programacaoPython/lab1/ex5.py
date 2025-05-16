#ask for  number
starting=int(input("Please insert the starting number:"))
#ask for last number
final=int(input("Please insert the final number:"))

if starting<final:
    for i in range(starting,(final+1)):
        if i%2 ==0:
            print(i)
        else:
            continue
elif starting>final:
    for i in range(starting,(final-1),-1):
        if i%2==0:
            print(i)
        else:
            continue
else:
    print("The numbers are the same")