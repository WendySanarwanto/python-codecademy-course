#### is_prime ####

# A helper to calculate factorial of a number
# 1. For each number n from 2 to x - 1, test if x is evenly divisible by n.
# 2. If it is, return False.
# 3. If none of them are, then return True.
def is_prime(x):
    if x < 2:
        return False
    for n in range(2, x):
        if x % n == 0:
            return False
    return True
    
# Main
entry = ""
while entry != "q":
    entry = raw_input("Enter number or 'q' for exit: ")
    if entry == 'q':
        print "Bye bye"
        break
    else:
        number = int(entry)        
        result = is_prime(number)
        if result:
            print "%s is prime number" % number
        else:            
            print "%s is NOT prime number" % number
