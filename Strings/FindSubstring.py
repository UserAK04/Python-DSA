# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=problem-list-v2&envId=string

# Approach:
# Using pointer, traverse the haystack string till n - length of needle
# If ith ele is equal to needle's first ele
# Then take substring out of haystack till length of needle and compare with needle


# Input:
haystack, needle = "sadbutsad", "sad"
# Output: 0

# Input:
# haystack, needle = "leetcode", "leeto"
# Output: -1


def solve(haystack, needle):

    for i in range(len(haystack) - len(needle) + 1):

        if haystack[i] == needle[0]:

            if haystack[i : i + len(needle)] == needle:
                return i

    return -1


print(solve(haystack, needle))
