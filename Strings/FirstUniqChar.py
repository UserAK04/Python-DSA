# https://leetcode.com/problems/first-unique-character-in-a-string/description/

# Approach:
# Use hash map to store each ele
# For each unique ele store it's index
# And for the ele already present in the map
# Store "#" symbol
# Compare and return that value which is not equal to symbol

# Input:
# s = "leetcode"
# Output: 0

# Input:
# s = "loveleetcode"
# Output: 2

# Input:
# s = "aabb"
# Output: -1


def firstUniqChar(s):
    map = {}

    for i in range(len(s)):
        if map.get(s[i], -1) == -1:
            map[s[i]] = i
        else:
            map[s[i]] = "#"

    for key in map:
        if map[key] != "#":
            return map[key]

    return -1
