#### scrabble score ####

# def anti_vowel(text):
#     result = ""
#     length = len(text)
#     for i in range(0, length):
#         letter = text[i]
#         if letter != "a" and letter != "A" and letter != "i" and letter != "I" \ 
#             and letter != "u" and letter != "U" and letter != "e" and letter != "E" \
#             and letter != "o" and letter != "O":
#             result += letter
#     return result
def scrabble_score(word):
    result = 0;
    for w in word:
        print "w= %s" % w
        counter = 0
        for key in score:
            if key == w.lower():
                result += score[key]
                print score[key]
                break
    return result

# Main
entry = ""

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

while entry != "q":
    entry = raw_input("Enter text or 'q' for exit: ")
    if entry == 'q':
        print "Bye bye"
        break
    else:
        result = scrabble_score(entry)
        print "score: %s" % result
