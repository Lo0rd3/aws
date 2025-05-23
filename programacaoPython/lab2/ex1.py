sentence=input('Please input a sentence:')
#verify if word is in a sentence
word=input ('Please input a word to search for:')
if word in sentence:
    print('The word you are looking for is in the sentence.')
else:
    print('The word you are looking for is not present in the sentence.')
#replace spaces with -
print('\nReplace spaces with - in the sentence.')
print (sentence.replace(" ", "-"))

#verify if strates with "hello" or ends with "!"

if (sentence.split())[0].lower() == "hello":
    print("The sentence starts with hello.")
else:
    print("The sentence does NOT start with hello.")

if sentence[-1:] =="!":
    print ("The sentence ends with !")
else:
    print("The sentence does NOT end with !")



    