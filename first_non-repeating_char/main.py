def non_repeating(s):
    char_dict = {}

    for char in s:
        char_dict[char] = char_dict.get(char, 0) + 1

    for i in s:
        if char_dict[i] == 1:
            return i
        
    return "_"





print(non_repeating("abacabad"))