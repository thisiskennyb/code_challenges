def str_to_camel(s):
    str_list = []

    for i in range(len(s)):
        if s[i].isalpha():
            str_list.append(s[i])
        else:
            str_list.append(" ")

    for j in range(len(str_list)):
        if j > 0 and str_list[j-1] == " ":
            str_list[j] = str_list[j].upper()
            
    first_str = "".join(str_list)
    no_space = first_str.split(" ")
    return "".join(no_space)





print(str_to_camel("the-stealth-warrior"))