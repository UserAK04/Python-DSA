# https://leetcode.com/problems/longest-palindrome/description/

# Approach:
# Use hashmap to store ele and it's freq
# Count all freqs who are even
# if value is odd then substract 1 and add to result
# if result is even and current ele is odd the add 1 to result


# Input:
s = "abccccddd"
# Output: 7

# Input:
s = "a"
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

        res += (map[key] // 2) * 2  # if value is odd then substract 1
        # OR
        # res += map[key] - 1 if map[key] % 2 else map[key]

        if res % 2 == 0 and map[key] % 2 == 1:
            res += 1

    return res


print(solve(s))
