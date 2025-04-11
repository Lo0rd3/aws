#ask user to input max and min input num
min=int(input("please input the minimum number:"))
max=int(input("Please input the maximum number"))

while min!=max:
    if min%5==0:
        print (min)
        min +=1
    else:
        min+=1