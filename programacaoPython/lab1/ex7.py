students=int(input("How many students does your class have?\n"))
threshold=int(input("what is the threshold of age?\n"))
older=0
for i in range(students):
    while True:
        age=int(input("Please input the age of your student:"))
        if age< 0 or age >=115:
            print("Please insert a valid age[0-115]")
        else:
            if age>threshold:
                older+=1
            break
            
percentage=(older/students)*100
print(f"{percentage}% of your class is older than {threshold} years old.")