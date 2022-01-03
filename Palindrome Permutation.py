#Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that
# is the same forwards and backwards. A permutation is a rearrangement of letters.The palindrome does not need to be
# limited to just dictionary words. You can ignore casing and non-letter characters.
#EXAMPLE
#Input: Tact Coa
#Output: True (permutations: “taco cat”. “atco cta”. etc.)

def palindrome_permutation(x):
    nx = x.replace(" ", "")
    li = list(nx)
    arr = []
    for i in li:
        new_li = li.count(i)
        arr.append(new_li)
    count = 0
    odd = 0
    for i in arr:
        if int(i) % 2 == 0:
            count = count + 1
        else:
            odd = odd + 1

    if count >= 0 and odd <= 1:
        print(True)
    else:
        print(False)


a = palindrome_permutation("taco cat")
