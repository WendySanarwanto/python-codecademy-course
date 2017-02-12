#### anti_vower ####

# A helper to remove vowels from a text
# anti_vowel("Hey You!") should return "Hy Y!".
# Don't count Y as a vowel.
# Make sure to remove lowercase and uppercase vowels.
def anti_vowel(text):
    result = ""
    length = len(text)
    for i in range(0, length):
        letter = text[i]
        if letter != "a" and letter != "A" and letter != "i" and letter != "I" \ 
            and letter != "u" and letter != "U" and letter != "e" and letter != "E" \
            and letter != "o" and letter != "O":
            result += letter
    return result
    
# Main
entry = ""
while entry != "q":
    entry = raw_input("Enter text or 'q' for exit: ")
    if entry == 'q':
        print "Bye bye"
        break
    else:
        result = anti_vowel(entry)
        print "result %s" % result
