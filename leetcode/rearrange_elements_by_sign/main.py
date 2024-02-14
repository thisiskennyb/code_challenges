def elem_by_sign(nums):
    positive_int = []
    negative_int = []

    answer = []

    pointer = 0

    for num in nums:
        if num > 0:
            positive_int.append(num)
        else:
            negative_int.append(num)

    while pointer < len(positive_int) or pointer < len(negative_int):
        answer.append(positive_int[pointer])
        answer.append(negative_int[pointer])
        pointer += 1

    return answer






print(elem_by_sign([3,1,-2,-5,2,-4]))