def remove_elements(nums, val):
    left = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[left] = nums[i]
            left += 1

    return left



print(remove_elements([0,1,2,2,3,0,4,2], 2))