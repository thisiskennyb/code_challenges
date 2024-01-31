def longest_substring(s):
    left = 0
    ans = 0
    subarr_set = set()

    for i in range(len(s)):
        subarr_set.add(s[i])
        
        print(i, "right")
        # print(left,"left")
        # print(len(subarr_set), "set")
        # print(i+1 - left, "i minus left")
        # print(ans, "ans")
        print(subarr_set)
       
        

        if len(subarr_set) < i+1 - left:
            ans = max(ans, i+1 - left)
            if s[left] in subarr_set:  # Check if the element exists in the set before removal
                subarr_set.remove(s[left])
            left += 1
            
    return ans

print(longest_substring("pwwkew"))

# def longest_substring(s):
#     left = ans = 0
#     seen = {}

#     for right, letter in enumerate(s):
#         if seen.get(letter, -1) >= left:
#             left = seen[letter] + 1
#         ans = max(ans , right - left + 1)
#         seen[letter] = right
#     return ans


