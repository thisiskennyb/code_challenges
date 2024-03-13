# Initialize left and right pointer for sliding window
# Initialize empty array to append sub arrays to
# sort each subarray and add to hash map where sum is key and array is value. Append sum to array as well
# sort sum array
# loop through sum array and append sub arrays


def sort_num_seq(sequence):
    l = 0
    r = 0  # Start r at 0 instead of 4

    ans = []
    sum_arr = []
    map_sum_to_subarray = {}

    while r < len(sequence):
        if sequence[r] == 0:
            sorted_subarr = sorted(sequence[l:r]) + [0]  # Sort from l to r (excluding r)
            subarr_sum = sum(sorted_subarr)
            sum_arr.append(subarr_sum)
            # Store both sorted subarray and the original indices of its elements
            map_sum_to_subarray[subarr_sum] = (sorted_subarr, list(range(l, r)))
            l = r + 1  # Move l to the next index after the zero
        r += 1

    sorted_sum_arr = sorted(sum_arr)

    for num in sorted_sum_arr:
        # Append elements from the subarray in their original order
        ans += map_sum_to_subarray[num][0]

    return ans

# Test cases
print(sort_num_seq([3,2,1,0,5,6,4,0,1,5,3,0,4,2,8,0]))  # Output: [1, 2, 3, 0, 1, 3, 5, 0, 2, 4, 8, 0, 4, 5, 6, 0]
print(sort_num_seq([3,2,1,0,5,6,4,0,1,5,3,0,2,2,2,0]))  # Output: [1, 2, 3, 0, 2, 2, 2, 0, 1, 3, 5, 0, 4, 5, 6, 0]
print(sort_num_seq([2,2,2,0,5,6,4,0,1,5,3,0,3,2,1,0]))  # Output: [2, 2, 2, 0, 1, 2, 3, 0, 1, 3, 5, 0, 4, 5, 6, 0]
