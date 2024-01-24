def iso_str(s, t):
    s_set = set(s)
    t_set = set(t)

    if len(s_set) == len(t_set):
        return True
    return False

one_string = "foo"
two_string = "bar"
print(iso_str(one_string, two_string))