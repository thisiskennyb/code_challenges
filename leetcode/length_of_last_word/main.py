def length_of_last_word(s):
    
    str_arr = s.split(" ")
    right = len(str_arr) - 1
    while len(str_arr[right]) == 0:
        right -= 1
    
    return len(str_arr[right])
    # print(str_arr)




print(length_of_last_word("   fly me   to   the moon  "))