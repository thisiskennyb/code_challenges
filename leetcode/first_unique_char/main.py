def first_unique(s):

    char_dict = {}

    for char in s:
        char_dict[char] = char_dict.get(char, 0) + 1

    for i in range(len(s)):
        if char_dict[s[i]] < 2:
            return i
        
    return -1







print(first_unique("leetcode"))