counter=0
total=0

while total<100 or counter<5:
    number=int(input("Please input a number:"))
    total+=number
    counter+=1
else:
    print(f"The result of sum is:{total}")