def valid_palindrome(s):
    filtered_list = []
    left = 0
    right = len(filtered_list)-1

    for char in s:
        if char.isalnum():
            filtered_list.append(char.lower())
    print(filtered_list)

    return filtered_list == filtered_list[::-1]


input = "A man, a plan, a canal: Panama"
print(valid_palindrome(input))