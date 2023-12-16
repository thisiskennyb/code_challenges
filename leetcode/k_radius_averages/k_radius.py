def k_radius(nums, k):

    prefix_sum = [nums[0]]
    diameter = k*2 + 1
    avg_list = []

    for i in range(1, len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[-1])

    if k == 0:
        return prefix_sum

    for i in range(len(nums)):
        if i - k >= 0 and i + k <= len(nums) - 1:
            if i - (k) == 0:
                avg_list.append(int(prefix_sum[i + (k)]/diameter))
            else:
                avg_list.append(int((prefix_sum[i + (k)] - prefix_sum[i - (k+1)])/diameter))
        else:
            avg_list.append(-1)
 
    return avg_list








# nums_arr = [7,4,3,9,1,8,5,2,6]
# radius = 3
# nums_arr = [8]
# radius = 100000
nums_arr = [100000]
radius = 0
print(k_radius(nums_arr, radius))