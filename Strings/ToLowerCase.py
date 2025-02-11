# https://leetcode.com/problems/to-lower-case/description/?envType=problem-list-v2&envId=string

# Approach:
# Think about the different capital letters and their ASCII codes and
# how that relates to their lowercase counterparts. Does there seem to be any pattern there?
# Any mathematical relationship that we can use?

# Input:
# s = "Hello"
# Output: "hello"

# Input:
# s = "here"
# Output: "here"

# Input:
s = "LOVELY"
# Output: "lovely"


def toLowerCase(s):

    result = ""
    for letter in s:
        if ord(letter) >= 65 and ord(letter) <= 90:
            result += chr(ord(letter) + 32)
        else:
            result += letter

    return result


print(toLowerCase(s))
