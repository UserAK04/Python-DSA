# https://leetcode.com/problems/longest-palindrome/description/?envType=problem-list-v2&envId=string

# Input:
s = "abccccddd"
# Output: 7

# Input:
# s = "a"
# Output: 1


def solve(s):

    map = {}
    for ch in s:
        if map.get(ch, 0) == 0:
            map[ch] = 1
        else:
            map[ch] += 1

    res = 0
    for key in map:
        res += (map[key] // 2) * 2
        if res % 2 == 0 and map[key] % 2 == 1:
            res += 1

    return res


print(solve(s))
