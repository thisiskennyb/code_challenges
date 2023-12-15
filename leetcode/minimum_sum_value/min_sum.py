def min_sum(nums):
    prefix = [nums[0]]
     
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    start_value = 1 - prefix[0] if 1 - prefix[0] > 0 else 1

    for i in prefix:
        
        if 1 - i >= 1:
            start_value = max(start_value, 1 - i)
        elif 1 - i < 1 and start_value - 1 == 0:
            start_value = 1
        print(start_value, "start")
    return start_value
            

    
    print(prefix)



# num_array = [-3,2,-3,4,2]
# num_array = [1,2]
# num_array = [1,-2,-3]
num_array = [2,3,5,-5,-1]

print(min_sum(num_array))