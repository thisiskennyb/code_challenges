def two_sum(nums, target):
    dict = {}

    for i in range(len(nums)):
        sum_num = target - nums[i]
        if sum_num in dict:
            return [i, dict[sum_num]]
        else:
            dict[nums[i]] = i







num = 9
input_nums = [2,7,11,15]
print(two_sum(input_nums, num))