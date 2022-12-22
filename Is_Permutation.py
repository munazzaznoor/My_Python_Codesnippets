def Is_Permuatation(str1,str2):
    my_list = list(str1)
    my_list2 = list(str2)
    my_list.sort()
    my_list2.sort()
    if my_list == my_list2:
        return True
    return False

my_permuatation('prison','nopris')
