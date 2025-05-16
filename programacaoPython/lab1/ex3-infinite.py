counter=0
sum=0

while True:
    if counter ==0:
       while True:
            score=int(input("Please insert the first student score[0-20]:"))
            if score < 0 or score>20:
                print("Wrong score! please input a grade betwen 0 and 20")
            else:
                break
    else:
        while True:
            score=int(input("Please insert the next student score[0-20]:"))
            if score < 0 or score>20:
                print("Wrong score! please input a grade betwen 0 and 20")
            else:
                break
    counter +=1
    sum+=score
    
    proceed="a"    
    while proceed !="y" and proceed!="n":
        proceed=input("Do you want to add another student? y/n:")
        if proceed !="y" and proceed !="n":
            print("Error! Please reply with y or n")
    if proceed=="n":
        average=sum/counter
        print(f"The average score of your students is:{average}")
        break
