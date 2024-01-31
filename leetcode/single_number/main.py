#Input non-empty array of integers
#Output integer with no duplicates within input array


# create hash map
#iterate through the input array
#add the number of occurances of each element to the hash map
#iterate through the input array and check hash map for occurance equal to 1



def single_number(nums):

    num_occurance = {}

    for num in nums:
        num_occurance[num] = num_occurance.get(num, 0) + 1

    for i in nums:
        if num_occurance[i] == 1:
            return i





print(single_number([1]))