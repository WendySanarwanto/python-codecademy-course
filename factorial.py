#### Factorial ####

# A helper to calculate factorial of a number
def factorial(x):
    result = 1
    multiplier = x
    #4 => 4 * 3 * 2 * 1
    # a = 1
    # 0: a * 4 => 1 * 4 = 4
    # 1: a * 3 => 4 * 3 = 12
    # 2: a * 2 => 12 * 2 = 24
    # 3: a * 1 => 24 * 1 = 24
    for i in range(0, x):
        result *= multiplier
        multiplier -= 1

    return result

# Main
entry = ""
while entry != "q":
    entry = raw_input("Enter number or 'q' for exit: ")
    if entry == 'q':
        print "Bye bye"
        break
    else:
        number = int(entry)        
        result = factorial(number)
        print "Factorial of %s is %s" % ( number, result)
