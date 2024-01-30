def remove_dup(nums):
    nums_set = set()
    unique_list = []
    next = 0
    
    for i in range(len(nums)):
        print(nums[i])
        print(next, "next")
        if nums[i] not in nums_set:
            nums[next] = nums[i]
            next += 1
            nums_set.add(nums[i])

    return len(nums_set), nums


print(remove_dup([0,0,1,1,1,2,2,3,3,4]))