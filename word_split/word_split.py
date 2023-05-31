def word_split(strArr):
   dict_list = strArr[1].split(',') 
   match_listfb = []
   match_listbf = []
   search_word = strArr[0]
   for i in range(len(search_word)):
      if search_word[:i] in dict_list:
        match_listfb.append(search_word[:i])
      if search_word[i:] in dict_list:
        match_listbf.append(search_word[i:])
   print(match_listfb)
   print(match_listbf)         
    






print(word_split(["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]))


# Input: ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]
# Output: base,ball