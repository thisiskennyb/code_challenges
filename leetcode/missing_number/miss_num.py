def missing_num(nums):
    num_set = set(nums)  

    for i in range(len(nums) + 1):
        if i not in num_set:
            return i
    




input = [9,6,4,2,3,5,7,0,1]
print(missing_num(input))