def is_panagram(sentence):
    sent_set = set(sentence)
    return len(sent_set) == 26

# s = "thequickbrownfoxjumpsoverthelazydog"
s = "leetcode"
print(is_panagram(s))