import time
import timeit
def next_bigger(n):
    import itertools
    combo_list = []
    num_list = list(str(n))
    arrangements = itertools.permutations(num_list)
    for arrangement in arrangements:
        number = ''.join(str(num) for num in arrangement)
        combo_list.append(number)
    combo_list.sort()
    no_dup_list = []
    for i in range(len(combo_list)):
        if combo_list[i] in no_dup_list:
            continue
        else:
            no_dup_list.append(combo_list[i])
    if no_dup_list.index(str(n)) == len(no_dup_list)-1:
        return -1
    else:
        next_big = no_dup_list[no_dup_list.index(str(n))+1]
        return int(next_big)     
        




startTime = time.time()

print(next_bigger(60543))
print(time.time() -startTime)
# 60543
# 63054
# 63045