#ask user to input average balance
bal=float(input("Please input the average balance:"))
#calculate credit
if bal <= 200:
    print(f"You have no credit. Your average balance is {bal}")
elif bal>=201 and bal<=400:
    print(f"You have 20% credit.\nYour average balance is:{bal}€.\nYou have {bal*0.2}€ in credit.")
elif bal>=401 and bal<=600:
    print(f"You have 30% credit.\nYour average balance is:{bal}€.\nYou have {bal*0.3}€ in credit.")
else :
    print(f"You have 40% credit.\nYour average balance is:{bal}€.\nYou have {bal*0.4}€ in credit.")