Problem:
""" There are three types of edits that can performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.
 
  Example:
    pale, ple   -> true
    pales, pale -> true
    pale, bale  -> true
    pale, bake  -> false"""

def one_away(x, y):
    i = 0
    count = 0
    for i in range(0, len(x) - 1):
        if len(x) == len(y):
            if x[i] != y[i]:
                count += 1
        elif len(x) > len(y):
            if x[i + count] == y[i]:
                i += 1
            else:
                count += 1
        else:
            if y[i + count] == x[i]:
                i += 1
            else:
                count += 1
    if count <= 1:
        print(True)
    else:
        print(False)


a = one_away("pale", "ple")
a = one_away("pales", "pale")
a = one_away("pale", "bale")
a = one_away("pale", "bake")
