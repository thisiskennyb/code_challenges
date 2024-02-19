def find_largest_perim(nums):
    if len(nums) <= 2:
        return -1
    
    nums = sorted(nums)
    sum = nums[0] + nums[1] if len(nums) >= 2 else nums[0]

    

    left = 0
    right = 2
    ans = -1

    if len(nums) == 3 and nums[right] > sum:
        return -1

    while nums[right] >= sum and right < len(nums)-1:
        
        print(sum, nums[right])
        sum += nums[right]
        right += 1

    while nums[right] < sum:
        sum += nums[right]
        right += 1

    print(sum)
    ans = max(ans, sum)
    return ans
   


print(find_largest_perim([5,5,50]))