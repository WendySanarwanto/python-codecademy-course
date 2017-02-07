pyg = "ay"

## 1. Ask the user to input a word in English.
entry = input("Please input word in english: ")

## 2. Make sure the user entered a valid word
if not entry or entry.isalpha() == False:
    print ("Please enter non empty valid word")
else:    
## 3. Convert the word from English to Pig Latin.
    firstLetter = entry[0]
    output = entry.lower() + pyg
    output = output[1:len(output)]
## 4. Display the translation result.
    print ("The Pig latin version of your input is: " + output)