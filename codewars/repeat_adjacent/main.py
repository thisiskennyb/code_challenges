# Initialize left and right pointer
# Initialize a while loop to make sure it stops when left pointer == len(st)

# Use pointers to find substring with repeating characters
# User a set to keep track of unique characters



# def repeat_adjacent(st):
#     l = 0
#     r = 1

    

#     big_groups = []
#     sub_string = []

    
#     while l < len(st):
    
#         while st[l] == st[r] and r < len(st)-1:
#             r = r+1 if r+1 < len(st)-1 else r

#         if len(st[l:r]) > 1:
#             sub_string.append(st[l:r])
#             l = r
#             r = l+1 if l+1 <= len(st) else l
#         elif len(st[l:r]) == 1:
#             if len(sub_string) > 1:
#                 big_groups.append(sub_string)
#                 sub_string = []
#             sub_string = []
#             l = r
#             r = l+1 if l+1 <= len(st) else l
        
#     print(big_groups)

# print(repeat_adjacent("ccccoodeffffiiighhhhhhhhhhttttttts"))

def repeat_adjacent(st):
    l = 0
    r = 1

    big_groups = []
    sub_string = []

    while l < len(st):
        while r < len(st) and st[l] == st[r]:
            r += 1

        if len(st[l:r]) > 1:
            sub_string.append(st[l:r])
            l = r
            r = l + 1 if l + 1 <= len(st) else l
        elif len(st[l:r]) == 1:
            if len(sub_string) > 1:
                big_groups.append(sub_string)
                sub_string = []
            sub_string = []
            l = r
            r = l + 1 if l + 1 <= len(st) else l
    
    # Append the last big group if it exists
    if len(sub_string) > 1:
        big_groups.append(sub_string)
    
    # Count the number of big groups
    return len(big_groups)

print(repeat_adjacent("ccccoodeffffiiighhhhhhhhhhttttttts"))