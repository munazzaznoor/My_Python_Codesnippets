def palindrome_permutation(str):
    len_str = len(str)
    empty_list = []
    for i in range(len_str):
        mn=str.count(str[i])
        empty_list.append(mn)
    
    
    if empty_list.count(2) % 2 == 0 and empty_list.count(1) == 1:
        print("True") 
    
    elif empty_list.count(2) % 2 == 0 and empty_list.count(1) == 0:
        print("True")

    else:
        print("False")
    

palindrome_permutation("1racecar1")
