#ask to input a sentence
sentence=input("Please input a sentence:\n")

#start variables
counter=0

#counter of characters

for char in sentence:
    counter+=1

print(f"There are {counter} characters in your sentence.")
#print the input in uppercase
print (sentence.upper())
#capilalize the sentence
print(sentence.capitalize())
#does the sentence only letter?
print(f"Is your input only letters? {sentence.isalpha()}")
#split of the sentence
print (f"Your sentence split:\n {sentence.split()}")