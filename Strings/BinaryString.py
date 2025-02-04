# https://www.geeksforgeeks.org/problems/binary-string-1587115620/1

# Approach:
# [ n * (n-1) / 2 ]
# Is the formula of Combinatrics
# Which is used to calculate
# Number of ways in which unique pairs can be formed

# Input:
# N = 4
# S = 1111
# Output: 6

# Input:
n = 5
s = "01101"
# Output: 3


def binarySubstring(n, s):

    c = s.count("1")
    return int(c * (c - 1) // 2)


print(binarySubstring(n, s))
