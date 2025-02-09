# https://leetcode.com/problems/find-the-difference/description/?envType=problem-list-v2&envId=string

# Input:
s = "abcd"
t = "abcde"
# Output: "e"

# Input:
# s = ""
# t = "y"
# Output: "y"

# s = "Aks"
# t = "Aksh"


def solve(s, t):

    if len(s) == 0:
        return t

    sumS = 0
    sumT = 0

    for x in s:
        sumS += ord(x)

    for x in t:
        sumT += ord(x)

    return chr(sumT - sumS)


print(solve(s, t))
