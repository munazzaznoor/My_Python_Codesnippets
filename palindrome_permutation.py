#Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that
# is the same forwards and backwards. A permutation is a rearrangement of letters.The palindrome does not need to be
# limited to just dictionary words. You can ignore casing and non-letter characters.
#EXAMPLE
#Input: Tact Coa
#Output: True (permutations: “taco cat”. “atco cta”. etc.)
def palindrome_permutation(str):
    str = str.replace(" ","")
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
    

palindrome_permutation("1race car1")
