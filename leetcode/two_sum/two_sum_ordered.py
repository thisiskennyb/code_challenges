def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] > target:
            right -= 1
            print("right greater")
        
        elif numbers[left] + numbers[right] < target:
            left += 1
            print("left greater")

        elif numbers[left] + numbers[right] == target:
            print("equal")
            return [left+1, right+1] 

# input_nums = [2,7,11,15]






num = 9
input_nums = [2,7,11,15]
print(two_sum(input_nums, num))