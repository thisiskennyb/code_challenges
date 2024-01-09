def count_elem(arr):
    hash_set = set(arr)
    count = 0
    for x in arr:
        if x + 1 in hash_set:
            count += 1
    return count

num_list = [1,2,3]
print(count_elem(num_list))