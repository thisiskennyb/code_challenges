def sum_no_duplicates(l):
  count_dict = {}
  new_arr = []
  for num in l:
    if num in count_dict:
      count_dict[num] += 1
    elif num not in count_dict:
      count_dict[num] = 1
  for nums in count_dict:
    if count_dict[nums] == 1:
      new_arr.append(nums)
  return sum(new_arr)