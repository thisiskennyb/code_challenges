def longest_subseq (arr):
    left = 0
    curr = 0
    ans = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            curr = (i - left) + 1
            ans = max(ans, curr)
        else:
            left = i
    return ans



input = [1,3,2,3,4,6,4,5,2]
print(longest_subseq(input))