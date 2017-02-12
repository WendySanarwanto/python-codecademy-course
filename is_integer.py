#### is_int #####

# A helper to determine whether a number has rounded decimal integer or not
def is_int(x):
    rounded_x = round(x, 0)
    print "rounded_x = %s" % rounded_x
    diff = 0;
    if x >= 0:
        diff = rounded_x - x
    else:
        diff = x - rounded_x
    print "diff = %s" % diff
    if diff != 0:
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
        number = float(entry)        
        if is_int(number):
            print "%s is an integer." % (str(entry))
        else:
            print "%s is NOT an integer." % (str(entry))
