def count_elem(arr):
    dict = {}

    for num in arr:
        if not dict[num]:
            dict[num] = 1
        else:
            dict[num] += 1

    print(dict)


num_list = [1,2,3]
print(count_elem(num_list))