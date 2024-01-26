def valid_anagram(s, t):

    s_map = {}
    t_map = {}
    
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        s_map[s[i]] = s_map.get(s[i], 0) + 1
        t_map[t[i]] = t_map.get(t[i], 0) + 1
       
    
    return s_map == t_map




print(valid_anagram("anagram", "nagaram"))