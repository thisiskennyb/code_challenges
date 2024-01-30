def search_input_position(nums, target):
    left = 0
    right = len(nums)-1

    while left < right:
        while nums[left] < target and left < len(nums):
            if nums[left] == target:
                return left
            left += 1
        while nums[right] > target:
            if nums[right] == target:
                return right
            right -= 1
        return left
        # elif right == left+1 and nums[left] < target < nums[right]:
        #     return left + 1
        # elif nums[left] < target:
        #     left += 1
        # elif nums[right] > target:
        #     right -= 1





print(search_input_position([1,3,5,6], 5))