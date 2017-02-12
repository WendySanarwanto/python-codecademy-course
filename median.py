#### median ####

# A helper to remove vowels from a text
# anti_vowel("Hey You!") should return "Hy Y!".
# Don't count Y as a vowel.
# Make sure to remove lowercase and uppercase vowels.
def median(numbers):
    length_numbers = len(numbers)
    sorted_numbers = numbers
    sorted_numbers.sort()
    result = 0
    if length_numbers % 2 == 0:
        mid_right_index = length_numbers / 2
        mid_left_index = mid_right_index - 1
        result = float( sorted_numbers[mid_right_index] + sorted_numbers[mid_left_index] ) / 2

    else:
        median_index = length_numbers / 2 
        result = sorted_numbers[median_index]
    return result
    
# Main
entry = [5,5,4,4]
result = median(entry)
print result
