# initialize variable as an empty set to keep track of duplicates
# sort the given input number array
# Initialize a for loop, on every iteration initialize two pointers with a while loop
# The iteration of the nums array is the main value while t



def three_sum(nums):
    sorted_nums = sorted(nums)
    three_sum_list = []
    num

    for num in sorted_nums:
        
        l = 0
        r = len(sorted_nums)
        if num not in sorted_nums:
            while l != r:

                if sorted_nums[l] + sorted_nums[r] + num == 


    print(sorted_nums)



print(three_sum([-1,0,1,2,-1,-4]))