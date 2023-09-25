

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
    print(combo_list)

    if no_dup_list.index(str(n)) == len(no_dup_list)-1:
        return -1
    else:
        next_big = no_dup_list[no_dup_list.index(str(n))+1]
        return int(next_big)     
        


print(next_bigger(14614))

