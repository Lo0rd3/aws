#ask user to input a name
name =input("Please input your name:")
#verify is is only letters and print results
while name.isalpha()==False:
    name =input("Please input only letters!\nPlease input your name:")
print (name.upper())