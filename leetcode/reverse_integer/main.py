def reverse_integer(x):
    x = str(x)
    char_list = [char for char in x]

    if char_list[0] == '-':
        char_list = [char_list[0]] + char_list[1:][::-1]

    else:
        char_list = char_list[::-1]

    reverse_num = int("".join(char_list))
    
    return  reverse_num if reverse_num > (2**31)*-1 and reverse_num < (2**31)-1 else 0


print(reverse_integer(-123))