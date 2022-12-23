def URLify(given_str,str_len):
    converted_list = list(given_str)
    empty_list = []
    string1 = ' '
    for i in range(str_len):
        if converted_list[i] != ' ' :
            s=empty_list.append(converted_list[i])
           
        else :
            new_str=given_str[i].replace(' ','%20')
            empty_list.append(new_str)
    for i in range(len(empty_list)):
        string1+=str(empty_list[i])
    print(string1) 

URLify("Mr John Smith  ", 13)
