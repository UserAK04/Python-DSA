# https://leetcode.com/problems/length-of-last-word/description/?envType=problem-list-v2&envId=string

# Approach:
# Keep a ptr at last index of string
# Omit all Spaces
# Count/Store all eles except Spaces


# Input:
s = "Hello World"
# Output: 5

# Input:
# s = "   fly me   to   the moon  "
# Output: 4

# Input:
# s = "luffy is still joyboy"
# Output: 6

# s = " "


def solve(s):

    i = len(s) - 1
    cnt = 0
    while i >= 0 and s[i] == " ":
        i -= 1

    while i >= 0 and s[i] != " ":
        cnt += 1
        i -= 1

    return cnt


print(solve(s))
