secretNum=int(input("Please insert the secret number:"))
tryCount=0
for _ in range (10):
    tryCount +=1
    playerGuess=int(input("Guess the number:"))
    if playerGuess < secretNum:
        print("The secret number is bigger")
    elif playerGuess > secretNum:
        print("The secret number is smaller")
    else:
        print("hurray!! you guessed the number")
        break