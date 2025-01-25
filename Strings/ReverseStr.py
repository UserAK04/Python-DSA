# https://leetcode.com/problems/reverse-string/submissions/1519636204/?envType=problem-list-v2&envId=string

# Input:
s = ["h", "e", "l", "l", "o"]
# Output: ["o","l","l","e","h"]

# Input:
# s = ["H", "a", "n", "n", "a", "h"]
# Output: ["h","a","n","n","a","H"]


def rev(s):

    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1

    return s


def solve(s):

    result = ""
    for i in range(len(s) - 1, -1, -1):
        result += s[i]

    return result


# print(rev(s))
print(solve(s))
