"""You are given a string that may or may not contain repeated characters. Write a function that "compresses" the
string so that repeated characters that are next to each other are replaced by the character and the count. If the
length of the compression is longer than the length of the original string, return the original string.
Input - aaaabbccd
Output - a4b2c2d1 """


def compression(x):
    count = 1
    strc = ""
    for i in range(0, len(x) - 1):
        if x[i] == x[i + 1]:
            count += 1
        else:
            strc += x[i] + str(count)
            count = 1
    strc += x[len(x) - 1] + str(count)

    if len(x) < len(strc):
        return x
    else:
        return strc


a = compression("aaaabbccd")
print(a)
