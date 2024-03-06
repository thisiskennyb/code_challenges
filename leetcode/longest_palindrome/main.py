# use hash map and loop to count the occurance of each character
# loop through the dictionary and build an array with numbers that are greater than one
# Initialize separate variable to find char that occurs once
# If number of chars is > 1 and odd then subtract one and add half the number of characters remaining
# If number is even then add the half



def longest_palindrome(s):
    char_count = {}
    single_char = ''
    palindrome_count = 0
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for letter, count in char_count.items():
        if count == 1 or count % 2 == 1:
            single_char = letter
        if count > 1 and count % 2 == 1:
            palindrome_count += (count-1)
        elif count % 2 == 0:
            palindrome_count += count

    
    return palindrome_count + len(single_char)


print(longest_palindrome("abccccdd"))