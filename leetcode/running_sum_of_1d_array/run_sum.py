def running_sum(nums):
    prefix = [nums[0]]
    print(nums)

    for i in range(1, len(nums)):
        curr = nums[i] + prefix[-1]
        prefix.append(curr)
    
    return prefix




nums_array = [1,2,3,4]
print(running_sum(nums_array))