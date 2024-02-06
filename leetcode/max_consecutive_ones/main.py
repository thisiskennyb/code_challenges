def max_consecutive(nums):
    left = ans = 0

    for i in range(len(nums)):
        while nums[left] == 0 and left < len(nums) - 1:
            left += 1

        if nums[i] == 0:
            ans = max(ans, i-left)
            left = i+1

        ans = max(ans, (i+1)-left)

    return ans



print(max_consecutive([1,1,0,1,1,1]))