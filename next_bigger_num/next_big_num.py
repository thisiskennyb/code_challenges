import math

def next_bigger(n):

# '''    
# take the number from the end and if its not smallest number then compare to all previous numbers in order of place value. 
# insert the number with the smallest place value that it is greater than
# take digits following the inserted digit, not including the original digit and arrange in ascending order
# '''
    digit_list = list(str(n))
    length = len(digit_list)
    # test = digit
    # if "".join(digit_list.sort(reverse=True))

  
        #   for i in range(len(digit_list)-1, -1, -1)
        #   if (i != 0) and any(digit_list[i] > digit_list[k] for k in range(i-1, -1, -1))]
    for i in range(len(digit_list)-1, -1, -1):
        # print(i)
        if i == 0: return -1
        for k in range(i-1, -1, -1):      
            if digit_list[i] > digit_list[k]:
                digit_list[k], digit_list[i] = digit_list[i], digit_list[k]
                return int("".join(digit_list[:k+1] + digit_list[k+1:][::-1]))
    return -1
            # else: return -1
                # print(sorted(digit_list[i-1:]))
                # return digit_list
            # print(digit_list)
        # for i in digit_list[digit:]:
        #     print(digit, i)


    

    # while array.join = n and solved = false
    


        









#print(next_big(2274))
print(next_bigger(9764321))
# print(next_big(37907))
# print(next_big(41076))
# print(next_big(17643))


# Incorrect answer for n=59884848459853: 59884848534895 should equal 59884848483559
# 5214459889 should equal 5198924458
# 29061106836116 should equal 29061061166138
# 4014787889976 should equal 1679988804477
# 9144374124784 should equal 9144372714448
# 64900631534 should equal 64900614533
# 2392208922747 should equal 2392074728229
# 4101910093 should equal 4101909013

# 22125632 should equal 21252236