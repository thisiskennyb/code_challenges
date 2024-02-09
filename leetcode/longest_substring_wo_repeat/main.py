# Declare an empty set
# Declare left and right pointer variables
# Declare an answer variable

# create a while loop with a base case where right is less than length of string - 1
# while letter in set increase left pointer and remove letters from left
# add letter to set then increase right pointer by one
# update answer for max subarray



def longest_substring(s):
    char_set = set()

    left = right = ans = 0

    while right < len(s):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        ans = max(ans, (right-left)+1)
        right += 1

    return ans








print(longest_substring("abcabcbb"))



