#ask for number of students
students=int(input("How many students do you have?\n"))
#ask for grade 
negative=0
positive=0
for i in range(students):
    while True:
        if i==0:
            score=float(input("Please insert the first student score[0-20]:"))
        else:
            score=float(input("Please insert the next student score[0-20]:"))
                
        if score < 0 or score>20:
            print("Wrong score! please input a grade betwen 0 and 20")
        else:
            break
    if score<9.5:
        negative+=1
    else:
        positive+=1
print(f"{positive} of your students passed and {negative} failed.")