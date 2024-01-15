def large_unique(nums):
    dict = {}

    largest_num = -1

    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    for num in dict:
        if dict[num] == 1 and num > largest_num:
            largest_num = num
    
    return largest_num




input = [9,9,8,8]
print(large_unique(input))