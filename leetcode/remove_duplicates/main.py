def remove_elements(nums, val):
    left = 0

    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[left] = nums[i]
            left += 1
        elif nums[i] == val:
            nums[i] = 0

    return left+1




print(remove_elements([3,2,2,3], 3))