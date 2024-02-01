def get_different_number(arr):
   """
   Problem:
   - Given an array arr of unique non-negative integers, implement a function
   getDifferentNumber which finds the smallest non-negative integer that is NOT
   in the array.

    Ex:
    - In: arr = [0, 1, 2, 3]
    - Out: 4
    
    Ex:
    -In: arr = [0, 2, 3, 4]
    -Out: 1

    Think:
    - First step may to be to find a 
    way to extract largest number of the array.
    - 2nd step is to get that max_int & increment by 1.

    - Or, use combination of range & set. Meaning, store each integer in the set
   """
    
   max_num = max(arr)
   num_set = set(arr) 
   print(range(4))
   
   for i in range(max_num):
      if i not in num_set:
        return i
      
   return max_num + 1
  
print(get_different_number([0, 2, 3]))  