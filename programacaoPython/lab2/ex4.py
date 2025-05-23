#ask to input a sentence
sentence=input("Please input a sentence:\n")

#start variables
counter=0
vowels="aeiou"

#counter of vowels
for char in sentence:
    if char.lower() in vowels:
        counter+=1
print(f"There are {counter} vowels in your sentence.")

#sentence backwards
print(f"Your sentence backwards:\n{sentence[::-1]}")
#sentence split
print(f"Your sentence split:\n{sentence.split()}")
#join a list 
words=sentence.split()

print(":" .join(words))