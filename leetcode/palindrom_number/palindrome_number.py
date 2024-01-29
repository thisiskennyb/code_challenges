def palindrome_num(x):
    num_to_str = str(x)
    if x < 0:
        return False
    elif len(num_to_str) == 1:
        return True
    
    left = 0
    right = len(num_to_str) - 1

    while left < right:
        if num_to_str[left] != num_to_str[right]:
            return False
        left += 1
        right -= 1 
    return True




print(palindrome_num(121))