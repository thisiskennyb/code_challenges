# Initialize a dictionary to keep track of the occurance of each unique element
# Initialize a variable to keep the highest count
# Initialize variable to keep track of the element matching the highest count
# loop through input array and build the dictionary 
# loop through the dictionary and update the the count and the unique element variables with the current majority value





def majority_element(nums):
    num_count = {}
    majority_element = None
    element_occurances = 0

    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1

    for key, value in num_count.items():
        if value > element_occurances:
            element_occurances = value
            majority_element = key

    return majority_element
         



print(majority_element([2,2,1,1,1,2,2]))