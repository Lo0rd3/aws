#ask user for how many students he wants to add
students=int (input("Please input how many students you have:"))

total=0

for i in range(students):
    if i ==0:
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
    total+=score

average=total/students
print(f"The average score of your students is: {average}")



